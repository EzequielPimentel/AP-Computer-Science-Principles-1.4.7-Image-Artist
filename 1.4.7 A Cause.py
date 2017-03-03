import PIL
import os.path
import PIL.ImageDraw
import PIL.ImageFilter

class ImageRetriever():
    def __init__(self, directory = os.getcwd()):
        self.directory = directory

    def retrieve__all_image_names(self):
        absolute_file_list = []
        entry_list = []
        directory_list = os.listdir(self.directory)

        for entry in directory_list:
            absolute_filename = os.path.join(directory, entry)
            try:
                image = PIL.Image.open(absolute_filename)
                absolute_file_list += [absolute_filename]
                entry_list += [entry]
            except IOError:
                pass # ignore the error if it's not an image

        return absolute_file_list, entry_list

    def retrieve_all_images(self):
        image_list = []

        directory_list = os.listdir(directory)

        for entry in directory_list:
            absolute_filename = os.path.join(directory, entry)
            try:
                image = PIL.Image.open(absolute_filename)
                image_list += [image]

            except IOError:
                pass # ignore the error if it's not an image

        return image_list

    def retrieve_image(self, name):
        absolute_filenames, entry_list = retrieve_all_image_names()

        for entry, absolute_filename in entry_list, absolute_filenames:
            if entry == name:
                return PIL.Image.open(absolute_filename)
