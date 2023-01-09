<!-- Output copied to clipboard! -->

<!-----

Yay, no errors, warnings, or alerts!

Conversion time: 1.038 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β34
* Fri Jan 06 2023 09:20:13 GMT-0800 (PST)
* Source doc: README
* Tables are currently converted to HTML tables.
----->


**<span style="text-decoration:underline;">Introduction</span> :**

Plants are living organisms absorbing water and inorganic substances through their roots, and synthesizing nutrients in their leaves by photosynthesis using the green pigment chlorophyll. The epidermis[^1] and its waxy cuticle provides a protective barrier against mechanical injury, water loss, and infection. The main difference between epidermis and epithelium[^2] is that epidermis is the outermost protective layer of the skin of animals whereas epithelium is one of the four types of tissues in the plants. The epithelium occurs in both plants and animals. Epithelium is a layer of cells that form a continuous sheet which cover surfaces that may come in contact with foreign substances. Indeed, the leaf epithelia is very important for plants, as it acts as a protective layer, and an exchanger of gas and water. Studying its structure and organization can help to understand how plants develop. The aim of our project was to analyze the shape of the cells in leaf epithelia using image analysis techniques. All cells are surrounded by a membrane[^3] that separates the cytoplasm from the extracellular matrix and helps in maintaining the cell structure and function. Moreover, the cell wall[^4] is a semi-rigid thick protective structure that surrounds the cell membrane of some types of cells for protection and defining the shape of the cell. An important notion to introduce in this project is Turgor pressure which causes the cell wall to expand during growth. It is the force exerted by stored water against a cell wall. As water fills the cells, it pushes against the cell membrane and cell wall, producing turgor pressure. Plants use their turgor pressure[^5] to create various forms and regulate the turgor pressure in their cells by directing water into specialized vacuoles. Turgor Pressure induces mechanical stress in the cell wall, which is the ratio of the force acting on a cross-section of the material (cell wall) scaled by the area of the material resisting the force.

Microtubules[^6] are also very important in the development of plants. They are made of α-tubulin and β-tubulin and use the hydrolysis of GTP_. _Different types of microtubules exist, such as kinetochore microtubules, polar microtubules, astral microtubules, or cortical microtubules which direct the deposition of cellulose fibrils in the cell wall. Microtubules play different roles in the cell (in the meiosis, the mitosis, the transport of vesicles…) and particularly in  plant cell[ morphogenesis](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/morphogenesis). Indeed, they constrain the movement of cellulose synthase complexes, which is important for elongation growth in plants. 

In our project, we studied different types of plant’s epitheliums images, with different types of cross sections: adaxial cross sections (Directed to the axis or stem), and abaxial cross sections (which is attached parallel to the axis, away from the axis or stem). All the images have been colored with the toluidine blue staining. We will answer three questions, a basic thiazine metachromatic dye which colors the membranes and the cell walls. How are cells connected? How can we infer the cell expansion direction? How many cells are there? 

**<span style="text-decoration:underline;">Python dependencies</span> : **

We used jupyter notebooks to code for this project. We needed to install some libraries : 



* matplotlib
* napari
* pandas
* numpy
* skimage 
* seaborn 
* glob

You can install these libraries from your terminal as follow :

‘pip install “napari[all]'

‘pip install scikit-image pandas numpy matplotlib scipy scikit-images’

‘conda install seaborn -c conda-forge’

‘pip install -U scikit-learn’

**<span style="text-decoration:underline;">"How to use" tutorials</span> :** 


    **<span style="text-decoration:underline;">Different types of cells:</span>** 

<span style="text-decoration:underline;">Group 1:</span> composed of rounded cells with stomata. These cells are moderately colored. 

![group 1 cell type](/docs/example_groupe_1.png?raw=true "Group 1 cell type")

<span style="text-decoration:underline;">Group 2:</span> Cells with a geometric form, and visible veinous, moderately colored. 

