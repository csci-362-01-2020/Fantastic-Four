#!/bin/bash

for module in sugar{-datastore,-artwork,-toolkit,-toolkit-gtk3,}; do
    git clone https://github.com/sugarlabs/$module.git
done
