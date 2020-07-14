import sys


class Node():
    def __init__(self, value):
        self.character = None
        self.value = value
        self.left = None
        self.right = None
        pass


def huffman_encoding(data):
    """
    Get the encoded string and the encoding Huffman tree.

    Args:
      data(str): the string to encode
    Returns:
        The encoded string and the tree to use for decoding
    """
    frequencies = get_frequency_nodes(data)
    tree = merge_min_nodes(frequencies)
    huffman_code = get_huffman_code(tree[0], [], {})
    encoded_data = encode_data(data, huffman_code)
    return encoded_data, tree


def encode_data(data, huffman_code):
    """
    The encoded data from the huffman code.

    Args:
      data(str): the string to encode
      huffman_code(dic): The dictionary with the binary representation

    Returns:
        The encoded data
    """
    encoded_data = ""
    for char in data:
        encoded_data += huffman_code[char]
    return encoded_data


def get_huffman_code(node, path, table):
    """
    Get the table of encoding.

    Args:
      node(class:Node): the node to start the calculation
      path(array): the array of steps from root
      table(dic): the [cached] dictionary for the final table
    Returns: 
        The table dictionary with the binary representation
    """
    current = node

    if not current.left and not current.right:
        # when we reach a leaf we update the table to keep the path of the current Node
        table[current.character] = "".join(path[:])
        path = []
        return table
    path.append("0")
    table = get_huffman_code(current.left, path, table)
    path.pop()
    path.append("1")
    get_huffman_code(current.right, path, table)
    path.pop()
    return table


def merge_min_nodes(frequencies):
    """
    Merge of each element to create a huffman tree.

    Args:
      frequencies(classNode): The current tree to merge the 2 smallest nodes
    Returns: 
        The new tree with the 2 lowest nodes merged
    """
    if(len(frequencies) == 1):
        return frequencies

    frequencies = sorted(frequencies, key=lambda x: x.value)

    new_node = Node(frequencies[0].value + frequencies[1].value)
    new_node.left = frequencies[0]
    new_node.right = frequencies[1]

    new_tree = [new_node]
    for item in range(2, len(frequencies)):
        new_tree.append(frequencies[item])
    return merge_min_nodes(new_tree)


def get_frequency_nodes(data):
    """
    Get the nodes with the frequency.

    Args:
      data(str): the input string to convert into nodes for the Huffman tree
    Returns the array of nodes and frequency
    """
    frequency_table = {}
    sorted_table = []
    frequency_nodes = []
    for char in data:
        if char not in frequency_table:
            frequency_table[char] = 1
        else:
            frequency_table[char] += 1
    # create graph with nodes
    sorted_table = sorted(frequency_table.items(), key=lambda x: x[1])
    print("sorted:", sorted_table)
    for item in sorted_table:
        prepared_node = Node(item[1])
        prepared_node.character = item[0]
        frequency_nodes.append(prepared_node)
    return frequency_nodes


def huffman_decoding(data, tree):
    """
    Get the original string calculated from the huffman tree and the binary representation.

    Args:
      data(str): the binary encoded string
      tree(class:Group): the root node of the Huffman tree
    Returns: 
        The original decoded string
    """
    decoded_string = ""
    current = tree[0]
    for bit in data:
        if bit == "0":
            next = current.left
        else:
            next = current.right
        if(not next.left and not next.right):
            decoded_string += next.character
            next = tree[0]
        current = next

    return decoded_string


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
