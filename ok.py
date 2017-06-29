from PIL import Image


myImage = Image.open("dice.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []



### Functions

def darkBlue(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    red = 0
    green = 51
    blue = 76
    
    p = (red,green,blue)
  
    newPixelList.append(p)



def red(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    red = 217
    green = 26
    blue = 33
   
    p = (red,green,blue)

    newPixelList.append(p)


def lightBlue(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    red = 112
    green = 150
    blue = 158

   


    p = (red,green,blue)

    newPixelList.append(p)    

def yellow(pixel):
    red = 252
    green = 227
    blue = 166

    p = (red,green,blue)

    newPixelList.append(p) 


### RUNNING CODE

newPixelList = []


counter = 0

for pixel in pixelList:

    intensity = pixel[0] + pixel[1] + pixel[2]
    



#pixel manipulation

    if intensity < 182:
        darkBlue(pixel)
    elif (intensity > 182)and ( intensity < 364):
        red(pixel)
    elif (intensity > 364) and (intensity < 546):
        lightBlue(pixel)
    else:
        yellow(pixel)
    
    

#open the image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()


    
