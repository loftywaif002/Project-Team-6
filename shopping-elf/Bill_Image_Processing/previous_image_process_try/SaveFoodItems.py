from flask import Flask
from flask import request
from flask import json
import requests
app = Flask(__name__)

import urllib

@app.route("/v1/imageSave/<filename>", methods=['POST'])
def userInput(filename):
	if request.method == 'POST':
		payload = {'isOverlayRequired': 'true',
               	   'apikey': 'helloworld',
               	   'language': 'eng',
               	  }
    	with open(filename, 'rb') as f:
    		r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    	print r.json()
    	return r.content.decode()
    	#res_json = json.load(r.content.decode())
    	#dicti = res_json['WordText']
    	#return res_json
		
if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
