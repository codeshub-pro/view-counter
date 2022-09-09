from flask import Flask
from replit import db
app = Flask(__name__)

@app.route("/")
def index():
  return "Welcome to View-Counter"

@app.route("/<website>/counter.js")
def counter(website=""):
  if website:
    count = db[website] = int(db.get(website,0)) + 1
    return f"VIEW_COUNT = {count};"
  else:
    return "//No Output "

@app.route("/reset/<website>")
def reset(website=""):
  if website:
    db[website] = 0;
    return "Done"
  else:
    return "//No Output"
@app.route("/check/<website>")
def check(website):
  return str(db.get(website,0))
  
app.run(host="0.0.0.0",port=81)
