# A git-aware file directory tool

A lightweight, Python-based terminal utility that generates a visual directory tree while respecting `.gitignore` rules and OS-level hidden file conventions. It also gives you the choice to not respect those conventions.

## Features

- **Git-Aware:** Automatically detects and parses your `.gitignore` file, hiding matched entries by default.
- **Hidden File Filtering:** Respects OS-level hidden files — `FILE_ATTRIBUTE_HIDDEN` on Windows, dotfiles on Unix.
- **Auto-Copy:** Automatically copies the generated tree to your clipboard for easy pasting into docs or LLM prompts.
- **Empty Directory Suppression:** Directories with no visible children are omitted entirely from the output.

## Prerequisites

You will need the `pathspec` and `pyperclip` libraries installed:

```
pip install pathspec pyperclip
```

## Usage

The simplest way to use this is to set up up global usage. (See instructions below) Then just open a terminal in the folder you want to view and run `gtree`.

```
PS C:\Users\John\g-tree> gtree
C:\Users\John\g-tree
├── .cursorindexingignore
├── .gitignore
├── gtree.py
└── readme.md
```

### Occasional usage

If you only plan to use `gtree.py` occasionally, you can run it like a normal Python command-line script. If you plan to use it often, see the global access section below.

In the examples below, pretend the script is stored here:

`C:\Users\John\Desktop\gtree.py` 

Replace `John` with your own Windows username.

PowerShell

```powershell
# View the folder you are currently in
python "C:\Users\John\Desktop\gtree.py"

# View a specific folder
python "C:\Users\John\Desktop\gtree.py" "C:\Users\John\Documents\MyWebsite"
```

The first path is the location of gtree.py. The second path is the folder you want to scan.

## Setting Up Global Access (Recommended)

To run `gtree` from any folder without typing the full path, add it to your PowerShell profile:

1. Using your PowerShell terminal, open your profile in Notepad by typing this in your terminal: `notepad $PROFILE`

2. In the notepad text file that just opened, add a function that points to wherever you saved `gtree.py`:

   ```powershell
   function gtree {
       python "C:\Users\John\Programs" $args
   }
   ```

3. Save, close, and restart PowerShell.

4. You can now type `gtree`, `gtree -a`, etc. from any directory.

## Command Line Flags

If you know what you are doing and don't need help setting it up, here are the flags.

| **Flag**                | **Description**                                                                            |
| ----------------------- | ------------------------------------------------------------------------------------------ |
| [No flag]               | Shows the folder contents, but respects .gitignore file and doesn't print OS-hidden files. |
| `-ng`, `--no-gitignore` | Bypass `.gitignore` rules, but OS-hidden files are not printed.                            |
| `-a`, `--all`           | Shows everything: OS-hidden files and `.gitignore`-excluded entries.                       |
| **Special Flags**       |                                                                                            |
| `-nc`, `--no-copy`      | Does not copy the output to the clipboard, just displays in the terminal                   |
| `-h`, `--help`          | Shows the help menu with all available options.                                            |

### Usage Summary

In other words...

| Command                             | `.gitignore` respected | OS-hidden files respected |
| ----------------------------------- | ---------------------- | ------------------------- |
| `gtree`                             | Yes                    | Yes                       |
| `gtree -ng` `gtree- --no-gitignore` | No                     | Yes                       |
| `gtree -a` `gtree -all`             | No                     | No                        |

4. 
