from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def edit():
    if request.method == "POST":
        movies_name = request.form["movie_name"]
        author = request.form["author"]
        number = request.form["number"]
        channel_name = request.form["channel_name"]

    return render_template("forms.html")


if __name__ == "__main__":
    app.run(debug=True)
