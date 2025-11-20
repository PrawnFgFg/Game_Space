import curses
import random
import time
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.rocket.rocket_animation import animate_spaceship
from src.rocket.utils import get_rocket_frames
from src.stars.stars import blink

NUMBER_FOR_COUNTING_STARS = 35    


def get_starry_sky(canvas, height, weidth):
    cosmo_items = ["*", ":", "+", "."]
    many_stars_blink = [blink(canvas=canvas, 
            row=random.randint(1, height-2), 
            column=random.randint(1,weidth-2),
            symbol=random.choice(cosmo_items),
            offset_ticks=random.randint(20, 50))
                for _ in range(1, int((height * weidth)/NUMBER_FOR_COUNTING_STARS))
        ]
    return many_stars_blink
    
    
def get_animation_rocket(canvas, height, weidth):
    r1, r2 = get_rocket_frames()
    animate_rocket = animate_spaceship(canvas=canvas, height=height, weidth=weidth)
    return animate_rocket


def start_game(canvas, height, weidth):
    coroutines = [
        *get_starry_sky(canvas, height, weidth),
        get_animation_rocket(canvas, height, weidth)
    ]
    
    while True:
        dead_coroutines = []
        try:
            for coro in coroutines.copy():
                coro.send(None)
        except StopIteration:
            dead_coroutines.append(coro)
            
        for dead_coro in dead_coroutines:
            coroutines.remove(dead_coro)
        
        time.sleep(0.1)
        
        if not coroutines:
            break
        
    

def main(canvas):
    canvas.border()
    curses.curs_set(False)
    canvas.nodelay(True)
    curses.start_color()
    curses.use_default_colors()
     
    height, weidth = canvas.getmaxyx()
    start_game(canvas, height, weidth)
       
    
if __name__ == "__main__":
    curses.update_lines_cols()
    curses.wrapper(main)
    
    
    
