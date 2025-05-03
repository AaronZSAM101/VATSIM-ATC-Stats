from GetData import classify_callsign
def calculate_minutes_per_area(sessions):
    """根据session数据计算每个地区的上线时间"""
    area_minutes = {"home_division": 0, "Others": 0}

    for session in sessions:
        area = classify_callsign(session['callsign'])
        area_minutes[area] += float(session['minutes_on_callsign'])

    return area_minutes

def check_tvcp_compliance(sessions):
    """检查是否符合 TVCP 要求"""
    area_minutes = calculate_minutes_per_area(sessions)
    area_hours = {
        "home_division": area_minutes["home_division"] / 60,
        "others": area_minutes["Others"] / 60,
        "total": (area_minutes["home_division"] + area_minutes["Others"]) / 60
    }
    home = area_hours["home_division"]
    other = area_hours["others"]
    total = area_hours["total"]

    messages = []

    if home < 3:
        messages.append("本分部（Home Division）时长不足 3 小时。")

    if home < other:
        messages.append(f"Home Division 上线时长 ({home:.2f} 小时) 少于其他区域 ({other:.2f} 小时)。")
    else:
        messages.append(f"Home Division 上线时长 ({home:.2f} 小时) 大于等于其他区域 ({other:.2f} 小时)。")

    if home < total / 2:
        messages.append(f"未满足 TVCP 要求：Home Division 上线时间为总时长的 {home / total:.1%}，应至少为 50%。")
    else:
        messages.append("满足 TVCP 要求：Home Division 上线时间占总时长至少 50%。")

    return "\n".join(messages)
