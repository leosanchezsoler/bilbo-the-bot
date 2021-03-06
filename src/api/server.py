from flask import Flask, render_template, url_for, request, redirect


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_json', methods=['GET', 'POST']) 
def get_json():
    if request.method == 'POST'
    
    return 

if __name__ == '__main__':
    app.run(debug=True)
    