# BrickView-Guvi-Project
My first Guvi HCL Project
# BrickView: Real Estate Analytics Platform

*BrickView* is an interactive real estate analytics dashboard built using Python, SQL, and Streamlit.
It helps users analyze property listings, sales trends, agent performance, and buyer behavior through data-driven insights and visualizations.

## Objectives

* Analyze real estate listings and pricing trends
* Track agent performance and sales efficiency
* Understand buyer behavior and financing patterns
* Provide an interactive dashboard with filters and visual insights

## Installation Setup
### Clone the repository

```bash
git clone https://github.com/your-username/BrickView.git
cd BrickView
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run data pipeline

```bash
cd scripts

python data_cleaning.py
python create_db.py
python insert_data.py
```

### Run Streamlit app

```bash
cd ../app
streamlit run app.py

## Features

### Filters

* City selection
* Property type selection
* Price range filtering

### Visualizations

* Average price by city (Bar chart)
* Sales trend over time (Line chart)
* Property type distribution
* Interactive map of listings

### SQL Insights

* Pricing trends
* Sales performance
* Agent performance
* Buyer behavior

### CRUD Operations

* Add new listings
* Delete listings
* View database records

## Key SQL Queries

* Average listing price by city
* Monthly sales trend
* Property type distribution
* Top-performing agents

## Results

* Built a full-featured real estate dashboard
* Generated actionable insights using SQL queries
* Created an interactive UI for data exploration
* Implemented end-to-end data pipeline

## Future Enhancements

* Multi-page Streamlit navigation
* Advanced visualizations using Plotly
* Machine learning for price prediction
* Deployment on Streamlit Cloud

## Learning Outcomes

* Data cleaning and preprocessing
* SQL database design and querying
* Dashboard development using Streamlit
* End-to-end project implementation

---
