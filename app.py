import json
import pathlib
import html

from flask import Flask, render_template
import markdown2

app = Flask(__name__)

conversations = json.loads(pathlib.Path("conversations.json").read_text())


@app.route("/")
def index():
    return render_template(
        "index.jinja2",
        conversations=conversations,
        markdown2=markdown2,
        html=html,
    )


def main():
    app.run(port=8085, debug=True)


if __name__ == "__main__":
    main()