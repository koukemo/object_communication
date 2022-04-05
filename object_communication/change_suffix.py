import pathlib
import shutil
import os


obj_dir = os.getcwd() + '/src/object_communication/data/'

def change_txt_obj(file_name):
    sf = pathlib.PurePath(obj_dir + file_name + '.txt').suffix

    if sf == '.txt':
        st = pathlib.PurePath(obj_dir + file_name + '.txt').stem
        to_name = st + '.obj'

        shutil.move(obj_dir + file_name + '.txt', obj_dir + to_name)


def change_obj_txt(file_name):
    sf = pathlib.PurePath(obj_dir + file_name + '.obj').suffix

    if sf == '.obj':
        st = pathlib.PurePath(obj_dir + file_name + '.obj').stem
        to_name = st + '.txt'

        shutil.move(obj_dir + file_name + '.obj', obj_dir + to_name)