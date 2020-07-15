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

    def append_block(self, data, tail_node, chain={}):
        """
        Create a new block with data and append in the given chain
        Args:
            data(string): the data to add in the Block
            tail_node(Block): the current tail of the queue(head of chain)
            chain(dic):optional, the existing chain to append the Block

        Returns:
            the added Block, 
            the new chain
        """
        # if there is nothing to append we return the expected objects
        if data == "" or data == None:
            return tail_node, chain

        if tail_node != None:
            previous_hash = tail_node.hash
        else:
            previous_hash = None
        block_to_add = Block(time.gmtime(), data, previous_hash)
        chain[block_to_add.hash] = block_to_add
        return block_to_add, chain

    def create_chain(self, data):
        """
        Create a chain of the array in input data

        Args:
            data(string[]): the data to add in the blocks
        Returns: 
            the starting Blok
            the chain 
        """
        if data == None:
            return
        chain = {}
        tail_node = None
        for datum in data:
            tail_node, chain = self.append_block(datum, tail_node, chain)
        return tail_node, chain


if __name__ == "__main__":
    # Tests

    def get_string_test_block(current):
        data = ""
        while current.previous_hash is not None:
            data += current.data + " ->"
            current = my_chain[current.previous_hash]
        data += current.data
        print(data)
        return data

    block_chain = Block_chain()  # ideally we want to create a new one for each test
    print("call create chain with a b c as data")
    head, my_chain = block_chain.create_chain(["a", "b", "c"])
    print("call append_block to add one more block with data = d")
    head, my_chain = block_chain.append_block("d", head, my_chain)

    data = get_string_test_block(head)
    assert data == "d ->c ->b ->a", f"the chain should print all the nodes in reverse order"

    print("call append with empty data")
    head, my_chain = block_chain.append_block("", head, my_chain)
    data = get_string_test_block(head)
    assert data == "d ->c ->b ->a", f"the chain should print all the nodes in reverse order"

    print("call append with none chain with 1 item")
    head, my_chain = block_chain.append_block(None, head, my_chain)
    data = get_string_test_block(head)
    assert data == "d ->c ->b ->a", f"the chain should print all the nodes in reverse order"

    print("call append 1000 times")
    for i in range(1000):
        head, my_chain = block_chain.append_block(str(i), head, my_chain)
    data = get_string_test_block(head)
    assert data != None, f"the chain should print all the nodes in reverse order"

    block_chain2 = Block_chain()
    print("call create chain with 1 item")
    head, my_chain = block_chain2.create_chain(["c"])
    data = get_string_test_block(head)
    assert data == "c", f"the chain should print one item"

    print("call create a chain with no input")
    head, my_chain = block_chain2.create_chain("")
    assert head == None, f"the chain should not exist"
    print("all passed")
