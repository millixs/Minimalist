# Music Player

This is a minimalist terminal-based music player written in Python using the `pygame` library. It allows you to browse `.mp3` files from a local `songs` folder, play a selected track, and control playback with simple keyboard commands.

![music_player](screenshots/music_player.png)

## Files

- `main.py`: The main Python script that runs the music player, loads songs, and handles playback controls.
- `songs/`: Folder containing your `.mp3` music files.

## How to Use

1. **Install the required dependency:**

```bash
pip install pygame
```

2. **Place your music files:**

Add your `.mp3` files into the `songs` folder.

3. **Run the player:**

```bash
python main.py
```

You will see a list of available songs from the `songs` folder. Enter the number of the song you want to play.

4. **Playback Controls**

While a song is playing, use the following commands:

- `P` - Pause the current song
- `R` - Resume playback
- `S` - Stop the current song and return to the menu
- `Q` - Quit the player from the main menu

## How It Works

The program uses `pygame.mixer` to handle audio playback. Here is how the main flow works:

- The script initializes the audio mixer when the app starts.
- It reads the `songs` directory and lists all `.mp3` files.
- When you choose a song, it loads and plays the file.
- During playback, you can pause, resume, or stop the song using simple commands.

## Notes

- This project is designed to be simple and lightweight for learning and personal use.
- Only `.mp3` files in the `songs` folder are recognized by the player.
- Playback depends on your system audio setup and the availability of `pygame`.
