import sys
def input():return sys.stdin.readline().rstrip() # fastInput
sys.setrecursionlimit(int(1e6)) # set recursion depth

# init graph and reversed graph
def init(graph : list, r_graph : list) -> None:
    i, j = map(int, input().split())
    graph[-i].append(j)
    graph[-j].append(i)
    r_graph[j].append(-i)
    r_graph[i].append(-j)

def dfs(cur, graph : list, visited : list, L : list) -> None:
    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = 1
            dfs(nxt, graph, visited, L)
    L.append(cur)

# strongly connected component (Kosaraju)
def get_scc(N, graph : list, r_graph : list) -> list:
    visited = [0] * (N * 2 + 1)
    stack = []
    for i in range(-N, N + 1):
        if i == 0:
            continue
        if not visited[i]:
            visited[i] = 1
            dfs(i, graph, visited, stack)

    visited = [0] * (N * 2 + 1)
    scc = []
    while stack:
        cur = stack.pop()
        if not visited[cur]:
            visited[cur] = 1
            tmp = []
            dfs(cur, r_graph, visited, tmp)
            scc.append(tmp)
    return scc

# check satisfiable
def is_2CNF(scc_list : list) -> bool:
    for scc in scc_list:
        for c in scc:
            if -c in scc:
                return False
    return True

# get satisfiable bool values
def B_SAT(N, scc_list : list) -> list:
    res = [-1] * (N + 1)
    for scc in scc_list[::-1]:
        for c in scc:
            if res[abs(c)] == -1:
                res[abs(c)] = [0,1][c > 0]
    return res[1:]

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N * 2 + 1)]
    r_graph = [[] for _ in range(N * 2 + 1)]
    for _ in range(M):
        init(graph, r_graph)

    scc_list = get_scc(N, graph, r_graph)
    flag = is_2CNF(scc_list)
    if flag:
        print(*B_SAT(N, scc_list))
    else:
        print(flag)

if __name__ == '__main__':
    main()
