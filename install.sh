#!/usr/bin/env bash
host_dir=`pwd`
lib_root_dir=`pwd`
cp -rf $lib_root_dir/deps/lib* /usr/lib
cp -rf $lib_root_dir/deps/mapnik /usr/lib/
cp -rf $lib_root_dir/deps/getMvtTiles.so  /usr/lib/python2.7/site-packages/
ldconfig
