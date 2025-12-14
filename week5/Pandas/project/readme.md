📌 Project Overview

This project is part of my Generative AI learning journey, where I am strengthening my foundations in data handling and preprocessing using Pandas.

The goal of this project is to take a raw, real-world sales dataset and transform it into a clean, structured, analysis-ready dataset using a proper project-based approach instead of ad-hoc notebooks.

This reflects how data is actually prepared before being used in:

Machine Learning models

Analytics dashboards

AI / GenAI pipelines

🗂 Project Structure
week5/
│
├── data/
│   └── sales_data_sample.csv        # Raw dataset (unchanged)
│
├── output/
│   └── cleaned_sales.csv            # Cleaned & processed data
│
├── scripts/
│   └── run_pipeline.py              # End-to-end Pandas pipeline
│
└── README.md
📊 Dataset Description

The dataset contains sales order information, including:

Order details (order number, date, status)

Customer and location details

Product and pricing information

Sales and quantity metrics

This type of dataset is commonly used for business analysis and forecasting.

🧠 What I Learned (Concept-wise)
1️⃣ Loading & Exploring Data

Reading CSV files using pd.read_csv()

Handling encoding issues (latin1)

Inspecting dataset shape, columns, and structure

Understanding how real datasets are organized

2️⃣ Data Cleaning

Converting string dates into proper datetime format

Handling missing values using fillna()

Standardizing categorical data

Removing duplicate records

This step helped me understand that most real-world data is messy and must be cleaned before any analysis or AI work.

3️⃣ Selecting & Filtering Data

Filtering rows based on conditions (e.g. order status, sales threshold)

Applying multiple conditions together

Selecting meaningful subsets of data

This taught me how to extract relevant data instead of working with everything blindly.

4️⃣ Feature Engineering

Extracting year and month from date columns

Creating new calculated columns (e.g. revenue)

Adding derived features to support future analysis

Feature engineering is a critical step before using data in ML or GenAI systems.

5️⃣ Data Pipeline Thinking

Separating raw and processed data

Writing reusable, script-based logic

Using dynamic paths instead of hard-coded file locations

Running the pipeline end-to-end with one command

This shifted my mindset from "learning Pandas" to "building data systems".

⚙️ How to Run the Project

From the project root directory:

python scripts/run_pipeline.py

This will:

Load the raw dataset from data/

Clean and transform the data

Save the final output to output/cleaned_sales.csv

🎯 Key Takeaways

Clean data is the foundation of AI and GenAI applications

Pandas is not just for analysis, but for building data pipelines

Proper project structure makes code reusable and professional

Learning by building real projects leads to deeper understanding

🚀 Next Steps

Perform Exploratory Data Analysis (EDA)

Add visualizations

Connect this cleaned data to ML / GenAI workflows

Extend the pipeline with logging and validation

This project represents hands-on learning, not just theory, as part of my ongoing GenAI journey.