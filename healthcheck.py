from flask import Flask


def main():
    app = Flask(__name__)
    app.run(port=8080, host="0.0.0.0")

    @app.route("/")
    def hello_world():
        return "Hello, World!"


if __name__ == '__main__':
    main()
