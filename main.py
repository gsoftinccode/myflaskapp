from flask import request, jsonify, Flask,json

app= Flask(__name__)
app.config["DEBUG"] = True

data= { "name": "Godwin",
         "age": 24,
         "gender":"Male"
	}
@app.route('/home')
def sendBack():

	return "Hellow word there"
if __name__=="__main__":
	app.run(host='0.0.0.0', port=80)
