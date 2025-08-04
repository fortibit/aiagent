import os


def get_files_info(working_directory, directory="."):  # example "calculator", "pkg"
    full_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(full_path)

   
    # get directory contents
    directory_contents = os.listdir(absolute_path)

    if directory == ".":
        current_dir_str = "current"
    else:
        current_dir_str = directory

    # build a return strings list
    result = []
    result.append(f"Result for '{current_dir_str}' directory:")

    # check if the absolute path is outside of working_directory
    if working_directory not in absolute_path:
        result.append(f'    Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return "\n".join(result)
    
    # check if {directory} is not a directory
    if not os.path.isdir(absolute_path):
        result.append(f'    Error: "{directory}" is not a directory')
        return "\n".join(result)
    
    # get each result info
    for item in directory_contents:
        file_path = os.path.join(absolute_path, item)
        result.append(f" - {item}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}")
    
    return "\n".join(result)
