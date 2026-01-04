# RGB Color Space Visualizer

An interactive web application that visualizes the RGB color distribution of any image in 3D space. Upload an image or search for one online, and see each pixel plotted as a point in a 3D color cube.

![RGB Visualizer Demo](https://img.shields.io/badge/Status-Live-success)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green)

## Features

- 📸 **Image Upload**: Upload JPEG/PNG images from your local machine
- 🔍 **Image Search**: Search for images online using DuckDuckGo integration
- 🎨 **3D Visualization**: Interactive 3D scatter plot showing RGB color distribution
- 🔄 **Auto-Resize**: Automatic image resizing for optimal performance
- 🎯 **Interactive Controls**: Rotate, zoom, and pan the 3D visualization
- 🚀 **Fast Processing**: Client-side pixel extraction for quick results

## Demo

The visualizer maps each pixel to a 3D point where:
- **X-axis** = Red intensity (0-1)
- **Y-axis** = Green intensity (0-1)
- **Z-axis** = Blue intensity (0-1)

Each point is colored to match its original pixel color, creating a beautiful 3D representation of the image's color palette.

## Tech Stack

### Frontend
- HTML5 + Vanilla JavaScript
- [Plotly.js](https://plotly.com/javascript/) for 3D visualization
- Canvas API for pixel extraction

### Backend
- Python 3.9+
- [FastAPI](https://fastapi.tiangolo.com/) for API endpoints
- [Pillow](https://python-pillow.org/) for image processing
- [ddgs](https://github.com/deedy5/duckduckgo_search) for image search
- [httpx](https://www.python-httpx.org/) for async HTTP requests

## Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/rgb-color-visualizer.git
   cd rgb-color-visualizer
   ```

2. **Navigate to the project directory**
   ```bash
   cd rgb-visualizer
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python3 main.py
   ```

5. **Open in browser**
   ```
   http://localhost:8080
   ```

## Usage

### Upload Local Image
1. Click "Choose File" in the "Local Image" section
2. Select a JPEG or PNG image
3. Click "Upload & Visualize"
4. Interact with the 3D plot using your mouse

### Search for Images
1. Enter a search term in the "Image Search" box (e.g., "galaxy", "sunset")
2. Click "Search"
3. Click on any thumbnail to visualize it
4. The image will be automatically resized for optimal performance

### Interactive Controls
- **Rotate**: Click and drag on the plot
- **Zoom**: Use mouse scroll wheel
- **Pan**: Shift + drag

## Project Structure

```
rgb-visualizer/
├── main.py              # FastAPI backend server
├── static/
│   └── index.html       # Frontend application
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## How It Works

1. **Image Loading**: Images are loaded via file upload or fetched from search results
2. **Preprocessing**: Images larger than 160,000 pixels are automatically resized
3. **Pixel Extraction**: Canvas API extracts RGB values from each pixel
4. **Normalization**: RGB values (0-255) are normalized to coordinates (0-1)
5. **Visualization**: Plotly.js renders an interactive 3D scatter plot
6. **Interaction**: Users can explore the color space in real-time

## Performance

- Handles images up to 160,000 pixels efficiently
- Client-side processing for instant feedback
- Server-side image resizing for search results
- Maintains 30+ fps during 3D interactions

## Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## API Endpoints

### `GET /`
Serves the main application

### `POST /search`
Search for images
- **Body**: `{ "query": "search term", "max_results": 10 }`
- **Returns**: List of image URLs and metadata

### `GET /proxy-image?url={image_url}`
Fetches and resizes external images
- **Query**: `url` - Image URL to fetch
- **Returns**: Resized JPEG image (max 400x400)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- 3D visualization powered by [Plotly.js](https://plotly.com/javascript/)
- Image search via [DuckDuckGo Search](https://github.com/deedy5/duckduckgo_search)

## Author

**Your Name**
- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- Portfolio: [your-website.com](https://your-website.com)

---

⭐ If you found this project interesting, please consider giving it a star!
