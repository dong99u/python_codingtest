from collections import defaultdict

def solution(genres, plays):
    genres_dict = defaultdict(list)
    counts_dict = defaultdict(int)

    for idx, (genre, play) in enumerate(zip(genres, plays)):
        genres_dict[genre].append((idx, play))
        counts_dict[genre] += play

    sorted_genres = sorted(counts_dict, key=lambda x: counts_dict[x], reverse=True)

    answer = []
    for genre in sorted_genres:
        top_2 = sorted(genres_dict[genre], key=lambda x: x[1], reverse=True)[:2]
        answer.extend([i for i, count in top_2])

    return answer




if __name__ == '__main__':
    print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))