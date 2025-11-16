import asyncio

from src.curses_tools import draw_frame, read_controls, get_frame_size

async def animate_spaceship2(canvas, height, weidth, rocket_1, rocket_2):
    
    row = height // 4
    column = weidth // 2.5
    size_rocket = list(get_frame_size(rocket_1))
    
    while True:
        
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

    
        draw_frame(canvas, row + x, column + y, rocket_1)
        # draw_frame(canvas, 3, 20, "current_position" + str(current_position))
        # draw_frame(canvas, 1, 20, str(["x", x, "y", y]))
        # draw_frame(canvas, 1, 40, str(["row", row, "column", column]))
        canvas.refresh()
        for _ in range(2):
            await asyncio.sleep(0)
        
        draw_frame(canvas, row + x, column + y, rocket_1, negative=True)
        await asyncio.sleep(0)
        
        
        draw_frame(canvas, row + x, column + y, rocket_2)
        canvas.refresh()
        for _ in range(1):
            await asyncio.sleep(0)
        
        draw_frame(canvas, row + x, column + y, rocket_2, negative=True)
        await asyncio.sleep(0)
        # draw_frame(canvas, 3, 20, "current_position" + str(current_position), negative=True)
        # draw_frame(canvas, 1, 20, str(["x", x, "y", y]), negative=True)
        # draw_frame(canvas, 1, 40, str(["row", row, "column", column]), negative=True)
        row += x
        column += y
    
       