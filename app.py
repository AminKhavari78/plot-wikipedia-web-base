import base64
from io import BytesIO
# in this example use some basic flask app
from flask import Flask
from flask import render_template, request, redirect, url_for,flash
from matplotlib.figure import Figure
import sqlite3
from wiki.analysis import final


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/login')
def login():
    return render_template("login.html");


@app.route('/validate', methods=["POST"])
def validate():

    if request.method == 'POST':
        name = request.form.get('name')
        search = request.form.get('search')
        finals = final(search)

        for x in finals:
            f = open("myfile.txt", "a")
            f.write(str(x))
            f.write(",")
            f.close()

        #Database Insertion
        conn = get_db_connection()
        conn.execute('INSERT INTO posts (name, search) VALUES (?, ?)',
                     (name, search))
        conn.commit()
        conn.close()

        return redirect(url_for("success"))
    return redirect(url_for("login"))


@app.route('/success')
def success():
    flash("The processing get some time be Funny")

    conn = get_db_connection()
    res = conn.execute("SELECT search FROM posts").fetchone()

    conn.commit()
    conn.close()

    f = open("myfile.txt", "r+")
    read = f.read()
    read = list(read)
    listShow = read
    for x in listShow:
        if x == ",":
            listShow.remove(x)
    integer_map = map(int, listShow)
    integer_list = list(integer_map)
    f.truncate(0)
    f.close()

    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    # plot it
    ax.hist(integer_list)
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"


if __name__ == '__main__':
    app.run(debug=True)