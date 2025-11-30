import sys, math
def input():return sys.stdin.readline().rstrip() # fastInput

# 두 점 사이의 거리 제곱
def dist(x1, y1, x2, y2) -> int:
    return (x1 - x2) ** 2 + (y1 - y2) **2

# 세 점에 대해 ccw
def ccw(x1, y1, x2, y2, x3, y3) -> int:
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

# 방향벡터 생성
def vector(p1 : tuple, p2 : tuple) -> tuple:
    return (p2[0] - p1[0], p2[1] - p1[1])

# 두 방향벡터에 대해 ccw
def v_ccw(v1 : tuple, v2 : tuple) -> int:
    return v1[0] * v2[1] - v1[1] * v2[0]

# 좌표 각도정렬
def angle_sort(pos : list) -> list:
    x0, y0 = min(pos, key=lambda x : (x[1], x[0]))
    angle_pos = [(0, 0, x0, y0)]
    for x, y in pos:
        if (x, y) == (x0, y0):
            continue
        d = dist(x, y, x0, y0)
        angle_pos.append((math.atan2(y - y0, x - x0), d, x, y))
    angle_pos.sort()
    return angle_pos

# 볼록 껍질
def convex_hull(angle_pos : list) -> list:
    hull = []
    for _, _, x, y in angle_pos:
        while len(hull) > 1 and \
        ccw(hull[-2][0], hull[-2][1], hull[-1][0], hull[-1][1], x, y) <= 0:
            hull.pop()
        hull.append((x, y))
    return hull

# 두 점 사이의 거리 최댓값
def max_distance_with_rotating_calipers(hull : list) -> int:
    ans = 0
    L = len(hull)
    lo = 0
    for hi in range(1, L):
        v1 = vector(hull[lo + 1], hull[lo])
        v2 = vector(hull[(hi + 1) % L], hull[hi])
        while v_ccw(v1, v2) < 0:
            d = dist(hull[lo][0], hull[lo][1], hull[hi][0], hull[hi][1])
            ans = max(ans, d)
            lo += 1
            v1 = vector(hull[lo + 1], hull[lo])
        d = dist(hull[lo][0], hull[lo][1], hull[hi][0], hull[hi][1])
        ans = max(ans, d)
    return ans

def main():
    n = int(input())    # 2차원상의 좌표 개수
    pos = [tuple(map(int, input().split())) for _ in range(n)]  # 좌표
    angle_pos = angle_sort(pos)
    hull = convex_hull(angle_pos)
    print(max_distance_with_rotating_calipers(hull))

if __name__ == '__main__':
    main()
