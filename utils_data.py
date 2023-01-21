import configparser
import pickle

import yaml
from yaml.loader import SafeLoader


def save_pickle(pickle_path, save_object):
    with open(pickle_path, "wb") as handle:
        pickle.dump(save_object, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load_pickle(pickle_path):
    with open(pickle_path, "rb") as handle:
        return pickle.load(handle)


def load_yaml(yaml_path):
    with open(yaml_path) as f:
        data = yaml.load(f, Loader=SafeLoader)
    return data


def load_txt(txt_path):
    with open(txt_path) as f:
        lines = f.readlines()
    return lines


def load_ini(ini_path):
    config = configparser.ConfigParser()
    config.read(ini_path)
    return config
