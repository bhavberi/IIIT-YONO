from flask import Flask, request
from flask import *
from Vindhya_Navigation.main import *

app = Flask(__name__)
instructions = list()


@app.route('/navigate', methods=['GET', "POST"])
def navigate_form():
    if request.method == "POST":
        global instructions
        b = request.form['block']
        f = request.form['floor']
        room = request.form['room']
        special = request.form["special"]
        print(b,f,room,special)
        if special:
            instructions = navigate(special_code=special)
        elif room:
            instructions = navigate(block=b, room_no=int(room))
        elif f:
            instructions = navigate(block=b, floor=int(f))
        if instructions == -1 or not instructions:
            return -1
            # return render_template('wrong_input.html')
        # return str(instructions)
        return redirect(url_for('result', number="1"), code=307)
    return render_template('navigation_form.html')


@app.route('/navigate/<int:number>', methods=["POST"])
def result(number):
    global instructions
    print(instructions, number)
    number = int(number)
    if number == 0:
        return render_template('final.html')
    instruction = instructions[number-1]
    if number == len(instructions):
        number = 0
    else:
        number += 1
    return render_template('result.html', n=number, ins=instruction)

@app.route('/destress')
def destress():
    return render_template('destress.html')

@app.route('/destress/video1')
def destress_video1():
    return render_template('video1.html')

@app.route('/destress/video2')
def destress_video2():
    return render_template('video2.html')

@app.route('/destress/video3')
def destress_video3():
    return render_template('video3.html')

@app.route('/destress/video4')
def destress_video4():
    return render_template('video4.html')

@app.route('/destress/video5')
def destress_video5():
    return render_template('video5.html')

@app.route('/destress/video6')
def destress_video6():
    return render_template('video6.html')

@app.route('/destress/video7')
def destress_video7():
    return render_template('video7.html')

@app.route('/destress/video8')
def destress_video8():
    return render_template('video8.html')

@app.route('/evals')
def evals():
    return render_template('evals.html')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    