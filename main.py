import requests

def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
# if __name__ == '__main__':
def call_external_api(url, params=None):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # 检查请求是否成功
        return response.json()  # 返回API的响应结果，这里假设返回的是JSON数据
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None

# 调用外部系统的接口示例
api_url = "https://api.example.com/data"
api_params = {"param1": "value1", "param2": "value2"}

result = call_external_api(api_url, params=api_params)

if result:
    print("API调用成功！")
    print(result)
else:
    print("API调用失败！")