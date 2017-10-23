from flask import Flask, request
from flask import render_template
import os

app = Flask(__name__)

fake_news = ["a Banana is a better president that an orange", "Fruit declares war", "Meat running scared"]

@app.route("/")
def index(): # function is beeing called from within flask after the "/" in the web address.
    return render_template("search.html")
    
@app.route("/search/")
def do_search(): # function is beeing called from within flask after the "/search" in the web address.
    #q = request.args.get("query") #pulls out the query from the url/uri
    #return "You searched for {}".format(q)
    
    return render_template("results.html", items = fake_news)

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))