import os, time, sys
import itertools
import threading
import numpy as np
import struct
from open3d import *
from pathlib import Path

fpath = Path("/home/kanakim/Documents/")
fpath = fpath.glob("*.bin")
done = False

def convert_bin_to_pcd(binFilePath):
    size_float = 4
    list_pcd = []
    with open(binFilePath, "rb") as f:
        byte = f.read(size_float * 4)
        while byte:
            x, y, z, intensity = struct.unpack("ffff", byte)
            list_pcd.append([x, y, z])
            byte = f.read(size_float * 4)
    np_pcd = np.asarray(list_pcd)
    pcd = PointCloud()
    pcd.points = Vector3dVector(np_pcd)
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
        convert_pcd = convert_bin_to_pcd(k)
        open3d.io.write_point_cloud("/home/kanakim/Documents/"+k.stem+".pcd", convert_pcd)
        cnt = cnt + 1

    time.sleep(1)  
    done = True
    print("\rAll ["+str(cnt)+"] *.bin files were converted to *.pcd")


#open3d.read_point_cloud("./sample/open3d_xyz.txt", format='xyz')
