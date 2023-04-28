from flask import Flask, render_template
import requests

app = Flask(__name__)
blogs_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blogs_url)
blogs_data = response.json()
print(blogs_data[0]['title'])


def post():
    blog2_title = blogs_data[1]['title']
    blog2_subtitle = blogs_data[1]['subtitle']
    return render_template("post.html", title=blog2_title, subtitle=blog2_subtitle)


@app.route('/')
def home():
    blog1_title = blogs_data[0]['title']
    blog1_subtitle = blogs_data[0]['subtitle']
    blog2_title = blogs_data[1]['title']
    blog2_subtitle = blogs_data[1]['subtitle']
    return render_template("index.html", title=blog1_title, subtitle=blog1_subtitle,
                           title2=blog2_title, subtitle2=blog2_subtitle)


@app.route('/<int:num>')
def post_blog(num):
    print(num)

    return render_template("post.html", body_post=blogs_data[num]['body'])

    # elif num == 2:
    #     body1 = blogs_data[1]['body']
    # else:
    #  print("sdfs")


if __name__ == "__main__":
    app.run(debug=True)
