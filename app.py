import os
from flask import Flask, render_template, request, send_file
import pandas as pd

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_files():
    reference_file = request.files['reference']
    target_file = request.files['target']

    # Save uploaded files
    ref_path = os.path.join(app.config['UPLOAD_FOLDER'], reference_file.filename)
    target_path = os.path.join(app.config['UPLOAD_FOLDER'], target_file.filename)
    reference_file.save(ref_path)
    target_file.save(target_path)

    # Load Excel files
    reference_df = pd.read_excel(ref_path)
    target_df = pd.read_excel(target_path)

    # Perform your processing
    reference_lookup = dict(zip(reference_df["Donnée du modèle"], reference_df["Xpath"]))
    target_df["Xpath"] = target_df["Donnée du modèle"].apply(lambda x: reference_lookup.get(x, "Not Found"))

    # Save output file
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.xlsx')
    target_df.to_excel(output_path, index=False)

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
