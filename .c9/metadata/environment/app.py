{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["import os","from flask import Flask","","app = Flask(__name__)","","","@app.route('/')","def hello():","    return 'Hello World ...again'","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)",""],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":15,"column":0},"end":{"row":15,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1565037119202,"hash":"5db321f800b98353b5047c89b1972f1acf5891bd"}