![group 2 cell type](/docs/example_groupe_2.png?raw=true "Group 2 cell type")

<span style="text-decoration:underline;">Group 3</span>: Cells with a puzzle shape, and a pale dyeing.

According to the article Why plants make puzzle cells, and how their shape emerges, we find this type of cells in the leaves, because it reduces the stress in the epidermal cell walls.

![group 3 cell type](/docs/example_cellules_groupe_3.png?raw=true "Group 3 cell type")

<span style="text-decoration:underline;">Group 4:</span> Cells which have a geometric form and a visible nucleus, and some stomates. These images of cells are dark or moderately dyeing. 

![group 4 cell type](/docs/example_cellules_groupe_4.png?raw=true "Group 4 cell type")

<span style="text-decoration:underline;">Group 5</span>: Cells with a long form, moderately dyeing or a pale dyeing. These cells had an anisotropic growth, which is an advantageous strategy as it limits the stress magnitude. 

![group 5 cell type](/docs/example_cellules_groupe_2.png?raw=true "Group 5 cell type")

**      <span style="text-decoration:underline;">Database structure</span> : **

How database is composed of:** **



* One folder with the cell database: <span style="text-decoration:underline;">“FDV_cell_database”</span>:

    Each file is named like this: 


![image name type](/docs/csv_organization.png?raw=true "image name type")



* One folder with the leaves database: <span style="text-decoration:underline;">“FDV_leaf_database”</span>

    Each file is a photo with the name of the plants species. 

* The <span style="text-decoration:underline;">global database</span>:

    An excel file in which we can find 4 columns:


    First, the plant name is written. After that, we have the cell name, the leaf identity with the image magnification. Finally, the leaf orientation (adaxial or abaxial) is written. 


    _<span style="text-decoration:underline;">exemple:</span>_


<table>
  <tr>
   <td colspan="5" >
Astragalus_penduliflorus,3-06-700x-1-01,3.6,abaxial
<p>
<strong>      <span style="text-decoration:underline;"> Cleaning the database: </span></strong>
<p>
We chose to only keep cell plant images without stomatal pores and also we got rid of those with thick shady lines we think would be an obstacle to our segmentation process. 
<ul>

<li>For the 3.07 images, we kept the stomata. We did it because during the segmentation of these images, some little cells were erased. As a consequence,  the presence of the stomata counterbalanced the ab

<li>For the 3.15 images, we just removed the images with very dark shadows (corresponding to the venous). 

<li>For the 4.01, 7.23 and 6.21 images, we removed those with stomates because it was too complicated to make the difference between these stomates and cells during the segmentation.

<li>For the 4.17 images, we kept those which had a form of puzzle, and removed all the images with visible venous. 

<li>We kept all the 4.02 and the 4.15 images because it was possible to distinguish the limits of the cells under the shadows of the venous. 

<li>For the 6.19 images, we removed those with dark shadows.

<li>We kept all the 7.24 images even if there were some stomates because there were not abundant, so the error during the segmentation was very low. 

<p>
After having selected all the images that we wanted to remove, we also removed them from the global database. This way, we created the cell database cleaned.
</li>
</ul>
   </td>
  </tr>
</table>


<span style="text-decoration:underline;">Cell segmentation : </span>

You can find the code of this part in the Notebook “Cell segmentation”.



*   Goal of the cell segmentation:

![segmentation](/docs/segmentation.png?raw=true "Segmentation")



