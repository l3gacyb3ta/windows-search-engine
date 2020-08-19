from flask import Flask, request, render_template, send_from_directory
import sqlite3, os
app = Flask(__name__)

conn = sqlite3.connect('tiny_BETA.db')
c = conn.cursor()

@app.route('/', methods=['GET','POST'])
def hello_world():

    return render_template("index.html")

@app.route('/data', methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect('tiny_BETA.db')
    c = conn.cursor()
    data = request.form['query']
    c.execute("SELECT * FROM files WHERE FILENAME LIKE '%"+data+"%'")
    data = c.fetchall()
    conn.close()
    
    return render_template("data.html", len = len(data), data = data)

@app.route('/img/<path:path>', methods=['GET', 'POST'])
def send_js(path):
    return send_from_directory('templates', path)


@app.route('/open/<path:path>', methods=['GET', 'POST'])
def open(path):
    os.system("start "+path)
    return "Opened!"

