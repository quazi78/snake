import random
import curses
stdscr = curses.initscr()
curses.curs_set(0)
screenh, screenw = stdscr.getmaxyx()
window = curses.newwin(screenh, screenw, 0, 0)
window.keypad(1)
window.timeout(int(1000 / 30))

snake_x = int(screenw/4)
snake_y = int(screenh/2)

snake = [
        [snake_y, snake_x],
        [snake_y, snake_x-1],
        [snake_y, snake_x-2]
]

food = [int(screenh/2), int(screenw/2)]
window.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, int(screenh)] or snake[0][1] in [0, int(screenw)] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, screenh-1),
                random.randint(1, screenw-1)
            ]
            food = nf if nf not in snake else None
        window.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
