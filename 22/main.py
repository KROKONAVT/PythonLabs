maze = [
    "####B######################",
    "# #       #   #      #    #",
    "# # # ###### #### ####### #",
    "# # # #       #   #       #",
    "#   # # ######### # ##### #",
    "# # # #   #       #     # #",
    "### ### ### ############# #",
    "# #   #     # #           #",
    "# # #   ####### ###########",
    "# # # #       # #         C",
    "# # ##### ### # # ####### #",
    "# # #     ### # #       # #",
    "#   ##### ### # ######### #",
    "######### ### #           #",
    "# ####### ### #############",
    "A           #   ###   #   #",
    "# ############# ### # # # #",
    "# ###       # # ### # # # #",
    "# ######### # # ### # # # F",
    "#       ### # #     # # # #",
    "# ######### # ##### # # # #",
    "# #######   #       #   # #",
    "# ####### ######### #######",
    "#         #########       #",
    "#######E############D######"
]

result = []
visited = []

def step(weight: int, height: int) -> int:
    if (weight, height) in visited:
        return
    if weight < 0 or weight >= len(maze[0]) or height < 0 or height >= len(maze) or maze[height][weight] == '#':
        return
    visited.append((weight, height))
    if maze[height][weight] != '#' and maze[height][weight] != ' ':
        result.append(maze[height][weight])
    step(weight - 1, height)
    step(weight, height - 1)
    step(weight + 1, height)
    step(weight, height + 1)
  
print('Введите координаты x и y через пробел') 
weight, height = map(int, input().split())
if weight < 0 or weight >= len(maze[0]) or height < 0 or height >= len(maze) or maze[height][weight] == '#':
    print('Не верные координаты')
    exit()
    
step(weight, height)

for i in range(0, len(result)):
    print(result[i], end = ' ')