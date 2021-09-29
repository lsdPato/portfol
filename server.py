from flask import Flask, render_template,url_for, request, redirect
import json
import csv
#para correr flask
# $ export FLASK_APP=hello
# $ flask run
#export FLASK_ENV=development
app = Flask(__name__)
print(__name__)

#/<username> esto flask le entiende como un parametro que se requiere
# @app.route("/<username>/<int:post_id>")
# def hello_world(username=None, post_id=None):
#     return render_template('index.html', name=username,post_id=post_id)
@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_csv(data):
    with open('database.csv', mode ='a', newline='') as my_file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(my_file,delimiter=',' ,quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_csv(data)
        #esta es una manera de solucionarlo
        # data_string = json.dumps(data)
        # with open('database.txt', mode ='a') as my_file:
        #     text = my_file.write(data_string)
        #     print(text)
        #     print(data) 
        return redirect('./thankyou.html')
    else:
        return 'something was wrong'   