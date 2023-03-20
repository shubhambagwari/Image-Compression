import numpy as np
import cv2

def compress_img(img,num_coeffs_to_keep):
    img = cv2.imread(img)

    block_size = 8

    h, w, c = img.shape
    num_blocks_h = h // block_size
    num_blocks_w = w // block_size
    blocks = np.zeros((num_blocks_h, num_blocks_w, block_size, block_size, c))

    for i in range(num_blocks_h):
        for j in range(num_blocks_w):
            block = img[i*block_size:(i+1)*block_size, j*block_size:(j+1)*block_size, :]
            blocks[i,j,:,:,:] = block

    dct_blocks = np.zeros(blocks.shape)

    for i in range(num_blocks_h):
        for j in range(num_blocks_w):
            for k in range(c):
                dct_block = cv2.dct(blocks[i,j,:, :, k].astype(np.float32))
                dct_blocks[i,j,:, :, k] = dct_block

    dct_blocks_compressed = np.zeros(dct_blocks.shape)

    for i in range(num_blocks_h):
        for j in range(num_blocks_w):
            for k in range(c):
                dct_block = dct_blocks[i,j,:, :, k]
                dct_block_compressed = np.zeros(dct_block.shape)
                dct_block_compressed[:num_coeffs_to_keep,:num_coeffs_to_keep] = dct_block[:num_coeffs_to_keep,:num_coeffs_to_keep]
                dct_blocks_compressed[i,j,:, :, k] = dct_block_compressed

    compressed_blocks = np.zeros(blocks.shape)

    for i in range(num_blocks_h):
        for j in range(num_blocks_w):
            for k in range(c):
                dct_block_compressed = dct_blocks_compressed[i,j,:, :, k]
                compressed_block = cv2.idct(dct_block_compressed.astype(np.float32))
                compressed_blocks[i,j,:, :, k] = compressed_block

    compressed_img = np.zeros((h, w, c))

    for i in range(num_blocks_h):
        for j in range(num_blocks_w):
            compressed_block = compressed_blocks[i,j,:,:,:]
            compressed_img[i*block_size:(i+1)*block_size, j*block_size:(j+1)*block_size, :] = compressed_block

    compressed_img = compressed_img.astype(np.uint8)
    return compressed_img
