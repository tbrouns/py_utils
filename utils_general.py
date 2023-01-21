import os


def get_basename_no_ext(filepath):
    return os.path.splitext(os.path.basename(filepath))[0]
