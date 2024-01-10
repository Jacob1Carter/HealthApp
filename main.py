from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def landing():
    return render_template("landing.html")


@app.route('/results', methods=['GET'])
def results():
    search = request.args.get('query')

    url = 'https://trackapi.nutritionix.com/v2/search/instant/?query=' + search
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'x-app-id': 'e8aee087',
        'x-app-key': 'ee3fc88b259cf08a43ac94f8dd1afb62'
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    return render_template("results.html", search=search, data=data)


@app.route("/details/<item>")
def details(item):
    url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    headers = {
        "Content-Type": "application/json",
        "x-app-id": 'e8aee087',
        "x-app-key": 'ee3fc88b259cf08a43ac94f8dd1afb62'
    }
    query_data = {
        "query": item
    }
    response = requests.post(url, headers=headers, json=query_data)
    data = response.json()
    food_item = data["foods"][0]
    print(food_item)

    return render_template("details.html", item=food_item)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
