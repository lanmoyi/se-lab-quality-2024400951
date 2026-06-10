from flask import Flask
app = Flask(__name__)

# 首页接口
@app.route('/')
def hello():
    return "DevOps 综合实践实验成功！应用已正常运行～"

# 健康检查接口（测试用）
@app.route('/health')
def health():
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
