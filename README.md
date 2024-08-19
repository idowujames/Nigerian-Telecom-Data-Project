# Nigerian Telcom Data - Project

**Context:**
This dataset is a synthetic collection of transaction records from the Nigerian telecom industry, capturing a wide array of customer interactions with major telecom operators such as MTN, Airtel, Glo, and 9mobile. This dataset provides insights into the transactional behaviors of telecom customers, encompassing various types of transactions such as airtime purchases, data purchases, and bill payments. It includes over 50,000 records, reflecting real-world challenges telecom operators face, such as data inconsistencies, missing information, and varied data formats.

**PS - This is a fake dataset generated using Faker. It is only meant to simulate a real-world dataset for eductaional purposes. Also due to the way the data was generated, after the cleaning was done, it shows that the dataset does not lend it self to much variability, making it not suitable for analytic purposes but excellent for data cleaning purposes**

### **Columns:**
**Transaction ID:** A unique identifier for each transaction, though some values may be missing due to data entry errors.

**Customer ID:** A unique identifier for each customer, with some missing values reflecting potential data collection issues.

**Transaction Date**: The date and time of the transaction, presented in various formats to reflect the diversity of data sources.
Operator Name: The name of the telecom operator, including common typographical errors (e.g., "MNT" for "MTN").

**Transaction Type:** The type of transaction, such as airtime purchase, data purchase, or bill payment, with potential typographical errors.

**Transaction Amount:** The amount of money involved in the transaction, displayed in inconsistent formats (e.g., varying decimal places, inclusion of currency symbols).

**Customer Age:** The customer's age, with some missing values.
Customer Gender: The gender of the customer, with inconsistent labels (e.g., "Male", "male", "Female", "female", "Other").

**Customer Location:** The geographic location of the customer, including cities and states, with some inconsistencies in format.
Service Plan: The type of service plan (e.g., Prepaid, Postpaid), including possible typographical errors.

**Data Usage (MB):** The amount of data used in megabytes, with inconsistent formatting.

**Call Duration (min):** The duration of calls in minutes, presented in varying formats.

**SMS Sent:** The number of SMS messages sent by the customer.
Internet Package: The type of internet package (e.g., Daily, Weekly, Monthly), with possible typographical errors.

**Transaction Status:** The status of the transaction (e.g., Completed, Pending, Failed), with potential typographical errors.

**Key Points:**

**Real-World Data Challenges:** This dataset includes intentional messiness to simulate real-world data challenges, such as missing values, inconsistent data formats, typographical errors, extra spaces, and duplicates.

**Large Volume:** With over 50,000 records, this dataset provides a substantial volume for thorough data analysis and machine learning applications.

**Diverse Transactions:** Captures various types of transactions and customer details relevant to the Nigerian telecom industry, offering a broad spectrum for analysis.
