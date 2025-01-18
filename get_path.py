from pathlib import Path

def get_directory(folder_name="Downloads"):
    """
    Retrieve the path of a desired folder and create it if necessary.
    
    Parameters:
        folder_name (str): Name of the folder to retrieve.
                           Options: "Downloads" or "Organized Downloads".

    Returns:
        str: A properly formatted path to the specified folder.
    """
    home = Path.home()
    if folder_name == "Downloads":
        folder_path = home / "Downloads"
    elif folder_name == "Organized Downloads":
        folder_path = home / "Desktop" / "Organized_downloads"
    else:
        raise ValueError("Invalid folder_name. Choose 'Downloads' or 'Organized Downloads'.")

    # Create the folder if it doesn't exist
    folder_path.mkdir(parents=True, exist_ok=True)

    # Return a properly formatted path
    return str(folder_path.resolve())
# Example usage

downloads_path = get_directory("Downloads")
organized_downloads_path = get_directory("Organized Downloads")

print(f"{downloads_path}\n{organized_downloads_path}")