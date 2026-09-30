# Dataset

This folder contains the dataset used for risk categorization in the new product development case study.

## Dataset Description

The dataset contains risk-related observations used to identify groups of similar risks through unsupervised learning.

The main variables used in the clustering analysis are:

| Variable | Description        |
| -------- | ------------------ |
| `Code`   | Risk identifier    |
| `P`      | Risk-related score |
| `R`      | Risk-related score |
| `F`      | Risk-related score |
| `C`      | Risk-related score |

The dataset contains 39 risk observations.

## File

* `Data.xlsx` — dataset used as input for the clustering analysis.

## Usage

The clustering scripts in the `src/` directory read the relevant worksheet from this Excel file.

The dataset is included in this repository because it is suitable for public sharing for this project and does not identify the specific factory by name.
