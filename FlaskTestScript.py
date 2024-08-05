import subprocess

from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    input_text = request.form['input_text']

    # Execute the Python script and capture the output
    try:
        output = execute_script(input_text)
    except Exception as e:
        output = str(e)

    return render_template('result.html', input_text=input_text, output=output)

def execute_script(input_text):
    try:
        # Define the path to your Python script
        script_path = r"C:\Users\BSA-OliverJ'22\OneDrive\Desktop\Documents\Programming\Projects\CDB Server\CDBSearchTool\CDB_Search_Tool.py"  # Replace with the actual path to your script
        
        # Use subprocess to run the script with the input_text as an argument
        cmd = ['python', script_path, input_text]
        
        # Run the script and capture the output
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        stdout, stderr = process.communicate()
        
        # Check for any errors
        if process.returncode != 0:
            return f"Error: {stderr}"
        
        # Return the script's output
        return stdout
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)