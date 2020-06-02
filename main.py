from flask import request, jsonify, Flask,json
import flask
print(flask.__version__)
app= Flask(__name__)
app.config["DEBUG"] = True
print(flask.__version__)
data= { "name": "Matha Mabka",
         "age": 24,
         "gender":"Male"
	}
info= { "name": "Mik Berlin ",
         "age": 56,
         "gender":"Female"
	}
@app.route('/home', methods=['GET'])
def sendBack():

	return "Hellow word there"

@app.route('/view', methods=['GET'])
def view_container():

	return jsonify(info)
if __name__=="__main__":
	app.run(host='0.0.0.0', port=80)
