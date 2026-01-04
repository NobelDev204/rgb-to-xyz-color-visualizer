from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, Response
from pydantic import BaseModel
from ddgs import DDGS
from PIL import Image
import httpx
import os
import logging
import io

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

class SearchQuery(BaseModel):
    query: str
    max_results: int = 10

@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

@app.post("/search")
async def search_images(search_query: SearchQuery):
    """
    Search for images using DuckDuckGo.
    """
    logger.info(f"Searching for: {search_query.query}")
    try:
        # Initializing DDGS() directly as suggested
        results = []
        ddgs_results = DDGS().images(
            query=search_query.query,
            max_results=search_query.max_results,
            safesearch="moderate",
            region="us-en"
        )
        
        # Standardize results
        for result in ddgs_results:
            results.append({
                "title": result.get("title", "No Title"),
                "image_url": result.get("image"),
                "thumbnail_url": result.get("thumbnail"),
                "width": result.get("width"),
                "height": result.get("height"),
                "source": result.get("source")
            })
        return {"results": results}
    except Exception as e:
        logger.error(f"Search failed: {e}")
        # Log stack trace for better debugging if it still fails
        import traceback
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/proxy-image")
async def proxy_image(url: str):
    """
    Fetch an image from a URL, resize it to 400x400 (or maintain aspect ratio under 160k pixels),
    and return it with CORS headers allowed for our frontend.
    This is necessary because Canvas cannot read pixel data from cross-origin images 
    without CORS approval (tainted canvas).
    """
    if not url:
        raise HTTPException(status_code=400, detail="Missing URL parameter")

    MAX_PIXELS = 160000
    TARGET_SIZE = 400  # Target 400x400 for simplicity

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, follow_redirects=True, timeout=10.0)
            response.raise_for_status()
            
            # Load image from bytes
            img = Image.open(io.BytesIO(response.content))
            
            # Convert to RGB if necessary (handles RGBA, P, etc.)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Calculate current pixels
            current_pixels = img.width * img.height
            
            # Resize if needed
            if current_pixels > MAX_PIXELS or img.width > TARGET_SIZE or img.height > TARGET_SIZE:
                # Use thumbnail to maintain aspect ratio
                img.thumbnail((TARGET_SIZE, TARGET_SIZE), Image.Resampling.LANCZOS)
                logger.info(f"Resized image to {img.width}x{img.height}")
            
            # Save to bytes
            output = io.BytesIO()
            img.save(output, format='JPEG', quality=85)
            output.seek(0)
            
            return Response(content=output.read(), media_type="image/jpeg")
            
    except Exception as e:
        logger.error(f"Proxy failed for {url}: {e}")
        raise HTTPException(status_code=400, detail=f"Failed to fetch image: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
