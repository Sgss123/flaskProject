from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from random import randint
import os
import sys

app = Flask(__name__)

WIN = sys.platform.startswith("win")
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = "sqlite:///"
else:  # 否则使用四个斜线
    prefix = "sqlite:////"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = prefix + os.path.join(app.root_path, "data.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # 关闭对模型修改的监控
# 在扩展类实例化前加载配置
db = SQLAlchemy(app)

@app.route("/")
def hello_world():  # put application's code here
    return render_template("homepage.html", type="首页", name=name)


@app.route("/friend", methods=["GET", "POST"])
def index():
    if request.methods == "POST":
        return "<h1>Hello World</h1>"
    return render_template(
        "friend.html", type="申请友情链接", name=name, id=randint(1, 6553625565)
    )


@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    # 返回模板和状态码
    return (render_template("404.html", name=name), 404)


if __name__ == "__main__":
    app.run()

name = "Sgss"

class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字
    email = db.Column(db.String (40))
    pwd = db.Column(db.Text)