import asyncio, json
import websockets
from pynput import keyboard

CLIENTS=set()
LOOP=None
SPECIAL={keyboard.Key.space:"SPACE"}
ALLOWED={"A","D","W","S","R","F","E","1","2","3","4","5"}

def normalize(key):
    if key in SPECIAL: return SPECIAL[key]
    ch=getattr(key,"char",None)
    if ch:
        ch=ch.upper()
        if ch in ALLOWED: return ch
    return None

async def broadcast(payload):
    if CLIENTS:
        await asyncio.gather(*(c.send(payload) for c in list(CLIENTS)),return_exceptions=True)

def emit(name,down):
    if LOOP:
        asyncio.run_coroutine_threadsafe(
            broadcast(json.dumps({"key":name,"down":down})),LOOP)

def on_press(key):
    name=normalize(key)
    if name: emit(name,True)

def on_release(key):
    name=normalize(key)
    if name: emit(name,False)

async def handler(ws):
    CLIENTS.add(ws)
    try: await ws.wait_closed()
    finally: CLIENTS.discard(ws)

async def main():
    global LOOP
    LOOP=asyncio.get_running_loop()
    listener=keyboard.Listener(on_press=on_press,on_release=on_release)
    listener.start()
    print("Keyboard tracker active on 127.0.0.1:8765")
    print("Start the Cloudflare tunnel in a second Command Prompt.")
    print("Keep both windows open while streaming. Ctrl+C stops this helper.")
    async with websockets.serve(handler,"127.0.0.1",8765):
        await asyncio.Future()

if __name__=="__main__":
    try: asyncio.run(main())
    except KeyboardInterrupt: print("Stopped.")
