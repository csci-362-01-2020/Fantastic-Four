#!/bin/bash

for module in sugar{-artwork,-toolkit-gtk3,-datastore,}; do
    cd $module
    ./autogen.sh --with-python3
    make
    sudo make install
    cd ..
done
