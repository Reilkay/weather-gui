import requests


class WeeklyWeather:
    def __init__(self, config: dict, city: str) -> None:
        # 请求地址
        self.url = "https://www.tianqiapi.com/api?version=v1&appid=" + config[
            'appid'] + "&appsecret=" + config['appsecret'] + "&city=" + city

    def get(self) -> dict:
        # 发送get请求
        content = requests.get(self.url)
        # 获取返回的json数据
        return content.json()
