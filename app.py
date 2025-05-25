from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
        <h1>Hello, World! 🌍</h1>
        <img src="/static/image.png" alt="Hello Image" width="300">
    '''

# Optional route to directly access the image
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
