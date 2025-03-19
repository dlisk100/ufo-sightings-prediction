# UFO Sightings Prediction

A data science project to predict UFO sighting locations and durations using historical data. This project is being developed by a team of 4 NYU Stern MBA students.

## Project Overview
### Objective and Dataset
- **Objective**: Predict UFO sighting locations and durations using comprehensive historical data for media/government use
- **Primary Dataset**: Complete Kaggle UFO sightings dataset (80,000+ records, 1949-2014)
- **Additional Data Sources**:
  - NOAA weather data
  - US Bureau of Economic Analysis GDP data
  - Population density data
  - Media coverage data
  - Additional UFO databases and reports

## Project Structure
### Directory Organization
- `/data`: Datasets storage (not tracked in git for large files)
- `/notebooks`: Jupyter notebooks for analysis
- `/scripts`: Python scripts for data processing
- `/docs`: Project documentation
- `/models`: Machine learning models

## Getting Started
### Local Development
#### Cloning the Repository
1. Clone the repository:
```bash
git clone https://github.com/dlisk100/ufo-sightings-prediction.git
cd ufo-sightings-prediction
```

#### Setting Up the Development Environment
2. Set up the development environment:
#### For Mac/Linux Users
```bash
./setup.sh
```
#### For Windows Users
```batch
setup.bat
```
This will:
- Create a virtual environment
- Activate the virtual environment
- Install all required dependencies

### Activating the Virtual Environment
3. Activate the virtual environment (for subsequent sessions):
#### For Mac/Linux
```bash
source venv/bin/activate
```
#### For Windows
```batch
venv\Scripts\activate.bat
```

### Google Colab Integration

To work with this repository in Google Colab:

1. Open [Google Colab](https://colab.research.google.com)
2. Click `File` → `Open notebook`
3. Select the `GitHub` tab
4. Enter the repository URL: `https://github.com/dlisk100/ufo-sightings-prediction`
5. Choose the notebook you want to work on

#### Saving Changes Back to GitHub

1. Mount your Google Drive (if needed for data):
```python
from google.colab import drive
drive.mount('/content/drive')
```

2. Clone the repository and configure Git:
```python
!git clone https://github.com/dlisk100/ufo-sightings-prediction.git
%cd ufo-sightings-prediction

!git config --global user.email "your.email@example.com"
!git config --global user.name "Your Name"
```

3. After making changes, commit and push:
```python
!git add .
!git commit -m "Update notebook with new analysis"
!git push
```

Note: For pushing changes, you'll need to authenticate with GitHub. We recommend using a [Personal Access Token](https://github.com/settings/tokens) for authentication.

## Branching Strategy
- `main`: Stable production code
- `feature/*`: Individual feature branches (e.g., `feature/data-cleaning`)
- Use pull requests for code review and merging

## Project Milestones
- Week 2: Data Collection Complete
- Week 4: Exploratory Data Analysis Complete
- Week 6: Initial Model Development
- Week 8: Model Refinement and Validation

## Professor Feedback Response
This project emphasizes descriptive analysis and practical model applications, particularly focusing on media use cases such as news coverage planning. We are working with a focused subset of U.S. sightings from 2000-2014 to ensure thorough analysis within project constraints.
