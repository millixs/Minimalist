# `matrix classic`

A minimalist matrix rain animation built with HTML5 Canvas, CSS, and vanilla JavaScript. This project creates a full screen animated effect inspired by the Matrix movie, with falling characters rendered on two canvas layers.

![matrix_classic](/screenshots/matrix_classic.png)

## Files

- `index.html`: The page structure and canvas elements used for the animation.
- `style.css`: Styles to make the animation fill the screen and apply blur effects.
- `script.js`: Animation logic that draws falling characters, animates two canvas layers, and handles window resizing.

## Prerequisites

- A modern web browser with JavaScript enabled.
- No build tools or server are required for basic usage.
- Optionally, use a local web server for the best development experience.

## How to Use

1. Open `index.html` in your browser.

2. Or run a local server from the project folder, for example using Python:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

3. The animation will start automatically and fill the browser window.

## How It Works

`script.js` creates two fullscreen canvas elements and draws random characters in a falling rain effect.

- `Symbol`: Represents a single falling character, with a position, font size, and random text selection.
- `Effect`: Manages a column of symbols for each horizontal position and resets them when they reach the bottom.
- `animate()`: Uses `requestAnimationFrame` to render frames at a target frame rate.
- `window.resize` event: Updates the canvas dimensions and regenerates the symbol grid when the browser window changes size.

### Rendering Behavior

- `canvas1` draws the primary green matrix rain effect.
- `canvas2` draws a white overlay layer with a blur filter for a glowing highlight.
- The animation clears and redraws the canvases every frame to create smooth motion.

## Notes

- The effect is intentionally simple and lightweight.
- You can customize the character set, font size, color, or speed by editing `script.js`.
- The current design uses a transparent fade effect on `canvas1` rather than clearing the full frame, creating trailing drops.

