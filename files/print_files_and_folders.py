from os import path, walk


def print_all_files(top_dir: str):
    """Print directories and files on top_dir.

    :param top_dir: Path to the folder.
    """

    for dir_path, dir_names, files in walk(top_dir):
        for file_name in files:
            print(f"file {path.join(dir_path, file_name)}")
        for dir_name in dir_names:
            print(f"directory {path.join(dir_path, dir_name)}")
