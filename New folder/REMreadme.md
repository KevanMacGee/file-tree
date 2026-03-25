# gtree.py

A lightweight, Python-based terminal utility that generates a visual directory tree structure while intelligently respecting your project's `.gitignore` rules.

## Features

- **Git-Aware:** Automatically detects and parses your `.gitignore` file.
- **Auto-Copy:** Automatically copies the generated tree to your clipboard for easy pasting into docs or LLM prompts.
- **Clean Output:** Uses standard ASCII characters to draw the tree structure.
- **Customizable:** Options to reveal hidden git metadata or bypass ignore rules.

## Prerequisites

You will need the `pathspec` and `pyperclip` libraries installed:

PowerShell

```
pip install pathspec pyperclip
```

## Usage

Run the script using Python. By default, it processes the current directory:

You can just copy the .py file to the directory you want, open your terminal and run

PowerShell

```
python gtree.py
```

```
# View the current directory (and copy to clipboard)
python "C:\Users\User\Development\file-tree\gtree.py"

# View a specific directory
python "C:\Users\User\Development\file-tree\gtree.py" C:\Path\To\Project
```

### Command Line Flags

| **Flag**           | **Description**                                               |
| ------------------ | ------------------------------------------------------------- |
| `-a`, `--all`      | Includes the `.git` folder in the output (hidden by default). |
| `--no-ignore`      | Shows every file and folder, bypassing `.gitignore` logic.    |
| `-nc`, `--no-copy` | Run the command without copying the output to the clipboard.  |
| `-h`, `--help`     | Shows the help menu with all available options.               |

## Setting Up Global Access (Recommended)

To run `gtree` from any folder without typing the full path, add it to your PowerShell Profile:

1. Open your profile in Notepad: `notepad $PROFILE`

2. Add the following function to the file:
   
   PowerShell
   
   ```
   function gtree {
       python "C:\Users\User\Development\file-tree\gtree.py" $args
   }
   ```

3. Save, close, and restart PowerShell.

4. You can now simply type `gtree`, `gtree -a`, or `gtree --no-ignore` anywhere.