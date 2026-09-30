# Spectral Clustering for New Product Development Risk Analysis

**A data-driven case study for categorizing new product development risks using unsupervised learning and Spectral Clustering.**

## Overview

Risk management in new product development involves multiple risks with different characteristics and potential impacts.

This project applies an unsupervised machine learning approach to identify groups of similar risks and support data-driven risk categorization.

The analysis combines statistical assessment, cluster-number selection methods, and Spectral Clustering to identify meaningful risk groups.

---

## Problem

A set of risks associated with new product development needs to be categorized into meaningful groups.

Instead of assigning predefined labels, this project investigates whether the underlying structure of the data can be used to discover natural groups of similar risks.

The main question is:

> Can unsupervised learning be used to identify meaningful risk categories from the available risk-related data?

---

## Objective

The objectives of this project are to:

* Evaluate whether the dataset contains a meaningful clustering structure.
* Determine an appropriate number of clusters.
* Apply Spectral Clustering to categorize the risks.
* Evaluate the resulting clusters.
* Interpret the identified risk groups in the context of new product development.

---

## Dataset

The dataset contains **39 risk observations** and the main variables used in the clustering analysis are:

* `Code`
* `P`
* `R`
* `F`
* `C`

The dataset is provided in:

```text
data/Data.xlsx
```

The dataset used in this repository does not identify the specific factory by name and is included for reproducibility of the analysis.

---

## Methodology

The complete analytical workflow is:

```text
Risk Data
    ↓
Data Preparation
    ↓
Hopkins Test
    ↓
Determine Number of Clusters
    ↓
Elbow Method + Gap Statistic
    ↓
Spectral Clustering
    ↓
Cluster Evaluation
    ↓
Risk Interpretation
```

### 1. Hopkins Test

The Hopkins statistic is used to assess whether the observations exhibit a tendency toward clustering.

The analysis produced a mean Hopkins statistic of approximately **0.747** across repeated calculations, indicating a clustering tendency in the dataset.

### 2. Elbow Method

The Elbow Method is used to examine how within-cluster variation changes as the number of clusters increases.

The resulting analysis supports considering **four clusters** for the final clustering stage.

### 3. Gap Statistic

The Gap Statistic provides an additional criterion for determining the appropriate number of clusters.

The maximum Gap Statistic in the analysis occurs at **four clusters**.

### 4. Spectral Clustering

Spectral Clustering is then applied using four clusters.

The implementation uses the risk-related feature dimensions to identify groups of observations with similar characteristics.

### 5. Cluster Evaluation

The resulting clusters are evaluated using clustering validation measures and by examining the characteristics of the observations assigned to each group.

---

## Results

The final analysis identifies **four risk clusters**.

The clusters can be interpreted in relation to different areas of the new product development environment, including:

* Process and new product development
* Incremental growth
* Management across the value chain
* Market and environmental factors

The resulting groups provide a data-driven categorization of the risks rather than relying only on manually predefined categories.

### Visual Results

#### Elbow Method

![Elbow Method](results/figures/elbow-method.png)

#### Gap Statistic

![Gap Statistic](results/figures/gap-statistic.png)

#### Spectral Clustering

![Spectral Clusters](results/figures/spectral-clusters.png)

#### Cluster Characteristics

![Cluster Scores](results/figures/cluster-scores.png)

---

## How to Run

Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the analysis scripts in the following order:

```bash
python src/01_hopkins_test.py
python src/02_elbow_method.py
python src/03_gap_statistic.py
python src/04_spectral_clustering.py
```

The dataset used by the analysis is located at:

```text
data/Data.xlsx
```

---

## Key Takeaway

This project demonstrates an end-to-end unsupervised learning workflow for a real-world risk categorization problem:

**data → clustering validation → model selection → unsupervised learning → evaluation → business interpretation**

The project combines machine learning methodology with a practical decision-support problem in new product development.

---

## Reference

**Haghshenas, M., & Ashrafi, M. (2023). "Spectral clustering for effective risk categorization in new product development: a case study", The 19th Iranian International Industrial Engineering Conference (IIIEC 2023), Amirkabir University of Technology, Tehran, Iran.**

