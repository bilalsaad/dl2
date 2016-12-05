
import random
from glob import glob
import os
import shutil


def create_test_set(path = '/media/pics/train/*'):
    dirs = glob(path) #the directories of the images
    # we want to pick a random sample of 420 from 2220
    # then we want to move those images from each dir to pics/test/#n
    sample = random.sample(xrange(2220), 420)
    for direc in dirs:
        comps = direc.split("/")
        pics = glob(direc +'/*.png')
        c_dst = '/media/pics/test/'
        for src in [pics[i] for i in sample]:
            dst = c_dst + comps[-1] + '/'
            if not os.path.exists(dst):
                os.makedirs(dst)
            shutil.move(src, dst)
