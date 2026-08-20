# A git-aware file directory tool

A lightweight, Python-based terminal utility that generates a visual directory tree while respecting `.gitignore` rules and OS-level hidden file conventions. It also gives you the choice to not respect those conventions.


When you run the command, it prints the directory in the terminal window and also copies it to your clipboard.

## Features

- **Git-Aware:** Automatically detects and parses your `.gitignore` file, hiding matched entries by default.
- **Hidden File Filtering:** Respects OS-level hidden files — `FILE_ATTRIBUTE_HIDDEN` on Windows, dotfiles on Unix.
- **Auto-Copy:** Automatically copies the generated tree to your clipboard for easy pasting into docs or LLM prompts.
- **Empty Directory Suppression:** Directories with no visible children are omitted entirely from the output.

## Getting Started

Download gtree.py from the releases page [here](https://github.com/KevanMacGee/file-tree/releases/download/1.0.0/gtree.py).

You will need the `pathspec` and `pyperclip` libraries installed before you use the tool:

```
pip install pathspec pyperclip
```

## Usage

The simplest way to use this is to set up global usage. (See instructions below) Then just open a terminal in the folder you want to view and run `gtree`.

```
PS C:\Users\John\g-tree> gtree
C:\Users\John\g-tree
├── .cursorindexingignore
├── .gitignore
├── gtree.py
└── readme.md
```

### Occasional usage

If you only plan to use `gtree.py` occasionally, you can run it like a normal Python command-line script. If you plan to use it this way, you'll need some extra commands as listed below.

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
       python "C:\Users\John\Programs\gtree.py" $args
   }
   ```

3. Save, close, and restart PowerShell.

4. You can now type `gtree`, `gtree -a`, etc. from any directory.

## Command Line Flags


<table>
  <thead>
    <tr>
      <th width="220" nowrap="nowrap">Flag</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td nowrap="nowrap">[No flag]</td>
      <td>Shows the folder contents, but respects <code>.gitignore</code> file and doesn't print OS-hidden files.</td>
    </tr>
    <tr>
      <td nowrap="nowrap"><code>-ng</code>, <code>--no-gitignore</code></td>
      <td>Bypass <code>.gitignore</code> rules, but OS-hidden files are not printed.</td>
    </tr>
    <tr>
      <td nowrap="nowrap"><code>-a</code>, <code>--all</code></td>
      <td>Shows everything: OS-hidden files and <code>.gitignore</code>-excluded entries.</td>
    </tr>
    <tr>
      <td nowrap="nowrap"><strong>Special Flags</strong></td>
      <td></td>
    </tr>
    <tr>
      <td nowrap="nowrap"><code>-nc</code>, <code>--no-copy</code></td>
      <td>Does not copy the output to the clipboard, just displays in the terminal</td>
    </tr>
    <tr>
      <td nowrap="nowrap"><code>-h</code>, <code>--help</code></td>
      <td>Shows the help menu with all available options.</td>
    </tr>
  </tbody>
</table>

### In other words...

| Command                            | `.gitignore` respected | OS-hidden files respected |
| ---------------------------------- | ---------------------- | ------------------------- |
| `gtree`                            | Yes                    | Yes                       |
| `gtree -ng` `gtree --no-gitignore` | No                     | Yes                       |
| `gtree -a` `gtree --all`           | No                     | No                        |
