from PIL import Image, ImageFilter

white = (255,255,255)
black = (0,0,0)

def imageToArray(filepath):
   img = Image.open(filepath)
   pArray = []
   count = 0
   edges = img.filter(ImageFilter.FIND_EDGES)
   array = edges.getdata()
   while(count < img.size[0]*img.size[1]):
      if(array[count] == black):
         pArray.append(white)
      elif(array[count] == white):
         pArray.append(black)
      else:
         pArray.append(white)
      count += 1
   return pArray
   
def compare(array1, array2):
   count = 0
   array = []
   if(len(array1) == len(array2)):
      while(count < len(array1)):
         if(array1[count] == array2[count]):
            array.append(array1[count])
         elif(array1[count] != array2[count]):
            array.append((200,0,0))#NEED SOME WORK HERE
         count += 1
   else:
      print("ERROR : array length does not match")
   return array

#Write here you image's path
filePath1 = ""
filePath2 = ""

array1 = imageToArray(filePath1)
array2 = imageToArray(filePath2)
image = Image.new("RGB",(50,50),black)
image.putdata(compare(array1, array2))
image.show()
