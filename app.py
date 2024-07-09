import requests
from flask import Flask,jsonify,request
from dotenv import load_dotenv
import os
app = Flask(__name__)
load_dotenv()
# print(f"Bearer ${os.getenv('TOKEN')}")
API_URL = "https://api-inference.huggingface.co/models/BAAI/bge-small-en-v1.5"
headers = {"Authorization": f"Bearer {os.getenv('TOKEN')}"}

@app.route("/",methods=["POST"])
def getembeddings():
    data = request.json['input']
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    output = query({
        "inputs": f"${data}"
    })
    return output

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)