from web3 import Web3, HTTPProvider
import eth_utils
import json


def sign_and_send_transaction(unsigned_tx, priv_key, web3_client):
    try:
        signed_tx = web3_client.eth.account.signTransaction(unsigned_tx,
                                                            priv_key)

        tx_hash = web3_client.eth.sendRawTransaction(signed_tx.rawTransaction)
        return tx_hash

    except:
        raise


def register_identity(web3_client, contract, address,
                      private_key, first_name, last_name,
                      date_of_birth, home_addr):

    nonce = web3_client.eth.getTransactionCount(address)

    unsigned_tx = contract.functions.registerIdentity(
        first_name,
        last_name,
        date_of_birth,
        home_addr
    )
   
    unsigned_tx = unsigned_tx.buildTransaction(
        {
    	'nonce': nonce,
    	'value': 0,
        'gas': 2000000,
    	'from': address})
    
    tx_hash = sign_and_send_transaction(unsigned_tx,
                                        private_key,
                                        web3_client)
    
    return tx_hash.hex() 


def register_document(web3_client, contract, owner_address, owner_private_key,
                      name, description, year, id_address):

    nonce = web3_client.eth.getTransactionCount(owner_address)

    unsigned_tx = contract.functions.registerDocument(
        name,
        description,
        year,
        id_address
    )
    
    unsigned_tx = unsigned_tx.buildTransaction(
        {
    	'nonce': nonce,
    	'value': 0,
        'gas': 2000000,
    	'from': owner_address})
    
    tx_hash = sign_and_send_transaction(unsigned_tx,
                                        owner_private_key,
                                        web3_client)
    
    return tx_hash.hex() 


def get_document_from_identity(id_address, contract):
    document = contract.functions.documents(id_address).call()
    return document


def get_identity(id_address, contract):
    document = contract.functions.identities(id_address).call()
    return document


# Ganache LocalNet
#owner_address = "0x5EFd3143AaaeC686c2e27F7d3AfBD42d1f44c54C"
#owner_private_key = "0x59edc805b16cc8c2d111a63c90337ab09868c010e0a96832ef422862c3a96553"
#id_address = "0x3568b00A5dB316bcC89737fb2A397a7B28D596a3"
#id_private_key = "0x58be6cc06639d97c4024187ce7287bcbb320500b251596ec1819892a29be531c"
#eth_uri = "http://0.0.0.0:8545"
#contract_addr = "0x6B2132f543a6B6C596B215A6ba9F82D30F6ca62E"

# Ropsten Testnet
owner_address = "0x345f0069ACbbdadd04d4305aEC59FacA9f740eb8"
owner_private_key = "0x916B9CB1C8BB5EA811BF54C6808260341019D71EA1794C1163EB5DF639FB6E15"
id_address = "0xE453328B5E8105F49B5F76f2996c414dB85D7335"
id_private_key = "0xC97D92882F29E09A7B55D8F4A33A600300D696A3ACF0CF345175F7814E09441C"
eth_uri = "https://ropsten.infura.io/v3/f4d75f103707425dac50b43ff917a6d9"
contract_addr = "0x20A2aCfCbd259bdd0783577e6B3666806F2fA051"


owner_address = eth_utils.to_checksum_address(owner_address)

abi = json.loads(open("abi.json", "r").read())

web3_client = Web3(HTTPProvider(eth_uri))
contract = web3_client.eth.contract(address=contract_addr, abi=abi)

first_name = "John"
last_name = "Doe"
date_of_birth = "01/01/1991"
home_addr = "Brasil"
reg_id_tx = register_identity(web3_client, contract, id_address,
                              id_private_key, first_name, last_name,
                              date_of_birth, home_addr)

name = ("Some Document")
description = "Lorem Ipsum"
year = 2000
reg_doc_tx = register_document(web3_client, contract, owner_address,
                               owner_private_key, name, description,
                               year, id_address)


document = get_document_from_identity(id_address, contract)
identity = get_identity(id_address, contract)

print("register identity tx hash: %s" % reg_id_tx)
print("identitiy: \n" + str(identity))

print("register document tx hash: %s" % reg_doc_tx)
print("document: \n" + str(document))

import pdb; pdb.set_trace()