* First, you can find in the Notebook the useful functions from the script save in the src folder and the important libraries to import. 
* You write the data folder path 
* Once you have selected the images of the different groups according to the precedents criterions, you choose your parameters. The different parameters that are needed are:
* The blurring intensity: This parameter corresponds to the intensity of blurring (10 for all type of cells)/
* The local threshold: This parameter corresponds to the local neighborhood of each pixel (35 for the cells which have a lot of contrast of color inside of them, 15 for the other cells). 
* The closing radius: This parameter corresponds to the erosion dilation intensity (2 for all types of cells)
* The opening radius : This parameter corresponds to the dilation erosion intensity (1 for all types of cells). 
* The erosion radius : This parameter corresponds to the erosion intensity (3 for all types of cells)
* The minimum size of the object (2000 for all types of cells)
* The minimum size of the holes (3000 for the cells that have a nucleus at the center of their structure, and 2000 for the others).
* When you have changed all the parameters, you can run the code.
* Limits of our code:

    The cells of some images can be counted twice or more. Moreover, some cells can be canceled or counted several times. If some cells are not counted and others are counted too much time, it can compensate and give a good result. Another limit of our code is that it doesn’t work with all epithelial cells. Indeed, it works with clear images, with epithelial cells without dark venous, and cells which are very well delimited. 

