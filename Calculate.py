from GetData import classify_callsign
def calculate_minutes_per_area(sessions):
    """根据session数据计算每个地区的上线时间"""
    area_minutes = {"home_division": 0, "Others": 0}

    for session in sessions:
        area = classify_callsign(session['callsign'])
        area_minutes[area] += float(session['minutes_on_callsign'])

    return area_minutes

def check_tvcp_compliance(home_division_hours, other_hours):
    """根据TVCP要求检查时长是否符合要求"""
    messages = []
    
    if home_division_hours < 3:
        messages.append("本分部时长不够")
    
    if home_division_hours < other_hours:
        messages.append(f"Home_Division上线时长({home_division_hours:.2f} 小时) 少于其他分部的时长({other_hours:.2f} 小时)。")
    else:
        messages.append(f"Home_Division上线时长({home_division_hours:.2f} 小时) 大于等于其他分部的时长({other_hours:.2f} 小时)。")
    
    return "\n".join(messages)
