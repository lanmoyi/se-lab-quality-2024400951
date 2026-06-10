import pytest
from app import app

# 测试首页接口
def test_hello_route():
    response = app.test_client().get('/')
    assert response.status_code == 200

# 测试健康检查接口
def test_health_route():
    response = app.test_client().get('/health')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "ok"
