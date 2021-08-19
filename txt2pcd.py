import os, time, sys
import itertools
import threading

import numpy as np
import struct
from open3d import *
from pathlib import Path

fpath = Path("/home/kanakim/Documents/")
fpath = fpath.glob("*.txt")
done = False

def convert_txt_to_pcd(txtFilePath):
    pcd = open3d.read_point_cloud(txtFilePath, format='xyz')
    return pcd

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

if __name__ == "__main__":
    cnt = 0
    t = threading.Thread(target=animate)
    t.start()

    for k in fpath :
        convert_pcd = convert_txt_to_pcd(k)
        open3d.io.write_point_cloud("/home/kanakim/Documents/"+k.stem+".pcd", convert_pcd)
        cnt = cnt + 1

    time.sleep(1)  
    done = True
    print("\rAll ["+str(cnt)+"] *.txt files were converted to *.pcd")

