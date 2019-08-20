import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())
for tc in range(1, T+1):
    C = list(map(str, input().split()))
    M = list(map(str, input().split()))

    num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    M_num = []
    num_str = ''
    i = 0
    while i < int(C[1]):
        if M[i] in num:
            for k in range(10):
                if num[k] == M[i]:
                    M_num.append(k)
            i = i+1

    # 33333
    # for i in range(len(M_num)):
    #     for j in range(i+1, len(M_num)):
    #         if M_num[i] > M_num[j]:
    #             M_num[i], M_num[j] = M_num[j], M_num[i]
    #
    # i = 0
    # for j in range(10):
    #     while i < int(C[1]):
    #         if M_num[i] == j:
    #             num_str += num[j]+' '
    #             i += 1
    #         else:
    #             break
    # print('%s\n%s' % (C[0], num_str))


    #22222
    for k in range(10):
        M_cnt = M_num.count(k)
        num_str += (num[k]+' ') * M_cnt

    print('%s\n%s' % (C[0], num_str))


    #11111
    # for i in range(len(M_num)):
    #     for j in range(i+1, len(M_num)):
    #         if M_num[i] > M_num[j]:
    #             M_num[i], M_num[j] = M_num[j], M_num[i]
    #
    # j = 0
    # while j < len(M):
    #     for k in num:
    #         if M_num[j] == num.index(k):
    #             num_str += k+' '
    #     j += 1
    #
    # print('%s\n%s' % (C[0], num_str))
