import curses
from conway import World, add_pattern

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)

x,y=stdscr.getmaxyx()
stdscr.addstr(10,10, "python simple conways game of life")
stdscr.addstr(12,10, "x: %s, y: %s" % (x,y))
stdscr.addstr(14,10, "Space to update, r to randomize, q to quit.")
#w=World(size_x=x, size_y=y)
w=World(size_x=x-1, size_y=y-1)

# wait for a keypress then go for it.
c=stdscr.getch()
stdscr.erase()

stdscr.nodelay(True)

w.randomize()
while 1:
  stdscr.refresh()
  w.update()
  c = stdscr.getch()
  if c == ord('q'): break  # Exit the while()
  elif c == ord('r'): w.randomize()
  for pos in w.scope():
    cell=w.get(pos)
    try:
      if cell:
        stdscr.addstr(pos[0], pos[1], "*")
      else:
        stdscr.addstr(pos[0], pos[1], " ")
    except:
      print(stdscr.getmaxyx())

# ending

curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()

