import cv2
import os, time, sys
import itertools
import threading
import numpy as np
import struct
from pathlib import Path

fpath = Path("/media/psf/kandisk/20210825/20210825_154516/cam/cam4/data/")
fpath = fpath.glob("*.mp4")
done = False

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

if __name__=="__main__" :
    t = threading.Thread(target=animate)
    t.start()

    file_count = 0

    for k in fpath :
        count = 0
        vidcap = cv2.VideoCapture(str(k))
        success,image = vidcap.read()
        while success:
            if count ==0 or count%30 == 0 :
                cv2.imwrite("/media/psf/Karucial X6/2D/210825/02/"+"%d.png" % file_count, image)     # save frame as JPEG file      
                file_count = file_count + 1
            success,image = vidcap.read()
            count = count+1
        print("\r"+str(k)+" done")
    time.sleep(1)
    done = True