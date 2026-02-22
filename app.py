from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from tarot_data import draw_cards, interpret_card
from tarot_data import get_card_by_id
from fastapi.responses import Response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="./static"), name="static")


@app.get("/")
async def index():
    return FileResponse("static/index.html")

@app.get("/api/draw")
async def api_draw(n: int = 3):
    """Draw `n` tarot cards."""
    cards = draw_cards(n)
    return {"cards": cards}

@app.post("/api/interpret")
async def api_interpret(payload: Request):
    """Interpret provided cards. Expects JSON {"cards": [{"id":..., "reversed": bool}, ...]}"""
    data = await payload.json()
    cards = data.get("cards", [])
    results = []
    for c in cards:
        interp = interpret_card(c)
        results.append(interp)
    return {"interpretations": results}


@app.get('/api/card_svg/{cid}')
async def card_svg(cid: int, reversed: bool = False):
        """Return a simple SVG representing the card. Use ?reversed=true to rotate."""
        entry = get_card_by_id(cid)
        if not entry:
                return JSONResponse({"error": "invalid card id"}, status_code=404)
        name = entry['name']
        # simple SVG with name text; rotate if reversed
        transform = 'rotate(180 90 110)' if reversed else ''
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="180" height="260" viewBox="0 0 180 260">
    <rect x="2" y="2" width="176" height="256" rx="10" ry="10" fill="#fff" stroke="#b98"/>
    <g transform="{transform}">
        <text x="90" y="130" font-size="16" font-family="Arial, Helvetica" text-anchor="middle" fill="#333">{name}</text>
    </g>
</svg>'''
        return Response(content=svg, media_type='image/svg+xml')

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
