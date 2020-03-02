from Chapter5.zip_processor import ZipProcessor
# from zip_processor import ZipProcessor
import sys
# pillow lib
from PIL import Image


class ScaleZip(ZipProcessor):

    def process_files(self):
        """Scale each image in the directory to 640x480"""
        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize((640, 480))
            scaled.save(str(filename))

# $: python c5_20_scaleimage_inheritance.py hi.zip opa opalq
if __name__ == "__main__":
    ScaleZip(*sys.argv[1:4]).process_zip()
