from flask import *
from flask_cors import CORS
from os import path,getcwd
app=Flask(__name__)
CORS(app)


FLAG_PATH = path.join(getcwd(), "flag.txt")
with open(FLAG_PATH, "w") as f:
    f.write("42HN{sn34ky_f1l3_r34d3r}")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/read', methods=['POST'])
def read_file():
    if request.method == 'POST':
        file = request.form['filename']
        if file == 'flag.txt' or file == './flag.txt':
            return "Try harder ;)"
        else:
            try:
                with open(file, 'r') as filename:
                    content = filename.read()  
                return content
            except FileNotFoundError:
                return 'File not found ;('
            except Exception as e:
                return f'An error occurred: {e}', 500


if __name__ == '__main__':
    app.run(debug=False, port=3001)
