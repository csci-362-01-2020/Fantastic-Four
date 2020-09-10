#!/bin/bash

for module in sugar{-datastore,-artwork,-toolkit,-toolkit-gtk3,}; do
    sudo apt build-dep $module
done
sudo apt install python{,3}-six python3-empy


sudo apt install autoconf autogen intltool libtool automake autotools-dev libopts25 libopts25-dev libglib2.0-dev gtk+-3.0 librsvg2-dev libasound2-dev python-empy GTK+-2.0 python2.7-dev python-dev gtk2.0 icon-naming-utils
