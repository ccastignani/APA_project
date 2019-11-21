APA Project: Cellular morphology
================================

Large-scale measurements of cellular morphology upon perturbations of cells with small molecules.  The morphological (image-based) profiling data is acquired by microscopy and can be mined for various purposes, such as understanding chemical mechanism-of-action or side effects of compounds.

## Data resource

The data source can be found here: https://www.broadinstitute.org/chembio-therapeutics/mlpcnprofiling

## Orientative literature

- Bray et al., 2016 Cell Painting, a high-content image-based assay for morphological profiling using multi-plexed fluorescent dyes
- Ljosa et al., 2013 Comparison of Methods for Image-Based Profiling of Cellular Morphological Responses to Small-Molecule Treatment
- Wang et al., 2016 Drug-induced adverse events prediction with the LINCS L1000 data

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
python3 morphocell.py -i tests/test_data/profiles.txt 
                      -f tests/test_data/features.txt 
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
