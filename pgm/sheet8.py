#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 17:42:18 2017

@author: catherine
"""

import networkx as nx
import matplotlib.pyplot as plt
from scipy import misc
import random


def denoise(image1,w11,w01):
    """ denoises the image using graphcuts"""

    x,y = image1.shape
    #load test images
    
    #construct vertices and edges between pixels
    G=nx.grid_2d_graph(x,y)
    G.add_nodes_from(['s','t'])
    
    #add weights and edges to s and t
    ws = 1
    wt = 1
    
    for i in range(x):
        for j in range(y):
            colorij = image1[i,j]
            for n in nx.all_neighbors(G,(i,j)):
                if image1[n] != colorij:
                    G.edge[n][(i,j)]['capacity']=w01
                else:
                    G.edge[n][(i,j)]['capacity']=w11
            if colorij==0:
                G.add_edge((i,j),'s')
                G.edge[(i,j)]['s']['capacity']=ws
            else:
                G.add_edge((i,j),'t')
                G.edge[(i,j)]['t']['capacity']=wt
                
    # get minimum cut
    cut_value, partition = nx.minimum_cut(G,'s','t')
    reachable,non_reachable = partition
    #G.remove_edges_from(list(partition))
    
    for n in reachable:
        if 's' not in n:
            image1[n]=0
    for n in non_reachable:
        if 't' not in n:
            image1[n]=255
    return image1


# task 1
image_name = 'ex2test'
image_name2 = 'a'
w11=3
w01=1

image1 = misc.imread('Assignment8/' + image_name + '.png') 
image2 = misc.imread('Assignment8/' + image_name2 + '.png') 

"""
image1 = denoise(image1,w11,w01)
misc.imsave( 'Assignment8/' +image_name + '_denoised_w11='+ str(w11) + '_w01='+ str(w01) + '.png', image1)

image2 = denoise(image2,w11,w01)
misc.imsave( 'Assignment8/' +image_name2 + '_denoised_w11='+ str(w11) + '_w01='+ str(w01) + '.png', image2)
"""
# task 2
def add_noise(image,flip_prob,name="",save=True):
    x,y = image.shape
    for i in range(x):
       for j in range(y):
           if random.random() <= flip_prob:
               image[i,j] = abs(image[i,j] - 255)
    misc.imsave( 'Assignment8/' +name + '_fp='+ str(flip_prob)  + '.png', image)
    return image

fp = 0.5
w11 = 2
w01 = 1
       
image1 = add_noise(image1,fp,image_name)
image2 = add_noise(image2,fp,image_name2)

image1 = denoise(image1,w11,w01)
misc.imsave( 'Assignment8/' +image_name +'_fp='+ str(fp)  + '_denoised_w11='+ str(w11) + '_w01='+ str(w01) + '.png', image1)

image2 = denoise(image2,w11,w01)
misc.imsave( 'Assignment8/' +image_name2 +'_fp='+ str(fp)  +'_denoised_w11='+ str(w11) + '_w01='+ str(w01) + '.png', image2)


#display graph
#nx.draw(G)
#plt.savefig("path.png")

