# -*- coding: utf-8 -*- 

# 문자열을 다루는 여러가지 방법
## 일반 문자열
str1 = "Python's favorite food is perl"
str2 = 'Python is very easy'

## 멀티 라인
str3 = """
Life is too short
You need python
"""
str4 = '''
Life is too short
You need python
'''


# 문자열 연산
## 문자열 더하기
head = "Python"
tail = " is fun!"
context = head + tail

## 문자열 곱하기
print("=" * 50)
print("My Program")
print("=" * 50)


## 문자열 길이 구하기
a = "Life is too short, You need python"
len(a)


# 문자열 인덱싱
life = "life"
print(life[3]) # e
print(life[-1]) # e > 뒤에서 부터 첫 번째 문자를 가리킴
print(life[0] == life[-0]) # 0과 -0은 같다.

## 문자 가져오기
### 인덱싱을 이용하여 가져오기
word1 = a[0] + a[1] + a[2] + a[3]
print(word1)

### 슬라이싱을 이용하여 가져오기
str_slice1 = a[0:4] # 4번 인덱스 이전 문자까지 잘라냄
print(str_slice1) #life
str_slice2 = a[5:8]
print(str_slice2) #is


