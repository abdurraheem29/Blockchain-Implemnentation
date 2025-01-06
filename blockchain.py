# Importing the Block class from block.py
from block import Block
import datetime

# Number of blocks you want to add
num_blocks_to_add = 10

# Creating the blockchain list with the genesis block
block_chain = [Block.create_genesis_block()]

# Print out the genesis block
print("The genesis block has been created.")
print("Hash: %s" % block_chain[0].hash)

# Adding new blocks to the blockchain
for i in range(1, num_blocks_to_add):
    block_chain.append(Block(block_chain[i-1].hash,
                             "Block number %d" % i,
                             datetime.datetime.now()))  # Provide a timestamp
    print("Block #%d created." % i)
    print("Hash: %s" % block_chain[-1].hash)
