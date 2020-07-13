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
    Return the encoded string and the encoding Huffman tree.

    Args:
      data(str): the string to encode
    """
    frequencies = get_frequency_nodes(data)
    tree = merge_min_nodes(frequencies)
    huffman_code = get_huffman_code(tree[0], [], {})
    encoded_data = encode_data(data, huffman_code)
    return encoded_data, tree


def encode_data(data, huffman_code):
    """
    Return The encoded data from the huffman code.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    encoded_data = ""
    for char in data:
        encoded_data += huffman_code[char]
    return encoded_data


def get_huffman_code(node, path, table):
    """
    Return Get the table of encoding.

    Args:
      node(class:Node): the node to start the calculation
      path([]): the array of steps from root
      table({}): the [cached] dictionary for the final table
    """
    current = node

    if not current.left and not current.right:
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
    Return a merge of each element to create a huffman tree.

    Args:
      freequencies(classNode): The current tree to merge the 2 smallest nodes
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
    Return the array of nodes including frequency.

    Args:
      data(str): the input string to convert into nodes for the Huffman tree
    """
    frequency_table = {}
    frequency_nodes = []
    for char in data:
        if char not in frequency_table:
            frequency_table[char] = 1
        else:
            frequency_table[char] += 1
    # create graph with nodes
    frequency_table = sorted(frequency_table.items(), key=lambda x: x[1])
    for item in frequency_table:
        prepared_node = Node(item[1])
        prepared_node.character = item[0]
        frequency_nodes.append(prepared_node)
    return frequency_nodes


def huffman_decoding(data, tree):
    """
    Return the original string calculated from the huffman tree and the binary representation.

    Args:
      data(str): the binary encoded string
      tree(class:Group): the root node of the Huffman tree
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
