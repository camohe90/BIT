# -- coding: utf-8 --

from eth_typing.ethpm import ContractName
from web3 import Web3
import sys 
url = 'http://127.0.0.1:7545'

abi_contract= [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "initialMessage",
				"type": "string"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [],
		"name": "message",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "newMessage",
				"type": "string"
			}
		],
		"name": "setMessage",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]

bytecode_contract= "608060405234801561001057600080fd5b506040516107853803806107858339818101604052810190610032919061015a565b806000908051906020019061004892919061004f565b50506102f6565b82805461005b90610224565b90600052602060002090601f01602090048101928261007d57600085556100c4565b82601f1061009657805160ff19168380011785556100c4565b828001600101855582156100c4579182015b828111156100c35782518255916020019190600101906100a8565b5b5090506100d191906100d5565b5090565b5b808211156100ee5760008160009055506001016100d6565b5090565b6000610105610100846101c0565b61019b565b90508281526020810184848401111561011d57600080fd5b6101288482856101f1565b509392505050565b600082601f83011261014157600080fd5b81516101518482602086016100f2565b91505092915050565b60006020828403121561016c57600080fd5b600082015167ffffffffffffffff81111561018657600080fd5b61019284828501610130565b91505092915050565b60006101a56101b6565b90506101b18282610256565b919050565b6000604051905090565b600067ffffffffffffffff8211156101db576101da6102b6565b5b6101e4826102e5565b9050602081019050919050565b60005b8381101561020f5780820151818401526020810190506101f4565b8381111561021e576000848401525b50505050565b6000600282049050600182168061023c57607f821691505b602082108114156102505761024f610287565b5b50919050565b61025f826102e5565b810181811067ffffffffffffffff8211171561027e5761027d6102b6565b5b80604052505050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b6000601f19601f8301169050919050565b610480806103056000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c8063368b87721461003b578063e21f37ce14610057575b600080fd5b61005560048036038101906100509190610228565b610075565b005b61005f61008f565b60405161006c91906102a2565b60405180910390f35b806000908051906020019061008b92919061011d565b5050565b6000805461009c90610378565b80601f01602080910402602001604051908101604052809291908181526020018280546100c890610378565b80156101155780601f106100ea57610100808354040283529160200191610115565b820191906000526020600020905b8154815290600101906020018083116100f857829003601f168201915b505050505081565b82805461012990610378565b90600052602060002090601f01602090048101928261014b5760008555610192565b82601f1061016457805160ff1916838001178555610192565b82800160010185558215610192579182015b82811115610191578251825591602001919060010190610176565b5b50905061019f91906101a3565b5090565b5b808211156101bc5760008160009055506001016101a4565b5090565b60006101d36101ce846102e9565b6102c4565b9050828152602081018484840111156101eb57600080fd5b6101f6848285610336565b509392505050565b600082601f83011261020f57600080fd5b813561021f8482602086016101c0565b91505092915050565b60006020828403121561023a57600080fd5b600082013567ffffffffffffffff81111561025457600080fd5b610260848285016101fe565b91505092915050565b60006102748261031a565b61027e8185610325565b935061028e818560208601610345565b61029781610439565b840191505092915050565b600060208201905081810360008301526102bc8184610269565b905092915050565b60006102ce6102df565b90506102da82826103aa565b919050565b6000604051905090565b600067ffffffffffffffff8211156103045761030361040a565b5b61030d82610439565b9050602081019050919050565b600081519050919050565b600082825260208201905092915050565b82818337600083830152505050565b60005b83811015610363578082015181840152602081019050610348565b83811115610372576000848401525b50505050565b6000600282049050600182168061039057607f821691505b602082108114156103a4576103a36103db565b5b50919050565b6103b382610439565b810181811067ffffffffffffffff821117156103d2576103d161040a565b5b80604052505050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b6000601f19601f830116905091905056fea264697066735822122034e3cfab7b69da05b6d953ec90d67e2f9ab9f0dc0d02a3776258cad3df23618164736f6c63430008010033"

account_a = "0x39a19E317e85BF3E2dA6b42D2c1B204df7269929"
key_a = "127229dcd939df4de1fa2cefdf2b9fbe46ded5f1b4fedcf916757af8df2d0ea8"
constract_addres= "0xCA8A40B21912f1E55De5D1c958e86b17B125Ae2f"

web3 = Web3(Web3.HTTPProvider(url))

def read():
    

    address = web3.toChecksumAddress(constract_addres)
    contract = web3.eth.contract(address=address, abi= abi_contract)
    data = contract.functions.message().call()
   
    print(data)

read()