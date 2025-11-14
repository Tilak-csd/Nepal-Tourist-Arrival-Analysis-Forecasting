# Nepal Tourist Arrival Data Analysis & Forecasting

This project analyzes tourist arrival trends in Nepal from 1992 to 2024, visualizes key patterns, and forecasts future tourist arrivals using Holt's Linear Trend method. The analysis covers pre-COVID, during COVID, and post-COVID periods, with detailed insights by year, month, and country of origin.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset Description](#dataset-description)
- [Features](#features)
- [Data Cleaning & Processing](#data-cleaning--processing)
- [Visualizations](#visualizations)
- [Tourist Arrival Forecasting](#tourist-arrival-forecasting)
- [Installation & Requirements](#installation--requirements)
- [Usage](#usage)
- [License](#license)

## Project Overview
Nepal is a popular tourist destination with diverse cultural and natural attractions. This analysis aims to:

- Understand yearly and monthly tourist arrival trends.
- Evaluate the impact of COVID-19 on tourism.
- Identify tourist arrivals by nationality.
- Forecast tourist arrivals for the next five years.

## Dataset Description
The analysis uses the following datasets:

- **Yearly Tourist Arrival (1992 - 2024):** Total annual tourist arrivals in Nepal.
- **Monthly Arrival Data (1995 - 2023):** Monthly tourist arrivals across different years.
- **Arrival by Country (2014 - 2023):** Tourist arrivals in Nepal by nationality.

## Dataset Files

The project uses the following Excel files, stored in the `EXCEL` folder:

- `data.xlsx`
- `1995 - 2005 monthly arrival list.xlsx`
- `2006 - 2023 monthly arrival list.xlsx`
- `arrival.xlsx`

Processed CSV files are saved in the `CSV` folder:

- `Pre_Covid_Arrival.csv`
- `Covid_Arrival.csv`
- `Post_Covid_Arrival.csv`
- `data.csv`

- 
## Features
- **Time-based Analysis:**
  - Tourist arrivals before COVID (pre-2020)
  - During COVID (2020-2022)
  - After COVID (post-2022)
- **Average Tourist Arrivals:** Computed per COVID timeline.
- **Country Breakdown:** Tourist arrivals per nationality.
- **Growth Rate Analysis:** Year-over-Year (YoY) growth visualization.
- **Forecasting:** Predicting tourist arrivals for the next five years using Holt’s Linear Trend method.

## Data Cleaning & Processing
- Removed duplicates and missing values.
- Filled missing country data with `0` for calculations.
- Converted year column to datetime format.
- Categorized years into pre-COVID, COVID, and post-COVID for trend analysis.

## Visualizations
- **Bar Plot:** Tourist arrivals by COVID timeline.
- **Pie Chart:** Average tourist arrivals by COVID timeline.
- **Line Plot:** Growth rate over years.
- **Bar Plot:** Tourist arrivals per country.

*All plots use formatted y-axis values for better readability (millions or thousands).*

## Tourist Arrival Forecasting
- **Method:** Holt’s Linear Trend Method
- Forecasting is based on recent years’ data (2019-2024) with level (`L`) and trend (`T`) calculation.
- Multi-step forecast is performed to predict arrivals for 2025.
- Visualization shows actual vs forecasted tourist numbers.

## Installation & Requirements
**Python Version:** 3.9+  

**Required Libraries:**
```bash
pip install pandas matplotlib seaborn numpy openpyxl
```
## Usage

1. Place all Excel data files in the `EXCEL` folder.
2. Run the Python script:

```bash
  python main.py
```

3. Visualizations will display automatically. Uncomment plotting functions if necessary.

## License

This project is licensed under the MIT License.  
© 2025 Tilak Man Gubhaju.
Permission is granted to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of this software. The software is provided "as is" without warranty of any kind.


