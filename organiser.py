# Import the argparse module to handle command-line arguments.
import argparse

# Import the pathlib module to work with file system paths in an object-oriented way.
import pathlib
import sys
import shutil

#(BRAINS OF OUR FILE. KEY- folder we create eg-Images and Value- file extension(.png,.jpg))
FILE_TYPE_NAME={     
   "Images" : ['.bmp','.jpeg','.jpg','.gif','.svg','.png'],
    "Documents" : ['.txt','.pdf','.doc','.ppt','.xls','.xlsx'],
    "Audio" : ['.mp3','.wav','.aac','.flac'],
    "Videos" : ['.mp4','.avi','.mkv','.mov'],
    "Archives" : ['.zip','.rar','.tar','.gz'],
    "Others" : []                                             # This category will be used for files that don't match any of the above types 
    }  

def organise_directory(source_path : pathlib.Path):
    """
    Scans a directory and organizes files into subdirectories based on their type.

    This function is the main workhorse of the script. It will contain the logic
    for iterating through files, determining their type, creating destination
    folders, and moving the files.

    Args:
        source_path (pathlib.Path): The Path object representing the directory
                                    to be organized.
    """
    print(f"Organising files in: {source_path}")


    for item in source_path.iterdir():                              # Iterate through each item in the source directory
        if item.is_file():                                          # Check if the item is a file (not a directory)
            file_extension = item.suffix                            # Get the file extension 
            
                        
            destination_folder_name = 'Other'                       # Default folder for files that don't match any type
            
            
            for category, extensions in FILE_TYPE_NAME.items():     # Iterate through the FILE_TYPE_NAME dictionary
                if file_extension in extensions:                    # Check if the file extension matches any in the current category
                        destination_folder_name = category          # If it matches, set the destination folder name to the current category     
                        break                                       # Exit the loop since we've found a match
                
            destination_dir = source_path / destination_folder_name  # Create the full path for the destination folder
            destination_dir.mkdir(parents=True, exist_ok=True)       # Create the destination folder if it doesn't exist and its parent directories if necessary
            destination_path = destination_dir / item.name           # Create the full path for the destination file
            shutil.move(item, destination_path)                      # Move the file to this exact location
            print(f"Moved: {item} -> {destination_path}")           # Print a message

# This block of code will only run when the script is executed directly
# from the command line. It's the main entry point for our application.
if __name__ == "__main__":
    parser=argparse.ArgumentParser(description="Organise files in a directory by their type")
    
    parser.add_argument('source_directory', help='The path to the directory you want to organize.')    #(added a postional argument)
    
    args = parser.parse_args()                                        #(This object contains the user-provided arguments as attributes.so that we can access them in our code.)
    
    source_path = pathlib.Path(args.source_directory)          #(This converts the user-provided directory path into a Path object, which provides methods for file system operations.)
   
    if not source_path.is_dir() or not source_path.exists():    #(This checks if the provided path is a valid directory. If it's not, we print an error message and exit the program.)
       print(f"Error: 'source_directory' is not a valid directory path or does not exist.")
       sys.exit(1)                    #(This exits the program with a non-zero status code, indicating an error.)

    organise_directory(source_path)   #(If the path is valid, we call the organise_directory function, passing the Path object as an argument to start the file organization process.)
    