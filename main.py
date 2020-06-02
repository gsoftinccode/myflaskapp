from flask import request, jsonify, Flask,json

app= Flask(__name__)
app.config["DEBUG"] = True

data= { "name": "Matha Mabka",
         "age": 24,
         "gender":"Male"
	}
info= { "name": "Mik Berlin ",
         "age": 56,
         "gender":"Female"
	}
@app.route('/home', METHOD=['GET'])
def sendBack():

	return "Hellow word there"

@app.route('/home', METHOD=['GET'])
def sendBack():

	return jsonify(info)
if __name__=="__main__":
	app.run(host='0.0.0.0', port=80)
