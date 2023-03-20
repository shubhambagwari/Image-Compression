import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import cv2

def pca_transformed_color(img, percentage, num_bits):
    img = cv2.imread(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert from BGR to RGB
    img_flat = img.reshape((-1, 3)).astype(np.float32) # reshape to a 2D array
    img_flat /= 255.0 # scale pixel values to the range [0, 1]
    percentage = percentage / 100
    tsqizzle_pca = PCA(n_components=percentage).fit(img_flat)
    transformed = tsqizzle_pca.transform(img_flat)

    # Quantization
    transformed /= (1.0 / (2 ** num_bits))
    transformed = np.round(transformed)
    transformed *= (1.0 / (2 ** num_bits))

    projection = tsqizzle_pca.inverse_transform(transformed)
    projection *= 255.0 # rescale pixel values back to the range [0, 255]
    projection = projection.reshape(img.shape) # reshape to original shape
    projection = cv2.cvtColor(projection, cv2.COLOR_RGB2BGR) # convert from RGB to BGR
    return projection
    # cv2.imwrite('PCA_output.png', projection)



