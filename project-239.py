import hashlib

import json

from time import time

def block(proof,previous_hash=None):
	transaction={
	'sender':'Satoshi',
	'recipient':'Mike',
	'amount':'5 ETH'
	}
	data={
	'block_height':12913586,
	'timestamp':time(),
	'transactions':transaction,
	'Block Reward':2.557430954505356948,
	'Uncles Reward':0,
	'Difficulty':7317161775076869,
	'Total Difficulty':28115205704610921164128,
	'Gas Used':14935987,
	'Gas Limit':14955,
	'proof':proof,
	'previous_hash':previous_hash,
	}
	print("Block info : ",data)
	string_object=json.dumps(data)
	block_string=string_object.encode()
	hashed_block_string=hashlib.sha512(block_string)
	hexadecimal_string=hashed_block_string.hexdigest()
	print("hashcode of the block : ",hexadecimal_string)

block(proof=000,previous_hash="No previous hash because it is the first block")