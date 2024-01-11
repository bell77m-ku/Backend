from flask import Flask, jsonify

app = Flask(__name__)

books = [{"id":1,"title":"Book1", "author":"me"},{"id":2,"title":"Book2", "author":"me"},{"id":3,"title":"Book3", "author":"me"}]

@app.route("/")
def Greet():
    return "<p>Hello world</p>"

@app.route("/books", methods=["GET"])
def get_all_books():
    return jsonify({"books":books})

@app.route("/books/<int:book_id>", methods=["GET"])
def get_books(book_id):
    book = next((b for b in books if b["id"]==book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error":"Book not found"}), 404


if __name__ == "__main__":
    app.run(host="localhost", port="5000" ,debug=True)