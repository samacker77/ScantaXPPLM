from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
from transformers.modeling_gpt2 import GPT2LMHeadModel
# This downloads GPT-2 Medium, it takes a little while
_ = GPT2LMHeadModel.from_pretrained("gpt2-medium")
from run_pplm import run_pplm_example
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
        per=""
        if drop == 'science':
            per='Scientist'
        elif drop== 'religion':
            per='Preacher'
        elif drop== 'military':
            per='Navy SEAL'
        elif drop== 'politics':
            per='Politician'
        elif drop== 'positive':
            per='Optimist'
        x = run_pplm_example(cond_text=text,num_samples=1,bag_of_words=drop,length=20,stepsize=0.03,sample=True,num_iterations=3, window_length=5,gamma=1.5,gm_scale=0.95,kl_scale=0.01,verbosity='regular')      
    return render_template('result.html',prediction=[text,per,x[13:]])
# run the app.
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
