#!/bin/sh

curl -sL https://deb.nodesource.com/setup_10.x | bash -

apt install -y nodejs

# install truffle
npm install -g truffle --silent

# install ganache
npm install -g ganache-cli --silent

# install hdwallet
sudo npm -g install --save truffle-hdwallet-provider --silent
