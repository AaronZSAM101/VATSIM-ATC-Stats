from GetData import *
from Calculate import *
from PersonalData import cid

def main():
    # 获取当前季度的开始和结束日期
    start_date, end_date = get_current_quarter()

    # 获取ATC sessions数据
    sessions = fetch_sessions_data(cid, start_date, end_date)

    # 计算每个地区的上线时间（分钟）
    area_minutes = calculate_minutes_per_area(sessions)

    # 将分钟数转换为小时数
    home_division_hours = area_minutes["home_division"] / 60
    other_hours = area_minutes["Others"] / 60

    # 打印每个地区的上线时间
    print(f"本分部/vACC的上线时间为: {home_division_hours:.2f} 小时\n其他分部/vACC的上线时间为: {other_hours:.2f} 小时")

    # 检查是否符合TVCP要求
    result = check_tvcp_compliance(home_division_hours, other_hours)
    input(result)

if __name__ == "__main__":
    main()
