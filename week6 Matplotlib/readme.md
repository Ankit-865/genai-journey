# 📊 Matplotlib Sales Data Visualization Project

This project documents my **step-by-step learning journey of Matplotlib**, starting from loading a real-world dataset to building meaningful visualizations using **Pandas + Matplotlib**.

This is part of my **GENAI-JOURNEY → Week 6 (Matplotlib)** learning track.

---

## 📁 Project Structure

```
week6 Matplotlib/
└── project/
    ├── mpl_script.py        # Main Matplotlib visualization script
    ├── sales_data.csv       # Sales dataset
    ├── mpl_workings.py      # Practice / experimentation file
    ├── mpb.py               # Additional matplotlib basics
    ├── output.png           # Saved visualization output (optional)
    └── README.md            # Project documentation
```

---

## 🎯 Project Objective

The main goal of this project was to:

* Learn **Matplotlib from scratch**
* Understand how to **load and explore datasets** using Pandas
* Build **meaningful visualizations** for data analysis
* Learn **correct project structure and file handling**
* Apply **industry-level best practices** for Python scripts

---

## 📦 Dataset Overview

The dataset (`sales_data.csv`) is a **real-world sales dataset** containing:

* Order details
* Product categories
* Monthly and yearly sales information
* Quantity and pricing data

### Key Columns Used

| Column Name   | Description                 |
| ------------- | --------------------------- |
| `SALES`       | Total sales value per order |
| `PRODUCTLINE` | Product category            |
| `MONTH_ID`    | Month of the order          |
| `YEAR_ID`     | Year of the order           |

---

## 🧠 What I Learned (Step-by-Step)

### 1️⃣ Loading Data Correctly

I learned that Python reads files relative to the **current working directory**, not the script location.

To avoid `FileNotFoundError`, I used a **safe and professional approach**:

```python
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "sales_data.csv")
```

This ensures the dataset is always found, no matter where the script is run from.

---

### 2️⃣ Basic Data Exploration

Before plotting, I explored the dataset using:

* `df.head()` → preview first 5 rows
* `df.info()` → understand data types & null values

This step helped me understand what kind of visualizations were meaningful.

---

### 3️⃣ Visualization 1: Sales Distribution (Histogram)

```python
plt.hist(df["SALES"], bins=30)
```

**Why this plot?**

* To understand how sales values are distributed
* To detect skewness and outliers

**Key Insight:**

* Most sales fall in a lower range
* Few high-value orders create right-skewed distribution

---

### 4️⃣ Visualization 2: Total Sales by Product Line (Bar Chart)

```python
df.groupby("PRODUCTLINE")["SALES"].sum()
```

**Why this plot?**

* Best way to compare categorical data

**Key Insight:**

* Some product lines contribute significantly more to revenue
* Helps in business prioritization

---

### 5️⃣ Visualization 3: Monthly Sales Trend (Line Plot)

```python
df.groupby("MONTH_ID")["SALES"].sum()
```

**Why this plot?**

* To analyze sales trends over time

**Key Insight:**

* Sales show seasonal behavior
* Certain months have peak performance

---

## 🧩 Tools & Technologies Used

* **Python 3**
* **Pandas** → data loading & manipulation
* **Matplotlib** → data visualization
* **VS Code** → development environment

---

## 🚀 How to Run This Project

### Step 1: Navigate to project folder

```bash
cd "week6 Matplotlib/project"
```

### Step 2: Run the script

```bash
python mpl_script.py
```

All visualizations will be displayed sequentially.

---

## 📌 Key Takeaways

* Learned **core Matplotlib plotting techniques**
* Understood **real-world dataset handling**
* Learned **path resolution using `__file__`**
* Built **EDA-style visualizations**
* Followed **clean project structure**

---

## 🔮 Next Steps

* Add scatter plots (Quantity vs Sales)
* Save all figures automatically
* Upgrade visualizations using **Seaborn**
* Apply similar analysis on Kaggle datasets

---

## 📎 Learning Context

This project is part of my **6-month Generative AI & Data Science learning journey**, where strong data visualization skills are essential for:

* Exploratory Data Analysis (EDA)
* Machine Learning debugging
* Model evaluation
* GenAI & RAG analytics

---

✅ **Status:** Completed

📅 **Week:** 6 (Matplotlib)

---

> *This README represents not just a project, but a learning milestone.*
