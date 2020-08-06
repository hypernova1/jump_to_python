# -*- coding: utf-8 -*- 

# 딕셔너리: key, value 쌍으로 이루어진 자료형

## 선언
dic = {'name': 'sam', 'phone': '01011112222', 'birth': '1990'}

## 추가하기
a = {1: 'a'}
a[2] = 'b'
a # {1: 'a', 2: 'b'}

a['name'] = 'kwon'
a # {1: 'a', 2: 'b', 'name': 'kwon'}

## 삭제하기
del a[1]
a # {2: 'b', 'name': 'kwon'}

## 값 가져오기
a[2] # 'b'


## 내장 함수
### 키 리스트 가져오기: 리스트와 비슷하지만 리스트 고유 함수를 쓸 수 없다.
for k in a.keys():
    print(k)

list(a.keys()) # 키를 배열로 만들기

### 값 리스트 가져오기
a.values() # dict_values(['b', 'kwon'])

### 쌍 얻기
a.items() # dict_items([(2, 'b'), ('name', 'kwon')])

### key로 value 얻기
### a['name']과의 차이: a['name']의 경우 키가 존재하지 않으면 오류가 발생하지만 a.get('name')은 None을 반환한다.
a.get('name')

### key가 없을 경우 디폴트 값을 가져오기
a.get('foo', 'bar')

### key가 있는지 검사
'name' in a # True

### 요소 비우기
a.clear() # {}