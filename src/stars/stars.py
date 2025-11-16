import random
import asyncio
import curses

async def blink(canvas, row=1, column=20, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        for _ in range(random.randint(15,30)):
            await asyncio.sleep(0)
        
        
        canvas.addstr(row, column, symbol)
        for _ in range(random.randint(3,30)):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        for _ in range(random.randint(6,30)):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(random.randint(3,30)):
            await asyncio.sleep(0)
            
def blink_animation(canvas, height, weidth):
    cosmo_items = ["*", ":", "+", "."]
    stars_animation = [blink(
        canvas=canvas, 
        row=random.randint(1, height-1),
        column=random.randint(1,weidth-1),
        symbol=random.choice(cosmo_items)
        ) for i in range(1, int((height * weidth)/35))]
    
    return stars_animation
