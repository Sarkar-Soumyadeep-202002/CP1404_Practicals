import os


def main():
    """Store files in the directory specified by user."""
    extension_to_category = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]
        if extension not in extension_to_category:
            category = input("Enter the category for {} files: ".format(extension))
            extension_to_category[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass
        os.rename(filename, "{}/{}".format(extension_to_category[extension], filename))


main()
