import PIL
import os.path
import PIL.ImageDraw
import PIL.ImageFilter

class ImageFileHandler():
    def __init__(self, directory = os.getcwd()):
        self.directory = directory

    def retrieve_all_image_names(self):
        absolute_file_list = []
        entry_list = []
        directory_list = os.listdir(os.getcwd())

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

        for (entry, absolute_filename) in zip(entry_list, absolute_filenames):
            if entry == name:
                return PIL.Image.open(absolute_filename)
    def save_images(self, images, base_name):
        modified_folder = os.path.join(self.directory, 'modified_images')
        if not os.path.isdir(modified_folder):
            os.makedirs(modified_folder)

        for file in os.listdir(modified_folder):
            file_path = os.path.join(modified_folder, file)
            os.unlink(file_path)

        stepper = 0
        for image in images:
            im_format = image.format
            file_name = os.path.join(modified_folder, base_name + str(stepper) + '.' + im_format)
            print(file_name)
            image.save(file_name)
            stepper += 1

class FilterApplier():

class PasteImage():

    def __init__(self, images, pasted_logo):
        self.images = images
        self.pasted_logo = pasted_logo

    def paste_logo(self, image):
        width, height = image.size
        pasted_logo = self.pasted_logo.resize((20, 20))
        image.paste(pasted_logo, (0, 0))
        return image

    def paste_logo_on_images(self):
        images = []
        for image in self.images:
            pasted_image = self.paste_logo(image)
            images += [pasted_image]

        return images

def paste_image_test():
    image_retriever = ImageFileHandler()
    images = image_retriever.retrieve_all_images()
    pasted_logo = image_retriever.retrieve_image("Save tree logo.png")
    paste_image = PasteImage(images, pasted_logo)
    pasted_images = paste_image.paste_logo_on_images()
    image_retriever.save_images(pasted_images, "paste_image_test")
