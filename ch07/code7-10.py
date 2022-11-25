# 기능성
def your_life_expectancy(age):
    if age<85:
        return 72 - 0.8 * age
    return 22 - 0.2 * age

# 사용자 인터페이스
age = int(input('몇살인가요? '))

# 기능성을 사용자 입력과 조합하고 결과를 출력
exp_years = your_life_expectancy(age)
print(f'당신의 기대 여명은 {exp_years} 년입니다. 현명하게 사용하세요!')