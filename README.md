# DocID-dapp

## Install tools

Truffle:
```bash
$ npm install -g truffle
```

Ganache:
```bash
$ npm install -g ganache-cli
```

https://www.trufflesuite.com/

## Deploy contract

Running ganache:
```bash
$ ganache-cli
```

Compiling the contract:
```bash
$ truffle compile
 ```
 
 Deploying the contract:
```bash
 $ truffle migrate
 ```
 
 Deploying the contract on Ropsten Testnet:
 ```bash
 $ truffle deploy --network ropsten
 ```

## Configure Python

1. For **Ubuntu 16.04**, install them with the following command line:
    ```bash
    $ sudo add-apt-repository ppa:jonathonf/python-3.6
    $ sudo apt-get update -y
    $ sudo apt install python3.6-dev virtualenv python-pip build-essential libcurl4-openssl-dev libssl-dev -y
    ```

2. Then you need to create a **Python 3.6 virtual environment**. From inside the root folder, run:
    ```bash
    $ export LC_ALL="en_US.UTF-8" && export LC_CTYPE="en_US.UTF-8"
    $ virtualenv -p python3.6 venvclient
    $ source venvclient/bin/activate
    ``` 

3. To install **requirements**, run:
    ```bash
    $ pip install -r requirements.txt
    ```
