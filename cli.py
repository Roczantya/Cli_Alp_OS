import os
import sys
import shutil

from extras import *

# Lists the contents of a directory (default is the current directory)
def list_directory(path="."):
    try:
        items = os.listdir(path)
        print(f"Contents of {path}:")
        for item in items:
            print(item)
    except FileNotFoundError:
        print(f"Error: {path} not found.")

# Prints the current working directory
def print_working_directory():
    print(os.getcwd())

# Changes the current working directory
def change_directory(path):
    try:
        os.chdir(path)
        print(f"Changed directory to {path}")
    except FileNotFoundError:
        print(f"Error: Directory {path} not found.")

# Creates a new directory at the specified path
def make_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Directory '{path}' created successfully.")
    except Exception as e:
        print(f"Error creating directory: {e}")

# Removes an empty directory
def remove_directory(path):
    try:
        os.rmdir(path)
        print(f"Directory '{path}' removed successfully.")
    except Exception as e:
        print(f"Error removing directory: {e}")

# Creates an empty file at the specified path
def create_file(path):
    try:
        with open(path, 'w') as f:
            f.write("")
        print(f"File '{path}' created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")

# Removes a file at the specified path
def remove_file(path):
    try:
        os.remove(path)
        print(f"File '{path}' removed successfully.")
    except Exception as e:
        print(f"Error removing file: {e}")

# Copies a file from source to destination
def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"File '{source}' copied to '{destination}'.")
    except Exception as e:
        print(f"Error copying file: {e}")

# Moves or renames a file or directory
def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f"File '{source}' moved to '{destination}'.")
    except Exception as e:
        print(f"Error moving file: {e}")

# Displays the list of available commands and their descriptions
def show_help():
    print("Available commands:")
    print("1. ls [path] - List directory contents")
    print("2. pwd - Print working directory")
    print("3. cd <path> - Change directory")
    print("4. mkdir <path> - Create a new directory")
    print("5. rmdir <path> - Remove an empty directory")
    print("6. touch <path> - Create a new empty file")
    print("7. rm <path> - Remove a file")
    print("8. cp <source> <destination> - Copy a file")
    print("9. mv <source> <destination> - Move or rename a file/directory")
    print("10. clear - Clear the screen")   
    print("11. extra - List of extra command in fany's CLI")
    print("12, exit - Exit the CLI")

# Clears the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Searches for files or directories matching a pattern
def search_files(pattern):
    for root, dirs, files in os.walk("C:\\"):
        for name in files + dirs:
            if pattern in name:
                print(os.path.join(root, name))

# Recursively displays the directory structure as a tree
def display_tree(path=".", indent=""):
    try:
        items = os.listdir(path)
        for item in items:
            full_path = os.path.join(path, item)
            print(indent + item)
            if os.path.isdir(full_path):
                display_tree(full_path, indent + "  ")
    except Exception as e:
        print(f"Error displaying tree: {e}")
import os

def display_tree_DirC(path="C:\\", indent="", max_entries=200, current_entries=0, max_depth=200, current_depth=0):
    try:
        # Check if the maximum entries limit is reached
        if max_entries is not None and current_entries >= max_entries:
            return

        # Check if the maximum depth is reached
        if max_depth is not None and current_depth >= max_depth:
            return

        items = os.listdir(path)
        for item in items:
            full_path = os.path.join(path, item)
            print(indent + "|-- " + item)
            current_entries += 1  # Increment the entry count

            # If the current entries exceed max_entries, stop processing further
            if current_entries >= max_entries:
                return

            if os.path.isdir(full_path):
                current_entries = display_tree_DirC(full_path, indent + "  ", max_entries, current_entries, max_depth, current_depth + 1)

        return current_entries  # Return the current entry count after recursion
    except PermissionError:
        print(indent + "|-- [Permission Denied]")
    except Exception as e:
        print(f"Error displaying tree for {path}: {e}")


# Finds files larger than a specified size (in KB)
def find_large_files(size_kb):
    try:
        size_bytes = size_kb * 1024
        count = 0
        max_results = 10  # Batasi hingga 10 file
        for root, dirs, files in os.walk("C:\\"):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.getsize(file_path) > size_bytes:
                    print(f"{file_path} - {os.path.getsize(file_path) / 1024:.2f} KB")
                    count += 1
                    if count >= max_results:
                        print("Pencarian dibatasi hingga 10 file.")
                        return
    except Exception as e:
        print(f"Error finding large files: {e}")

def get_file_size(file_name):
    try:
        size = os.path.getsize(file_name)
        print(f"File '{file_name}' size: {size / 1024:.2f} KB")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"Error getting file size: {e}")

# Main function to process user input and execute commands
def main():
    print("Selamat datang di Fany's CLI! Silakan ketik 'help' untuk mengetahui command apa yang bisa digunakan di sini.")
    while True:
        command = input("Fany's CLI> ").strip().split()
        if not command:
            continue
        cmd = command[0]
        args = command[1:]

        if cmd == "ls":
            list_directory(args[0] if args else ".")
        elif cmd == "pwd":
            print_working_directory()
        elif cmd == "cd":
            if args:
                change_directory(args[0])
            else:
                print("Usage: cd <path>")
        elif cmd == "mkdir":
            if args:
                make_directory(args[0])
            else:
                print("Usage: mkdir <path>")
        elif cmd == "rmdir":
            if args:
                remove_directory(args[0])
            else:
                print("Usage: rmdir <path>")
        elif cmd == "touch":
            if args:
                create_file(args[0])
            else:
                print("Usage: touch <path>")
        elif cmd == "rm":
            if args:
                remove_file(args[0])
            else:
                print("Usage: rm <path>")
        elif cmd == "cp":
            if len(args) == 2:
                copy_file(args[0], args[1])
            else:
                print("Usage: cp <source> <destination>")
        elif cmd == "mv":
            if len(args) == 2:
                move_file(args[0], args[1])
            else:
                print("Usage: mv <source> <destination>")
        elif cmd == "help":
            show_help()
        elif cmd == "clear":
            clear_screen()

        elif cmd == "extra":
            extra()

        elif cmd == "search":
            if args:
                search_files(args[0])
            else:
                print("Usage: search <pattern>")
        elif cmd == "tree":
            display_tree(args[0] if args else ".")
        elif cmd == "treec":
            display_tree_DirC(path="C:\\", max_entries=200)
        elif cmd == "find_large":
            if args:
                try:
                    size_kb = int(args[0])
                    find_large_files(size_kb)
                except ValueError:
                    print("Usage: find_large <size_in_kb>")
            else:
                print("Usage: find_large <size_in_kb>")
        elif cmd == "size":
            if args:
                get_file_size(args[0])
            else:
                print("Usage: size <file_name>")
        elif cmd == "kobo":
            kobo_kanaeru()
        elif cmd == "pantun":
            pantun_menu()
        elif cmd == "exit":
            print("Exiting CLI...")
            tokyo()
            break
        else:
            print(f"Unknown command: {cmd}. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()
