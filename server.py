from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            with open("database.csv", "a") as f:
                csv_write = csv.writer(f, delimiter=",", quotechar="'", newline='')
                csv_write.writerow([data['email'], data['subject'], data['message']])
            return redirect('/thankyou.html')
        except:
            return 'something went wrong try again'
    else:
        return 'something went wrong try again'
