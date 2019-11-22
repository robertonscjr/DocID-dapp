from web3 import Web3, HTTPProvider
import json


def sign_and_send_transaction(unsigned_tx, priv_key, web3_client):
    """
        the signing could be done in another application that will be run on
        SGX to enhance security
    """
    try:
        signed_tx = web3_client.eth.account.signTransaction(unsigned_tx,
                                                            priv_key)

        tx_hash = web3_client.eth.sendRawTransaction(signed_tx.rawTransaction)
        return tx_hash

    except:
        raise


address = "0x5EFd3143AaaeC686c2e27F7d3AfBD42d1f44c54C"
private_key = "0x59edc805b16cc8c2d111a63c90337ab09868c010e0a96832ef422862c3a96553"

eth_uri = "http://0.0.0.0:8545"
contract_addr = "0x881ad5E0409f4982a74A0a0886ecF6B59782bfBa"
abi = json.loads(open("abi.json", "r").read())

web3_client = Web3(HTTPProvider(eth_uri))
contract = web3_client.eth.contract(address=contract_addr, abi=abi)


nonce = web3_client.eth.getTransactionCount(address)

first_name = "John"
last_name = "Doe"
date_of_birth = "01/01/1991"
home_address = "Brasil"

unsigned_tx = contract.functions.registerIdentity(
    first_name,
    last_name,
    date_of_birth,
    home_address
)


unsigned_tx = unsigned_tx.buildTransaction(
    {
        'nonce': nonce,
        'from': address})

tx_hash = sign_and_send_transaction(unsigned_tx,
                                    private_key,
                                    web3_client)


import pdb; pdb.set_trace()
