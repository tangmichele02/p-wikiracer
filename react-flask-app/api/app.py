from flask import Flask, render_template, request, jsonify
import time
from flask_cors import CORS
import wikipediaapi
import wikipedia

app = Flask(__name__)
CORS(app)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route("/", methods=['GET', 'POST'])
def send():
    return render_template('home.html')

@app.route('/api')
def api():
    
    searchTerm = request.args.get("textInput")

    print(searchTerm)

    # myResults = [searchTerm, searchTerm + "1", searchTerm + "2"]
    myResults = get_searches(searchTerm,5)

    response = {'searchResult': myResults}
    return jsonify(response)


def get_searches(text, count):
    # wiki = wikipediaapi.Wikipedia('en')
    searches = wikipedia.search(text, results=count)
    print(searches)
    return searches

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)

# from flask import Flask, render_template, request
# app = Flask(__name__)

# @app.route("/", methods=['GET', 'POST'])
# def send():
#     if request.method == 'POST':
#         start = request.form['start']
#         end = request.form['end']
#         if (start != "") and (end != ""):
#             path_val = path(start, end)
#             return render_template('output.html',path_val=path_val)
#     return render_template('home.html')


# # will replace by importing backend function 
# def path(start, end):
#     return ("The final path is " + start + " to " + end)


# if __name__ == '__main__':
#     app.run(host = '0.0.0.0', port = 8080)