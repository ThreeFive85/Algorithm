# implementation 유형

'''
문제 설명 - 문자열 재정렬
    - 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에,
    그 뒤에 모든 숫자를 더한 겂을 이어서 출력합니다.
    - 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.
'''

'''
문제 해결 아이디어
    - 요구사항대로 충실히 구현하면 되는 문제
    - 문자열이 입력되었을 때 문자를 하나씩 확인
        - 숫자인 경우 따로 합계를 계산
        - 알파벳인 경우 별도의 리스트에 저장
    - 결과적으로 리스트에 저장된 아파벳을 정렬해 출력하고, 합계를 뒤에 붙여 출력
'''


def solution(s):
    alpha = []
    num = 0

    for spel in s:
        if spel.isalpha():
            alpha.append(spel)
        else:
            num += int(spel)

    # print(alpha.sort())
    # print(type(alpha))
    sort_alpha = sorted(alpha)

    if num != 0:
        sort_alpha.append(str(num))

    print(''.join(sort_alpha))
    return(''.join(sort_alpha))


solution("K1KA5CB7")  # ABCKK13
solution("AJKDLSI412K4JSJ9D")  # ADDIJJJKKLSS20
