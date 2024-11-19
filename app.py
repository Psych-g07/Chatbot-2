from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['GET'])
def studentnumber():
    return{'studentnumber':200610320}

@app.route('/webhook', methods=['GET'])
def weather():
  return{'Newyork':'12 C'}

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=105)