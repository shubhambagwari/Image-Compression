import cv2
import numpy as np
import pickle

# RLE Compression function
def rle_compress(channel):
    compressed_data = []
    prev_pixel = None
    count = 0
    
    for pixel in channel.flat:
        if pixel == prev_pixel:
            count += 1
        else:
            if prev_pixel is not None:
                compressed_data.append((prev_pixel, count))
            prev_pixel = pixel
            count = 1
    
    # Add the last run
    compressed_data.append((prev_pixel, count))
    
    return compressed_data


# RLE decompress function
def rle_decompress(compressed_data, width, height):
    y_data = []
    cr_data = []
    cb_data = []
    
    for channel_name in ['y', 'cr', 'cb']:
        channel_compressed = compressed_data[channel_name]
        channel_data = []
        
        for pixel, count in channel_compressed:
            channel_data += [pixel] * count
        
        # Pad the data to fill the image dimensions
        channel_data += [0] * (width*height - len(channel_data))
        
        if channel_name == 'y':
            y_data = channel_data
        elif channel_name == 'cr':
            cr_data = channel_data
        else:
            cb_data = channel_data
    
    # Merge the color channels into a single image
    merged_data = np.stack((y_data, cr_data, cb_data), axis=-1)
    merged_data = merged_data.reshape(height, width, 3)
    
    # Convert the image back to BGR color space
    decompressed_image = cv2.cvtColor(merged_data, cv2.COLOR_YCR_CB2BGR)
    
    return decompressed_image