* Link of our Notebook: [https://drive.google.com/file/d/1e5l3oWzIp-Iv6jONZbOk7shKcxM1GvOe/view?usp=share_link](https://drive.google.com/file/d/1e5l3oWzIp-Iv6jONZbOk7shKcxM1GvOe/view?usp=share_link) 

<span style="text-decoration:underline;">How many cells</span> ?

You can find the code of this part in the Notebook “How many cells?”.



* Goal of this Notebook: 

![how many cells](/docs/How_many_cells.png?raw=true "How many cells")



* First, you can find in the Notebook the useful functions from the script save in the src folder and the important libraries to import. 
* You write the data folder path
* After that, the user has to import his csv containing the cell database cleaned, with the different groups that we made. 
* The global function uses the different steps of the segmentation and several parameters that the user must enter in the function: the blurring intensity, the local threshold, the closing and the opening radius, the minimum size hole, the minimum size object, and finally, the erosion radius. 
* After that, the user can run the code for each group.
* The final step of the code is the creation of the final csv. The user just has to change the name of the csv file if he wants. 
* Limits:  This code does not work for all type of epithelium. Indeed, as for the segmentation, it works with clear images, with epithelial cells without dark veins, and cells which are very well delimited.
* Link of our notebook : [https://drive.google.com/file/d/10sbviTnL-2t-55f5dCraNL3Jse3oBGik/view?usp=share_link](https://drive.google.com/file/d/10sbviTnL-2t-55f5dCraNL3Jse3oBGik/view?usp=share_link)  

<span style="text-decoration:underline;">How are cells connected</span> ?

In this notebook we answer the following question : how are cells connected ? First we count the number of non triangular junctions between cells per image and create a csv with their coordinates. Then we create another csv resuming the number of non triangular junctions between cells and the total number of junctions per image but also the name of the first csv corresponding to the image. Finally we will sum up our finding on a bar plot.



* The goal of this notebook is : 

![How are cells connected](/docs/How_are_cells_connected.png?raw=true "How are cells connected")



* First, we imported our csv containing the cell database cleaned, with the different groups that we made, the libraries to import and useful functions from the script save in the src folder. 
* You write the data folder path 
* You can create a csv of the  non triangular junctions for each images following steps : 
* You create an empty dataframe df_how_cells_are_connected
* Since you start from the mask created and saved in the cell segmentation notebook you just have to inverse the mask to highlight the membranes instead of the cells
* Then you create the skeleton of the membrane and you can compute the neighborhood of each pixel
* You compute the connection point between the cell membranes and assign each of them a single label
* You compute the total number of junctions and create a dataframe and an array with the coordinates of their centroid
* You compute the distance between each centroid and their nearest neighbors
* You then just have to create a dataframe of the non triangular junctions coordinates and compute their number for each image
* You can finally create and save the non_triangular_junctions-image_name.csv file
* You can also from this point file the df_how_cells_are_connected dataframe and convert it to a csv
* You can now sum up all your data by creating a bar plot of number of non triangular junction according to the plant species just by adding the column “plant_name” to your dataframe df_how_cells_are_connected

<span style="text-decoration:underline;">How can we infer the cell expansion directions</span> ? 

![How can we infer the cell expansion directions ](/docs/How_can_we infer_the_cell_expansion_directions .png?raw=true "How can we infer the cell expansion directions ")

In this notebook, we want to make the figures 6.A (but with violin plot rather than bar plot) and 6.C from the article “Why plants make puzzle cells, and how their shape emerges",_ A. Sapala et al_ with our cleaned database.  



* First, we imported our csv containing the cell database cleaned, with the different groups that we made, the libraries to import and useful functions from the script save in the src folder. 
* You write the data folder path 
* You can create a “parametric map” of the morphogenesis quantification criteria as intermediate results in the Notebook to check if the segmentation works. Indeed, we get a parametric map of our mask with little cells in blue and bigger cells in red. 
* For that you start from the masks. Let’s create a csv for each image composed of a dataframe with the labels, area of each cell, perimeter of each cell and the perimeter of the convex hull of each cell. 
* Then, make a general csv composed of a dataframe with the name of the image, the area of the cells of the image, the species and the lobeyness along with the plant-code needed. 
* Now let’s make a violin plot to get the quantification of cell shape (lobeyness) for every specie :
*  To make this you have to install and import seaborn and use the components of the general dataframe. 
* Use the lobeyness which is as the perimeter of the cell divided by the perimeter of its convex hull that we sorted by species. The convex hull of a shape or a group of points is a tight convex boundary around the points or the shape. So you measure the convex hull perimeter with skimage and a function created using the mask. 
* Then, make a scatter plot with seaborn of the lobeyness according to the area of the cell of the image for every specie:
*  For this, you use again the components of the dataframe, the lobeyness and cell area that was measured with skimage with the masks. 

<span style="text-decoration:underline;">Results limits :</span>

Regarding our results on our two graphs, if we look at the violin plot, we can see that we have coherent violins because the quantification of cell shape or lobeyness is higher for the puzzled cell images and lower for those that have a more geometric shape. Indeed on our scatter graph, we observe that the smaller the area, the greater the lobeyness of the cell. 

Now, regarding the limits of our results, our violin graph is not perfect, the values spread over a large range which might be because of the segmentation of the image. If we had more time, I would try to take this into account to modify our segmentation which could always be improved with the parameters. We also don’t see the outlayer on this graph because our violins are small. What’s more, we don’t have a parametric map of our lobeyness which could be a good possibility.


<!-- Footnotes themselves at the bottom. -->
## Notes

[^1]:
     _Source: britannica.com_

[^2]:
     _Source: britannica.com_

[^3]:
     _Source: biologyonline.com_

[^4]:
     _Source: biologyonline.com_

[^5]:
     _Source: “Why plants make puzzle cells, and how their shape emerges” (2018)<span style="text-decoration:underline;"> https://elifesciences.org/articles/32794</span>_

[^6]:
     _Source:_ _ ¨Microtubule dynamics, Rebecca Heald, Eva Nogales (2002) _
    _[https://journals.biologists.com/jcs/article/115/1/3/2723/Microtubule-dynamics](https://journals.biologists.com/jcs/article/115/1/3/2723/Microtubule-dynamics) _
    _ ¨Microtubule dynamics, Rebecca Heald, Eva Nogales (2002) _
    _[https://journals.biologists.com/jcs/article/115/1/3/2723/Microtubule-dynamics](https://journals.biologists.com/jcs/article/115/1/3/2723/Microtubule-dynamics) _
    _Progress in understanding the role of microtubules in plant cells (2004)_[https://www.sciencedirect.com/science/article/abs/pii/S1369526604001293](https://www.sciencedirect.com/science/article/abs/pii/S1369526604001293) 
    _Why plants make puzzle cells, and how their shape emerges _
    _[https://elifesciences.org/articles/32794](https://elifesciences.org/articles/32794) _
