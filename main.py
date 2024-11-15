from flask import Flask, render_template, request
from flask_wtf import FlaskForm
import wtforms


app = Flask(__name__, template_folder="temp/templ_1")
app.secret_key = "123"


class PostForm(FlaskForm):
    author = wtforms.StringField("Напишіть автора")
    text = wtforms.TextAreaField("Напишіть свою статтю")
    price = wtforms.IntegerField("Введіть ціну")
    submit = wtforms.SubmitField("Відправити")


@app.route("/add_post_wtf/", methods=["GET", "POST"])
def add_post_wtf():
    form =  PostForm()
    if request.method == "POST":
        author = form.author.data
        text = form.text.data
        price = form.price.data
        return f"{author = }; {text = }; {price = }"
    return render_template("add_post_wtf.html", form=form)


@app.route("/add_post/", methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        author = request.form.get("author")
        text = request.form.get("text")
        print(f"{author = }")
        print(f"{text = }")
        return f"{author = }; {text = }"
    return render_template("add_post.html")




if __name__ == "__main__":
    app.run(debug=True)