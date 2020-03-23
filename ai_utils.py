###
# C. Bryan Daniels
# https://github.com/prairie-guy
# 3/24/2018
# ai_utils.py
#
###

__all__ = ['methods_of', 'attributes_of']
import inspect, os, imghdr
from pathlib import Path

# print methods of an object
def methods_of(obj,lr=False):
    for attr in dir(obj):
        if attr.startswith("_"): continue
        try:
            if callable(getattr(obj,str(attr),None)):
                print(f"{attr}{str(inspect.signature(getattr(obj,str(attr), None)))}:")
                if lr==True: print()
        except: pass

# print attributes of an object
def attributes_of(obj, *exclude):
    for attr in dir(obj):
        if attr.startswith("_"): continue
        try:
            if not callable(getattr(obj,str(attr),None)):
                if attr in exclude:
                    print(f"{attr}: ...")
                else:
                    print(f"{attr}: {getattr(obj,attr)}")
        except: pass

"""
ai_utils.py
contains:
atttributes_of(obj, *exclude): -> prints obj attributes
methods_of(obj,lr=False):      -> prints obj methods

usage: import ai_utils

> data = ImageClassifierData.from_paths(PATH, tfms=tfms_from_model(arch, sz))
> attributes_of(data.trn_dl.dataset,'fnames')
c: 2
fnames: ...
is_multi: False
is_reg: False
n: 23000
path: data/dogscats/
sz: 224
y: [0 0 0 ... 1 1 1]

> methods_of(data.trn_dl.dataset)
denorm(arr):
get(tfm, x, y):
get_c():
get_n():
get_sz():
get_x(i):
get_y(i):
resize_imgs(targ, new_path):
transform(im, y=None):
"""
