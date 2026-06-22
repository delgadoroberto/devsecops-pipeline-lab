from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "environment": "lab",
        "message": "DevSecOps Pipeline API is running smoothly!"
    }), 200

if __name__ == '__main__':
    # Running on 0.0.0.0 to allow container binding
    app.run(host='0.0.0.0', port=5000, debug=False)
