from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def landing():
    return render_template("landing.html")


@app.route('/results', methods=['GET'])
def results():
    search = request.args.get('query')

    #yeaaaaaaaaaaaaaaaaaaaaaaaaa

    return render_template("results.html", search=search)


@app.route("/details/<item>")
def details(item):
    return render_template("details.html", item=item)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
