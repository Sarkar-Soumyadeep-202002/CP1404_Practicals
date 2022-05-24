"""
CP1404 Practicals
Name: Soumyadeep Sarkar
Description: Program to add files to folders with the same name as their extensions.
"""
import os


def main():
    """Move files into their respective folders which have the same name as their extension."""
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):  # Only process the files not the directories.
            continue
        extension = filename.split('.')[-1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        print("{}/{}".format(extension, filename))
        os.rename(filename, "{}/{}".format(extension, filename))


main()
