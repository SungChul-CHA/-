# 월급(세후) : salary
# 월 수익률 : rate
# 이익실현 : 3개월
# 월세 : rent
# 식비(1일) : food
# 교통비(편도) : traffic
# 통신비 : communication
# 저축률 : save_rate
MONTH = 3
HOLIDAY = 4

salary = 3_500_000
rate = 0.03
rent = 700_000
food = 10_000
traffic = 7_000
communication = 54_000
save_rate = 0.5

def see_better(money):
    money_str = str(int(money))
    parts = []
    
    while len(money_str) > 3:
        parts.append(money_str[-3:])
        money_str = money_str[:-3]
    
    parts.append(money_str)
    parts.reverse()
    
    formatted_money = ','.join(parts)
    return formatted_money

def pos_deposit_per_month(salary, rent, food, traffic, communication):
    food_per_month = food * 3 * 30
    traffic_per_month = traffic * 2 * (30 - HOLIDAY) # 4일 제외
    left = salary - rent - food_per_month - traffic_per_month - communication

    return left

def after_invest(seed):
    investment_per_month = seed * (1 + rate)
    return int(investment_per_month) * MONTH

def invest(money, year):
    month = 12 * year
    month_3 = int(month / 3)

    profit = after_invest(money)
    result = profit
    for _ in range(month_3 - 1):
        result = int(result * (1 + rate)) + profit

    return result

def calculate_years_to_target(annual, target_money):
    current_money = 0
    year = 0
    annual_increase_rate = 0.001

    while current_money < target_money:
        salary = int(annual / 12)
        left = pos_deposit_per_month(salary, rent, food, traffic, communication)
        seed = int(left * save_rate)
        year += 1
        current_money = invest(seed, year)
        
        print(f"{year}년차 : {see_better(current_money)}원, 월급: {see_better(salary)}원, 나머지: {see_better(left)}원")

        annual += int(annual * annual_increase_rate)

    return year
    
def calculate_future_salary(starting_salary, years, raise_rate):
    future_salary = starting_salary
    for _ in range(years):
        future_salary += future_salary * (raise_rate / 100)
    print(f"{years}년 후 연봉: {future_salary:.2f}원")
    return future_salary

def calculate_required_raise_rate(starting_salary, target_salary, years):
    raise_rate = ((target_salary / starting_salary) ** (1 / years) - 1) * 100
    print(f"{years}년 후 목표 연봉을 달성하기 위한 연간 임금 상승률: {raise_rate:.2f}%")
    return raise_rate

# 테스트 코드
target_money = 1_000_000_000
annual = 36_000_000
years_needed = calculate_years_to_target(annual, target_money)
print(f"{see_better(target_money)}원을 달성하는데 걸리는 시간: {years_needed}년")

year = 10

left = pos_deposit_per_month(salary, rent, food, traffic, communication)
seed = int(left * save_rate)
result = invest(seed, year)
s_money = see_better(seed)

print("투자금: ", s_money)
print(year, "년 투자 결과: ", see_better(result))

seed = 2_000_000
result = invest(seed, 5)
print("2,000,000원을 5년간 투자한 결과: ", see_better(result))

calculate_future_salary(45000000, 10, 6)  # 초봉 4500만원, 10년, 연간 임금 상승률 6%
calculate_required_raise_rate(50000000, 100000000, 10)  # 초봉 5000만원, 목표 연봉 1억원, 10년
