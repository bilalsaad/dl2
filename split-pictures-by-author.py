# classifies images under their author, the author is the second number in the 
# file name.

import glob
import os
import shutil

# Given a path of an image it will extract the author name.
def author_name(x): 
    clean_name = os.path.basename(x)
    return clean_name.split("-", 2)[1]

# Creates a directory 'authors' with subwords of that author under it.
def create_author_dirs(ds):
    authors = {}
    def create_author_dir(authors, author):
        if authors.has_key(author):
            # this key exists just the value
            return authors.get(author)
        # If the author does not exist create the appropriate directory and
        # return it.
        path = os.path.join('authors/', author)
        if not os.path.exists(path):
            os.makedirs(path)
        authors[author] = path
        return path
    for d in ds:
        for f in glob.glob(d+"/*"):
            author = author_name(f)
            author_path = create_author_dir(authors, author)
            #shutil.copyfile(f,
             #       os.path.join(author_path, os.path.basename(f)))

TRAIN_GLOB = 'train/*'
TEST_GLOB = 'test/*'

train_dirs = glob.glob(TRAIN_GLOB)
test_dirs = glob.glob(TEST_GLOB)

create_author_dirs(train_dirs)
create_author_dirs(test_dirs)

