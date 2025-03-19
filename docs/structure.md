# Project Structure

This document outlines the organization of the UFO Sightings Prediction project.

## Directory Layout

### /data
- Storage for datasets
- Not tracked in git due to size constraints
- Contains both raw and processed data
- Access instructions in data_access.md

### /notebooks
- Jupyter notebooks for analysis
- Naming convention: [number]_[purpose].ipynb (e.g., 01_initial_eda.ipynb)
- Contains templates and examples for team use

### /scripts
- Python scripts for data processing and modeling
- Reusable code that's imported by notebooks
- Data pipeline components
- Utility functions

### /docs
- Project documentation
- Data dictionaries
- Process documentation
- Meeting notes and decisions

### /models
- Trained machine learning models
- Model evaluation results
- Model metadata and parameters
- Serialized model files (if not too large)
