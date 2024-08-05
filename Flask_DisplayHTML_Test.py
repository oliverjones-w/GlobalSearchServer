from flask import Flask, render_template, request
import subprocess
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name_to_search = request.form.get('name')
        script_path = 'search_tool.py'
        
        try:
            result = subprocess.run(
                ['python', script_path, name_to_search],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            output = result.stdout
            data = json.loads(output)
            return render_template('results.html', data=data)
        except subprocess.CalledProcessError as e:
            error_message = e.stderr
            return render_template('error.html', error_message=error_message)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
