import re

text = '''
    Ha! let me see her: out, alas! She’s cold:
    Her blood is settled, and her joints are stiff;
    Life and these lips have long been separated:
    Death lies on her like an untimely frost
    Upon the sweetest flower of all the field.
'''

# 글자 ‘f’로 시작하는 모든 단어들을 찾음.
f_words = re.findall('\\bf\w+\\b', text)
print(f_words)

# 글자 ‘l’로 시작하는 모든 단어들을 찾음.
l_words = re.findall('\\bl\w+\\b', text)
print(l_words)