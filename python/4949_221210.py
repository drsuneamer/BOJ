# [BOJ] 4949. 균형잡힌 세상

OP = ['(', '[']
CP = [')', ']']

while 1:
    S = input()
    if S == '.':
        break

    # 괄호가 아예 없는 경우 yes 처리
    if '(' not in S and ')' not in S and '[' not in S and ']' not in S:
        print('yes')

    # 여기서부터 문제풀이
    else:
        ans = 'yes'
        stack = []
        for s in S:
            if s in OP:  # 여는 괄호일 경우 stack에 push
                stack.append(s)

            elif s in CP:   # 닫는 괄호일 경우
                if len(stack) == 0:
                    ans = 'no'
                elif s == ')' and stack[-1] != '(':
                    ans = 'no'
                elif s == ')' and stack[-1] == '(':
                    stack.pop(-1)
                elif s == ']' and stack[-1] != '[':
                    ans = 'no'
                elif s == ']' and stack[-1] == '[':
                    stack.pop(-1)

        # 처리가 끝나도 아직 열린 괄호가 남아있는 경우
        if len(stack) > 0:
            ans = 'no'

        print(ans)
