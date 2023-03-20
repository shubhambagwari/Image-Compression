#!/usr/bin/env python
# coding: utf-8

# In[35]:


import heapq
import os
import cv2
import numpy as np

def compress_image(image_path):
    class Node:
        def __init__(self, freq, pixel=None, left=None, right=None):
            self.freq = freq
            self.pixel = pixel
            self.left = left
            self.right = right

        def __lt__(self, other):
            return self.freq < other.freq

        def __eq__(self, other):
            return self.freq == other.freq

    def frequency_table(image):
        freq_table = {}
        height, width, channels = image.shape
        for y in range(height):
            for x in range(width):
                pixel = tuple(image[y, x])
                if pixel not in freq_table:
                    freq_table[pixel] = 0
                freq_table[pixel] += 1
        return freq_table
    
    def huff_tree(freq_table):
        heap = []
        for pixel, freq in freq_table.items():
            heapq.heappush(heap, Node(freq, pixel))

        while len(heap) > 1:
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)
            merged_node = Node(node1.freq + node2.freq, left=node1, right=node2)
            heapq.heappush(heap, merged_node)

        return heap[0]

    def huff_codes(tree, current_code="", codes={}):
        if tree is None:
            return

        if tree.pixel is not None:
            codes[tree.pixel] = current_code

        huff_codes(tree.left, current_code + "0", codes)
        huff_codes(tree.right, current_code + "1", codes)

        return codes

    image = cv2.imread(image_path)
    freq_table = frequency_table(image)
    huffman_tree = huff_tree(freq_table)
    huffman_codes = huff_codes(huffman_tree)
    compressed_data = ""
    height, width, channels = image.shape
    for y in range(height):
        for x in range(width):
            pixel = tuple(image[y, x])
            compressed_data += huffman_codes[pixel]
    while len(compressed_data) % 8 != 0:
        compressed_data += "0"
    compressed_bytes = bytearray(int(compressed_data[i:i+8], 2) for i in range(0, len(compressed_data), 8))
    return compressed_bytes, huffman_tree, height, width, channels


def decompress_image(compressed_data, huffman_tree, height, width, channels):
    binary_str = ""
    for byte in compressed_data:
        binary_str += format(byte, '08b')
    decoded_pixels = []
    current_node = huffman_tree
    for bit in binary_str:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.pixel is not None:
            decoded_pixels.append(current_node.pixel)
            current_node = huffman_tree

    decoded_pixels = np.array(decoded_pixels, dtype=np.uint8)  
    decoded_pixels = decoded_pixels.reshape((height, width, channels))
    return decoded_pixels

