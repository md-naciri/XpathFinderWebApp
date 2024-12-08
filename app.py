import os
from flask import Flask, render_template, request, send_file
import pandas as pd
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_files():
    if 'reference' not in request.files or 'target' not in request.files:
        return "Missing files. Please upload both files."

    reference_file = request.files['reference']
    target_file = request.files['target']

    if reference_file.filename == '' or target_file.filename == '':
        return "No file selected."

    ref_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(reference_file.filename))
    tgt_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(target_file.filename))

    reference_file.save(ref_path)
    target_file.save(tgt_path)

    try:
        # Read Excel files
        reference_df = pd.read_excel(ref_path)
        target_df = pd.read_excel(tgt_path)

        # Create lookup dictionary
        reference_lookup = dict(zip(reference_df["Donnée du modèle"], reference_df["Xpath"]))

        # Map the Xpath
        target_df["Xpath"] = target_df["Donnée du modèle"].map(reference_lookup).fillna("Not Found")

        # Name the output file based on the target file name
        output_filename = os.path.splitext(target_file.filename)[0] + "_output.xlsx"
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)

        # Save the output
        target_df.to_excel(output_path, index=False)

        return send_file(output_path, as_attachment=True)

    except Exception as e:
        return f"Error processing files: {e}"

if __name__ == '__main__':
    app.run(debug=True)
