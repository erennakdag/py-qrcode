import qrcode
from fastapi import FastAPI
from fastapi.responses import FileResponse
from typing import Optional

app = FastAPI()

@app.get('/', response_class=FileResponse)
async def bruh(link: Optional[str] = None):
    if link:
        img = qrcode.make(link)
        img.save('code.png')
        return 'code.png'
    return 'index.html'
