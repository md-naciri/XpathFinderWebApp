import os
from flask import Flask, render_template, request, send_file, flash, redirect
import pandas as pd
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for flashing error messages

app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process_files():
    # Initialize error flag
    error_flag = False

    try:
        # Check if files are uploaded
        reference = request.files.get('reference')
        target = request.files.get('target')

        # Validate file extensions
        if not reference or not target:
            flash("Both files are required!", "danger")
            error_flag = True

        elif not (reference.filename.endswith('.xlsx') and target.filename.endswith('.xlsx')):
            flash("Please upload valid Excel files (.xlsx only).", "danger")
            error_flag = True

        if error_flag:
            return redirect(request.url)

        # Save files temporarily
        ref_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(reference.filename))
        target_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(target.filename))
        reference.save(ref_path)
        target.save(target_path)

        # Read the Excel files
        reference_df = pd.read_excel(ref_path)
        target_df = pd.read_excel(target_path)

        # Check if required columns exist in the reference file
        if "Donnée du modèle" not in reference_df.columns or "Xpath" not in reference_df.columns:
            flash("Missing required columns ('Donnée du modèle' or 'Xpath') in the reference file.", "danger")
            error_flag = True

        if error_flag:
            return redirect(request.url)

        # Create lookup dictionary
        reference_lookup = dict(zip(reference_df["Donnée du modèle"], reference_df["Xpath"]))

        # Map the Xpath
        target_df["Xpath"] = target_df["Donnée du modèle"].map(reference_lookup).fillna("Not Found")

        # Name the output file based on the target file name
        output_filename = os.path.splitext(target.filename)[0] + "_output.xlsx"
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)

        # Save the output
        target_df.to_excel(output_path, index=False)

        # Return the file for download
        return send_file(output_path, as_attachment=True)

    except Exception as e:
        flash(f"Error processing files: {e}", "danger")
        return redirect(request.url)


if __name__ == '__main__':
    app.run(debug=True)