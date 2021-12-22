from PIL import Image, ImageFilter

class Transform:
    def __init__(self, imageUrl):
        self.imageUrl = imageUrl

    def show(self):
        image = Image.open(self.imageUrl)
        image.show()


class TransformBlur(Transform):

    def showBlur(self):
        image = Image.open(self.imageUrl)
        showImage = image.filter(ImageFilter.BLUR)
        showImage.show()


class TransformContour(TransformBlur):

    def showContour(self):
        image = Image.open(self.imageUrl)
        showImage = image.filter(ImageFilter.CONTOUR)
        showImage.show()


class TransformRotate(TransformContour):

    def showRotate(self):
        image = Image.open(self.imageUrl)
        im_rotate = image.rotate(40)
        im_rotate.show()


transform1 = TransformRotate('corsa.jpg')
transform1.show()
# transform1.showBlur()
# transform1.showContour()
# transform1.showRotate()