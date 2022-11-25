def your_life_expectancy():
    age = int(input('몇살인가요? '))

    if age<85:
        exp_years = 72 - 0.8 * age
    else:
        exp_years = 22 - 0.2 * age

    print(f'당신의 기대 여명은 {exp_years} 년입니다. 현명하게 사용하세요!')

your_life_expectancy()