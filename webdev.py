from flask import Flask, render_template, request
from runcode import runcode
app = Flask(__name__)

default_c_code1 ="""#include<stdio.h>
int main()
{

return 0;
}
"""
default_c_code2 = """
Put C2 code here

"""
default_c_code3 = """
Put C3 code here

"""
default_c_code4 = """
Put C4 code here

"""
statement1="In publishing and graphic design, lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document without relying on meaningful content (also called greeking). Replacing the actual content with placeholder text allows designers to design the form of the content before the content itself has ..?"

statement2="Whatsup nigga?"

statement3="Whatsup fag?"

statement4="Whatsup?"

default_rows = "15"
default_cols = "60"

@app.route("/")
@app.route("/run1", methods=['POST', 'GET'])
def run1():
    if request.method == 'POST':
        code = request.form['code']
        run = runcode.RunCCode(code)
        rescompil, resrun = run.run_c_code()
        if not resrun:
            resrun = 'No result!'
    else:
        code = default_c_code1
        resrun = 'No result!'
        rescompil = ''
    next="run2"
    return render_template("main.html",
                           code=code,
                           statement=statement1,
                           target="run1",
                           next=next,
                           resrun=resrun,
                           rescomp=rescompil,
                           rows=default_rows, cols=default_cols)


@app.route('/run2', methods=['POST', 'GET'])
def run2():
    if request.method == 'POST':
        code = request.form['code']
        run = runcode.RunCCode(code)
        rescompil, resrun = run.run_c_code()
        if not resrun:
            resrun = 'No result!'
    else:
        code = default_c_code2
        resrun = 'No result!'
        rescompil = ''
    next="run3"
    return render_template("main.html",
                           statement=statement2,
                           code=code,
                           target="run2",
                           next=next,
                           resrun=resrun,
                           rescomp=rescompil,
                           rows=default_rows, cols=default_cols)



@app.route('/run3', methods=['POST', 'GET'])
def run3():
    if request.method == 'POST':
        code = request.form['code']
        run = runcode.RunCCode(code)
        rescompil, resrun = run.run_c_code()
        if not resrun:
            resrun = 'No result!'
    else:
        code = default_c_code2
        resrun = 'No result!'
        rescompil = ''
    next="run4"
    return render_template("main.html",
                           statement=statement3,
                           code=code,
                           target="run3",
                           next=next,
                           resrun=resrun,
                           rescomp=rescompil,
                           rows=default_rows, cols=default_cols)
@app.route('/run4', methods=['POST', 'GET'])
def run4():
    if request.method == 'POST':
        code = request.form['code']
        run = runcode.RunCCode(code)
        rescompil, resrun = run.run_c_code()
        if not resrun:
            resrun = 'No result!'
    else:
        code = default_c_code2
        resrun = 'No result!'
        rescompil = ''
    next="run1"
    return render_template("main.html",
                           statement=statement4,
                           code=code,
                           target="run4",
                           next=next,
                           resrun=resrun,
                           rescomp=rescompil,
                           rows=default_rows, cols=default_cols)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True,threaded=True)
