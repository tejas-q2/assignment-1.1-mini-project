Project: Superstore Sales Analysis
Project Overview

This project involves the analysis of the Superstore" dataset to identify key insights into sales, profit, and regional performance. The workflow included sourcing the data, cleaning and preparing it using Python, and finally, creating visualizations and performing in-depth analysis in Microsoft Power BI.
1. Data Source

The raw data used for this project was the "Sample - Superstore" dataset, which was downloaded from Kaggle. This dataset contains detailed information on orders, products, customers, and shipping for a fictional superstore.
2. Data Cleaning & Preparation (Python)

Before the analysis could begin, the raw data required significant cleaning and preparation. A series of Python scripts using the pandas library were created to perform the following tasks:

Loading Data: The initial .csv file was loaded into a pandas DataFrame.

Duplicate Removal: All duplicate rows were identified and removed to ensure the integrity of the analysis.

Handling Missing Values: Missing postal codes were filled in using the most frequently occurring postal code in the dataset.

3. BI Analysis & Visualization (Power BI)

The cleaned CSV file was imported into Microsoft Power BI. Within Power BI's Power Query Editor, some final manual data transformations were performed to fix any remaining state name inconsistencies that were not addressed in the Python script.

Once the data was fully prepared, it was used to build an interactive dashboard to analyze key business metrics, including:

Sales and profit by region and state.

Performance of different product categories.

Customer segment analysis.
