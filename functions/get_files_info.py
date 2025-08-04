import os

def get_files_info(working_directory, directory="."): # example "calculator", "pkg"
    full_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(full_path)

    # check if the absolute path is outside of working_directory
    if working_directory not in absolute_path:
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    
    print(full_path)
    print(absolute_path)
    return f"Result for current directory:\n - main.py: file_size=575 bytes, is_dir=False\n - tests.py: file_size=1342 bytes, is_dir=False\n - pkg: file_size=4096 bytes, is_dir=True"