from PIL import Image

## FUNCTIONS

newPixelList = []
myImage = Image.open("ele2.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)
length = len(pixelList)
halfway = length//3

def k(pixel):
    #pixel manipulation

    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    
    newRed = red//2
    newGreen = green//2
    newBlue = blue//2
        
    p = (newRed,newGreen,newBlue)

    newPixelList.append(p)

def negative(pixel):
    #pixel manipulation

    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    
    newRed = 255 - red
    newGreen = 255 - green
    newBlue = 255 - blue
        
    p = (newRed,newGreen,newBlue)

    newPixelList.append(p)

def overExposed(pixel):
    #pixel manipulation
    
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]

        newRed = red*2
        if newRed > 255:
            newRed = 255

        newGreen = green*2
        if newGreen > 255:
            newGreen = 255
            
        newBlue = blue*2
        if newBlue > 255:
            newBlue = 255
            
        p = (newRed,newGreen,newBlue)
        newPixelList.append(p)

counter = 0        
for pixel in pixelList:
    if (counter < halfway): #this is the top half of the photo
        overExposed(pixel)
        
    else: #this is the bottom half of the photo
        negative(pixel)

    counter = counter + 1

    #create new pixel
    
#open the image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
#newImage.save("newPhoto.jpeg","jpeg")
