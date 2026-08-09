# `matrix: rainbow`

This is a minimalist Matrix style animation built with HTML, CSS, and JavaScript using the HTML5 canvas API. It creates a falling digital rain effect with layered canvases and multicolored ASCII characters for a smooth and visually striking presentation.

![Matrix Demo](demo.gif)

## Files

- `index.html`: The main HTML file that creates the canvas elements used for the animation.
- `style.css`: Contains the styling for the full-screen background and canvas layers.
- `script.js`: Implements the Matrix effect, including symbol generation, animation timing, and responsive resizing.
- `demo.gif`: A short preview of the animation.

## How to Use

1. **Open the Project**

   You can open `index.html` directly in your browser, or serve the folder with a simple local server.

   ```bash
   python -m http.server 8000
   ```

   Then visit `http://localhost:8000/` in your browser.

2. **View the Animation**

   The Matrix effect starts automatically when the page loads. Resizing the browser window will update the animation to match the new screen size.

## How It Works

The animation uses two overlapping canvas layers to create a layered digital rain effect.

- `Symbol`: Represents an individual falling character and randomly selects from a set of characters.
- `Effect`: Creates and manages a column-based stream of symbols across the canvas.
- `requestAnimationFrame`: Drives the animation loop at a steady frame rate.
- `resize` handling: Rebuilds the symbol layout whenever the window size changes.

## Notes

- This project is intentionally lightweight and requires no build tools or dependencies.
- You can customize the look by changing the character set, colors, speed, blur effect, or animation density in `script.js` and `style.css`.
- The project is ideal for learning canvas animation, JavaScript classes, and responsive rendering.
