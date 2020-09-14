#!/bin/bash

# check for updates and the chromium package via aptitude package manager
sudo apt update
sudo apt install chromium-browser

# prints the current working directory
# sed is an inline text editor that can accept text to be edited
pwd | sed 's:$:<br/>:' > list.html

# prints the output of ls -alth to the html file
ls -alth | sed 's:$:<br/>:' >> list.html

# Chromium will open the file and display it in a browser
chromium-browser list.html
