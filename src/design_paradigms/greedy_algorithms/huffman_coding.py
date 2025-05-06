import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparison operators for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequency):
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]  # Root of the Huffman Tree

def generate_huffman_codes(root, current_code, codes):
    if root is None:
        return

    if root.char is not None:  # Leaf node
        codes[root.char] = current_code
        return

    generate_huffman_codes(root.left, current_code + "0", codes)
    generate_huffman_codes(root.right, current_code + "1", codes)

def huffman_coding(data):
    # Calculate frequency of each character
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1

    # Build Huffman Tree
    root = build_huffman_tree(frequency)

    # Generate Huffman Codes
    codes = {}
    generate_huffman_codes(root, "", codes)

    # Encode the data
    encoded_data = "".join(codes[char] for char in data)

    return codes, encoded_data

