from markupsafe import escape

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def first():
    return "<p>这是我的第一个flask程序!</p>"


@app.route('/student/<name>')
def what_is_your_name(name):
    return f'你的名字是: {escape(name)}'


@app.route('/path/<path:subpath>')
def what_is_your_path(subpath):
    return f'你的路径是: {escape(subpath)}'


@app.route('/withslash/')
def with_slash():
    return '这是带slash的'


@app.route('/withoutslash')
def with_out_slash():
    return '这是不带slash的'


@app.route('/diffMethod', methods=['GET', 'POST'])
def diff_method():
    if request.method == 'POST':
        return '这是post'
    else:
        return '这是get'

@app.get('/getMethod')
def get_method():
     return '这是get'

@app.post('/postMethod')
def post_method():
     return '这是post'

if __name__ == '__main__':
    app.run()
