📘 Overview

This project demonstrates my understanding of NumPy — one of the most powerful Python libraries for numerical and scientific computing.

After learning core NumPy concepts such as arrays, indexing, slicing, data manipulation, and sorting, I applied that knowledge to a real-world dataset from Kaggle.

The goal of this project was to:

Load an unclean CSV dataset

Clean invalid or missing data

Sort and organize the dataset using NumPy

Save the final cleaned version for further analysis

🧩 Project Structure
numpy project/
├── data/
│   └── sample_sales.csv          # Raw dataset (downloaded from Kaggle)
├── scripts/
│   └── clean_data_numpy.py       # NumPy script for cleaning & sorting
├── output/
│   └── cleaned_sales.csv         # Cleaned and sorted data output
└── README.md                     # Project documentation

🧠 NumPy Concepts Used

Array creation and manipulation

Data loading with np.genfromtxt()

Handling missing / invalid data

Logical masking and filtering

Sorting arrays by specific fields

Saving cleaned data using np.savetxt()

Basic statistical operations (optional section)

⚙️ Steps Performed

Loaded raw CSV data using NumPy.

Detected and replaced invalid or missing numeric values.

Removed rows with 0 or missing entries in important columns.

Sorted the dataset by SALES in descending order.

Saved the cleaned dataset as a new CSV file.

📊 Output Example

The script generates a file:

output/cleaned_sales.csv


containing a clean, well-structured, and sorted dataset — ready for data analysis or visualization.

🧾 Dataset Source

Dataset: Sample Sales Data – Kaggle

🧑‍💻 Skills Demonstrated

Data Cleaning with NumPy

Data Organization & File Handling

Problem Solving with Array Operations

Real-world Data Processing

🏁 Conclusion

This project helped reinforce my understanding of NumPy fundamentals and how they apply in real data preprocessing workflows.
It showcases how Python’s numerical capabilities can be used to clean and prepare messy datasets efficiently — a critical step in any data science pipeline.