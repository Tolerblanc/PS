from collections import defaultdict


def get_record_table(friends, gifts, indexTable):
    table = [[0] * len(friends) for _ in range(len(friends))]
    # table[i][j] : i가 j에게 준 선물 개수

    for gift in gifts:
        giver, receiver = gift.split()
        table[indexTable[giver]][indexTable[receiver]] += 1

    return table


def calculate_gift_index(friends, recordTable, indexTable):
    index = defaultdict()
    for i, friend in enumerate(friends):
        index[friend] = i

    giftIndex = [0] * len(friends)
    transposedRecordTable = list(zip(*recordTable))  # 전치 행렬 만들기 (받은 선물 체크)
    for friend in friends:
        i = index[friend]
        giftIndex[i] = sum(recordTable[i]) - sum(transposedRecordTable[i])

    return giftIndex


def solution(friends, gifts):
    indexTable = defaultdict()
    for i, friend in enumerate(friends):
        indexTable[friend] = i

    recordTable = get_record_table(friends, gifts, indexTable)
    giftIndex = calculate_gift_index(friends, recordTable, indexTable)

    maxRecv = 0
    for i, recevier in enumerate(friends):
        localRecv = 0
        for j, giver in enumerate(friends):
            if i == j:
                continue
            if recordTable[i][j] > recordTable[j][i]:
                localRecv += 1
            elif recordTable[i][j] == recordTable[j][i]:  # 기록이 없거나 같다면
                if giftIndex[i] > giftIndex[j]:
                    localRecv += 1
        maxRecv = max(maxRecv, localRecv)
    return maxRecv
