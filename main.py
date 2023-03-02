# This is a sample Python script.
from statistics import median

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PIL import Image


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    im = Image.open("canstockphoto54158676.jpg")  # Can be different formats.
    pix = im.load()

    print(pix[0, 0][0])
    for x in range(im.width):
        for y in range(im.height):
            value = int((pix[x, y][0] + pix[x, y][1] + pix[x, y][2]) / 3)
            pix[x, y] = (value, value, value)

    im.save('test.jpg')  # Save the modified pixels image

    grayImage = Image.open("test.jpg")
    pix = grayImage.load()
    value = 0
    chosenPixel = (0, 0)
    contrastWidth = 9
    resultArray = []

    for x in range(grayImage.width):
        value = 0
        left = 0
        right = 0
        for y in range(grayImage.height - contrastWidth * 2):
            for pixel in range(contrastWidth):
                left += pix[x, y + pixel][0]
                right += pix[x, y + pixel + contrastWidth][0]
            checkValue = abs(left - right)
            if checkValue > value:
                value = checkValue
                chosenPixel = (x, y)
            if y == (grayImage.height - (contrastWidth * 2) - 1):
                resultArray.append(chosenPixel)

    print("result array is:", resultArray)

    buffLine = True

    if buffLine:
        # Add edge to picture
        index = 0
        medianAmount = 10
        medList = []
        for element in resultArray:
            medList.append(element[1])
            if len(medList) == medianAmount:
                medList.pop(0)
            if (element[0] - medianAmount / 2) >= 0:
                pix[element[0] - medianAmount / 2, median(medList) - 1]\
                    = pix[element[0] - medianAmount / 2, median(medList)] = (0, 0, 0)
            index += 1
    else:
        for element in resultArray:
            pix[element[0], element[1] - 1] = pix[element[0], element[1]] = (0, 0, 0)

    grayImage.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
