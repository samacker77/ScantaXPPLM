from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

# add a rule for the index page.
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data', methods=['POST'])


def get_data():
    if(request.method =='POST'):
        text = request.form['nlg']
        drop = request.form['personality']
        print(text,drop)
    return render_template('result.html',prediction=[text,drop])
'''def get_data():
	print("I am here!")
	if request.method == 'POST':
		text = request.form['nlg']
		print(text)
drop = request.form['personality']
        print(drop)
	return render_template('result.html')'''
# run the app.
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)