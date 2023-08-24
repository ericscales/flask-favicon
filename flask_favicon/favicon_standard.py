import os

from .abstract_favicon_group import AbstractFaviconGroup

BROWSER_TARGET_SIZES = [(16, 16), (32, 32), (48, 48)]


class FaviconGroupStandard(AbstractFaviconGroup):
    def __init__(self, conf, outdir):
        super().__init__(conf, outdir)
        self.sizes = BROWSER_TARGET_SIZES
        self.filenameSchema = 'favicon-{}x{}.png'

    def generate_images(self, favicon):
        self.generate_image(favicon, image_format='ICO')
        super().generate_images(favicon)