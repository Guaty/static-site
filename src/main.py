import os
import shutil

from copystatic import copy_dir


path_static = "./static"
path_public = "./public"

def main():
    copy_dir(path_static, path_public)

main()