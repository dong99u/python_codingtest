from collections import defaultdict

def solution(genres, plays):
    play_counts = defaultdict(int)
    songs = defaultdict(dict)
    answer = []

    for i, (genre, play) in enumerate(zip(genres, plays)):
        play_counts[genre] += play
        songs[genre][i] = play

    orders_of_genre = sorted(play_counts.keys(), key=lambda x: -play_counts[x])

    for order in orders_of_genre:
        answer += sorted(songs[order].keys(), key=lambda x: -songs[order][x])[:2]

    return answer


if __name__ == '__main__':
    print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))