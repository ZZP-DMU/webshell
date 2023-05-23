from flask import Flask,render_template,request
import subprocess
 
app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def hello_world():
    if request.method == 'POST':
        command = request.form['cli']
        
        result = subprocess.check_output(command,shell=True)
        result = result.decode('utf-8')
        
        result_format = str()
        for i in result:
            if i == '\n':
                result_format = result_format+' '
            else:
                result_format = result_format+i
        
        return render_template('index.html',data=result_format)
    else:
        result_format = None
        return render_template('index.html',data=result_format)



if __name__ == "__main__":
    app.run(port=2023,host="127.0.0.1")
