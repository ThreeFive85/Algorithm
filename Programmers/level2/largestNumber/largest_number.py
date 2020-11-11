# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42746
# 참고 블로그 : https://wooaoe.tistory.com/82

def solution(numbers):
    answer = ''
    str_number = list(map(str, numbers))
    print(str_number)
    str_number.sort(key=lambda x: x*3, reverse=True)
    print(str_number)

    return str(int(''.join(str_number)))


'''
참고로 ''.join(str_number)만 했을 경우 마지막 테스트 경우 실패한다.
생각에 문자열 00000은 숫자 0으로 변환해야하므로 문자열을 숫자로 변환해서 수를 만들고 다시 문자로 변환
'''

# 순열은 itertools.permutations() 함수를 사용하면 구할 수 있다.
# 참고 블로그 : https://programmers.co.kr/learn/courses/4008/lessons/12836
