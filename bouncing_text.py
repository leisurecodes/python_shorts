# Bouncing Text
import curses
import time

def get_user_input(stdscr):
    stdscr.clear()
    curses.echo()
    stdscr.addstr(0, 0, 
        "Enter text to bounce: ")
    user_text = stdscr.getstr(1, 0)
    user_text = user_text.decode("utf-8")
    curses.noecho()
    return user_text

def bounce_text(stdscr, user_text):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    # Initialize colors
    curses.start_color()
    curses.init_pair(
        1, curses.COLOR_GREEN, curses.COLOR_BLACK
    )
    color_pair = curses.color_pair(1)

    # height, width
    ht, wd = stdscr.getmaxyx()
    x = 0
    y = 0
    dx = 1
    dy = 1

    while True:
        stdscr.clear()
        stdscr.addstr(y, x, user_text, color_pair)
        stdscr.refresh()

        x += dx
        y += dy

        if x + len(user_text)>=wd or x<=0:
            dx *= -1
        if y >= ht - 1 or y <= 0:
            dy *= -1
        
        key = stdscr.getch()
        if key == ord('q'):
            break

        time.sleep(0.05)

def main(stdscr):
    user_text = get_user_input(stdscr)
    bounce_text(stdscr, user_text)

curses.wrapper(main)