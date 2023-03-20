'''
To perform compression, type the following command
Command: python main.py {Method_Name} {image_path}
     eg: python main.py RLE lena.jpg
         python main.py HuffC lena.jpg
         python main.py DCT lena.jpg
'''

import cv2
import pickle
import os
import RLE
import HuffC
import DCT_QM
import DCT_COEFF
import SVD
import PCA
import PSNR
import time
import argparse
parser = argparse.ArgumentParser(description="Image Compression via diff techniques")  
FUNCTION_MAP = {'RLE' : RLE,
                'HuffC' : HuffC,
                'DCT_QM' : DCT_QM,
                'DCT_COEFF' : DCT_COEFF,
                'SVD' : SVD,
                'PCA' : PCA}
parser.add_argument('command', choices=FUNCTION_MAP.keys())
# parser.add_argument("RLEm",help="Run-length encoding technique")
parser.add_argument("--i", default='.\\P_image.png', help="Give image path")
parser.add_argument("--s", default= 0.1, type=str, help="DCT_QM: Quantization Scale")
parser.add_argument("--c", default= 2, type=int, help="DCT_COEFF: Number of Coefficient to keep")
parser.add_argument("--p", default= 50, type=int,help="PCA: Varaiance/Percentage")
parser.add_argument("--q",default= 2, type=int, help="PCA: Quantization Value ")

if __name__ == "__main__":
    
    args = parser.parse_args()
    func = FUNCTION_MAP[args.command]

    # print("func:",args.command)
    input_path = args.i
    img = cv2.imread(input_path)

    if args.command =='RLE':
        #Image loding done. Now converting image to YCbCr color space
        w, h, c = img.shape
        # print(w,h,c)
        img_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
        y_channel, cr_channel, cb_channel = cv2.split(img_ycrcb)
        
        start_time = time.time()
        # Compressing Each channel
        y_compressed = func.rle_compress(y_channel)
        cr_compressed = func.rle_compress(cr_channel)
        cb_compressed = func.rle_compress(cb_channel)

        # Combine the compressed data into a single file
        compressed_data = {
            'y': y_compressed,
            'cr': cr_compressed,
            'cb': cb_compressed
        }

        # Save the compressed data to a file
        with open('compressed_data.pickle', 'wb') as f:
            pickle.dump(compressed_data, f)
        # Load the compressed data from the file
        with open('compressed_data.pickle', 'rb') as f:
            compressed_data = pickle.load(f)

        # Get the image dimensions
        height, width, channels = img.shape
        # print(height, width, channels)

        # Decompress operation is being perfomed after the compression and saving it to pwd.
        compressed_image = func.rle_decompress(compressed_data, width, height)
        end_time = time.time()

        # Save the decompressed image
        cv2.imwrite('RLE_compressed_image.png',compressed_image)
        output_path =  'RLE_compressed_image.png'     
        output_size = os.path.getsize('RLE_compressed_image.png')


    elif args.command =='HuffC':
        start_time = time.time()

        # Compression operation is being performed with will return values which help to genrate the final compressed image.
        compressed_data, huffman_tree, height, width, channels = func.compress_image(input_path)

        # Compression operation is being performed with will.
        compressed_image = func.decompress_image(compressed_data, huffman_tree, height, width, channels)
        end_time = time.time()
        cv2.imwrite("HuffC_compressed_image.png",compressed_image)
        output_path = 'HuffC_compressed_image.png'
        output_size = os.path.getsize(output_path)


    elif args.command =='DCT_QM':
        start_time = time.time()
        # Compression operation is being performed with will return values which help to genrate the final compressed image.
        compressed_image = func.compress_img(input_path,args.s)
        end_time = time.time()
        filename = f'DCT_QM_compressed_image_{args.s}.png'
        cv2.imwrite(filename,compressed_image)
        output_path = filename
        output_size = os.path.getsize(output_path)
        

    elif args.command =='DCT_COEFF':
        start_time = time.time()
        # Compression operation is being performed with will return values which help to genrate the final compressed image.
        compressed_image = func.compress_img(input_path,args.c)
        end_time = time.time()
        filename = f'DCT_COEFF_compressed_image_{args.c}.png'
        cv2.imwrite(filename,compressed_image)
        output_path = filename
        output_size = os.path.getsize(output_path)

    elif args.command == 'SVD':
        start_time = time.time()
        # Compression operation is being performed with will return values which help to genrate the final compressed image.
        compressed_image = func.svd_compress(input_path)
        end_time = time.time()
        filename = f'SVD_compressed_image.png'
        cv2.imwrite(filename,compressed_image)
        output_path = filename
        output_size = os.path.getsize(output_path)


    elif args.command == 'PCA':
        start_time = time.time()
        # Compression operation is being performed with will return values which help to genrate the final compressed image.
        print(args.p)
        compressed_image= func.pca_transformed_color(input_path, args.p , args.q)
        end_time = time.time()
        filename = f'PCA_compressed_image_{args.p}_{args.q}.png'
        cv2.imwrite(filename, compressed_image)
        # output_path = 'PCA_compressed_image_{}_{}.png'.format(args.p,args.q)
        output_path = filename
        # print(filename)
        output_size = os.path.getsize(output_path)

    else:
        print("Choose correct method to perform Compression")

input_size = os.path.getsize(input_path)
compression_ratio = input_size / output_size
psnr_value = PSNR.calculate_psnr(input_path,output_path)
print(f"Input size: {input_size} bytes")
print(f"Output size: {output_size} bytes")
print(f"Compression ratio: {compression_ratio:.2f}")
print(f"PSNR: {psnr_value:.3f}")
print("Time: {} ".format(end_time - start_time))

# #Display Compressed and Decompressed images
cv2.imshow("Input image",img)
compressed_img = cv2.imread(output_path)
cv2.imshow("compressed_image",compressed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()



