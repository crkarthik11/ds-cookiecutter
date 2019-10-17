from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def healthz():
    message = {"status": f"Welcome to {{ cookiecutter.repo_name }}!!"}
    response = jsonify(message)
    response.status_code = 200
    return response

@app.route('/healthz', methods=['GET'])
def healthz():
    message = {"status": f"{{ cookiecutter.repo_name }} server is up!!!"}
    response = jsonify(message)
    response.status_code = 200
    return response

@app.route('/predict', methods=['POST'])
def predict():
    """Predict API Call
    """
    responses = jsonify(predictions='sample predict works')
    responses.status_code = 200
    return (responses)

@app.errorhandler(400)
def bad_request(error=None):
	message = {
			'status': 400,
			'message': f"Error Request: ' + {request.url}"
	}
	resp = jsonify(message)
	resp.status_code = 400

	return resp

app.run(host='0.0.0.0', port=3000)