# Image-Compression

## Image Compression techniques
1. Run Length Encoding(RLE).
2. Huffman Coding.
3. Discrete Cosine Transform(DCT) with  Quantization Scale.
4. Discrete Cosine Transform(DCT) with Number of Coefficient to keep.
5. Singular Value Decomposition(SVD).
6. Principal Component Analysis(PCA) with percentage value and quantization to apply.

### Command to perform compression 
```
python main.py <Compression_technique> --i <image_path> <optional_arguments>
```
```
python main.py RLE --i P_image.png 
```

### For help
```
python main.py -h 
```

usage: main.py [-h] [--i I] [--s S] [--c C] [--p P] [--q Q] {RLE, HuffC, DCT_QM, DCT_COEFF, SVD, PCA} <br>

Image Compression via diff techniques <br>
positional arguments:
  {RLE,HuffC,DCT_QM,DCT_COEFF,SVD,PCA} <br>

optional arguments: <br>
  -h, --help            show this help message and exit  <br>
  --i I                 Give image path <br>
  --s S                 DCT_QM: Quantization Scale     <br>
  --c C                 DCT_COEFF: Number of Coefficient to keep <br>
  --p P                 PCA: Varaiance/Percentage <br>
  --q Q                 PCA: Quantization Value   <br>

### NOTE: 
Every technique have some deafult parameters. If the main file with technique name, the python script will run beacuse manual is optional feature.<br>
**Command**
```
python main.py <Compression_technique>
```

