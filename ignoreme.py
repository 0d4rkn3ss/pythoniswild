import curses
import random
import time

def random_color_pair():
    return random.randint(1, 7)

def setup_colors():
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)

def spam_ignore_me(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.clear()
    setup_colors()
    positions = []
    max_texts = 150

    while True:
        height, width = stdscr.getmaxyx()
        text = "ignore me"
        x = random.randint(0, max(0, width - len(text) - 1))
        y = random.randint(0, max(0, height - 1))
        color_pair = random_color_pair()

        try:
            stdscr.addstr(y, x, text, curses.color_pair(color_pair))
            positions.append((y, x))
        except curses.error:
            pass

        stdscr.refresh()

        if len(positions) > max_texts:
            oldest_y, oldest_x = positions.pop(0)
            try:
                stdscr.addstr(oldest_y, oldest_x, " " * len(text))
            except curses.error:
                pass

        time.sleep(0.1)

        if stdscr.getch() != -1:
            break

curses.wrapper(spam_ignore_me)