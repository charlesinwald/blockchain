import datetime
import hashlib


class Block:
    blockNo = 0
    # data we want to store
    data = None
    # pointer to next block
    next = None
    # The source of the immutability of the whole blockchain in tandem with the previous hash
    hash = None
    # a single use number to ensure the same transaction isn't submitted twice, we increment with
    # every guess
    nonce = 0
    # see hash comment
    previous_hash = 0x0
    # used for synchronization of multiple blockchains
    timestamp = datetime.datetime.now()

    # When we create a block, all we do is store its data
    def __init__(self, data):
        self.data = data

    # Calculate hash of the block
    def hashblock(self):
        h = hashlib.sha256()
        # Make one big string from the block's contents
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNo).encode('utf-8')
        )
        # run it through the sha256 algorithm
        return h.hexdigest()

    # stringify
    def __str__(self):
        return "Block Hash: " + str(self.hashblock()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(
            self.data) + "\nHashes: " + str(self.nonce) + "\n----------------"


# Basically just a linked list
class Blockchain:
    diff = 20
    # Two to the power of 32, the max integer
    maxNonce = 2 ** 32
    # The subtraction of the difficulty shortens the range of valid guesses
    target = 2 ** (256 - diff)

    # Genesis block is built into the block chain
    block = Block("Genesis")
    # Remember python is pass by reference
    # To set the head of the blockchain we use a dummy variable to make it pass by value so head
    # doesn't point to the same object as block
    dummy = head = block

    def add(self, block):
        # Backwards link the hash
        block.previous_hash = self.block.hashblock()
        # Populate block height
        block.blockNo = self.block.blockNo + 1
        # Add the block to the end of the linked list
        self.block.next = block
        self.block = self.block.next

    # Check if the block's hash is less than a given target number
    def mine(self, block):
        # guess from zero to the maximum nonce until we are correct
        for i in range(self.maxNonce):
            # Check if our guess is less than or equal to the target
            # Python needs us to convert to integer first for comparison
            if int(block.hashblock(), 16) <= self.target:
                # We are correct, add it to the blockchain and print it out
                self.add(block)
                print(block)
                # Stop mining
                break
            else:
                # We are trying again, update the nonce
                block.nonce += 1


# Execute our blockchain
blockchain = Blockchain()
# Mine 10 blocks
for n in range(10):
    blockchain.mine(Block("Block " + str(n + 1)))

# iterate through blockchain printing everything
while blockchain.head is not None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next
