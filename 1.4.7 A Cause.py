import PIL
import os.path
import PIL.ImageDraw
import PIL.ImageFilter

class ImageRetriever():

    def __init__(self, directory = os.getcwd()):
        self.directory = directory

    def retrieve_all_images():
        image_list = []
        file_list = []

        directory_list = os.listdir(directory)

        for entry in directory_list:
            absolute_filename = os.path.join(directory, entry)
            try:
                image = PIL.image.open(absolute_filename)
                file_list += [entry]
                image_list += [image]

            except IOError:
                pass # ignore the error if it's not an image

        return image_list, file_list

class FilterApplier():

    def __init__(self, image):
        self.image = image
