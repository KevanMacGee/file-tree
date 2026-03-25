# gtree.py

A lightweight, Python-based terminal utility that generates a visual directory tree while respecting `.gitignore` rules and OS-level hidden file conventions.

## Features

- **Git-Aware:** Automatically detects and parses your `.gitignore` file, hiding matched entries by default.
- **Hidden File Filtering:** Respects OS-level hidden files — `FILE_ATTRIBUTE_HIDDEN` on Windows, dotfiles on Unix.
- **Auto-Copy:** Automatically copies the generated tree to your clipboard for easy pasting into docs or LLM prompts.
- **Clean Output:** Uses standard box-drawing characters for the tree structure.
- **Empty Directory Suppression:** Directories with no visible children are omitted entirely from the output.

## Prerequisites

You will need the `pathspec` and `pyperclip` libraries installed:

```
pip install pathspec pyperclip
```

## Usage

Run the script using Python. By default, it processes the current directory:

```powershell
# View the current directory (and copy to clipboard)
C:\Users\[your user name]\Desktop
python path\to\gtree.py

# View a specific directory
python path\to\gtree.py path\to\project
```

### Command Line Flags

| **Flag**                | **Description**                                              |
| ----------------------- | ------------------------------------------------------------ |
| [No flag]               | Shows the folder contents, but respects .gitignore file and doesn't print OS-hidden files. |
| `-ng`, `--no-gitignore` | Bypass `.gitignore` rules. Hidden files are not printed.     |
| `-a`, `--all`           | Show everything: OS-hidden files and `.gitignore`-excluded entries. |
| **Special Flags**       |                                                              |
| `-nc`, `--no-copy`      | Does not copy the output to the clipboard, just displays in the terminal |
| `-h`, `--help`          | Shows the help menu with all available options.              |

### Behavior Summary

| | `.gitignore` respected | OS-hidden files shown | `.git` shown |
|---|---|---|---|
| `gtree` | Yes | No | No |
| `gtree -ng` | No | No | No |
| `gtree -a` | No | Yes | Yes |

## Setting Up Global Access (Recommended)

To run `gtree` from any folder without typing the full path, add it to your PowerShell profile:

1. Open your profile in Notepad: `notepad $PROFILE`

2. Add a function that points to wherever you saved `gtree.py`:

   ```powershell
   function gtree {
       python "C:\path\to\gtree.py" $args
   }
   ```

3. Save, close, and restart PowerShell.

4. You can now type `gtree`, `gtree -a`, `gtree -ng`, or `gtree --show-git` from any directory.
