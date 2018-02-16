import config
import traceback
from flask import request, redirect, url_for, flash, render_template, session, abort, jsonify
from flask_login import login_required
import json
from controllers.HomeController import HomeController


app = config.app
db = config.db
login_manager = config.login_manager




@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')
        # return "Hello Boss!!"
# @app.route('/events')
# def eventM():
#     return HomeController.getEvents(request)
# @app.route('/instructor')
# def m1():
#     return HomeController.view_page(request)

# @app.route('/testjson2')
# def testjson2():
#     return HomeController.listEvents(request)


# @app.route('/student')
# def m2():
#     return HomeController.listStudents(request)
# @app.route('/course')
# def m3():
#     return HomeController.listCourse(request)
# @app.route('/studentCList')
# def m4():
#     return HomeController.coursesTakenByStudent(request)
# def testt():
#     t1 = instructor(iid='212121',name='KKKKKK', mail='admin@example.com', Ipassword='12345678')
#     user  = instructor.query.filter_by(mail='admin@example.com').first()
#     # t2 = User(username='guest', email='guest@example.com')

#     # db.session.delete(user)
#     db.session.commit()
#     return "doneg"



@app.route('/', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

# @app.route('/static')
# def st():
#     return '<h2> test static folder</h2>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)

# if __name__ == "__main__":
#     app.secret_key = os.urandom(12)
#     app.run(debug=True,host='0.0.0.0', port=8082)
