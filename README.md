APA Project: Cellular morphology
================================

Large-scale measurements of cellular morphology upon perturbations of cells with small molecules.  The morphological (image-based) profiling data is acquired by microscopy and can be mined for various purposes, such as understanding chemical mechanism-of-action or side effects of compounds.

## Data resource

The data source can be found here: https://www.broadinstitute.org/chembio-therapeutics/mlpcnprofiling

## Orientative literature

- Bray et al., 2016 Cell Painting, a high-content image-based assay for morphological profiling using multi-plexed fluorescent dyes
- Ljosa et al., 2013 Comparison of Methods for Image-Based Profiling of Cellular Morphological Responses to Small-Molecule Treatment
- Wang et al., 2016 Drug-induced adverse events prediction with the LINCS L1000 data

Our Strategy
============

We thought to tackle the problem in a way that the user can re-use our code as a package. With this idea in mind, we wanted to create a reusable kd tree, and after some thinking and research, we found a way to create a kd tree that is reusable (is not modified when retrieving neighbors) and very fast. The inconvenience is that if we look for the k the nearest neighbors, we won't get the real k nearest neighbors, but instead we would get a very good approximation of those.

Once the tree is build, our strategy is to prune for branches that are out of the scope from the search (that the node is inside the area of our target, or in other words, every dimension of the node is inside every dimension ± the distance of the target). 

Installation
============

The easiest way to install morphocell is to download the repo and install via setup.py with:

    python setup.py install

Alternaively, if you don't want to install anything, you can move the script located inside bin folder, to the root of the project and execute it from there.

Tests
=====

Test are implemented using `pytest` and `pytest-cov` packages. So to run test simply call:

    /path/to/project/morphocell pytest

And to view the coverage: 

    /path/to/project/morphocell pytest --cov=morphocell tests/

Usage
=====

### Quick Start

#### Inputs 

```
-i  Imaging profiles file (REQUIRED)
-f  Feature names file (REQUIRED)
-c  Compound ID to which the distances should be calculated
-d  Distance threshold
-k  Number of max Nearest Neighbours
-l  Features to be used
--normalize
```
You can find small examples on how the required files should look like in the test folder. 

The specified compund ID is the compound for which the k-nearest neighbours are found.

You can add as many feature names as you wish after the -l parameter. These features will be the ones used for both the construction of the KD tree as well as the k-nearest neighbour search.

If the normalize option is selected, feature values will be normalized before constructing the KD tree. The normalization procedure consists in deviding each value by the sum of the values of that feature for all the compounds.


#### Example
Here a quick example you can run on the test data we provided: 
```
morphocell  -i /path/to/pdb/folder/profiles.txt 
            -f /path/to/pdb/folder/features.txt 
            -c BRD-K05686172-001-01-6 
            -d 50  
            -k 10 
            -l Cells_AreaShape_EulerNumber Cells_AreaShape_Perimeter 
            --normalize
```


Authors
=======

The project has been done as part of the APA subject from the [Universitat Pompeu Fabra](https://www.upf.edu/)'s [MCs in Bioinformatics for Heath Sciences](https://www.upf.edu/web/bioinformatics/), by the following authors:

- Castignani, Carla
- Pradas, Gerard
- Santus, Luisa
