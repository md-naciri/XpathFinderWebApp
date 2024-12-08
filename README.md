
# Xpath Finder Web App

Xpath Finder Web App is a web-based application built using Flask, designed to automate the task of mapping and processing Xpath data from a reference Excel file to a target Excel file. It simplifies the process of matching data and generating the required output by appending the Xpath to the target file.

---

## Overview

This web application was created to automate the repetitive task of extracting and mapping Xpath data from Excel files at work. The app allows you to upload a reference Excel file and a target Excel file, and it will automatically map and append the Xpath data to the target file, generating a processed output file for download.

***In addition to this web app, I also created a desktop version of the Xpath Finder tool, which you can find here: [XpathFinder](https://github.com/md-naciri/XpathFinder)***

---

## Features

- Upload two Excel files: one as the reference file and one as the target file.
- Automatically map the "Donnée du modèle" column from the reference file to the "Xpath" column and append it to the target file.
- Save the processed file with a new "_output" suffix in the same directory as the target file.
- User-friendly web interface.

---

## Requirements

To run the web application, you need the following Python packages:

- **Flask**: For building the web application.
- **pandas**: For reading and processing Excel files.
- **openpyxl**: For handling Excel files (.xlsx format).

You can install these dependencies by running:

```bash
pip install Flask
pip install pandas
pip install openpyxl
pip install Werkzeug
```
---

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/md-naciri/XpathFinderWebApp.git
   cd XpathFinderWebApp
   ```

2. Ensure you have Python 3.x installed and a virtual environment set up (optional but recommended).

3. Install the required dependencies by running:
   ```
   pip install Flask
   pip install pandas
   pip install openpyxl
   pip install Werkzeug
   ```

4. Run the Flask web application:
   ```bash
   python app.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000`

6. On the homepage, upload the Reference Excel File and the Target Excel File.

7. Click "Find the Xpath" to start processing the files. If both files are valid, the processed file will be automatically downloaded with the suffix "_output".

---

## Customization

If your Excel files have different column names, update the column references in the code:
- Replace `"Donnée du modèle"` with your source column name.
- Replace `"Xpath"` with your target column name.

---

## License

© 2024 md_naciri. All rights reserved.
