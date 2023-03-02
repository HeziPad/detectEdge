from statistics import median
from PIL import Image

if __name__ == '__main__':
    im = Image.open("canstockphoto54158676.jpg")  # Can be different formats.
    pix = im.load()
    # Turn image to grayscale
    for x in range(im.width):
        for y in range(im.height):
            value = int((pix[x, y][0] + pix[x, y][1] + pix[x, y][2]) / 3)
            pix[x, y] = (value, value, value)
    im.save('test.jpg')  # Save the modified pixels image

    grayImage = Image.open("test.jpg")
    pix = grayImage.load()
    edgeStrength = 0
    edgePixel = (0, 0)
    contrastWidth = 9  # determines how many pixels are used in edge calculation
    edgeArray = []

    for x in range(grayImage.width):
        edgeStrength = 0
        left = 0
        right = 0
        for y in range(grayImage.height - contrastWidth * 2):
            for pixel in range(contrastWidth):
                left += pix[x, y + pixel][0]
                right += pix[x, y + pixel + contrastWidth][0]
            edgeCandidateStrength = abs(left - right)
            if edgeCandidateStrength > edgeStrength:
                edgeStrength = edgeCandidateStrength
                edgePixel = (x, y)
            if y == (grayImage.height - (contrastWidth * 2) - 1):
                if edgeStrength > 10000:  # only strong edge counts
                    edgeArray.append(edgePixel)

    print("result array is:", edgeArray)

    smoothEdge = True

    if smoothEdge:
        # Add edge to picture
        index = 0
        smoothStrength = 10
        medList = []
        for element in edgeArray:
            medList.append(element[1])
            if len(medList) == smoothStrength:
                medList.pop(0)
            if (element[0] - smoothStrength / 2) >= 0:  # needed for first elements
                # median shifts the line, so need to draw "backward"
                pix[element[0] - smoothStrength / 2, median(medList) - 1] \
                    = pix[element[0] - smoothStrength / 2, median(medList)] = (0, 0, 0)
            index += 1
    else:
        for element in edgeArray:  # un-smoothed line
            pix[element[0], element[1] - 1] = pix[element[0], element[1]] = (0, 0, 0)

    grayImage.show()
