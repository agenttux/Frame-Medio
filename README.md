# Frame Medio

Frame Medio is a Python 3 script that outputs the average frame of an input video as a .png file.

## Requirements

Frame Medio requires `ffmpeg`[https://ffmpeg.org/download.html] and `python3`[https://www.python.org/].

## Installation

Install the requirements.

```bash

pip install -r requirements.txt
```

## Usage

Run the `frame-medio.py` script.

```bash
python3 frame-medio.py
What file do you want to get the average frame of? Filename: <path to input file>
How many frames per second do you use in your average? (24/1 = every frame, 1 = 1 image per second, 1/600 = 1 image every 10 minutes) Number: <frames per second to use in analysis>
What should the output file be called? Name: <output file name (don't add any extensions to the end of this)>
```

## Samples

The running scene from 1917 with 1 frame taken every 5 seconds (1/300):
![1917](samples/1917-12-fpm.png)

Luke and Vader's duel from The Empire Strikes Back with 1 frame taken every second:
![ESB](samples/duel-1-fps.png)

Isle of Dogs sushi scene with 24 frames taken every second:
![sushi](samples/wes-24-fps.png)

Swedish House Mafia's Ultra 2018 set with 1 frame taken every second:
!![SHM](samples/shm-1-fps.png)

## License

[MIT](https://choosealicense.com/licenses/mit/)
