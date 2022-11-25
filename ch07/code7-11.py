import matplotlib.pyplot as plt


def your_life_expectancy(age):
    '''기대 여명(단위 년)을 반환합니다.'''
    if age<85:
        return 72 - 0.8 * age
    return 22 - 0.2 * age


# 처음 100세까지 그래프 출력
plt.plot(range(100), [your_life_expectancy(i) for i in range(100)])

# 그래프 스타일 적용
plt.xlabel('나이')
plt.ylabel('기대 여명')
plt.grid()

# 표시하고 그래프를 저장
plt.savefig('age_plot.jpg')
plt.savefig('age_plot.pdf')
plt.show()
