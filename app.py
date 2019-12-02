from flask import Flask, request, render_template 
from api import WordSearchClass
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('homepage.html')


# find method on search button call operates.       
@app.route("/find",methods=['POST'] )
def find():

    # fetching input from the user
    document = request.form['text_doc']
    searchWord = request.form['word']

    #converting text to lower case
    searchWord = searchWord.lower()
    api = WordSearchClass(document)
    lists = api.searchForWord(searchWord)
    dictionary_paragraph = api.index()

    return render_template('result.html', lists = lists, len = len(lists),dictionary_paragraph = dictionary_paragraph, search_word = searchWord)


if __name__ == "__main__":
    app.run(debug=True)