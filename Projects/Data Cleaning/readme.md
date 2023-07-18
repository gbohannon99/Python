

# Customer Data Cleaning and Transformation

This project focuses on learning how to clean and transform customer data using the Python library Pandas. The objective is to clean a customer dataset to determine which customers can be contacted and provide it to the sales team. I have added the 'original' and 'cleaned data' into the folder

## Getting Started

1. Install the required libraries by running `pip install pandas openpyxl` in your Python environment.

2. Clone the repository or download the project files to your local machine.

3. Update the file path in the code to match the location of your customer dataset.

4. Run the Python script to execute the data cleaning and transformation process.

## Data Cleaning Process

The following steps were performed to clean and transform the customer dataset:

1. **Duplicate Removal:** Duplicate records were dropped from the dataset using the `drop_duplicates()` function.

2. **Column Removal:** The "Not_Useful_Column" was dropped using the `drop()` function.

3. **Stripping Functions:** The `lstrip()` and `rstrip()` functions were used to remove specific characters from the "Last_Name" column.

4. **Cleaning Phone Numbers:** Non-numeric characters were removed from the "Phone_Number" column using the `str.replace()` function and regular expressions. Then, the phone numbers were formatted using the `apply()` and `lambda` functions.

5. **Cleaning Address:** The "Address" column was split into separate columns for "Address", "State", and "Zip_Code" using the `str.split()` function and the `expand=True` parameter.

6. **Data Uniformity:** The `str.replace()` function was used to ensure uniformity in the "Paying Customer" and "Do_Not_Contact" columns.

7. **Handling Null Values:** "N/A" and NaN values were replaced or filled using the `replace()` and `fillna()` functions.

8. **Contact Preference Filtering:** Records of customers who do not wish to be contacted were removed by iterating through the dataset and dropping the corresponding rows.

9. **Missing Phone Number Filtering:** Records without a phone number were removed similarly by iterating through the dataset.

10. **Index Reset:** The index was reset to enhance readability using the `reset_index()` function.

11. **Saving the Cleaned Dataset:** The cleaned dataset was saved as an Excel file using the `to_excel()` function.

## Usage and Further Processing

The cleaned dataset, named "cleaned_dataset.xlsx," is available for further processing and analysis. You can open the file in spreadsheet software or use it as input for subsequent data analysis tasks.


