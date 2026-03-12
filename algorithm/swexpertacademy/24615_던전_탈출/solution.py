import sys

CMD_INIT = 0
CMD_ADD_GATE = 1
CMD_REMOVE_GATE = 2
CMD_GET_MIN_TIME = 3
MAX_N = 350

with open('input.txt', 'r') as f:
    data = f.read().split()
ptr = 0

def next_int():
    global ptr
    val = int(data[ptr]); ptr += 1
    return val


# ──────────────────────────────────────
# UserSolution
# ──────────────────────────────────────
from collections import deque, defaultdict
import heapq

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
INF = float('inf')

graph = defaultdict(list)
gates = defaultdict(tuple)
gate_max_num = 0

def init(N, mMaxStamina, mMap):
    global g_n, g_max_stamina, g_map, graph, gates, gate_max_num
    g_n, g_max_stamina, g_map = N, mMaxStamina, mMap
    graph = defaultdict(list)
    gates = defaultdict(tuple)
    gate_max_num = 0

def addGate(mGateID, mRow, mCol):
    global gate_max_num
    def bfs(source_x, source_y):
        global gates

        def in_range(x, y):
            return 0 <= x < g_n and 0 <= y < g_n
        def can_move(x, y, dist):
            return in_range(x, y) and g_map[x][y] == 0 and dist[x][y] == -1
        dist = [[-1] * g_n for _ in range(g_n)]
        dist[source_x][source_y] = 0
        q = deque([(source_x, source_y)])
        while q:
            x, y = q.popleft()
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if can_move(nx, ny, dist):
                    dist[nx][ny] = dist[x][y] + 1
                    if dist[nx][ny] < g_max_stamina:  # stamina 한도 내에서만 더 탐색
                        q.append((nx, ny))

        return [(tid, dist[x][y]) for tid, (x, y) in gates.items()]

    # 기존에 있는 게이트들과 새로 추가되는 게이트 간의 모든 거리들을 계산하여 그래프 집합에 저장함.
    # 단, mMaxStamina 보다 크다면 간선 정보를 저장하지 않는다.
    source_gate_id, source_x, source_y = mGateID, mRow, mCol
    for target_gate_id, weight in bfs(source_x, source_y):
        if weight == -1 or weight > g_max_stamina:
            continue
        graph[source_gate_id].append((target_gate_id, weight))
        graph[target_gate_id].append((source_gate_id, weight))

    # 이제 게이트 정보를 추가함
    gates[source_gate_id] = (source_x, source_y)
    gate_max_num += 1


def removeGate(mGateID):
    del gates[mGateID]
    graph.pop(mGateID, None)  # 키가 없어도 에러 안 남
    for gate_id in graph:
        graph[gate_id] = [(target_gate_id, weight) for target_gate_id, weight in graph[gate_id] if target_gate_id != mGateID]


def getMinTime(mStartGateID, mEndGateID):
    global gate_max_num

    def dijkstra(source_gate_id, target_gate_id):
        hq = [(0, source_gate_id)]
        dist = [INF] * (gate_max_num + 1)
        dist[source_gate_id] = 0
        while hq:
            curr_dist, curr = heapq.heappop(hq)
            if curr_dist > dist[curr]:
                continue
            for nxt, weight in graph[curr]:
                nxt_dist = curr_dist + weight
                if nxt_dist < dist[nxt]:
                    dist[nxt] = nxt_dist
                    heapq.heappush(hq, (nxt_dist, nxt))
        return dist[target_gate_id]
    result = dijkstra(mStartGateID, mEndGateID)

    return result if result != INF else -1

# ──────────────────────────────────────
# Driver
# ──────────────────────────────────────
def run():
    Q = next_int()
    okay = False

    for _ in range(Q):
        cmd = next_int()

        if cmd == CMD_INIT:
            N = next_int()
            maxStamina = next_int()
            mMap = [[0] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    mMap[i][j] = next_int()
            init(N, maxStamina, mMap)
            okay = True

        elif cmd == CMD_ADD_GATE:
            gateID = next_int()
            r = next_int()
            c = next_int()
            addGate(gateID, r, c)

        elif cmd == CMD_REMOVE_GATE:
            gateID = next_int()
            removeGate(gateID)

        elif cmd == CMD_GET_MIN_TIME:
            gateID1 = next_int()
            gateID2 = next_int()
            ret = getMinTime(gateID1, gateID2)
            ans = next_int()
            if ret != ans:
                okay = False

        else:
            okay = False

    return okay


def main():
    TC = next_int()
    MARK = next_int()

    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print(f"#{testcase} {score}")


if __name__ == "__main__":
    main()