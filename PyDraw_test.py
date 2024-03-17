from pydraw import *
screen = Screen(1050, 750, 'Python Projectile Motion Simulator')

fps = 30
running = True
while running:
    screen.update()
    screen.sleep(1 / fps)

screen.exit()
