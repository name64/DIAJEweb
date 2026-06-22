from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
     als = 'als love'
     return render_template('index1.html',
                            my_als = als)


@app.route('/hello/<name>/')
def hello_name(name):    
     return 'hello %s!' % name



if __name__ == "__main__":
     app.run(host='::', port = 5000, debug = False,threaded = True)