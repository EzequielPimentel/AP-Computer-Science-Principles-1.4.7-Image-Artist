import PIL
import os.path
import PIL.ImageDraw
import PIL.ImageFilter

class ImageRetriever():
    def __init__(self, directory = os.getcwd()):
        self.directory = directory

    def retrieve_all_image_names(self):
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
        absolute_filenames, entry_list = self.retrieve_all_image_names()

        for (entry, absolute_filename) in zip(entry_list, absolute_filenames):
            if entry == name:
                return PIL.Image.open(absolute_filename)

class PasteImage():
    
    def __init__(self, images, pasted_logo):
        self.images = images
        self.pasted_logo = pasted_logo
        
 
    
    def paste_logo(self):
        
        for image in self.images:
            width, height = image.size
            image.paste(self.pasted_logo, (width-30,height-30))
            
 
image_retriever = ImageRetriever()         
images = image_retriever.retrieve_all_images()
pasted_logo = image_retriever.retrieve_image("Save tree logo.png")
paste_image = PasteImage(images,pasted_logo)





