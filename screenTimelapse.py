# python3 author jin xiang
import time
from PIL import ImageGrab
import os
import cv2
import numpy
import argparse


def screenShot():
    im = ImageGrab.grab()
    return im

def PILImage2CVimage(image):
    img = cv2.cvtColor(numpy.asarray(image),cv2.COLOR_RGB2BGR)
    return img

def images_to_video(fps,size_w,size_h,record_time,wait_time,outputName):
    print("strat running...")
    size = (size_w,size_h)
    out = cv2.VideoWriter(outputName, cv2.VideoWriter_fourcc('M','P','4','2'), fps, size)
    loop = record_time//wait_time
    for i in range(loop):
        time.sleep(wait_time)
        out.write(PILImage2CVimage(screenShot()))
    out.release()

if __name__ == '__main__':
    parser = argparse.ArgumentParser("./screenTimelapse.py")
    parser.add_argument(
        '--FPS', '-f',
        type=int,
        required=False,
        default=30,
        help='frames per second',
    )
    parser.add_argument(
        '--width', '-wi',
        type=int,
        required=True,
        help='width pixels'
    )
    parser.add_argument(
        '--height', '-he',
        type=int,
        required=True,
        help='height pixels'
    )
    parser.add_argument(
        '--output', '-o',
        type=str,
        required=True,
        help='output file name'
    )
    parser.add_argument(
        '--record', '-r',
        type=int,
        required=True,
        help='record time(s)'
    )
    parser.add_argument(
        '--wait', '-w',
        type=int,
        required=True,
        help='wait time(s)'
    )
    FLAGS, unparsed = parser.parse_known_args()

    images_to_video(FLAGS.FPS,FLAGS.width,FLAGS.height,FLAGS.record,FLAGS.wait,FLAGS.output)