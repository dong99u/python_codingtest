from collections import defaultdict

def solution(today, terms, privacies):
    def plus_month(date, months):
        year, month, day = map(int, date.split('.'))

        # 개월 더하기
        month += months
        year += (month - 1) // 12  # 12개월 넘으면 년도 증가
        month = (month - 1) % 12 + 1  # 1~12 범위로 조정

        # 하루 빼기
        day -= 1
        if day == 0:  # 1일에서 하루 빼면 이전 달 28일
            month -= 1
            if month == 0:  # 1월에서 이전 달로 가면 작년 12월
                month = 12
                year -= 1
            day = 28

        return f"{year}.{month:02d}.{day:02d}"
    def is_over(date1, date2):
        year1, month1, day1 = date1.split('.')
        year2, month2, day2 = date2.split('.')

        if year1 < year2:
            return True
        elif year1 == year2:
            if month1 < month2:
                return True
            elif month1 == month2:
                if day1 < day2:
                    return True

        return False


    d = defaultdict(int)

    for term in terms:
        a, b = term.split()
        b = int(b)

        d[a] = b

    answer = []
    for idx, privacy in enumerate(privacies):
        date, term = privacy.split()

        months = d[term]

        date = plus_month(date, months)

        if is_over(date, today):
            answer.append(idx + 1)

    return answer

if __name__ == '__main__':
    print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))