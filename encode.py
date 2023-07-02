class HuffmanNode:
    def __init__(self, probability, symbol, left=None, right=None):
        self.probability = probability
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''

#calculates the probability of each symbol appearing in the data
def calculate_probability(data):
    symbols = dict()
    for element in data:
        if symbols.get(element) is None:
            symbols[element] = 1
        else:
            symbols[element] += 1
    return symbols

#prints the codes of symbols by traveling huffman tree
codes = dict()
def calculate_codes(node, val=''):
    newVal = val + str(node.code)

    if node.left:
        calculate_codes(node.left, newVal)
    if node.right:
        calculate_codes(node.right, newVal)
    if not node.left and not node.right:
        codes[node.symbol] = newVal
    return codes

#obtaining the encoded output
def output_encoded(data, coding):
    encoding_output = []
    for c in data:
        print(coding[c], end='')
        encoding_output.append(coding[c])
    string = ''.join([str(item) for item in encoding_output])
    return string

#encrypts the encoded data using a generator polynomial
#using the polynomial key to perform xor encryption
def polynomial_encryption(data, key):
    encrypted_data = []
    key_length = len(key)
    for i, symbol in enumerate(data):
        key_index = i % key_length
        encrypted_symbol = symbol ^ key[key_index]
        encrypted_data.append(encrypted_symbol)
    return encrypted_data

#getting the encoded data as a string
def get_encoded_string(data):
    symbol_probability_dictionary = calculate_probability(data)
    symbols = symbol_probability_dictionary.keys()
    probabilities = symbol_probability_dictionary.values()
    # print("symbols: ", symbols)
    # print("probabilities: ", probabilities)

    nodes = []
    for symbol in symbols:
        nodes.append(HuffmanNode(symbol_probability_dictionary.get(symbol), symbol))

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.probability)
        for node in nodes:
            print(node.symbol, node.probability)

        right = nodes[0]
        left = nodes[1]

        left.code = 0
        right.code = 1

        newNode = HuffmanNode(left.probability + right.probability, left.symbol + right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    huffman_encoding = calculate_codes(nodes[0])
    print(huffman_encoding)
    encoded_output = output_encoded(data, huffman_encoding)
    print("Encoded output: ", encoded_output)
    #padded_string = Add_Padding(encoded_output, 8)
    #print(padded_string)
    #return encoded_output, nodes[0]
    return encoded_output


# def Add_Padding(binary_string, block_size):
#     padding_length = block_size - (len(binary_string) % block_size)
#     padding = "0" * padding_length
#     padded_string = binary_string + padding
#     return padded_string


test = ['1','a','5','2','b','a','1','s','3','1','j','6','o']
#print(get_encoded_string(test))
a = get_encoded_string(test)
print(a, "this is print a command")
b = [int(x) for x in a]
print(b)
c = polynomial_encryption(b,[1, 0, 1])
print(c)
