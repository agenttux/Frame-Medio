import os
filename = input(
    "What file do you want to get the average frame of? Filename: ")
if os.path.isfile(filename):
    os.system("mkdir imagesTMP")
    frames = input(
        "How many frames per second do you use in your average? (24/1 = every frame, 1 = 1 image per second, 1/600 = 1 image every 10 minutes) Number: ")
    command = "ffmpeg -i " + filename + " -r " + \
        frames + " imagesTMP/output%07d.png"
    os.system(command)
    os.chdir("imagesTMP")
    images = os.listdir()
    with open("output0000001.png", "rb") as image:
        f = image.read()
        b = bytearray(f)
    os.chdir("..")
    with open('output.png', 'wb') as output:
        output.write(b)
    os.system("rm -rf imagesTMP")  # delete temporary directory
else:
    print("File does not exist!")
