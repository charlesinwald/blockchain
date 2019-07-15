import jsons

from block import Block

# Basically just a linked list
from blockchain import Blockchain


# Save the block to the filesystem
def save_block(block):
    chaindata_dir = 'chaindata'
    # Generate filename by interpolating a string, will be saved as json
    # i.e chaindata/42.json is block 42 in the chaindata folder
    filename = '%s/%s.json' % (chaindata_dir, block.blockNo)
    print(filename)
    # The with keyword executes a pair of related operations, with a block
    # of code in between. Here it will open a file, manipulate it, and automatically
    # close it. It is guaranteed to close the file regardless of how the nested block exits
    with open(filename, 'w') as block_file:
        print(block)
        block_file.write(str(jsons.dump(block)))


# Execute our blockchain
blockchain = Blockchain()
# Mine 10 blocks
for n in range(3):
    blockchain.mine(Block("Block " + str(n + 1)))

# iterate through blockchain printing everything
while blockchain.head is not None:
    print(blockchain.head)
    save_block(blockchain.head)
    blockchain.head = blockchain.head.next
