#!/bin/bash

# check for updates and the Google Chrome package via aptitude package manager
sudo apt update
sudo apt install google-chrome-stable

# prints the current working directory
# sed is an inline text editor that can accept text to be edited
pwd | sed 's:$:<br/>:' > list.html

# prints the output of ls -alth to the html file
ls -alth | sed 's:$:<br/>:' >> list.html

# Chrome will open the file and display it in a browser
google-chrome list.html
