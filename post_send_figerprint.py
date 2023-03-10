#pip3 install flask
from flask import Flask, request
import sqlite3

app = Flask(__name__)

# 处理POST请求的路由
@app.route('/fingerprint', methods=['POST'])
def process_fingerprint():
    # 获取POST请求中的指纹信息
    fingerprint = request.json['fingerprint']
    
    # 将指纹信息存储到数据库中
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO fingerprints (fingerprint) VALUES (?)', (fingerprint,))
    conn.commit()
    conn.close()
    
    # 返回响应
    return 'OK'
