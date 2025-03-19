#!/usr/bin/env python3
"""
Data Download Script for UFO Sightings Project
This script downloads and prepares all necessary datasets for the project.
"""

import os
import sys
import json
import pandas as pd
from pathlib import Path
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create data directories if they don't exist
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'data'
RAW_DIR = DATA_DIR / 'raw'
PROCESSED_DIR = DATA_DIR / 'processed'
EXTERNAL_DIR = DATA_DIR / 'external'

for dir_path in [RAW_DIR, PROCESSED_DIR, EXTERNAL_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)

def setup_kaggle():
    """Setup Kaggle API credentials"""
    kaggle_dir = Path.home() / '.kaggle'
    kaggle_dir.mkdir(exist_ok=True)
    
    # Check if Kaggle API token exists
    if not (kaggle_dir / 'kaggle.json').exists():
        print("Kaggle API token not found. Please follow these steps:")
        print("1. Go to https://www.kaggle.com/account")
        print("2. Scroll to API section and click 'Create New API Token'")
        print("3. Move the downloaded kaggle.json to ~/.kaggle/kaggle.json")
        print("4. Run this script again")
        sys.exit(1)

def download_ufo_data():
    """Download the UFO Sightings dataset from Kaggle"""
    try:
        import kaggle
        print("Downloading UFO Sightings dataset...")
        kaggle.api.authenticate()
        kaggle.api.dataset_download_files(
            'NUFORC/ufo-sightings',
            path=RAW_DIR,
            unzip=True
        )
        print("UFO dataset downloaded successfully!")
    except Exception as e:
        print(f"Error downloading UFO dataset: {e}")
        sys.exit(1)

def download_weather_data():
    """Download NOAA weather data"""
    # TODO: Implement NOAA API integration
    # Requires API token from https://www.ncdc.noaa.gov/cdo-web/webservices/v2
    print("Weather data download not yet implemented")

def download_economic_data():
    """Download economic data from BEA"""
    # TODO: Implement BEA API integration
    # Requires API key from https://apps.bea.gov/API/signup/
    print("Economic data download not yet implemented")

def download_population_data():
    """Download US Census population data"""
    # TODO: Implement Census API integration
    print("Population data download not yet implemented")

def main():
    """Main execution function"""
    print("Starting data download process...")
    
    # Setup Kaggle credentials
    setup_kaggle()
    
    # Download primary dataset
    download_ufo_data()
    
    # Download additional datasets
    download_weather_data()
    download_economic_data()
    download_population_data()
    
    print("\nData download process completed!")
    print(f"Raw data stored in: {RAW_DIR}")
    print(f"Processed data will be stored in: {PROCESSED_DIR}")
    print(f"External data stored in: {EXTERNAL_DIR}")

if __name__ == "__main__":
    main()
