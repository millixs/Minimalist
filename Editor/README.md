# Editor

This is a minimalist C-based text editor that lets you open a file, view its contents, choose a line to edit, and save the updated version back to the file. It is a simple command-line tool designed for quick in-place line editing.

![editor_demo](./editor_demo.gif)

## Files

- `editor.c`: Source code for the command-line editor that reads a file, edits a selected line, and writes the changes back.
- `a.txt`: A sample text file that can be used to test the editor.

## How to Use

1. **Compile the Program:**

```bash
gcc -o editor editor.c
```

2. **Run the Editor:**

```bash
./editor <filename>
```

Example:

```bash
./editor a.txt
```

3. **Edit a Line**

- The program will display the current file contents.
- You will be prompted to enter the line number you want to edit.
- You will then be asked to enter the new content for that line.
- The updated content will be written back to the file.

## How It Works

**Key Functions in `editor.c`:**

- `fopen()`: Opens the target file for reading and writing.
- `fread()`: Reads the file content into a buffer.
- `strchr()`: Finds newline characters to navigate through the file content.
- `scanf()`: Reads the selected line number and new content from the user.
- `strcpy()` and `strcat()`: Manipulate the file buffer while inserting the updated line.
- `fwrite()`: Writes the modified content back to the file.

**Editing Process:**

The program reads the entire file into memory, locates the requested line, replaces that line with the new content, and writes the modified text back to disk. This makes it easy to update a single line without needing a full text editor interface.

## Notes

- This is a simple demonstration program and is intended for basic text editing tasks.
- The current implementation works with a fixed-size buffer and is best suited for small text files.
- It can be expanded to support more advanced features such as multi-line editing, line insertion, or deletion.
