import psutil
from flask import Flask, render_template

app = Flask(__name__)

#Whenever user gonna come to home path i.e. "/"  app is going to run
@app.route("/")

#function
def index():
    cpu_per = psutil.cpu_percent()
    mem_per = psutil.virtual_memory().percent
    message = None
    if cpu_per > 80 or mem_per >80 :
        message = "High consumption.. Please scale"
    return render_template("index.html",cpu_perc=cpu_per, mem_perc=mem_per, message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



