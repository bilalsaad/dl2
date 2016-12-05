from PIL import Image, ImageDraw, ImageFont
import random
import numpy as np
from bidi.algorithm import get_display
import arabic_reshaper
import os
from scipy.misc import imread, imsave
import itertools
import image_functions

FONT_PREFIX= "/Library/Fonts/"
FONTS = ["Arial Unicode.ttf",
         "Al Nile.ttf",
         "AlBayan.tff",
         "Baghdad.tff",
         "Damascus.tff",
         "DecoTypeNash.tff",
         "Nadeem.ttc"]
DEFAULT_IMAGE_SIZES = [(100, 100), (120, 120)]
DEFAULT_FONT_SIZES = [40, 45, 50, 55, 60]
DEFAULT_LOCATIONS = [(25, 25), (30, 30), (33,33)] 
# this should be probably be dependant on sizes 

# here we want to create data for the words in words.txt
# for each word in words.txt we want to create a directory with ~100 images
def create_images(label,count=100,font_size = 17):
    #  here we want to create count images of label with 
    #  different filters/rotations etc..
    img = Image.new("L", (100, 100),200)
    draw=ImageDraw.Draw(img)
    font=ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", font_size)
    label_correct = arabic_reshaper.reshape(label)
    label_correct = get_display(label_correct)
    draw.text((22,22),label_correct,font=font)
    img.save('pics/' +label + '.png')
    img.close()

# direc + org = path to the picture
# this functions, reads the picture in path and creates different versions of it
# using the functions in image_functions.get()
def create_copies(direc, org, img_id):
    image_data = imread(direc+org).astype(np.float32)
    size = image_data.shape[0] # dimension of the image
    prefix = direc+'/test_out'
    index = 0
    funcs = image_functions.get()
    for f in funcs:
        ims = f(image_data, size)
        for im in ims:
            imsave(prefix + img_id + '-' +str(index) +'.png', im)
            index+=1

# creates a number of images from a single image.
# this function does not take close the picture.
def process_single_image(
        word, label, size, fontsize = 50, loc = (25,25), prefix = ""):
    if not os.path.exists('pics/' + label):
        os.makedirs('pics/' + label)
    img = Image.new("L", size ,256) # greyscale and white background
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", fontsize)
    label_correct = arabic_reshaper.reshape(word)
    label_correct = get_display(label_correct)
    draw.text(loc,label_correct,font=font)
    direc = 'pics/'+label
    img_path = '/' + prefix + 'original .png' 
    img.save(direc + img_path)
    img.close()
    # now we've created the base picture - now we can process it a bit more
    create_copies(direc, img_path, prefix)
    
def create_data(word, label, sizes = DEFAULT_IMAGE_SIZES,
        font_sizes = DEFAULT_FONT_SIZES,
        locations = DEFAULT_LOCATIONS,
        default_dir = 'pics/'):
    i = 0
    for (size, font_size, location) in itertools.product(
            sizes, font_sizes, locations):
        process_single_image(word, label, size, font_size, location, str(i))
        i += 1

def process_word(line,f=create_data):
    line = line.split()
    word, label = unicode(line[0], 'utf-8'), line[1].rstrip()
    f(word,label)

def create_words(f = 'words_and_labels.txt', process=process_word):
    words=open(f, 'r');
    for line in words:
        process(line)
    words.close()

if __name__=='__main__':
    create_words('words_and_labels.txt', process_word);
