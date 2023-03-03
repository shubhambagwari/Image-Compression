'''
To perform compression, type the following command
python main.py RLE image2.jpg
'''

from PIL import Image
import os
import RLE
import HuffC
import PSNR
import SSIM


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Image Compression via diff techniques")  
    FUNCTION_MAP = {'RLE' : RLE,
                    'HuffC' : HuffC }
    parser.add_argument('command', choices=FUNCTION_MAP.keys())
    # parser.add_argument("RLEm",help="Run-length encoding technique")
    parser.add_argument("image", help="Give image path")
    args = parser.parse_args()

    func = FUNCTION_MAP[args.command]

    # print("func:",args.command)
    input_path = args.image
    input_image = Image.open(input_path).convert('L')
    input_size = os.path.getsize(input_path)
    if args.command =='RLE':
        encoded_data = func.run_length_encode(input_image)
        output_path = 'output.png'
        output_image = func.run_length_decode(encoded_data, input_image.width, input_image.height)
        

    elif args.command =="HuffC":
        frequencies = input_image.histogram()
        tree = func.build_huffman_tree({i: frequency for i, frequency in enumerate(frequencies) if frequency > 0})
        codewords = func.build_codewords(tree)
        encoded_data = func.encode_image(input_image, codewords)
        output_path = 'output.png'
        output_image = func.decode_image(encoded_data, tree, input_image.width, input_image.height)


    
output_image.save(output_path)       
output_size = os.path.getsize(output_path)
compression_ratio = input_size / output_size
psnr_value = PSNR.calculate_psnr(input_path,output_path)
# ssim_value = SSIM.calculate_ssim(input_path,output_path)
print(f"Input size: {input_size} bytes")
print(f"Output size: {output_size} bytes")
print(f"Compression ratio: {compression_ratio:.2f}")
print(f"PSNR: {psnr_value:.3f}")
# print(f"SSIM: {ssim_value:.3f}")

