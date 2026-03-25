import os
import sys
import argparse
import pyperclip
from pathspec import PathSpec
from pathspec.patterns import GitWildMatchPattern


def get_gitignore_spec(folder):
    gitignore_path = os.path.join(folder, '.gitignore')
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as f:
            return PathSpec.from_lines(GitWildMatchPattern, f)
    return None


def is_os_hidden(filepath):
    if sys.platform == 'win32':
        # On Windows, "hidden" means the FILE_ATTRIBUTE_HIDDEN bit — not dotfile prefix.
        # Dotfiles are ordinary files on Windows and should be visible by default.
        try:
            import ctypes
            attrs = ctypes.windll.kernel32.GetFileAttributesW(filepath)
            return attrs != -1 and bool(attrs & 2)  # FILE_ATTRIBUTE_HIDDEN
        except Exception:
            return False
    else:
        # On Unix, dotfiles are hidden by OS convention.
        return os.path.basename(filepath).startswith('.')


def build_tree_string(dir_path, prefix="", spec=None, root_dir=None, show_all=False):
    if root_dir is None:
        root_dir = os.path.abspath(dir_path)
        header = f"{root_dir}\n"
    else:
        header = ""

    try:
        raw_items = os.listdir(dir_path)
    except PermissionError:
        return ""

    visible = []
    for name in raw_items:
        if name.startswith('$'):
            continue
        full = os.path.join(dir_path, name)
        if not show_all:
            if is_os_hidden(full):
                continue
        visible.append(name)
    visible.sort()

    # Apply gitignore filtering
    if spec:
        filtered = []
        for name in visible:
            full = os.path.join(dir_path, name)
            rel = os.path.relpath(full, root_dir)
            match_path = rel + '/' if os.path.isdir(full) else rel
            if not spec.match_file(match_path):
                filtered.append(name)
    else:
        filtered = visible

    # For directories, recurse first and skip those that produce no output
    lines = []
    for i, name in enumerate(filtered):
        full = os.path.join(dir_path, name)
        is_last = (i == len(filtered) - 1)
        connector = "└── " if is_last else "├── "
        new_prefix = prefix + ("    " if is_last else "│   ")

        if os.path.isdir(full):
            subtree = build_tree_string(full, new_prefix, spec, root_dir, show_all)
            if subtree:
                lines.append(f"{prefix}{connector}{name}/\n{subtree}")
        else:
            lines.append(f"{prefix}{connector}{name}\n")

    if not lines:
        return ""

    return header + "".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A git-aware directory tree generator.")
    parser.add_argument("path", nargs="?", default=".", help="Target directory")
    parser.add_argument("-a", "--all", dest="show_all", action="store_true",
                        help="Show absolutely everything, including hidden and gitignore-excluded files")
    parser.add_argument("-ng", "--no-gitignore", dest="no_gitignore", action="store_true",
                        help="Ignore .gitignore rules (hidden files are still excluded)")
    parser.add_argument("-nc", "--no-copy", dest="no_copy", action="store_true",
                        help="Do not copy output to clipboard")

    args = parser.parse_args()

    if args.show_all or args.no_gitignore:
        gitignore_spec = None
    else:
        gitignore_spec = get_gitignore_spec(args.path)

    tree_output = build_tree_string(
        args.path,
        spec=gitignore_spec,
        show_all=args.show_all,
    )

    print(tree_output)

    if not args.no_copy and tree_output:
        pyperclip.copy(tree_output)
        print("\n[Success: Tree structure copied to clipboard]")
