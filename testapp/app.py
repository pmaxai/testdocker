from flask import Flask, request, render_template,  redirect
app = Flask(__name__)

@app.route('/')
def html_home():
  return render_template("home.html")
  
