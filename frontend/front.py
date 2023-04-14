from flask import Flask,jsonify,request,render_template
import json
import requests

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    if request.method == 'POST':
        print('hej')
        text = request.form['text']
        ans = json.loads(requests.get(f'http://backend:5001/back/{text}').content.decode())['ans'].strip()
        print("frontend ans:",ans)
        return f"The length of the word `{text}` is {ans}"
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)