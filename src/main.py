import curses
import time
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.rocket.rocket_animation import  animate_spaceship2
from src.rocket.utils import get_rocket_frames
from src.stars.stars import blink_animation
# from src.rocket.shooting import fire

            

def game(canvas):
    canvas.border()
    curses.curs_set(False)
    canvas.nodelay(True)
    curses.start_color()
    curses.use_default_colors() 
       
    
    height, weidth = canvas.getmaxyx()
    r1, r2 = get_rocket_frames()
    
    animation_stars = blink_animation(canvas=canvas, height=height, weidth=weidth)
    animate_rocket2 = animate_spaceship2(canvas=canvas, height=height, weidth=weidth, rocket_1=r1, rocket_2=r2)
    
    # canvas.addstr(str(canvas.getmaxyx()))

    while True:

        # Мерцание звёзд
        for star in animation_stars.copy():
            try:
                star.send(None)
                canvas.refresh()
            except StopIteration:
                animation_stars.remove(star)
        
        # Анимация корабля
        animate_rocket2.send(None)  
        
        time.sleep(0.1)
        
    
curses.update_lines_cols()
curses.wrapper(game)


