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

def build_tree_string(dir_path, prefix="", spec=None, root_dir=None, show_all=False):
    output = ""
    if root_dir is None:
        root_dir = os.path.abspath(dir_path)
        output += f"{root_dir}\n"

    try:
        items = os.listdir(dir_path)
        valid_items = []
        for i in items:
            if i.startswith('$'): continue
            if i == '.git' and not show_all: continue
            valid_items.append(i)
        valid_items.sort()
    except PermissionError:
        return ""

    filtered_items = []
    for item in valid_items:
        full_path = os.path.join(dir_path, item)
        rel_path = os.path.relpath(full_path, root_dir)
        match_path = rel_path + '/' if os.path.isdir(full_path) else rel_path
        
        if spec and spec.match_file(match_path):
            continue
        filtered_items.append(item)

    for i, item in enumerate(filtered_items):
        is_last = (i == len(filtered_items) - 1)
        connector = "└── " if is_last else "├── "
        output += f"{prefix}{connector}{item}\n"
        
        full_path = os.path.join(dir_path, item)
        if os.path.isdir(full_path):
            new_prefix = prefix + ("    " if is_last else "│   ")
            output += build_tree_string(full_path, new_prefix, spec, root_dir, show_all)
    
    return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A git-aware directory tree generator.")
    parser.add_argument("path", nargs="?", default=".", help="Target directory")
    parser.add_argument("-a", "--all", action="store_true", help="Include .git folder")
    parser.add_argument("--no-ignore", action="store_true", help="Do not respect .gitignore rules")
    parser.add_argument("-nc", "--no-copy", action="store_true", help="Do not copy output to clipboard")
    
    args = parser.parse_args()
    gitignore_spec = None if args.no_ignore else get_gitignore_spec(args.path)
    
    tree_output = build_tree_string(args.path, spec=gitignore_spec, show_all=args.all)
    
    print(tree_output)
    
    if not args.no_copy and tree_output:
        pyperclip.copy(tree_output)
        print("\n[Success: Tree structure copied to clipboard]")