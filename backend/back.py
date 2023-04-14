from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/back/<sentence>")
def calc(sentence):
    
    ans = len(sentence.split(' '))
    print("backend ans:",ans)
    return jsonify(ans=f"{ans}")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)