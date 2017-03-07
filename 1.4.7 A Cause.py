import PIL
import os.path
import PIL.ImageDraw
import PIL.ImageFilter
import PIL.ImageEnhance

class ImageFileHandler():
    def __init__(self, directory = os.getcwd()):
        """
        Directory is set to the current working directory.
        """
        self.directory = directory

    def retrieve_all_image_names(self):
        """
        Returns the file list and a list of file names of all images in the
        current working directory.
        """
        absolute_file_list = []
        entry_list = []
        directory_list = os.listdir(os.getcwd())

        for entry in directory_list:
            absolute_filename = os.path.join(self.directory, entry)
            try:
                PIL.Image.open(absolute_filename)
                absolute_file_list += [absolute_filename]
                entry_list += [entry]
            except IOError:
                pass # ignore the error if it's not an image

        return absolute_file_list, entry_list

    def retrieve_all_images(self):
        """
        Returns a list of PIL images in the current working directory.
        """
        image_list = []

        directory_list = os.listdir(self.directory)

        for entry in directory_list:
            absolute_filename = os.path.join(self.directory, entry)
            try:
                image = PIL.Image.open(absolute_filename)
                image_list += [image]

            except IOError:
                pass # ignore the error if it's not an image

        return image_list

    def retrieve_image(self, name):
        """
        Returns a single PIL image. Used to retrieve the pasted logo. Name is the
        file name of the image you want to be retrieved.
        """
        absolute_filenames, entry_list = self.retrieve_all_image_names()

        for (entry, absolute_filename) in zip(entry_list, absolute_filenames):
            if entry == name:
                return PIL.Image.open(absolute_filename)
    def save_images(self, images, base_name):
        """
        Saves a list of images in a folder, "modified_images". Images is a list
        of images and base_name is a string that the images are saved under.
        """
        modified_folder = os.path.join(self.directory, 'modified_images')
        if not os.path.isdir(modified_folder):
            os.makedirs(modified_folder)

        for file in os.listdir(modified_folder):
            file_path = os.path.join(modified_folder, file)
            os.unlink(file_path)

        stepper = 0
        for image in images:
            print(type(image))
            print(type(image.format))
            im_format = image.format
            if im_format is None:
                im_format = 'JPG'

            file_name = os.path.join(modified_folder, base_name + str(stepper) + '.' + im_format)
            try:
                image.save(file_name)
            except AttributeError:
                pass
            stepper += 1

class FilterApplier():
    '''An object that handles the task of adding filters to images.'''
    def __init__(self, images):
        '''Specify the images you want to filter.'''
        self.images = images

    def blur(self, image):
        blurred_image = image.filter(PIL.ImageFilter.BLUR)
        return blurred_image

    def contrast(self, image):
        contraster = PIL.ImageEnhance.Contrast(image)
        contrasted_image = contraster.enhance(1.5)
        return contrasted_image

    def decrease_brightness(self, image):
        brightner = PIL.ImageEnhance.Brightness(image)
        brightened_image = brightner.enhance(0.6)
        return brightened_image

    def chain_filters(self, original_image):
        blurred_image = self.blur(original_image)
        contrasted_image = self.contrast(blurred_image)
        reduced_brightness_image = self.decrease_brightness(contrasted_image)
        return reduced_brightness_image

    def chain_filters_on_all_images(self):
        filtered_images = []
        for image in self.images:
            filtered_image = self.chain_filters(image)
            filtered_images += [filtered_image]

        return filtered_images

class PasteImage():

    def __init__(self, images, pasted_logo):
        """
        pasted_logo is the file name of a logo that will be pasted onto other
        images.
        """
        self.images = images
        self.pasted_logo = pasted_logo

    def paste_logo(self, image):
        """
        Pastes the logo specified onto an image. Returns a single modified image.
        image is a PIL image that will be modified.
        """
        width, height = image.size
        pasted_logo = self.pasted_logo.resize((20, 20))
        image.paste(pasted_logo, (0, 0))
        return image

    def paste_logo_on_images(self):
        """
        Iterates through a list of images, images, to paste a specified logo
        onto each image. Returns a list of modified images.
        """
        images = []
        for image in self.images:
            pasted_image = self.paste_logo(image)
            images += [pasted_image]

        return images

def fetch_images():
    image_handler = ImageFileHandler()
    images = image_handler.retrieve_all_images()
    return images

def paste_image_test():
    image_handler = ImageFileHandler()
    images = fetch_images()
    pasted_logo = image_handler.retrieve_image("Save tree logo.png")
    paste_image = PasteImage(images, pasted_logo)
    pasted_images = paste_image.paste_logo_on_images()
    image_handler.save_images(pasted_images, "paste_image_test")

def filter_test():
    image_handler = ImageFileHandler()
    images = fetch_images()
    filter_applier = FilterApplier(images)
    filtered_images = filter_applier.chain_filters_on_all_images()
    image_handler.save_images(filtered_images, "filter_image_test")
