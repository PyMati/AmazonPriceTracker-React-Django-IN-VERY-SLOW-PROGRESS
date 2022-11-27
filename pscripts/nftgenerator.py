"""NFT generator module."""
import os
from randimage import get_random_image
import matplotlib
from PIL import Image, ImageDraw, ImageFont
import time

SIZE = (300, 300)
COLOR = (255, 127, 80)
FONT = font = ImageFont.truetype("arial.ttf", 14)
FOLDER_PATH = ("", "Nft's", "")
# os.system("pycodestyle --first nftgenerator.py")
class NFT:
    """
        Class object which keeps all functionality connected to creating,
        adding to db and minting random NFT for user.
    """
    def __init__(self, adress_to_mint, image_id):
        self.adress = adress_to_mint
        self.path = os.path.join(FOLDER_PATH[0],
                                FOLDER_PATH[1],
                                f"{self.adress}.png")
        self._generate_nft()
        self._watermark()
        time.sleep(10)
        # self._delete()

    def _generate_nft(self):
        """Generates procedural image."""
        img = get_random_image(SIZE)
        matplotlib.image.imsave(self.path, img)

    def _watermark(self):
        """Adds watermark to image."""
        img = Image.open(self.path)
        writer = ImageDraw.Draw(img)
        writer.text((25, 25), "AmazonWebPriceTracker", font=FONT, fill=COLOR)
        img.save(self.path)

    def _add_id_to_db(self):
        """Add user's image ID to database."""
        pass

    def _mint(self):
        """Mints image for wallet"""
        pass

    def _delete(self):
        """Deletes file from server directory."""
        os.remove(self.path)
