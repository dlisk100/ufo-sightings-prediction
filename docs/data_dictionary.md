# Data Dictionary

## Primary Dataset: UFO Sightings

### Source

* Dataset: NUFORC UFO Sightings
* Provider: Kaggle (NUFORC/ufo-sightings)
* Time Range: 1949-2014
* Records: 80,000+

### Fields

| Field Name | Type | Description |
|------------|------|-------------|
| datetime | datetime | Date and time of the sighting |
| city | string | City where the sighting occurred |
| state | string | State/province where the sighting occurred |
| country | string | Country where the sighting occurred |
| shape | string | Shape of the UFO (e.g., circle, triangle, etc.) |
| duration_seconds | float | Duration of the sighting in seconds |
| duration_hours_min | string | Duration in hours/minutes format |
| comments | text | Witness description of the sighting |
| date_posted | datetime | Date the report was posted |
| latitude | float | Latitude of the sighting location |
| longitude | float | Longitude of the sighting location |

## Additional Datasets

### NOAA Weather Data

* Temperature
* Precipitation
* Cloud cover
* Wind conditions
* Visibility
* Other atmospheric conditions

### US Bureau of Economic Analysis (BEA) Data

* GDP by state
* Personal income
* Employment statistics
* Industry-specific economic indicators

### Population Data

* Population density
* Demographic information
* Urban vs. rural classification

### Media Coverage Data

* News articles
* TV coverage
* Social media mentions
* Related events

## Data Integration Plan

The datasets will be integrated using the following methods:

1. Location (latitude/longitude, city, state)
2. Date/time of sightings
3. Regional economic indicators
4. Population density metrics

## Data Quality Notes

### Primary Dataset

* Check for missing values
* Validate coordinates
* Standardize duration formats
* Clean and normalize location names

### Weather Data

* Match closest weather station to sighting location
* Interpolate missing weather data
* Account for time zone differences

### Economic Data

* Handle temporal aggregation (yearly to monthly/daily)
* Account for reporting delays
* Normalize monetary values

### Population Data

* Handle census period interpolation
* Account for population estimate updates
* Standardize geographic boundaries
