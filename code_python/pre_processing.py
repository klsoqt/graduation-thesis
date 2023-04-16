import os
import sys
import cv2
import numpy as np
from PIL import Image, ImageEnhance

def change_brightness(img, alpha, beta):
    img_new = np.asarray(alpha * img + beta, dtype=int)  # cast pixel values to int
    img_new[img_new > 255] = 255
    img_new[img_new < 0] = 0
    return img_new

def gauss_noise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.1
    sigma = var ** 0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss
    return noisy

def salt_pepper_noise(image):
    row, col, ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    out = np.copy(image)
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
    out[coords] = 1

    # Pepper mode
    num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
    out[coords] = 0
    return out

def poisson_noise(image):
    vals = len(np.unique(image))
    vals = 2 ** np.ceil(np.log2(vals))
    noisy = np.random.poisson(image * vals) / float(vals)
    return noisy

def speckle_noise(image):
    row, col, ch = image.shape
    gauss = np.random.randn(row, col, ch)
    gauss = gauss.reshape(row, col, ch)
    noisy = image + image * gauss
    return noisy

if __name__ == "__main__":
    #doc anh
    path = "C:/Users/khiem/OneDrive/Desktop/dataset/data/"
    imgs_name = os.listdir(path)
    #print(imgs_name)

    # # #resize
    # dim = (416, 416)
    # for img_name in imgs_name:
    #     # print(img_name)
    #     img = cv2.imread(path + img_name)
    #     img_resized = cv2.resize(img, dim)
    #     os.chdir("C:/Users/khiem/OneDrive/Desktop/dataset_chess/resized")
    #     cv2.imwrite(img_name, img_resized)


    # #chinh sang
    alpha = 0.5
    beta = 50
    if len(sys.argv) == 3:
        alpha = float(sys.argv[1])
        beta = int(sys.argv[2])
    for img_name in imgs_name:
        img = cv2.imread(path + img_name)
        img_new = change_brightness(img, alpha, beta)
        os.chdir("C:/Users/khiem/OneDrive/Desktop/dataset/0.5_50/")
        cv2.imwrite(img_name, img_new)

    # #them nhieu gauss
    # for img_name in imgs_name:
    #     img = cv2.imread(path + img_name)
    #     img_new = gauss_noise(img)
    #     os.chdir("C:/Users/khiem/OneDrive/Desktop/dataset_chess/gauss")
    #     cv2.imwrite(img_name, img_new)

    # #them nhieu salt and pepper
    # for img_name in imgs_name:
    #     img = cv2.imread(path + img_name)
    #     img_new = salt_pepper_noise(img)
    #     os.chdir("C:/Users/khiem/OneDrive/Desktop/dataset_chess/salt_pepper")
    #     cv2.imwrite(img_name, img_new)

    # #them nhieu poisson
    # for img_name in imgs_name:
    #     img = cv2.imread(path + img_name)
    #     img_new = poisson_noise(img)
    #     os.chdir("C:/Users/khiem/OneDrive/Desktop/dataset_chess/poisson")
    #     cv2.imwrite(img_name, img_new)
    #
    # #them nhieu speckle
    # for img_name in imgs_name:
    #     img = cv2.imread(path + img_name)
    #     img_new = speckle_noise(img)
    #     os.chdir("C:/Users/khiem/OneDrive/Desktop/dataset_chess/speckle")
    #     cv2.imwrite(img_name, img_new)