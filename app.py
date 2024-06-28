from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np

with open('lr_model.pkl', 'rb') as f:
    dt_clf = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    # Assuming content is a dictionary with keys corresponding to your columns
    duration = content.get('duration')
    protocol_type = content.get('protocol_type')
    service = content.get('service')
    flag = content.get('flag')
    src_bytes = content.get('src_bytes')
    dst_bytes = content.get('dst_bytes')
    count = content.get('count')
    dst_host_srv_count = content.get('dst_host_srv_count')
    dst_host_same_srv_rate = content.get('dst_host_same_srv_rate')
    dst_host_diff_srv_rate = content.get('dst_host_diff_srv_rate')
    class_value = content.get('class')
    
    # Here you can process or store the received data
    data_store.append(content)
    
    # Return a response
    return jsonify({'message': 'Data received successfully'}), 200

if __name__ == '__main__':
    app.run(debug=False,port=8080,host='0.0.0.0')
