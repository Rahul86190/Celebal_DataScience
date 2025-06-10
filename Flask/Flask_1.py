from flask import Flask
app=Flask(__name__)

@app.route('/')
def Home():
    return "<h1>This is Falsk. <br>Write I'm your name in the url for greetings</h1>"

@app.route("/I'm <name>")     # for int - <int:int_no>,  str-<str:any_str>,   float - <float:float_no>
def hallo_world(name):
    return "<h1>Hello %s </h1>" %name       # string - %s  , int - %d  , float - %f  

if __name__=="__main__":
    app.run(debug=True)