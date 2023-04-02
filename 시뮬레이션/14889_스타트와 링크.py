import sys
input = sys.stdin.readline

# depth: 현재까지 뽑은 팀원의 수
# s: 뽑을 수 있는 선수 중 가장 작은 번호
# e: 뽑을 수 있는 선수 중 가장 큰 번호
def solution(depth, s, e):
    global team, res
    
    # 한 팀에 들어갈 선수를 다 뽑은 경우
    if depth == e//2:
        start = 0
        link = 0
        # 각 팀의 능력치 합을 계산
        for i in range(e):
            for j in range(e):
                if i in team and j in team:  # 스타트 팀일 경우
                    start += li[i][j]
                elif i not in team and j not in team:  # 링크 팀일 경우
                    link += li[i][j]
        # 스타트 팀과 링크 팀의 능력치 차이의 절댓값을 저장
        res.append(abs(start-link))
    
    # 한 팀에 들어갈 선수를 더 뽑을 경우
    else:
        for i in range(s,e):
            if i not in team:
                team.append(i)
                solution(depth+1,i,e)
                team.remove(i)

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

# 스타트 팀을 구성하는 데 사용할 리스트
team = []
# 스타트 팀과 링크 팀의 능력치 차이를 저장할 리스트
res = []
# 모든 선수 중에 두 팀으로 나누어 진행하므로, 처음에는 모든 선수가 뽑을 수 있는 대상
solution(0,0,n)
# 스타트 팀과 링크 팀의 능력치 차이 중 최솟값을 출력
print(min(res))