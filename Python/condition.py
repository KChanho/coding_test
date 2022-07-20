#조건문

x = 15

if x >= 10:
  print("x >= 10")  #python에서 코드의 블록을 들여쓰기(4개의 공백 문자가 표준)로 지정

if x>0:
  print("x>0")
elif x == 0:
  print("x==0")
else:
  print("x<0")
 
#비교 연산자: ==, !=, >, <, >=, <=
#논리 연산자: and, or, not
#기타 연산자: in, not in (리스트, 튜플, 문자열, 딕셔너리 모두 사용 가능)
#pass 키워드: 아무것도 처리하고 싶지 않을 때, 틀만 미리 짤 때
#조건문의 간소화: 내용 소스코드가 한 줄인 경우 조건문과 내용 소스코드를 한 줄로 표현 가능
result = 'Success' if x >= 10 else 'Fail' #조건부 표현식: if ~ else 문을 한줄에 작성
if 0 < x < 20:  #수학의 부등식 사용 가능 (x>0 and x<20와 동일)
  print("0 < x < 20")
