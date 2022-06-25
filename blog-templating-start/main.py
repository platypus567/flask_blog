from flask import Flask, render_template
import requests
link = "https://api.npoint.io/c790b4d5cab58020d391"
res = requests.get(link)
data = res.json()
app = Flask(__name__)

@app.route('/')
def home():

    return render_template("index.html", data=data)
@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in data:
        if blog_post['id'] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)
