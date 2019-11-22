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
    	'from': owner_address})
    
    tx_hash = sign_and_send_transaction(unsigned_tx,
                                        owner_private_key,
                                        web3_client)
    
    return tx_hash.hex() 


def get_document_from_identity(id_address, contract):
    document = contract.functions.documents(id_address).call()
    return document


owner_address = "0x5EFd3143AaaeC686c2e27F7d3AfBD42d1f44c54C"
owner_private_key = "0x59edc805b16cc8c2d111a63c90337ab09868c010e0a96832ef422862c3a96553"
owner_address = eth_utils.to_checksum_address(
    owner_address)


id_address = "0x3568b00A5dB316bcC89737fb2A397a7B28D596a3"
id_private_key = "0x58be6cc06639d97c4024187ce7287bcbb320500b251596ec1819892a29be531c"
id_address = eth_utils.to_checksum_address(
    id_address)

eth_uri = "http://0.0.0.0:8545"
contract_addr = "0x6B2132f543a6B6C596B215A6ba9F82D30F6ca62E"
abi = json.loads(open("abi.json", "r").read())

web3_client = Web3(HTTPProvider(eth_uri))
contract = web3_client.eth.contract(address=contract_addr, abi=abi)

first_name = "John"
last_name = "Doe"
date_of_birth = "01/01/1991"
home_addr = "Brasil"
reg_id_tx = register_identity(web3_client, contract, owner_address,
                              owner_private_key, first_name, last_name,
                              date_of_birth, home_addr)

name = "My document"
description = "Lorem Ipsum"
year = 2000
reg_doc_tx = register_document(web3_client, contract, owner_address,
                               owner_private_key, name, description,
                               year, id_address)


document = get_document_from_identity(id_address, contract)

import pdb; pdb.set_trace()
