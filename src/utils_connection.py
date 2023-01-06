#!/usr/bin/env python
# coding: utf-8

# In[2]:


# We import some existent libraries 

import pandas as pd
from tifffile import imread
import napari
from skimage import restoration
import skimage.filters as filters
from skimage.morphology import disk
from skimage import morphology
from skimage.feature import peak_local_max
from skimage.morphology import convex_hull_image
from skimage.segmentation import watershed
from scipy import ndimage as ndi
import numpy as np
import pandas as pd
from skimage import measure
import matplotlib.pyplot as plt
import tifffile
from scipy import ndimage as ndi
import skimage
from skimage.color import rgb2gray
from typing import List
from magicgui import magicgui
from napari.types import ImageData, LabelsData, LayerDataTuple
import numpy as np
import glob
from skimage import feature
from sklearn.neighbors import NearestNeighbors


# Here are some useful functions for the notebook : How are cells connected ? 

# In[3]:


def mask_invertion(mask_cell_label):
    """
    Inverse a mask (= inverse the values of a label : here create a mask of the membranes)

    Arguments:
        mask_cell_label (arr): the array with each cell labelised in a single label

    Returns:
        arr: the inversed mask (=the label of the membranes)
    """
    mask_inverted = mask_cell_label
    mask_inverted = np.where(mask_cell_label!=0, 0, mask_inverted)
    mask_inverted = np.where(mask_cell_label==0, 1, mask_inverted)
    return mask_inverted


# In[4]:


def membrane_thinning(mask_inverted):
    """
    Thin a label (= here thin the membranes of the cells)

    Arguments:
        mask_inverted (arr): the array of the labelised membranes

    Returns:
        arr: the array of the thinned membranes 
    """
    mask_membrane_thin = skimage.morphology.thin(mask_inverted)
    return mask_membrane_thin


# In[5]:


def membrane_connection_definition(mask_membrane_thin, connection_footprint):
    """
    Create a label with each pixel labelised with the number of its neighbors' pixels labelised

    Arguments:
        mask_membrane_thin (arr): the array of the thinned membranes
        connection_footprint(arr) : the size of the neighbors' matrix 
    Returns:
        arr: the array of each pixel labelised with the number of its neighbors' pixels labelised
    """
    membrane_connection = skimage.filters.rank.sum(mask_membrane_thin, connection_footprint)
    return membrane_connection


# In[6]:


def connection_point_maskification(membrane_connection):
    """
    Create a label with each base of the branches (= the connection points of the membranes)

    Arguments:
        membrane_connection (arr): the array of each pixel labelised with the number of its neighbors' pixels labelised
    Returns:
        arr: the label with each base of the branches (= the connection points of the membranes)
    """
    connection_point = membrane_connection.copy()
    connection_point[membrane_connection > 2] = 1
    connection_point[membrane_connection <= 2] = 0
    return connection_point


# In[7]:


def connection_point_unique_labelisation(connection_point):
    """
    Create a unique label for each base of the branches (= the connection points of the membranes)

    Arguments:
        connection_point (arr): the label with each base of the branches (= the connection points of the membranes)
    Returns:
        arr: the array with unique label for each base of the branches (= the connection points of the membranes)
    """
    connection_point_unique_label = skimage.morphology.label(connection_point)
    return connection_point_unique_label


# In[ ]:


def total_junctions_count(connection_point_unique_label):
    """
    Count the number base of the branches (=connection points of the membranes)

    Arguments:
        connection_point_unique_label (arr): the array with unique label for each base of the branches 
        				     (= the connection points of the membranes)
    Returns:
        int: the number base of the branches (=connection points of the membranes)
    """
    unique_values = np.unique(connection_point_unique_label)
    total_junctions_number = len(unique_values)
    return total_junctions_number


# In[ ]:


def dataframe_total_junctions_coordinates_creation(connection_point_unique_label):
    """
    Create a dataframe with the coordinates of each connection points of the membranes

    Arguments:
        connection_point_unique_label (arr): the array with unique label for each base of the branches 
        				     (= the connection points of the membranes)
    Returns:
        DataFrame: dataframe with the coordinates of each connection points of the membranes in to columns
    """
    props = measure.regionprops_table(
        connection_point_unique_label,
        properties = ['label', 'centroid']
        )
    df_total_junctions_coordinates = pd.DataFrame(props)
    return df_total_junctions_coordinates


# In[ ]


def get_nearest_neighbors(total_junctions_centroids_coordinates):
    """
    Give the distance between each connection points of the membranes and their 2 nearest neighbors
    Arguments:
        total_junctions_centroids_coordinates (arr): array of the coordinates of each connection points of the membranes
    Returns:
        arr: distance between each connection points of the membranes and their 2 nearest neighbors (the first is themselves so its
             always 0)
    """
    nbrs = NearestNeighbors(n_neighbors = 2, algorithm = "ball_tree").fit(total_junctions_centroids_coordinates)
    distances, indices = nbrs.kneighbors(total_junctions_centroids_coordinates)
    return distances


# In[ ]


def get_non_triangular_junctions_dataframe(total_junctions_centroids_coordinates, distances):
    """
    Create a dataframe with the coordinates of each non triangular junctions of the membranes

    Arguments:
        total_junctions_centroids_coordinates (arr): array of the coordinates of each connection points of the membranes
        distances (arr): distance between each connection points of the membranes and their 2 nearest neighbors 
        (the first is themselves so its always 0)
    Returns:
        DataFrame: dataframe with the coordinates of each non triangular junctions of the membranes
    """
    non_triangular_junctions_array = total_junctions_centroids_coordinates[distances[:, 1]<10]
    df_non_triangular_junctions = pd.DataFrame(non_triangular_junctions_array, columns = ['axis-0','axis-1'])
    return df_non_triangular_junctions
