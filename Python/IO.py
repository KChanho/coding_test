#입력 함수
a = input() #한 줄의 문자열을 입력 받음
a = list(map(int, input().split())) #map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
a, b, c = map(int, input().split()) #abc를 공백을 기준으로 구분하여 입력
a = sys.stdin.readline().rstrip() #sys 라이브러리에 정의되어 있는 sys.stdin.readline() 메서드를 이용하면 입력 처리 속도가 빨라짐

#출력 함수
print(a, b, c, end=' ')  #콤마로 변수를 구분하여 출력, 기본적으로 출력 이후에 줄 바꿈 수행(end 속성 수정하여 변경 가능)
print(f"정답은 {a}입니다.") #f-string: 문자열 중간에 변수 출력 가능
