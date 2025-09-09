# World Happiness Report 2023 Analysis

## Project Structure
```
World-Happiness-Report-2023-Analysis/
│
├── screenshots                                # Folder containing visualizations and charts
├── README.md                                  # Project documentation
├── WHR2023.csv                                # Dataset
├── World Happiness Report 2023 Analysis.ipynb # Main analysis notebook
└── app.py                                     # Streamlit dashboard  
```

## Tools
- Python
- Pandas
- Plotly Express
- Streamlit

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## Overview
This project analyzes the **World Happiness Report 2023** dataset to uncover global happiness trends, identify key drivers of well-being, and highlight insights relevant for policy-making, economics, and social sciences.  

The project demonstrates:
- **End-to-end data preparation** (loading, cleaning, preprocessing)
- **Exploratory Data Analysis (EDA)** with descriptive statistics
- **Comparative insights** (top/bottom countries by key indicators)
- **Interactive visualizations** using Plotly
- **Professional storytelling** supported by data

## Dataset
The dataset includes multiple factors influencing national happiness:

- **Ladder Score** (overall happiness index)  
- **Logged GDP per capita**  
- **Social Support**  
- **Healthy Life Expectancy**  
- **Freedom to make life choices**  
- **Generosity**  
- **Perceptions of corruption**  
- **Dystopia + Residual** (baseline component used in report calculations)  

## Project Workflow
1. **Data Loading**  
   - Import CSV into a Pandas DataFrame  
   - Inspect structure and features  

2. **Data Cleaning**  
   - Standardize column names  
   - Select relevant variables  
   - Set *Country Name* as index  
   - Handle missing values (rows dropped for consistency)  
   - Verify duplicates (none found)  

3. **Exploratory Data Analysis (EDA)**  
   - Summary statistics for all indicators  
   - Distribution checks (GDP, Social Support, Life Expectancy)  
   - Comparative rankings (Top/Bottom 10 by happiness score, Top 5 by individual factors)  

4. **Key Insights**  
   - Nordic countries dominate global happiness due to strong balance of GDP, social support, and freedom  
   - Life expectancy alone does not guarantee happiness (e.g., Hong Kong, Japan)  
   - Economic prosperity is important but insufficient without governance and freedom (e.g., Lebanon, Cambodia)  
   - Generosity contributes but is not a primary driver of happiness  

5. **Visualizations**  
   - Bar charts and pie charts for top/bottom 10 countries  
   - Scatter plots showing correlations with happiness score:
     - Social Support  
     - Healthy Life Expectancy  
     - Freedom to make life choices  
     - Generosity  
     - Perceptions of corruption  
   - Boxplots for distribution analysis of GDP, Social Support, Life Expectancy  

## Key Findings
- **Top 10 Happiest Countries (2023):** Finland, Denmark, Iceland, Israel, Netherlands, Sweden, Norway, Switzerland, Luxembourg, New Zealand  
- **Bottom 10 Countries (2023):** Afghanistan, Lebanon, Sierra Leone, Zimbabwe, Congo (Kinshasa), Malawi, Comoros, Tanzania, Zambia, India  
- **Major Drivers of Happiness:** Social support and freedom show the strongest correlations with happiness.  
- **Economic Disparities:** High GDP improves happiness, but countries with governance or social issues may still score low despite strong economies.  
- **Trust in Institutions:** Lower perceptions of corruption strongly align with higher well-being.  

## Technologies Used
- **Python 3**  
- **Pandas** – Data cleaning and transformation  
- **Plotly Express** – Interactive data visualizations  
- **Jupyter Notebook** – Analysis workflow  

## Conclusion

The **World Happiness Report 2023** Analysis highlights that happiness is **multifactorial**.
While economic prosperity helps, it is the **combination of wealth, health, social support, freedom, and institutional trust** that drives true well-being.

This analysis demonstrates how **data-driven storytelling** can reveal patterns and insights, helping policymakers and researchers focus on what truly matters for global well-being.
