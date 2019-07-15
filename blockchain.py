from block import Block


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
