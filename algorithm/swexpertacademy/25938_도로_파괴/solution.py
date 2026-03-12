from collections import defaultdict
import heapq

INF = float('inf')

graph = defaultdict(list)
edges = defaultdict(list)
n = 0

def init(N, K, mId, sCity, eCity, mTime):
	global graph, edges, n

	graph = defaultdict(list)
	edges = defaultdict(tuple)
	n = N
	for mid, s, e, t in zip(mId, sCity, eCity, mTime):
		graph[s].append((e, t, mid))
		edges[mid] = [s, e, t, True]


def add(mId, sCity, eCity, mTime):
	global graph, edges

	graph[sCity].append((eCity, mTime, mId))
	edges[mId] = [sCity, eCity, mTime, True]


def remove(mId):
	global edges

	edges[mId][3] = False


def calculate(sCity, eCity):
	def dijkstra(source, target):
		hq = [(0, source)]
		dist = [INF] * n
		dist[source] = 0
		path = [None] * n
		while hq:
			curr_dist, curr = heapq.heappop(hq)
			if curr_dist > dist[curr]:
				continue
			for nxt, weight, nxt_mid in graph[curr]:
				if not edges[nxt_mid][3]: # 비활성화 된 간선이면 패스
					continue
				nxt_dist = curr_dist + weight
				if nxt_dist < dist[nxt]:
					dist[nxt] = nxt_dist
					heapq.heappush(hq, (nxt_dist, nxt))
					path[nxt] = nxt_mid
		if dist[target] == INF:
			return None, None
		node = target
		edge_list = []
		while node != source:
			mid = path[node]
			edge_list.append(mid)
			node = edges[mid][0]

		return dist[target], edge_list

	original_dist, path = dijkstra(sCity, eCity)
	if original_dist is None:
		return -1
	result = original_dist
	for mid in path:
		edges[mid][3] = False
		shortest_dist, _ = dijkstra(sCity, eCity)
		if shortest_dist is None:
			edges[mid][3] = True
			return -1
		result = max(result, shortest_dist)
		edges[mid][3] = True

	return result - original_dist
