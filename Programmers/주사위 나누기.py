from itertools import combinations
from bisect import bisect_left, bisect_right


def roll_dice(dice, idx):
    dice_comb = [1]
    for i in idx:
        temp = []
        for curr_dice in dice_comb:
            for next_dice in dice[i - 1]:
                temp.append(curr_dice + next_dice)
        dice_comb = temp[:]
        dice_comb.sort()
    return dice_comb


def get_game_result(a_comb, b_comb):
    total_win = 0
    total_lose = 0
    for b in b_comb:
        total_win += len(a_comb) - bisect_right(a_comb, b)
        total_lose += bisect_left(a_comb, b)
    return total_win, total_lose


def solution(dice):
    dice_idx = [i for i in range(1, len(dice) + 1)]
    idx_comb = list(combinations(dice_idx, len(dice) // 2))
    game = dict()
    for a_pick, b_pick in zip(idx_comb[:len(idx_comb)//2], reversed(idx_comb[len(idx_comb)//2:])):
        a_comb = roll_dice(dice, a_pick)
        b_comb = roll_dice(dice, b_pick)
        a_win, a_lose = get_game_result(a_comb, b_comb)
        game[a_pick] = a_win
        game[b_pick] = a_lose

    max_wins = 0
    max_win_comb = None
    for k, v in game.items():
        if v > max_wins:
            max_win_comb = k
            max_wins = v

    return list(max_win_comb)
