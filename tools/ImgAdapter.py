
class ImgAdapter:
    @staticmethod
    def adapteSize(pixmap,width,height):
        if height >= width:
            pixmap = pixmap.scaledToWidth(int(width))
            if pixmap.height() >= height:
                pixmap = pixmap.scaledToHeight(int(height))
        else:
            pixmap = pixmap.scaledToHeight(int(height))
            if pixmap.width() >= width:
                pixmap = pixmap.scaledToWidth(int(width))

        return pixmap