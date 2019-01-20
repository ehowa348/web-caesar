from flask import Flask
from caesar import rotate_string
from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True
form="""<html>
   <head>
   <style>
   form {
   background-color: #eee;
   padding: 20px;
   margin: 0 auto;
   width: 540px;
   font: 16px sans-serif;
   border-radius: 10px;
   }
   textarea {
   margin: 10px 0;
   width: 540px;
   height: 120px;
   }
   </style>
   </head>
   <body>
   <form method="post">
   <label>Rotate by:
   <input type="text" name="rot" placeholder="0"/>
   </label>
   <textarea name="text"></textarea>
   <input type="submit" value="Submit Query"/>
   </body>
  

</html>"""

@app.route('/')
def index():
    return form

if __name__ == "__main__":
    app.run()
@app.route("/")
def index():
    return form 

app.run()

@app.route("/", methods=["POST"])
def encrypt():
    to = str(request.form.get('to', None))
    text = str(request.form.get('text', None))

    return '<h1>' + rotate_string(text, to) + '</h1>'