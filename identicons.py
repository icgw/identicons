try:
    from PIL import Image, ImageDraw
except ImportError:
    print("You should install Pillow first. (#pip install pillow)")
    exit()

from hashlib import md5

class Identicon:
    def __init__(self, Id, GridSize = 60, BackGround = "#f0f0f0"):
        """
        Input User Id.
        The defaul size of grid is 60px.
        The background color is rgb(240, 240, 240)
        """
        self.id   = Id
        self.hash = md5(Id.encode()).hexdigest()
        self.img  = Image.new("RGB", (7 * GridSize, 7 * GridSize), BackGround)
        self.size = GridSize

    def generate(self):
        """
        Generate the image using the hash MD5 of id
        """
        hash_dec = int(self.hash, 16)
        color = (hash_dec & 0xff, hash_dec >> 8 & 0xff, hash_dec >> 16 & 0xff)
        Draw = ImageDraw.Draw(self.img)
        sq_x = sq_y = 0
        SIZE = self.size
        for x in range(15):
            hash_dec >>= 8
            if hash_dec & 1:
                x = SIZE + sq_x * SIZE
                y = SIZE + sq_y * SIZE
                Draw.rectangle(
                [x, y, x + SIZE - 1, y + SIZE - 1],
                fill = color,
                outline = color
                )

                x = 6 * SIZE - x
                Draw.rectangle(
                [x, y, x + SIZE - 1, y + SIZE - 1],
                fill = color,
                outline = color
                )
            sq_y += 1
            if sq_y == 5:
                sq_y = 0
                sq_x += 1

    def show(self):
        self.img.show()

    def output(self):
        """
        Output the image to the current directory.
        """
        with open(self.id + ".png", "wb") as out:
            self.img.save(out, "PNG")
