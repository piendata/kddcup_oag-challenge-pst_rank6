import os
from os.path import abspath, dirname, join


PROJ_DIR = '../data/'
DATA_DIR = '../data/'
OUT_DIR = '../data/'
DIR_PATH = '../data/PST/'

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(OUT_DIR, exist_ok=True)
DATA_TRACE_DIR = DATA_DIR
