from flask import Flask, request, render_template_string
import pickle
import os
import base64

app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Pickle Deserialization Challenge</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    color: #333;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .container {
                    background-color: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    width: 400px;
                }
                h1 {
                    text-align: center;
                    color: #007BFF;
                }
                form {
                    display: flex;
                    flex-direction: column;
                    gap: 10px;
                }
                textarea {
                    width: 100%;
                    padding: 10px;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                    font-size: 14px;
                    resize: vertical;
                }
                input[type="submit"] {
                    background-color: #007BFF;
                    color: white;
                    padding: 10px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 16px;
                }
                input[type="submit"]:hover {
                    background-color: #0056b3;
                }
                .output {
                    margin-top: 20px;
                    padding: 10px;
                    background-color: #f9f9f9;
                    border: 1px solid #ddd;
                    border-radius: 4px;
                    word-wrap: break-word;
                    font-family: monospace;
                    color: #e74c3c;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Pickle Deserialization Challenge</h1>
                <form method="POST" action="/deserialize">
                    <label for="data">Enter Base64 Encoded Pickled Data:</label>
                    <textarea name="data" rows="5" cols="40"></textarea><br>
                    <input type="submit" value="Submit">
                </form>
            </div>
        </body>
        </html>
    """)

@app.route('/deserialize', methods=['POST'])
def deserialize():
    pickled_data = request.form['data']
    
    try:
        pickled_bytes = base64.b64decode(pickled_data)
        ban=[b".",b"/",b"\\"]

        for pattern in ban:
            if pattern in pickled_bytes:
                raise ValueError(f"Payload contains banned characters! {pattern}")
        obj = pickle.loads(pickled_bytes)
        
        return render_template_string("""
            <div class="container">
                <h1>Deserialized Object</h1>
                <div class="output">{{ obj }}</div>
                <a href="/">Go back</a>
            </div>
        """, obj=obj)
    except Exception as e:
        return render_template_string("""
            <div class="container">
                <h1>Error</h1>
                <div class="output">{{ error_message }}</div>
                <a href="/">Go back</a>
            </div>
        """, error_message=str(e))

if __name__ == '__main__':
    app.run(debug=False)
