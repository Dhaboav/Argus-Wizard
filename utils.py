import os


def list_files_in_folder(folder_path: str, extension: str) -> list[str]:
    """
    List files in a folder with a specific extension.
    """
    return [f for f in os.listdir(folder_path) if f.endswith(extension)]


def split_filename(filename: str, delimiter: str = '_') -> tuple[str, str] | tuple[None, None]:
    """
    Split a filename into parts based on a delimiter.
    """
    filename_without_ext = os.path.splitext(filename)[0]
    parts = filename_without_ext.split(delimiter)

    if len(parts) == 2:
        return tuple(part.replace('-', ' ') for part in parts)
    return None, None


def handle_filename(filename: str) -> str:
    """
    Handle and format a filename.
    """
    artist_name, title = split_filename(filename)
    if artist_name and title:
        return f'Artist: {artist_name.title()}, Title: {title.title()}'
    return f'Invalid format {filename}'


def ensure_directory_exists(output_path: str):
    """
    Ensure that the directory for the given path exists, and create it if necessary.
    """
    directory = os.path.dirname(output_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")


def write_to_file(output_path: str, results: list[str]):
    """
    Write the results to a text file. Create the file and directory if they do not exist.
    """
    try:
        ensure_directory_exists(output_path)

        with open(output_path, 'w') as file:
            for result in results:
                file.write(result + '\n')

        print(f"Results written to {output_path}")

    except Exception as e:
        print(f"Error writing to file: {e}")


def count_files_with_extension(folder_path: str, extension: str) -> int:
    """
    Count the number of files with a specific extension in a folder.
    """
    return len(list_files_in_folder(folder_path, extension))
