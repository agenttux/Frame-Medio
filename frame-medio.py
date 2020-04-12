import os
import numpy as np
from PIL import Image
from tqdm import tqdm

filename = input(
    "What file do you want to get the average frame of? Filename: ")
if os.path.isfile(filename):
    os.system("mkdir imagesTMP")
    frames = input(
        "How many frames per second do you use in your average? (24/1 = every frame, 1 = 1 image per second, 1/600 = 1 image every 10 minutes) Number: ")
    command = "ffmpeg -i " + filename + " -r " + \
        frames + " imagesTMP/output%07d.png"
    outname = input("What should the output file be called? Name: ")
    os.system(command)
    os.chdir("imagesTMP")
    images = os.listdir()
    # Assuming all images are the same size, get dimensions of first image
    w, h = Image.open(images[0]).size
    N = len(images)

    # Create a numpy array of floats to store the average (assume RGB images)
    arr = np.zeros((h, w, 3), np.float)

    # Build up average pixel intensities, casting each image as an array of floats
    for im in tqdm(images):
        imarr = np.array(Image.open(im), dtype=np.float)
        arr = arr+imarr
    arr = arr/N
    # Round values in array and cast as 8-bit integer
    arr = np.array(np.round(arr), dtype=np.uint8)

    # Generate, save and preview final image
    out = Image.fromarray(arr, mode="RGB")
    os.chdir("..")
    out.save(outname + '.png')
    os.system("rm -rf imagesTMP")  # delete temporary directory
else:
    print("File does not exist!")
