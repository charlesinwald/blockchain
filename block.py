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
