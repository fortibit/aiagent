import os

def get_files_info(working_directory, directory="."): # example "calculator", "pkg"
    full_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(full_path)
    if working_directory not in absolute_path:
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    print(full_path)
    print(absolute_path)

get_files_info("calculator", "pkg")
get_files_info("calculator", "calculator.py")
get_files_info("calculator", "../")