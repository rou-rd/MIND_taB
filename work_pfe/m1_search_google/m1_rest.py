#!flask/bin/python
from flask import Flask, jsonify ,make_response,request
import search as ss
from database_mango import show_the_last_id, check_data_duplicate_db, insert_document
app = Flask(__name__)

def save_data(tasks):
	for xx in tasks:
		the_last_id=show_the_last_id("application_conccurent")
		xx['id']=the_last_id+1
		insert_document(xx,"application_conccurent")
		

def search(keywords):
	list_site=ss.search_google(keywords)
	list_name=ss.get_name(list_site)
	tasks=ss.get_data(list_site,list_name)
	task=tasks
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
