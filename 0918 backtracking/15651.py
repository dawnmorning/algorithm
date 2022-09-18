n, m = map(int, input().split())
st = []
def dfs(a):
    if a == m:
        print(*st)
        return
    for i in range(n):
        st.append(i+1)
        dfs(a+1)
        st.pop()
dfs(0)