import argparse                                                # Import the argparse module to handle command-line arguments.
import logging                                                 #(This module provides a flexible framework for emitting log messages from Python programs.                                                            
import pathlib                                                  # Import the pathlib module to work with file system paths in an object-oriented way.
import sys
import shutil

from tqdm import tqdm

#(BRAINS OF OUR FILE. KEY- folder we create eg-Images and Value- file extension(.png,.jpg))
FILE_TYPE_NAME={     
   "Images" : ['.bmp','.jpeg','.jpg','.gif','.svg','.png'],
    "Documents" : ['.txt','.pdf','.doc','.ppt','.xls','.xlsx'],
    "Audio" : ['.mp3','.wav','.aac','.flac'],
    "Videos" : ['.mp4','.avi','.mkv','.mov'],
    "Archives" : ['.zip','.rar','.tar','.gz'],
    "Others" : []                                                     # This category will be used for files that don't match any of the above types 
    }  

def organise_directory(source_path : pathlib.Path, dry_run: bool):
    """
    Scans a directory and organizes files into subdirectories based on their type.

    This function is the main workhorse of the script. It will contain the logic
    for iterating through files, determining their type, creating destination
    folders, and moving the files.

    Args:
        source_path (pathlib.Path): The Path object representing the directory
                                    to be organized.
    """
    logging.info(f"\nOrganising files in: {source_path}\n")
    if dry_run:
        logging.info("---Dry run mode enabled. No files will be moved.---\n")
    
    else:
        logging.warning("---Dry run mode disabled. Files will be moved.---\n")

    file_to_process = [item for item in source_path.iterdir() if item.is_file()] 
    
    for item in tqdm(file_to_process, desc="Organizing files"):
            file_extension = item.suffix                           
                        
            destination_folder_name = 'Others'                      
            for category, extensions in FILE_TYPE_NAME.items():     
                if file_extension in extensions:                     
                        destination_folder_name = category                
                        break          
                                                  
            destination_dir = source_path / destination_folder_name  
          
            if dry_run:
                destination_path = destination_dir / item.name
                logging.info(f"Dry run: Would move '{item.name}' to '{destination_path}'")
            else:
                
             destination_dir.mkdir(parents=True, exist_ok=True)       # Create the destination folder if it doesn't exist and its parent directories if necessary
            
            destination_path = destination_dir / item.name           
            
            counter = 1
            original_destination = destination_path                  

            if destination_path.exists():
                logging.warning(f"Conflict: '{item.name}' already exists. Renaming...")                                                              
            while destination_path.exists():                          # Now find an available name                 
                new_filename = f"{item.stem} ({counter}){item.suffix}"
                destination_path = destination_dir / new_filename
                counter += 1
                
            try:                                                       # Attempt to move the file to the destination path
                shutil.move(str(item), str(destination_path))         
                logging.info(f"Moved: {item} -> {destination_path}\n")     
                
            except PermissionError as e:                             
                logging.error(f"Permission error while moving '{item.name}'. Error: {e}")
                
            except Exception as e:
                logging.error(f"Unexpected error moving '{item.name}'. Error: {e}")

if __name__ == "__main__":                                             # This block of code will only run when the script is executed directly from the command line. It's the main entry point for our application.
    
    parser=argparse.ArgumentParser(description="Organise files in a directory by their type")
    parser.add_argument('source_directory', help='The path to the directory you want to organize.')    #(added a postional argument)
    parser.add_argument('--dry-run', action='store_true', help='Simulate the organization without making any changes.')  #(added an optional argument)
    args = parser.parse_args()          
  
    
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.StreamHandler(sys.stdout),logging.FileHandler('organiser.log')])       #(This sets up the logging configuration to display messages with a specific format that includes the timestamp, log level, and message content.
    
    source_path = pathlib.Path(args.source_directory)                                                 #(This converts the user-provided directory path into a Path object, which provides methods for file system operations.)
   
    if not source_path.is_dir() or not source_path.exists():                                          
       logging.error(f"Error: 'source_directory' is not a valid directory path or does not exist.")
       sys.exit(1)                                                                                    #(This exits the program with a non-zero status code, indicating an error.)

    organise_directory(source_path, args.dry_run)                                                                   #(If the path is valid, we call the organise_directory function, passing the Path object as an argument to start the file organization process.)
    