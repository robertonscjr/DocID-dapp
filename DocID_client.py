from web3 import Web3, HTTPProvider
import json


eth_uri = "127.0.0.1:8545"
contract_addr = "0x881ad5E0409f4982a74A0a0886ecF6B59782bfBa"
abi = json.load(open("abi.json", "r").read())

client = Web3(HTTPProvider(eth_uri))
contract = client.eth.contract(address=config.contract_addr, abi=abi)


import pdb; pdb.set_trace()
nonce = web3_client.eth.getTransactionCount(asset_provider_address)

unsigned_tx = contract.functions.register(
    name,
    price,
    asset_hash_bytes32,
    manifest_hash_bytes32,
    asset_sha256,
    storage_type_uint,
    file_type_uint,
    [],
    permissioned_applications_bf_bytes32,
    bloom.BLOOM_FILTER_M,
    bloom.BLOOM_FILTER_K
)

unsigned_tx = unsigned_tx.buildTransaction(
    {
        'nonce': nonce,
        'from': asset_provider_address,
        'value': value})

tx_hash = ethereum.sign_and_send_transaction(unsigned_tx,
                                             asset_provider_pk,
                                             web3_client)


