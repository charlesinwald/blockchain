from block import Block


# Basically just a linked list
from blockchain import Blockchain

# Execute our blockchain
blockchain = Blockchain()
# Mine 10 blocks
for n in range(10):
    blockchain.mine(Block("Block " + str(n + 1)))

# iterate through blockchain printing everything
while blockchain.head is not None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next
