from flask import request, jsonify, Flask,json

app= Flask(__name__)

data= { "name": "Godwin",
         "age": 24,
         "gender":"Male"
	}
@app.route('/home')
def sendBack():

	return jsonify(data)
if __name__=="__main__":
	app.run(host='0.0.0.0')
