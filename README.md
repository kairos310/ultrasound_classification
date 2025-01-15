# Authors: Marouf Paul and Kairos Wong

# Ultrasound Classification Project
display.ipynb 
basic classifier on raw data, currently overfitting becasue of small dataset

autoencoder.ipynb
encode signal into 16 dim latent space, then runs classifier on that
result is ranking of "important" features


## Overview
The Ultrasound Classification Project is designed for the analysis and classification of ultrasound signals. Utilizing a larger dataset, the project aims to overcome previous challenges like overfitting and to enhance the accuracy and robustness of the classification models.

## Contents

### Notebooks

#### 1. `display.ipynb`
   - **Purpose**: Implements a basic classifier on raw ultrasound data.
   - **Current Status**: Experiencing overfitting due to a small dataset.

#### 2. `autoencoder.ipynb`
   - **Purpose**: Encodes ultrasound signals into a 16-dimensional latent space, followed by classification.
   - **Output**: Ranks important features, aiding in feature extraction and dimensionality reduction.

#### 3. `parse.ipynb`
   - **Functionality**: Used for parsing and preparing ultrasound data for analysis and model training.

#### 4. `ultrasound_final.ipynb` (Emphasized)
   - **Purpose**: A comprehensive approach to ultrasound signal classification using a larger dataset.
   - **Highlights**: 
     - **Larger Dataset**: Addresses previous limitations by using a more extensive and diverse set of ultrasound data.
     - **Advanced Techniques**: Likely integrates enhanced data preprocessing, feature extraction, and classification models.
     - **Goal**: To improve model performance and generalization, reducing issues like overfitting.
     - **Significance**: Represents a culmination of the project's research and development efforts.

### Scripts

#### 1. `display.py`
   - **Functionality**: Used for data visualization and initial data analysis. Incorporates libraries such as matplotlib, numpy, and tensorflow.

### Data Files

#### 1. `densities.tsv`
   - **Content**: Contains data related to ultrasound signal densities, possibly used for in-depth analysis or modeling.

### Others

#### 1. `.gitignore`
   - **Purpose**: Specifies the files and directories that Git should ignore, including data folders, model files, and specific formats.

## Development Notes
- **Project Phase**: The project is in a developmental stage, focusing on enhancing machine learning applications in ultrasound signal analysis.
- **Future Directions**: Emphasis on using the larger dataset in `ultrasound_final.ipynb` for improved results and potentially exploring new machine learning algorithms or techniques.

