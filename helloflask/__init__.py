from flask import Flask, g, request, Response, make_response
from flask import session, render_template, Markup
from datetime import date, datetime

app = Flask(__name__)
app.debug = True
# app.jinja_env.trim_blocks = True


def ymd(fmt):
    def trans(date_str):
        return datetime.strptime(date_str, fmt)
    return trans

@app.route('/dt')
def dt():
    datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d'))
    return "우리나라 시간 형식: " + str(datestr)




# @app.route('/env')
# def env():
#     return ('REQUEST_METHOD: %(REQUEST_METHOD) s <br>'
#         'SCRIPT_NAME: %(SCRIPT_NAME) s <br>'
#         'PATH_INFO: %(PATH_INFO) s <br>'
#         'QUERY_STRING: %(QUERY_STRING) s <br>'
#         'SERVER_NAME: %(SERVER_NAME) s <br>'
#         'SERVER_PORT: %(SERVER_PORT) s <br>'
#         'SERVER_PROTOCOL: %(SERVER_PROTOCOL) s <br>'
#         'wsgi.version: %(wsgi.version) s <br>'
#         'wsgi.url_scheme: %(wsgi.url_scheme) s <br>'
#         'wsgi.input: %(wsgi.input) s <br>'
#         'wsgi.errors: %(wsgi.errors) s <br>'
#         'wsgi.multithread: %(wsgi.multithread) s <br>'
#         'wsgi.multiprocess: %(wsgi.multiprocess) s <br>'
#         'wsgi.run_once: %(wsgi.run_once) s') % request.environ

@app.route("/tmpl")
def t():
    name = {'first' : 'HyunOuk', 'second' : 'HyunMin'}
    return render_template('index.html', title="Title", name=name)


@app.route('/wc')
def make_cookie():
    key_data = request.values.get('key', 'default token', type=str)
    value_data = request.values.get('val', 'default token', type=str)
    res = Response("SET COKKIE")  
    res.set_cookie(key_data, value_data)
    return make_response(res)
    


@app.route('/rc')
def see_cookie():
    key_data = request.values.get('key', 'default token', type=str)
    return request.cookies.get(key_data, 'default token')



@app.route('/<username>')
def show_user(username):
    return username

@app.route('/test/<tid>')
def test3(tid):
	return ("tid is %s" %tid)

# @app.route('/test_wsgi')
# def wsgi_test():
#     def application(environ, start_response):
#         body = 'The request method was %s' % environ['REQUEST_METHOD']
#         headers = [ ('Content-Type', 'text/plain'), 
# 					('Content-Length', str(len(body))) ]
#         start_response('200 OK', headers)
#         return [body]

#     return make_response(application)

# @app.route('/res1')
# def res1():
#     custom_res = Response("Custom Response", 200, {'test': 'ttt'})
#     return make_response(custom_res)


# @app.before_request
# def before_request():
#     print("before_request!!!")
#     g.str = "한글"

# @app.route("/gg")
# def helloworld2():
#     return "Hello World!" + getattr(g, 'str', '111')

@app.route("/")
def helloworld():
    return "Hello Flask World!"
