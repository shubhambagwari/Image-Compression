import numpy as np
import cv2

def compress_img(img,quantization_scale):
    img=cv2.imread(img)
    block_size = 8
    quantization_table = np.array([
        [16,  11,  10,  16,  24,  40,  51,  61],
        [12,  12,  14,  19,  26,  58,  60,  55],
        [14,  13,  16,  24,  40,  57,  69,  56],
        [14,  17,  22,  29,  51,  87,  80,  62],
        [18,  22,  37,  56,  68, 109, 103,  77],
        [24,  35,  55,  64,  81, 104, 113,  92],
        [49,  64,  78,  87, 103, 121, 120, 101],
        [72,  92,  95,  98, 112, 100, 103,  99]])

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

    dct_blocks_quantized = np.zeros(dct_blocks.shape)

    for i in range(num_blocks_h):
        for j in range(num_blocks_w):
            for k in range(c):
                dct_block = dct_blocks[i,j,:, :, k]
                quantization_scale_block = quantization_table * quantization_scale
                quantized_block = np.round(dct_block / quantization_scale_block)
                dct_blocks_quantized[i,j,:, :, k] = quantized_block

    idct_blocks = np.zeros(blocks.shape)

    for i in range(num_blocks_h):
        for j in range(num_blocks_w):
            for k in range(c):
                dct_block_quantized = dct_blocks_quantized[i,j,:, :, k]
                idct_block = cv2.idct(dct_block_quantized.astype(np.float32))
                idct_blocks[i,j,:, :, k] = idct_block
    compressed_img = np.zeros((h, w, c))

    for i in range(num_blocks_h):
        for j in range(num_blocks_w):
            for k in range(c):
                block = idct_blocks[i,j,:, :, k]
                compressed_img[i*block_size:(i+1)*block_size, j*block_size:(j+1)*block_size, k] = block

 
    return compressed_img

