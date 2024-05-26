def read_input(file: str) -> str:
    """
    Opens the given file. Typically a puzzle input

    Args:
        file: The file to open

    Returns:
        The contents of the file
    """
    with open(f'input_files\\{file}', 'r') as file:
        text = file.read().strip()
    return text
