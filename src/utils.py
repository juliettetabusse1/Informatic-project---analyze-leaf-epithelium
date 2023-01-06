#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# Here are some useful functions for the notebooks : Cell segmentation, How many cells and How can we infer cell expansion.


# In[ ]:


def img_greying(img_original):
    """
    Convert a rgb image in a greyscale image.

    Arguments:
        img_original (arr): the rgb image

    Returns:
        arr: the greyscale image
    """
    img_grey = rgb2gray(img_original)
    return img_grey


# In[ ]:


def img_blurring(img_grey, blurring_intensity):
    """
    Blur an image.

    Arguments:
        img_grey (arr): the image to blur
        blurring_intensity(int) : the insensity of blurring 

    Returns:
        arr: the blurred image
    """
    img_blurred = filters.median(img_grey, footprint=np.ones((blurring_intensity, blurring_intensity)))
    return img_blurred


# In[ ]:


def cell_maskification(img_blurred, local_threshold_block_size):
     """
    Create a label from an image (more precisely a label of the cells)

    Arguments:
        img_blurred (arr): the image of which we want a mask
        local_threshold_block_size(int) : local neighborhoods of each pixel

    Returns:
        arr: the label of the image 
    """
    local_threshold = filters.threshold_local(img_blurred, block_size=local_threshold_block_size)
    mask_cell = img_blurred > local_threshold
    return mask_cell


# In[ ]:


def smooth(mask_cell, closing_radius, opening_radius):
    """
    Smooth the small holes and objects of a label

    Arguments:
        mask_cell (arr): the label to smooth
        closing_radius(int) : the erosion dilation intensity
        opening_radius(int) : the dilation erosion intensity

    Returns:
        arr: the smoothed label
    """
    mask_cell = morphology.binary_closing(mask_cell, morphology.disk(closing_radius))
    mask_smooth = morphology.binary_opening(mask_cell, morphology.disk(opening_radius))
    return mask_smooth


# In[ ]:


def small_hole_removing(mask_smooth, min_size_hole):
    """
    Remove the small holes in the label

    Arguments:
        mask_smooth (arr): the label of which the small holes are gonna be removed
        min_size_hole(int) : the minimum size of the holes

    Returns:
        arr: the label without small holes
    """
    mask_no_small_hole = skimage.morphology.remove_small_holes(mask_smooth, min_size_hole)
    return mask_no_small_hole



# In[ ]:


def small_object_removing(mask_no_small_hole, min_size_object):
    """
    Remove the small object in the label

    Arguments:
        mask_no_small_hole (arr): the label of which the small objects are gonna be removed
        min_size_object(int) : the minimum size of the objects

    Returns:
        arr: the label without small objects
    """
    mask_no_small_object = skimage.morphology.remove_small_objects(mask_no_small_hole, min_size_object)
    return mask_no_small_object


# In[ ]:


def cell_erosion(mask_no_small_hole, erosion_radius):
      """
    Errode the label

    Arguments:
        mask_no_small_hole (arr): the label we want to errode
        erosion_radius(int) : the errosion intensity

    Returns:
        arr: the label erroded
    """
    footprint = morphology.disk(erosion_radius)
    mask_eroded = morphology.binary_erosion(mask_no_small_hole, footprint)
    return mask_eroded


# In[ ]:


def cell_labelisation(mask_eroded):
    """
    Make a unique label for each object of a label (= make a unique label for each cell)

    Arguments:
        mask_eroded (arr): the label from which we want to isolate the cells in single labels 

    Returns:
        arr: the cell labelised
    """
    mask_cell_label = skimage.morphology.label(mask_eroded)
    return mask_cell_label


# In[ ]:


def cell_count(mask_cell_label):
    """
    Count the number of labels in an array (= count the number of cells)

    Arguments:
        mask_cell_label (arr): the array with each cell labelised in a single label

    Returns:
        int: the number of labels (=the number of cells)
    """
    unique_values = np.unique(mask_cell_label)
    cell_number = len(unique_values)
    return cell_number


# In[ ]:

def dataframe_cells_centroid_creation(mask_cell_label):
    """
    Create a dataframe of the centroid coordinates of each cell

    Arguments:
        mask_cell_label (arr): the array with each cell labelised in a single label

    Returns:
        DataFrame: the table with 3 columns : label (= the number of one cell), 
        			              centroid-0 (= the axis 0 cell coordinate),
        			              centroid-1 (= the axis 1 cell coordinate)
    """
    props = measure.regionprops_table(
        mask_cell_label,
        properties = ['label', 'centroid']
        )
    df_cells_centroid = pd.DataFrame(props)
    return df_cells_centroid
    
    
   
   # In[ ]:
   
def convex_hull(mask):
    """
    Measure the convex hull permeter of the cells

    Arguments:
        mask (arr): the array with each cell labelised in a single label

    Returns:
        int: the cell convex hull perimeter
    """
	convex_hull = convex_hull_image(mask)
	convex_hull_perimeter = measure.perimeter(convex_hull)
	return convex_hull_perimeter
    
    
    
    
    
