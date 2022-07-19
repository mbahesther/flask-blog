from flask import Flask
app = Flask(__name__)


@app.route('/adminn')
def hello_admin():
   return '<h1>Hello Admin</h1>'

@app.route('/guest')
def hello_guest():
   return 'Hello as Guest'

@app.route('/contact')
def contant():
    return 'hello my contant is ....'


@app.route('/blog')
def show_blog():
   return 'Blog Number'

if __name__ == '__main__':
   app.run(debug = True)