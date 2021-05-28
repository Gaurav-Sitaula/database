from flask import Flask,render_template  
app= Flask(__name__)

@app.route('/')
def home():

    #return "This is Gaurab first flask website";
    return render_template('hello.html')

@app.route('/about')
def About():
    return "<h1 style='color: red;'>This is Gaurab About Page</h1>";

@app.route('/greetings/<uname>')
def Greetings(uname):
    #return "Good Afternoon "+name+" Have a wonderful day ";
    return render_template('greetings.html',name=uname)

if __name__ =='__main__':  
    app.run(debug = True)