#!/bin/bash
sudo yum install -y docker
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker ec2-user


echo "**Log out and log back in, and then run ./dockstart.sh.**"
