# Import the argparse module to handle command-line arguments.
# This will allow us to specify the target directory when we run the script.
import argparse

# Import the pathlib module to work with file system paths in an object-oriented way.
# This makes path manipulation more intuitive and cross-platform compatible.
import pathlib

# This block of code will only run when the script is executed directly
# from the command line. It's the main entry point for our application.

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description="Organise files in a directory by their type")
    
    parser.add_argument('source_directory', help='The path to the directory you want to organize.')    #(added a postional argument)
    
    args = parser.parse_args()                                        #(This object contains the user-provided arguments as attributes.)
    
    print(f"organising files in: {args.source_directory}")