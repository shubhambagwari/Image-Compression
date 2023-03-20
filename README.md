# Image-Compression
## Image Compression techniques

### Command to perform compression 
python main.py <Compression_technique> --i <image_path> <optional_arguments>
     eg: python main.py RLE -i P_image.png
 
### For help
python main.py -h

usage: main.py [-h] [--i I] [--s S] [--c C] [--p P] [--q Q] {RLE,HuffC,DCT_QM,DCT_COEFF,SVD,PCA}

Image Compression via diff techniques
positional arguments:
  {RLE,HuffC,DCT_QM,DCT_COEFF,SVD,PCA}

optional arguments:
  -h, --help            show this help message and exit
  --i I                 Give image path
  --s S                 DCT_QM: Quantization Scale
  --c C                 DCT_COEFF: Number of Coefficient to keep
  --p P                 PCA: Varaiance/Percentage
  --q Q                 PCA: Quantization Value

### NOTE: 
Every technique have some deafult parameters. 
Command: python main.py <Compression_technique>
This will also work.
