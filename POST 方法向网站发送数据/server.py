import flask

app = flask.Flask(__name__)
#一般GET的数据时放在地址栏后面的，参数简单，数据量少，而POST的数据时表单数据，数据量大。

@app.route("/", methods=["GET", "POST"])#那么这个函数即可以接受GET请求也可以接受POST请求。

def index():
    try:
        province=flask.request.values.get("province")
        city=flask.request.values.get("city")
        note=flask.request.values.get("note")
        print(province)
        print(city)
        print(note)
        return province+"\n"+city+"\n"+note
    except Exception as err:
        print(err)

if __name__ == "__main__":
    app.run()