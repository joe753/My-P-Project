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
    return "우리나라 시간   형식: " + str(datestr)




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
    lst2 = [ ("만남1", "김건모", False), ("만남2", "노사연", True), ("만남3", "노사봉",False), ("만남4", "아무개",True) ]
    a = (1, "만남1", "김건모", False, [])
    b = (2, "만남2", "노사연", True, [a])
    c = (3, "만남3", "익명", False, [a,b])
    d = (4, "만남4", "익명", False, [a,b,c])
    return render_template('index.html', title="Title", lst2=lst2, lst=[a,b,c,d])

@app.route("/trythis")
def prac():
    a_1 = ("파이썬", "https://www.naver.com", [])
    a_2 = ("자바","https://www.naver.com", [])
    b_1_1 = ("jinja", "https://www.naver.com",[])
    b_1_2 = ("Genshi Cheetah","https://www.naver.com", [])
    b_1 = ("플라스크", "https://www.naver.com",[b_1_1, b_1_2])
    b_2 = ("스프링","https://www.naver.com", [])
    b_3 = ("노드JS", "https://www.naver.com",[])
    c_1 = ("나의 일상","https://www.naver.com", [])
    c_2 = ("이슈 게시판", "https://www.naver.com",[])
    a = ("프로그래밍 언어","https://www.naver.com", [a_1, a_2])
    b = ("웹 프레임워크","https://www.naver.com", [b_1, b_2, b_3])
    c = ("기타", "https://www.naver.com",[c_1,c_2])

    return render_template('trythis.html', lst=[a,b,c])

@app.route('/practice')
def practice():
    return render_template('p_main.html')

@app.route('/practice/2')
def pracitce1():
    return render_template('p_main2.html')

@app.route('/testt')
def testt():
    return render_template('tests.html')

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
