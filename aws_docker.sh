#!/bin/bash

# Downloads, enables, and starts docker on the EC2 Instance
sudo yum install -y docker
sudo systemctl enable docker
sudo systemctl start docker
# Allow access to the ec2 user
sudo usermod -a -G docker ec2-user

echo "*********************************************************"
echo "**Log out and log back in, and then run ./dockstart.sh.**"
echo "*********************************************************"
