# Image-Compression

## Description: 
This is a Python program for image compression using various techniques. The program allows the user to compress images using different techniques like: <br>
1. Run Length Encoding(RLE).
2. Huffman Coding.
3. Discrete Cosine Transform(DCT) with  Quantization Scale.
4. Discrete Cosine Transform(DCT) with Number of Coefficient to keep.
5. Singular Value Decomposition(SVD).
6. Principal Component Analysis(PCA) with percentage value and quantization to apply.

### Usage
To compress an image, use the following command:
```
python main.py <Compression_technique> --i <image_path> <optional_arguments>
```
For example, to compress an image using RLE, use the following command:
```
python main.py RLE --i P_image.png 
```
To get help, use the following command:
```
python main.py -h 
```

usage: ``` main.py [-h] [--i I] [--s S] [--c C] [--p P] [--q Q] {RLE, HuffC, DCT_QM, DCT_COEFF, SVD, PCA} ```

Image Compression via diff techniques <br>
positional arguments:
 ``` {RLE,HuffC,DCT_QM,DCT_COEFF,SVD,PCA} ```

### Optional arguments: <br>
 ```
 -h --help            show this help message and exit  
    --i  I            Give image path 
    --s  S            DCT_QM: Quantization Scale     
    --c  C            DCT_COEFF: Number of Coefficient to keep 
    --p  P            PCA: Varaiance/Percentage 
    --q  Q            PCA: Quantization Value   
```
### NOTE: 
Every technique has some default parameters. The main file can also run with just technique names because of these default parameters.<br>
**Command**
```
python main.py <Compression_technique>
```

