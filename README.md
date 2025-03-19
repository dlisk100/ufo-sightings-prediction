# UFO Sightings Prediction

A data science project to predict UFO sighting locations and durations using historical data. This project is being developed by a team of 4 NYU Stern MBA students.

## Project Overview
- **Objective**: Predict UFO sighting locations and durations using historical data for media/government use
- **Primary Dataset**: Kaggle UFO sightings dataset (80,000+ records, 1949-2014)
- **Additional Data**: Weather data, GDP, and other relevant sources will be integrated

## Project Structure
- `/data`: Datasets storage (not tracked in git for large files)
- `/notebooks`: Jupyter notebooks for analysis
- `/scripts`: Python scripts for data processing
- `/docs`: Project documentation
- `/models`: Machine learning models

## Getting Started
1. Clone the repository
```bash
git clone https://github.com/[username]/ufo-sightings-prediction.git
cd ufo-sightings-prediction
```

2. Create and activate virtual environment
```bash
# Using venv (Python 3.9)
python3.9 -m venv venv
source venv/bin/activate  # On Unix/macOS
# or
venv\Scripts\activate  # On Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Branching Strategy
- `main`: Stable production code
- `feature/*`: Individual feature branches (e.g., feature/data-cleaning)
- Use pull requests for code review and merging

## Project Milestones
- Week 2: Data Collection Complete
- Week 4: Exploratory Data Analysis Complete
- Week 6: Initial Model Development
- Week 8: Model Refinement and Validation

## Professor Feedback Response
This project emphasizes descriptive analysis and practical model applications, particularly focusing on media use cases such as news coverage planning. We are working with a focused subset of U.S. sightings from 2000-2014 to ensure thorough analysis within project constraints.
