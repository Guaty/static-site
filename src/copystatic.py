import os
import shutil


def copy_dir(source, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)
    list_dir = os.listdir(source)

    for item in list_dir:
        src_path = os.path.join(source, item)
        dest_path = os.path.join(dest, item)
        print((src_path, dest_path))

        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        elif os.path.isdir(src_path):
            copy_dir(src_path, dest_path)