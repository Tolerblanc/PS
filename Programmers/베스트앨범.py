from collections import defaultdict


def solution(genres, plays):
    answer = []
    genre_preference = defaultdict(int)
    genre_plays = defaultdict(list)

    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_plays[genre].append((play, i))
        genre_preference[genre] += play
    genre_preference = sorted(genre_preference.items(), key=lambda x: -x[1])

    for genre, _ in genre_preference:
        genre_plays[genre].sort(key=lambda x: (-x[0], x[1]))
        answer.append(genre_plays[genre][0][1])
        if len(genre_plays[genre]) > 1:
            answer.append(genre_plays[genre][1][1])

    return answer
