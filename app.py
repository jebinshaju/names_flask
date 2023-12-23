from flask import Flask, request, render_template, redirect, url_for

import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
   return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
 name = request.form.get('name')
 with open('names.json', 'r+') as f:
     try:
         data = json.load(f)
     except ValueError:
         data = []
     data.append(name)
     f.seek(0)
     json.dump(data, f)
     f.truncate()

 # Generate HTML table string
 table = "<table>\n<tr><th>Names</th></tr>\n" + \
         "\n".join([f"<tr><td>{name}</td></tr>" for name in data]) + \
         "</table>"

 # Add Clear button
 clear_button = '<form action="/clear" method="POST"><input type="submit" value="Clear Names"></form>'

 return f"Name saved successfully.<br>{table}<br>{clear_button}"



@app.route('/clear', methods=['POST'])
def clear():
   with open('names.json', 'w') as f:
       json.dump([], f)
   return redirect(url_for('index'))



if __name__ == "__main__":
   app.run(debug=True)

