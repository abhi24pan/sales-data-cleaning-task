# Sales Data Cleaning Task

This repository contains a cleaned sales dataset as part of a data analyst internship assignment. The original data included intentional issues such as missing values, inconsistent formats, and duplicates. All data cleaning was done using Python and the Pandas library.

---

## 📁 Files Included

- `sales_data_200_raw.csv` – Raw sales data with inconsistencies and missing values.
- `sales_cleaning.py` – Python script used to clean and preprocess the dataset.
- `sales_data_200_cleaned.csv` – Final cleaned dataset ready for analysis.

---

## 🛠 Tools Used

- Python 3.x
- Pandas
- Visual Studio Code (for code execution)

---

## 🧹 Cleaning Steps Performed

| Step                          | Description |
|-------------------------------|-------------|
| Missing Value Handling        | Filled missing values in `Region`, `Sales Rep` with `'Unknown'`; `Quantity` with median |
| Duplicates Removed            | Dropped any exact duplicate rows |
| Standardized Text Fields      | Capitalized inconsistent values in `Region` and `Sales Rep` |
| Date Format Standardization   | Converted mixed date formats to standard `datetime` objects |
| Recalculated `Total Price`    | Based on cleaned `Quantity` × `Unit Price` |
| Column Renaming               | Converted column headers to lowercase and underscore-separated |
| Data Type Fixing              | Ensured numeric fields are correct types (e.g., int, float) |



## 📌 Purpose

This task helps demonstrate proficiency in:
- Identifying and fixing common data quality issues
- Using Pandas for real-world data preprocessing
- Creating reproducible, clean datasets for analysis or modeling


   python sales_cleaning.py

