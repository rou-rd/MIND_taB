#!flask/bin/python
from flask import Flask, jsonify ,make_response,request
import total as tt

app = Flask(__name__)

def search(concurrent):
	if concurrent=="ooredoo":
		task=tt.ooredoo()
	elif concurrent=="ovh":
		task=tt.ovh()
	elif concurrent=="zenhosting()":
		task=tt.zenhosting()
	elif concurrent=="atlax":
		task=tt.atlax()
	elif concurrent=="besthost":
		task=tt.besthost()
	return task
"""
@app.route('/config', methods=['POST']) #allow both GET and POST requests
def form_example():
    return req_data = request.get_json()
"""
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/todo/api/v1.0/datas', methods=['GET'])
def get_tasks(): 
    return jsonify({'datas': search(request.args.get('keywords'))})

if __name__ == '__main__':
    app.run(debug=True)
