import os, sys
root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(root_path)

from flask import Flask, render_template, url_for, request, redirect, Response, jsonify
from utils.functions import read_json, read_my_json, tokenize_and_lemmatize
from utils.recommender import get_recommendations, new_one
import json, os
from flask_httpauth import HTTPBasicAuth, HTTPDigestAuth
from werkzeug.security import generate_password_hash, check_password_hash
import pickle
import pandas as pd 
        
app = Flask(__name__)
auth = HTTPBasicAuth()

tfidf_vect_pkl = pickle.load(open('models/tfidf_vec.pickle', 'rb'))
df = pd.read_json('data/data.json')

users = {
    'admin': generate_password_hash('35593809K'),
    'public': generate_password_hash('thebridge'),
}

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        mysearch = request.form['mysearch']
        get_recommendations(title= mysearch, df=df, tfidf_vect=tfidf_vect_pkl)
    return render_template('index.html')

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/get_json')
@auth.login_required
def auth_user():
    return read_my_json()

@app.route('/upload')
def upload_form():
    return render_template('get_json.html')


def main():
    print(os.path.dirname(os.getcwd()))
    
    # Get the settings fullpath
    # \\ --> WINDOWS
    # / --> UNIX
    #settings_file = os.path.dirname(os.getcwd()) + os.sep + "settings.json"

    settings_file = os.path.dirname(__file__) + os.sep + "settings.json"
    # Load json from file 
    json_readed = read_json(fullpath=settings_file)
    
    # Load variables from jsons
    SERVER_RUNNING = json_readed["server_running"]
    
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print("Server settings.json doesn't allow to start server. " + 
              "Please, allow it to run it.")

if __name__ == "__main__":
    main()
    