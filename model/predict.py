
# coding: utf-8

# In[92]:
caffe_root = '/home/xllau/PSPNet/'  # this file is expected to be in {caffe_root}/examples
import sys
sys.path.insert(0, caffe_root + 'python')

sys.path.insert(0,'../')

import caffe  

# coding=utf-8  
import os
import numpy as np
from matplotlib import pyplot as plt  
#import cv2
import shutil
import time
from PIL import Image

net_pretrained='../psp_10000.caffemodel'  
net_model_file='./deploy.prototxt'   
net = caffe.Net(net_model_file, net_pretrained, caffe.TEST)

caffe.set_device(0)
caffe.set_mode_gpu()

# In[93]:
dir = '../image/'

file_name_im = dir + 'um_000026.png'

print file_name_im

im = Image.open(file_name_im)


#start to predict
in_ = np.array(im, dtype=np.float32)
in_ = in_[:,:,::-1]
in_ -= np.array((103.939, 116.779,123.68), dtype=np.float32)
in_ = in_.transpose((2,0,1))

#    print gt.size[0], gt.size[1]
#    print in_.shape
out = np.zeros((gt.size[1],gt.size[0]),dtype = np.uint8)
#    print out.shape

crop_h = 233
crop_w = 713
in_crop = np.zeros((3,crop_h,crop_w),dtype = np.float32)
#first cut
in_crop = in_[:,-crop_h: ,:crop_w]
net.blobs['data'].reshape(1, *in_crop.shape)
net.blobs['data'].data[...] = in_crop
net.forward();
out_crop = net.blobs['conv6_interp'].data[0].argmax(axis=0)
out[-crop_h: ,0:350] = out_crop[:,0:350]
#second crop
in_crop = in_[:,-crop_h: ,250:crop_w+250]
net.blobs['data'].reshape(1, *in_crop.shape)
net.blobs['data'].data[...] = in_crop
net.forward();
out_crop = net.blobs['conv6_interp'].data[0].argmax(axis=0)
out[-crop_h: ,350:150+crop_w] = out_crop[:,100:crop_w - 100]

#third cut
in_crop = in_[:,-crop_h: ,-crop_w:]
net.blobs['data'].reshape(1, *in_crop.shape)
net.blobs['data'].data[...] = in_crop
net.forward();
out_crop = net.blobs['conv6_interp'].data[0].argmax(axis=0)
out[-crop_h: ,-400:] = out_crop[:,-400:]

name = names_gt[i]
print 'save image' + name[17:]   
plt.imsave('../'+name[17:],out)
     



