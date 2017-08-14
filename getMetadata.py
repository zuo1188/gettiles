# -*- coding: utf-8 -*-
#用于从mbtiles里面抽取metadata
import sqlite3, sys, logging, time, os, json, zlib, re

# intput = "/mnt/gettile_1.0/result/871_366.mbtiles"
intput_file = "/Users/lishiguang/Documents/heilongjiang/gettile_1.0/872_365.mbtiles"

def mbtiles_connect(mbtiles_file):
    try:
        con = sqlite3.connect(mbtiles_file)
        return con
    except Exception as e:
        print e
        sys.exit(1)


con = mbtiles_connect(intput_file)

tiles = con.execute('select * from metadata;')
t = tiles.fetchone()
print t[0]
print t[1]