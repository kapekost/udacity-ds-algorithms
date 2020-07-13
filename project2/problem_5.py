import hashlib
import time


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = "{}-{}".format(self.timestamp, self.data).encode(
            'utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class Block_chain:
    def __init__(self):
        pass

    def create_chain(self, data):
        """
        Create a chain of the array in input data
        return the tail node and chain 
        """
        chain = {}
        previous_hash = None
        for datum in data:
            ts = time.gmtime()
            new_block = Block(ts, datum, previous_hash)
            current_hash = new_block.hash
            new_block.previous_hash = previous_hash
            chain[current_hash] = new_block
            previous_hash = current_hash
        return new_block, chain


block_chain = Block_chain()
tail_block, my_chain = block_chain.create_chain(["a", "b", "c"])
current = tail_block
data = ""
while current.previous_hash is not None:
    data += current.data
    current = my_chain[current.previous_hash]
data += current.data

print(data)
