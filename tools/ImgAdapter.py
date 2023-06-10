
class ImgAdapter:
    @staticmethod
    def adapteSize(pixmap,width,height):
        '''
        put pixmap in label but pixmap too big ,so use this func adapte size

        :param pixmap:
        :param width: label width
        :param height: label height
        :return: adapted img
        '''
        if height >= width:
            pixmap = pixmap.scaledToWidth(int(width))
            if pixmap.height() >= height:
                pixmap = pixmap.scaledToHeight(int(height))
        else:
            pixmap = pixmap.scaledToHeight(int(height))
            if pixmap.width() >= width:
                pixmap = pixmap.scaledToWidth(int(width))

        return pixmap