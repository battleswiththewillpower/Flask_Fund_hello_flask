from flask import Flask, render_template
app = Flask(__name__) 
                        

@app.route('/')         
def hello_world():
    return render_template('index.html')  

@app.route('/success')
def success():
    return 'Success!'


@app.route('/hello/<string:ashley>/<int:num>')
def hello(ashley,num):
    return render_template("hello.html", ashley= ashley,num= num)

#this need to stay at the bottom
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

