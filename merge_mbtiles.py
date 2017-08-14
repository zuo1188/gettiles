# -*- coding: utf-8 -*-
#用于合并某个目录下的所有mbtiles，最后输出一个mbtile

import sqlite3, sys, logging, time, os, json, zlib, re

logger = logging.getLogger(__name__)


def flip_y(zoom, y):
    return (2**zoom-1) - y

def mbtiles_connect(mbtiles_file):
    try:
        con = sqlite3.connect(mbtiles_file)
        return con
    except Exception as e:
        logger.error("Could not connect to database")
        logger.exception(e)
        sys.exit(1)

def optimize_connection(cur):
    cur.execute("""PRAGMA synchronous=0""")
    cur.execute("""PRAGMA locking_mode=EXCLUSIVE""")
    cur.execute("""PRAGMA journal_mode=DELETE""")


def mbtiles_setup(cur):
    cur.execute("""
        create table tiles (
            zoom_level integer,
            tile_column integer,
            tile_row integer,
            tile_data blob);
            """)
    cur.execute("""create table metadata
        (name text, value text);""")
    cur.execute("""CREATE TABLE grids (zoom_level integer, tile_column integer,
    tile_row integer, grid blob);""")
    cur.execute("""CREATE TABLE grid_data (zoom_level integer, tile_column
    integer, tile_row integer, key_name text, key_json text);""")
    cur.execute("""create unique index name on metadata (name);""")
    cur.execute("""create unique index tile_index on tiles
        (zoom_level, tile_column, tile_row);""")


def merge(input_dir, output_file_path):
    allFiles = scandir(input_dir)
    con_output = mbtiles_connect(output_file_path)
    cur_output = con_output.cursor()
    optimize_connection(cur_output)
    mbtiles_setup(cur_output)

    try:
        # metadata = json.load(open(os.path.join("/Users/lishiguang/Documents/heilongjiang/test/", 'metadata.json'), 'r'))
        metadata = json.load(open(os.path.join("/mnt/gettile_1.0/", 'metadata.json'), 'r'))
        for name, value in metadata.items():
            print name
            print value
            cur_output.execute('insert into metadata (name, value) values (?, ?)',
                        (name, value))
        logger.info('metadata from metadata.json restored')
        print "hello"
    except IOError:
        logger.warning('metadata.json not found')




    for input in allFiles:
        if input.find(".DS_Store")!=-1:
            continue
        con = mbtiles_connect(input)

        tiles = con.execute('select zoom_level, tile_column, tile_row, tile_data from tiles;')
        t = tiles.fetchone()
        while t:
            z = t[0]
            x = t[1]
            y = t[2]
            # y = flip_y(z, y)
            # print('flipping')
            # tile_dir = os.path.join(base_path, str(z), str(x))
            # print z
            # print x
            # print y
            try:
                cur_output.execute("""insert into tiles (zoom_level,
                                        tile_column, tile_row, tile_data) values
                                        (?, ?, ?, ?);""",
                        # ( z, x, y, sqlite3.Binary(t[3])) )
                        ( z, x, y, (t[3]) ) )
            except Exception as e:
                print  e

            t = tiles.fetchone()

    con_output.commit()


def scandir(startdir):
    allFiles = []
    os.chdir(startdir)
    for obj in os.listdir(os.curdir):
        if os.path.isfile(obj):
            fullPathName = os.getcwd() + os.sep + obj
            # print fullPathName
            allFiles.append(fullPathName)

        if os.path.isdir(obj):
            scandir(obj)
            os.chdir(os.pardir)
    return allFiles



if __name__ == '__main__':
    wd = "/mnt/gettile_1.0/result"
    # wd = "/Users/lishiguang/Documents/heilongjiang/result/"
    merge(wd, "/mnt/all.mbtiles")
    # merge(wd, "/Users/lishiguang/Documents/heilongjiang/all.mbtiles")
