from skimage.metrics import structural_similarity
import cv2
import numpy as np

def calculate_ssim(image1, image2):
	image1 = cv2.imread(image1)
	image2 = cv2.imread(image2)

	(score, diff) = structural_similarity(image1, image2, full=True)
	return score