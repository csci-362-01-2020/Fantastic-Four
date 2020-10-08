#!/bin/bash

sudo apt install ssh

ssh-keygen

echo "Copy the following SSH key"

less /home/$USER/,ssh/id_rsa.pub