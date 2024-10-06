from datetime import datetime
import requests

# 各地区的callsign前缀
CALLSIGN_PREFIXES = {
    "home_division": ["PRC", "ZB", "ZG", "ZH", "ZJ", "ZL", "ZM", "ZP", "ZS", "ZW", "ZY"]
}

def get_current_quarter():
    """根据当前日期，返回季度的开始和结束日期"""
    now = datetime.now()
    current_year = now.year
    current_month = now.month

    if current_month in [1, 2, 3]:
        return f"{current_year}-01-01", f"{current_year}-03-31"
    elif current_month in [4, 5, 6]:
        return f"{current_year}-04-01", f"{current_year}-06-30"
    elif current_month in [7, 8, 9]:
        return f"{current_year}-07-01", f"{current_year}-09-30"
    else:
        return f"{current_year}-10-01", f"{current_year}-12-31"

def classify_callsign(callsign):
    """根据callsign前缀，归类到相应的地区"""
    for area, prefixes in CALLSIGN_PREFIXES.items():
        if any(callsign.startswith(prefix) for prefix in prefixes):
            return area
    return "Others"

def fetch_sessions_data(cid, start_date, end_date):
    """发送请求并获取ATC session数据"""
    url = f'https://api.vatsim.net/api/ratings/{cid}/atcsessions/?start={start_date}&end={end_date}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    else:
        raise Exception(f"请求失败，状态码: {response.status_code}")
