# Data Immersion & Wrangling Project


## 📌 Project Overview
This project focuses on Data Immersion and Data Wrangling using an IMDb movie dataset. 
The objective is to assess data quality, clean inconsistencies, and transform the dataset 
for further analysis.

## 📂 Dataset
- Source: IMDb
- Format: CSV
- Contains movie metadata, ratings, revenue, votes, etc.

## 🎯 Project Objectives
1. Data Quality Assessment
2. Data Cleaning
3. Data Transformation
4. Exploratory Data Analysis

## 🛠 Tools Used
- Python
- Pandas
- NumPy
- VS code

## 📊 Process
### 1️⃣ Data Immersion
- Understanding dataset structure
- Checking column names
- Identifying missing values
- Checking duplicates

### 2️⃣ Data Quality Assessment
- Missing value analysis
- Data type validation
- Outlier detection
- Inconsistency checks

### 3️⃣ Data Cleaning & Transformation
- Handling null values
- Removing duplicates
- Converting data types
- Feature engineering

## 📖 Data Dictionary

### 📌 Overview
This Data Dictionary provides structured definitions and descriptions of the dataset used in this project.  
The dataset is sourced from IMDb and contains detailed information about movies, ratings, and financial performance.

---

## 🎬 IMDB Movie Dataset

**Name:** imdb_movie_dataset  

**Description:**  
A cleaned movie dataset containing metadata, performance indicators, and audience engagement metrics.  
The dataset has been preprocessed to remove inconsistencies and ensure accurate analysis.

---

## 📊 Column Details

| Column Name       | Data Type | Description                                              | Relevance to Analysis |
|------------------|-----------|----------------------------------------------------------|-----------------------|
| movie_id         | String    | Unique identifier for each movie                        | Helps avoid duplicate records |
| title            | String    | Name of the movie                                       | Used for identification and reporting |
| release_year     | Integer   | Year the movie was released                             | Used for trend analysis over time |
| genre            | String    | Category of the movie (Drama, Action, etc.)             | Analyze rating and income by genre |
| duration_minutes | Integer   | Length of the movie in minutes                          | Study duration vs rating trends |
| country          | String    | Country of production                                   | Country-wise comparison |
| content_rating   | String    | Age classification (PG, R, etc.)                        | Audience segmentation analysis |
| director         | String    | Name of the director                                    | Director performance trends |
| income_usd       | Float     | Total box office revenue in USD                         | Financial performance analysis |
| votes            | Integer   | Number of audience votes                                | Measures popularity |
| imdb_score       | Float     | IMDb rating score (0–10)                                | Main performance indicator |

---

## 📈 Outcome
Cleaned and structured dataset ready for analysis.
