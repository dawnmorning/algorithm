import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split()))for _ in range(n)]
white = 0
blue = 0
# JavaScript 쓰다가  python 헷갈려요. 
def colorpaper(x,y,n):
    global white, blue
    color = paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != paper[i][j]:
                # 색종이 색깔이 맞지 않다면 4분할로 나눠서 생각하기
                colorpaper(x,y,n//2)
                colorpaper(x,y+n//2, n//2)
                colorpaper(x+n//2,y,n//2)
                colorpaper(x+n//2, y+n//2,n//2)
                return
        
    if color == 0:
        white += 1
    else:
        blue +=1


colorpaper(0,0,n)
print(white)
print(blue)