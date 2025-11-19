import asyncio
from itertools import cycle

from src.curses_tools import draw_frame, read_controls, get_frame_size
from src.rocket.utils import get_rocket_frames

DIV_FOR_CENTRAL_PLACEMENT_ROW = 4
DIV_FOR_CENTRAL_PLACEMENT_COLUMN = 2.5

async def animate_spaceship(canvas, height, weidth):
    rocket_frame_1, rocket_frame_2 = get_rocket_frames()
    
    row = height //DIV_FOR_CENTRAL_PLACEMENT_ROW
    column = weidth // DIV_FOR_CENTRAL_PLACEMENT_COLUMN
    size_rocket = list(get_frame_size(rocket_frame_1))
    
    for frame in cycle([rocket_frame_1, rocket_frame_1, rocket_frame_2, rocket_frame_2]):
        
        coord = read_controls(canvas)
        x = coord[0]
        y = coord[1]
        
        current_position = ([row + x, column + y]) 
        
        if current_position[1] <= 1:
            column = 1.1
            y = 0

        elif current_position[1] > (weidth - size_rocket[1]):
            column = weidth - size_rocket[1] - 1
            y = 0
            
        elif current_position[0] <= 1:
            row = 1 
            x = 0
            
        elif current_position[0] >= (height - size_rocket[0]):
            row = height - size_rocket[0] - 1
            x = 0
        
        draw_frame(canvas, row + x, column + y, frame)
        canvas.refresh()
        await asyncio.sleep(0)
        draw_frame(canvas, row + x, column + y, frame, negative=True)

        row += x
        column += y
