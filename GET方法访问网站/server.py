import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
        try:
                province = flask.request.args.get("province")
                city = flask.request.args.get("city")
                print(province, city)
                return province + "," + city
        except Exception as err:
                return str(err)


if __name__ == "__main__":
        app.run()



