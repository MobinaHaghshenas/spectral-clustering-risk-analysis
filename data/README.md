# Dataset

This folder contains the data and case-study context used in the risk categorization analysis.

## Case Study Context

The case study focuses on risks associated with **New Product Development (NPD)** in the agriculture industry.

The risks were identified through a combination of literature review and input from experts within the organization. Additional risks were identified through brainstorming sessions with seven organizational experts.

Due to confidentiality considerations, the detailed descriptions of the individual risks are not disclosed. Instead, the study provides the overall risk breakdown structure and assigns numerical codes to the risks used in the analysis.

## NPD Risk Structure

The risk structure considered in the case study is organized into five main categories:

* Production Risks
* Financial Risks
* Organizational Risks
* Technical Risks
* Marketing Risks

The following diagram illustrates the risk breakdown structure of the New Product Development case study.

![NPD Risk Structure](figures/npd-risk-structure.png)

The structure includes more specific risk areas such as production-related challenges, financial factors, organizational issues, technical risks, and marketing-related factors.

## Dataset

The dataset contains **39 risk observations**.

Before entering the clustering model, each risk was assigned a numerical code. The quantitative data represents the characteristics and intensity of the risks in relation to project objectives.

The main variables used in the clustering analysis are:

| Variable | Description                                |
| -------- | ------------------------------------------ |
| `Code`   | Numerical identifier assigned to each risk |
| `P`      | Risk-related project objective score       |
| `R`      | Risk-related project objective score       |
| `F`      | Risk-related project objective score       |
| `C`      | Risk-related project objective score       |

The detailed interpretation of the project-objective dimensions follows the case-study formulation.

## Files

### `Data.xlsx`

The Excel dataset used as input for the clustering analysis.

The relevant data table contains the coded risks and the quantitative variables used by the clustering algorithms.

### `npd-risk-structure.png`

The NPD risk breakdown structure used to provide context for the case study.

## Data Preparation and Analysis

The dataset is used in the following analytical workflow:

```text
Coded Risk Data
      ↓
Data Preparation
      ↓
Hopkins Test
      ↓
Elbow Method + Gap Statistic
      ↓
Spectral Clustering
      ↓
Cluster Validation
      ↓
Risk Categorization
```

The dataset initially passed the Hopkins test with a value of approximately **0.747**. The Elbow Method and Gap Statistic were then used to determine the appropriate number of clusters, resulting in four clusters for the subsequent Spectral Clustering analysis.

The complete analytical implementation is available in the `src/` directory.
