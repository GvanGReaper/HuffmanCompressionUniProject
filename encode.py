import random
import hashlib
#import json

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

#traveling huffman tree
codes = dict()
def calculate_codes(node, val=''):
    new_value = val + str(node.code)

    if node.left:
        calculate_codes(node.left, new_value)
    if node.right:
        calculate_codes(node.right, new_value)
    if not node.left and not node.right:
        codes[node.symbol] = new_value
    return codes

#obtaining the encoded output
def output_encoded(data, coding):
    encoding_output = []
    for c in data:
        print(coding[c], end='')
        encoding_output.append(coding[c])
    string = ''.join([str(item) for item in encoding_output])
    return string

#getting the encoded data as a string
def get_encoded_string(data):
    symbol_probability_dictionary = calculate_probability(data)
    symbols = symbol_probability_dictionary.keys()
    probabilities = symbol_probability_dictionary.values()

    nodes = []
    for symbol in symbols:
        nodes.append(HuffmanNode(symbol_probability_dictionary.get(symbol), symbol))

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.probability)
        # for node in nodes:
        #     print(node.symbol, node.probability)

        right = nodes[0]
        left = nodes[1]

        left.code = 0
        right.code = 1

        newNode = HuffmanNode(left.probability + right.probability, left.symbol + right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    huffman_encoding = calculate_codes(nodes[0])
    encoded_output = output_encoded(data, huffman_encoding)
    return encoded_output


#padding for the cyclic code to work properly
#!block size equal to the degree of the polynomial
def add_padding(binary_string, block_size):
    padding_length = block_size - (len(binary_string) % block_size)
    padding = [0] * padding_length
    padded_string = binary_string + padding
    return padded_string


#random degree for polynomial
def polynomial_degree_generator(max_degree):
    degree = random.randint(4,max_degree)
    return degree

#random polynomial generator
def polynomial_generator(degree):
    polynomial = [1,]
    for i in range(degree+1):
        coefficient = random.randint(0,1)
        polynomial.append(coefficient)
    return polynomial

#!doesn't work properly
def cyclic_encoding(data):
    max_degree = 16
    degree = polynomial_degree_generator(max_degree)
    polynomial = polynomial_generator(degree)
    padded_data = add_padding(data, degree)
    encoded_data = padded_data + [0] * (degree - 1)

    length = len(encoded_data)
    while length >= degree:
        first_divisible_digit = None
        for i, digit in enumerate(encoded_data):
            if digit:
                first_divisible_digit = i
                break

        if first_divisible_digit is not None:
            if first_divisible_digit + degree <= length:
                for i in range(degree):
                    encoded_data[first_divisible_digit + i] ^= polynomial[i]
            else:
                break
        else:
            break
        encoded_data += encoded_data[-(degree - 1):]
        length -=1
    decoded_data = encoded_data[:len(data)]
    return decoded_data

def reed_solomon():
    pass

#sha256 hashing
def calculate_hash(data):
    hash = hashlib.sha256()
    hash.update(data.encode('utf-8'))
    hash_value = hash.hexdigest()
    return hash_value

#sha256 hashing
def calculate_hash(data):
    hash = hashlib.sha256()
    hash.update(data.encode('utf-8'))
    hash_value = hash.hexdigest()
    return hash_value