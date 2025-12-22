# 📊 Seaborn Sales Data Visualization Project

## 📚 Seaborn Functions Covered (Learning Phase)

Before starting the sales dataset project, I first learned and practiced **all core Seaborn functions** using Seaborn’s built-in datasets (such as `penguins`). This helped me understand each plot deeply without worrying about data quality issues.

### ✅ Seaborn Functions I Practiced

* `sns.histplot()` – Distribution of numerical data
* `sns.kdeplot()` – Density estimation
* `sns.countplot()` – Count of categorical values
* `sns.barplot()` – Aggregated comparison using estimators (mean, sum)
* `sns.lineplot()` – Trend analysis
* `sns.scatterplot()` – Relationship between variables
* `hue`, `style`, `size` parameters – Multi-dimensional analysis
* `sns.boxplot()` – Outlier detection and spread
* `sns.violinplot()` – Distribution + density
* `sns.stripplot()` / `sns.swarmplot()` – Raw data visualization
* `sns.pairplot()` – Complete EDA overview
* `sns.heatmap()` – Correlation analysis

All of these functions were implemented and tested inside the `sbn.py` file.

---

## 🚀 Project Overview

## 📁 Folder Structure

```
week7.seaborn/
│
├── project/
│   ├── sales_data.csv   # Sales dataset
│   ├── sbproject.py     # Main Seaborn EDA project
│   ├── sbn.py           # Seaborn practice (built-in datasets)
│   └── readme.md        # Project documentation
```

---

## 🧠 What I Learned in This Project

### 1️⃣ Understanding the Dataset

* Loaded real-world CSV data using **Pandas**
* Handled encoding issues (`latin1`)
* Inspected structure using `head()` and `info()`

### 2️⃣ Sales Distribution Analysis

* Used `sns.histplot()` with KDE
* Understood skewness and spread of sales values

### 3️⃣ Category-wise Sales Analysis

* Used `sns.barplot()` with `estimator=sum`
* Analyzed total sales by **Product Line**

### 4️⃣ Deal Size Analysis

* Used `sns.boxplot()`
* Identified variability and outliers across deal sizes

### 5️⃣ Time-Series Trend Analysis

* Grouped data by month using Pandas
* Visualized trends using `sns.lineplot()`
* Identified seasonality and peak sales months

### 6️⃣ Relationship Analysis

* Used `sns.scatterplot()` with `hue`
* Analyzed relationship between quantity ordered and sales

### 7️⃣ Correlation Analysis

* Used `sns.heatmap()` on numerical features
* Understood feature relationships for ML readiness

---

## 🛠️ Libraries Used

* **Python**
* **Pandas**
* **Seaborn**
* **Matplotlib**

---

## ▶️ How to Run the Project

```bash
cd week7.seaborn/project
python sbproject.py
```

> Make sure `sales_data.csv` is in the same directory as `sbproject.py`.

---

## 📌 Key Takeaways

* Learned professional **EDA workflow**
* Practiced Seaborn visualization techniques
* Gained confidence in analyzing real-world datasets
* Built strong foundation for **ML & GenAI projects**

---

## 📈 Next Steps

* Save visualizations as image files
* Add business insights section
* Extend analysis using statistical techniques
* Prepare dataset for Machine Learning models

---

### 🔗 This project is part of my continuous learning journey in Data Science, Machine Learning, and Generative AI.
