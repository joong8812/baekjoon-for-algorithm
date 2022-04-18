import sys
input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
paper_list = []

def inspect_color_paper(x, y, n):
    curr_color = paper[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != curr_color:
                inspect_color_paper(x, y, n//2)
                inspect_color_paper(x+(n//2), y, n//2)
                inspect_color_paper(x, y+(n//2), n//2)
                inspect_color_paper(x+(n//2), y+(n//2), n//2)
                return 
    paper_list.append(curr_color)

inspect_color_paper(0, 0, n)
print(paper_list.count(0))
print(paper_list.count(1))
