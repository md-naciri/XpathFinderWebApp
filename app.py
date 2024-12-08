import os
from flask import Flask, render_template, request, send_file

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

    # Placeholder for processing logic
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.xlsx')

    # Simulate creating an output file
    with open(output_path, 'w') as f:
        f.write('Output file content')

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
