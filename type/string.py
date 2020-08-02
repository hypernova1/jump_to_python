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


# 문자열 포매팅
## 숫자 대입
format = "I eat %d apples." % 3

## 문자열 대입
format2 = "I eat %s apples." % "five"

## 두 개 이상의 값 넣기
number = 10
day = "three"
format3 = "I ate %d apples. so I was sick %s days." % (number, day)

## % 사용시
error = "Error is %d%%" % 98 # %%로 작성해야 표시가 된다. (문자열 안에 포매팅 연산자가 없으면 홀로 쓰여도 상관 없다.)

## 포맷 코드와 숫자 함께 사용하기
### 오른쪽 정렬
format4 = "%10s" % "hi" # '        hi'

### 왼쪽 정렬
format5 = "%-10sjane." % "hi" # 'hi        jane.'

### 소수점 표현하기
format6 = "%0.4f" % 3.42134234 # 3.4213
format7 = "%10.4f" % 3.42134234 # '    3.4213'


# format 함수를 이용한 포매팅
## 숫자 대입하기
format8 = "I eat {0} apples".format(3)

## 문자열 대입하기
format9 = "I eat {0} apples".format("five")

## 두 개 이상의 값 넣기
format10 = "I ate {0} apple. so I was sick for {1} days".format(10, "three")

## 이름으로 넣기
format11 = "I ate {number} apple. so I was sick for {day} days".format(number=10, day=3)


# f문자열 포매팅(파이썬 3.6 이상 부터 사용 가능)
name = "홍길동"
age = 30
f'나의 이름은 {name}입니다. 나이는 {age+1}입니다.'

## 딕셔너리 사용
d = {'name': '홍길동', 'age': 30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'


# 문자열 관련 함수들
## 문자 개수 세기
a = "hobby"
a.count('b') # 2

## 문자열 위치 찾기
a = "Python is the best choice"
a.find('b') # 14 (존재하지 않으면 -1을 반환)
a.index('b') # 14 (존재하지 않으면 오류 발생)

## 문자열 삽입
",".join("abcd") # 'a,b,c,d'
",".join(['a', 'b', 'c', 'd']) # 'a,b,c,d'