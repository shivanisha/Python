from flask import Flask , redirect, url_for, jsonify
from flask import request
app = Flask(__name__)

#
# @app.route('/', methods=['POST','GET'])
# def index():
#    return 'test'
@app.route('/aa', methods=['POST','GET'])
def index():
    value = request.json["key"]
    return value

# @app.route('/hello1/<name>')
# def hello_name(name):
#    return 'Hello %s!' % name


# @app.route('/success/<name>')
# def success(name):
#     return 'welcome %s' % name

#
# @app.route('/')
# def booksFunction():
#    if request.method == 'GET':
#        return get_books()
#    elif request.method == 'POST':
#        title = request.args.get('title', '')
#        author = request.args.get('author', '')
#        genre = request.args.get('genre', '')
#        return makeANewBook(title, author, genre)


#
@app.route('/postman', methods=['POST','GET'])
def math_operation_via_postman():
    if (request.method=='POST'):
        data = request.json['name']
        operation = request.json['class']
        result = data +"   "+operation


    #     operation = request.json['operation']
    #     num1= int(request.json['num1'])
    #     num2 = int(request.json['num2'])
    #     if operation=='add':
    #         r=num1+num2
    #     result='sum '+str(r)
    elif (request.method == 'GET'):
        return 'welcome'
    return jsonify(result)

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         user = request.form['nm']
#         return redirect(url_for('success', name=user))
#     else:
#         user = request.args.get('nm')
#         return redirect(url_for('success', name=user))

if __name__  == '__main__':
    print("this is  inside name")
    app.run(debug=True)
