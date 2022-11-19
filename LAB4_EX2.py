class Pyramid():
    pyramid_length = ""
    pyramid_width = ""
    pyramid_height = ""
    def value(self):
        print("Lenght =",str(self.pyramid_length.P_Length))
        print("Width =", str(self.pyramid_width.P_Width))
        print("Height =", str(self.pyramid_height.P_Height))
        print("Result =",str((self.pyramid_length.P_Length * self.pyramid_width.P_Width * self.pyramid_height.P_Height)/3))

class Length():
    P_Length = ""

class Width():
    P_Width = ""

class Height():
    P_Height = ""

ResultPyramid = Pyramid()

PyramidLength = Length()
PyramidWidth = Width()
PyramidHeight = Height()

PyramidLength.P_Length = 10
PyramidWidth.P_Width = 7
PyramidHeight.P_Height = 17

ResultPyramid.pyramid_length = PyramidLength
ResultPyramid.pyramid_width = PyramidWidth
ResultPyramid.pyramid_height = PyramidHeight

print(ResultPyramid.value())