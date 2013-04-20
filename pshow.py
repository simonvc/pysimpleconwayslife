from pyglet import font
from pyglet import window

from conway import World, add_pattern

win = window.Window()
w=World(size_x=60, size_y=45)
w.randomize()

glider="1,1 2,1 3,1 2,3 3,2"
blinker="1,1 1,2 1,3"
add_pattern(w, glider, (5,35))


ft = font.load('Arial', 20)

#run until the user hits exit
while not win.has_exit:
  win.dispatch_events()
  win.clear()
  w.update()
  rows=0
  cols=0
  # for each position in the world:
  for pos in w.scope():
    cell=w.get(pos)
    # if the cell is alive?
    if cell:
      # put an * on the screen, spaced 10 from the left, with 10 pixels between them.
      text=font.Text(ft, [" ", "*"][cell], x=10+pos[0]*10, y=pos[1]*10)
      text.draw()


  win.flip()
