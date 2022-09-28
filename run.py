from flask import Flask
from flask import render_template

app = Flask(__name__)


posts = ['Noticias','Deportes','Sociales','Entretenimiento']

@app.route("/")
def index():
    return render_template("index.html", num_posts=len(posts))
  # return '<!DOCTYPE html> <html lang="es"> <head>     <meta charset="UTF-8">    <title>Practica Flask: Miniblog</title> </head><body> 4 posts</body></html>'


@app.route("/p/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title=slug)


@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    return render_template("admin/post_form.html", post_id=post_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
