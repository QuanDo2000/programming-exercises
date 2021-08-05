# board = ["",
#          " ............",
#          " ............",
#          " ..*......*..",
#          " ............",
#          " ............",
#          " .....##.....",
#          " .....##.....",
#          " ............",
#          " .##......##.",
#          " .#*......*#.",
#          " ............",
#          " ............"]

ans = 'DL' * 24
temp = 'U' * 5 + 'L' * 2 + 'D' * 5 + 'L' + 'D' * 5
ans += temp * 4
ans += 'RRRRRRRRDDUUURDDDDUUUUULLDDDDRRUUUU'
# UURRRRRRRRRRRRRLLDRURRRRRRRRRRRLLDDLLRURUUUU
print(len(ans))
print(ans)
