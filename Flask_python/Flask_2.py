from flask import Flask ,redirect,url_for
app=Flask(__name__)

@app.route("/CEO")
def CEO():
    return "<h1>Welcome CEO</h>"

@app.route("/guest/<name>")
def guest(name):
    return "<h1> Welcome %s, our new guest.......</h1>" %name

@app.route("/user/<name>")
def user(name):
    if name=="CEO":return redirect(url_for("CEO"))
    else: return redirect(url_for("guest",name=name))

if __name__ == "__main__":
    app.run(debug=True)