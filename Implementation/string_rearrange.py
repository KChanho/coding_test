"""
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어짐
모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력
"""

data = input()
sum = 0
result = []

for d in data:
  if int(d) >= 0 and int(d) <= 9: #문자가 알파벳인지 확인하는 메소드 .isalpha()로 더 간단하게 작성 가능
    sum += int(d)
  else:
    result.append(d)

result.sort()
if sum != 0:
  result.append(str(sum))

print(''.join(result) #.join() 메소드를 사용하여 리스트의 원소들을 구분자 없이 합쳐 하나의 문자열로 반환
