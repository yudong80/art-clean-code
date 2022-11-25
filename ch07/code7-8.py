## 의존성
import re


## 데이터
page = '''
<!DOCTYPE html>
<html>
<body>

<h1>My Programming Links</h1>
<a href=”https://app.finxter.com/”>test your Python skills</a>
<a href=”https://blog.finxter.com/recursion/”>Learn recursion</a>
<a href=”https://nostarch.com/”>Great books from NoStarchPress</a>
<a href=”http://finxter.com/”>Solve more Python puzzles</a>

</body>
</html>
'''

## 한 줄짜리 프로그램
practice_tests = re.findall("(<a.*?finxter.*?(test|puzzle).*?>)", page)

## 결과
print(practice_tests)
# [('<a href="https://app.finxter.com/ ">test your Python skills</a>','test'),
# ('<a href="http://finxter.com/">Solve more Python puzzles</a>', 'puzzle')]