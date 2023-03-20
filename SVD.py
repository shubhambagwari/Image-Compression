import cv2
import numpy as np

def svd_compress(image_path):
    # Load image
    img = cv2.imread('P_image.png', cv2.IMREAD_COLOR)

    # Convert image to numpy array
    A = np.asarray(img)

    # Perform SVD on each color channel of the image
    U_r, s_r, VT_r = np.linalg.svd(A[:,:,0])
    U_g, s_g, VT_g = np.linalg.svd(A[:,:,1])
    U_b, s_b, VT_b = np.linalg.svd(A[:,:,2])

    # Set number of singular values to keep
    k = 100

    # Construct diagonal matrix of singular values for each color channel
    S_r = np.zeros((A.shape[0], A.shape[1]))
    S_g = np.zeros((A.shape[0], A.shape[1]))
    S_b = np.zeros((A.shape[0], A.shape[1]))
    S_r[:k, :k] = np.diag(s_r[:k])
    S_g[:k, :k] = np.diag(s_g[:k])
    S_b[:k, :k] = np.diag(s_b[:k])

    # Reconstruct compressed image from SVD components
    B_r = np.dot(U_r[:, :k], np.dot(S_r[:k, :k], VT_r[:k, :]))
    B_g = np.dot(U_g[:, :k], np.dot(S_g[:k, :k], VT_g[:k, :]))
    B_b = np.dot(U_b[:, :k], np.dot(S_b[:k, :k], VT_b[:k, :]))
    compressed_img = np.zeros_like(A)
    compressed_img[:,:,0] = B_r
    compressed_img[:,:,1] = B_g
    compressed_img[:,:,2] = B_b

    # Convert back to PIL Image for display
    compressed_img = cv2.cvtColor(compressed_img, cv2.COLOR_BGR2RGB)
    compressed_img = cv2.convertScaleAbs(compressed_img)
    compressed_img = cv2.cvtColor(compressed_img, cv2.COLOR_RGB2BGR)

    return compressed_img
