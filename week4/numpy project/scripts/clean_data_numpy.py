import numpy as np
import os

# --- Locate dataset dynamically ---
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "../data/sample_sales.csv")
output_path = os.path.join(base_dir, "../output/cleaned_sales.csv")

# --- Load dataset safely ---
data = np.genfromtxt(
    data_path,
    delimiter=",",
    names=True,
    dtype=None,
    encoding="latin1",
    invalid_raise=False
)

print("✅ File loaded successfully!")
print("Columns detected:", data.dtype.names)
print("Shape:", data.shape)
print("First 3 rows:")
print(data[:3])

# --- Data Cleaning ---
sales = np.array([float(x) if str(x).replace('.', '', 1).isdigit() else 0 for x in data['SALES']])
quantity = np.array([float(x) if str(x).replace('.', '', 1).isdigit() else 0 for x in data['QUANTITYORDERED']])

valid_rows = (sales > 0) & (quantity > 0)
clean_data = data[valid_rows]

print("✅ Rows after cleaning:", len(clean_data))

# --- Sorting (by SALES descending) ---
sorted_data = np.sort(clean_data, order='SALES')[::-1]

# --- Save cleaned and sorted data ---
header = ",".join(clean_data.dtype.names)
np.savetxt(output_path, sorted_data, delimiter=",", fmt="%s", header=header, comments='', encoding='latin1')

print(f"✅ Cleaned and sorted data saved to: {output_path}")

