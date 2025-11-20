import random
import asyncio
import curses

async def blink(canvas, row=1, column=20, symbol='*', offset_ticks=40):
    
    for _ in range(random.randint(1, offset_ticks)):
            await asyncio.sleep(0)
    
    while True:
        
        canvas.addstr(row, column, symbol, curses.A_DIM)
        for _ in range(20):
            await asyncio.sleep(0)
        
        canvas.addstr(row, column, symbol)
        for _ in range(3):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        for _ in range(5):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(3):
            await asyncio.sleep(0)
 
            
            
            
