from PIL import Image
import base64

class Message:

    def __init__(self, **kwargs):
        self.in_args = []
        self.in_name = []

        #print (sorted(kwargs))

        # get the key and values for input arguments
        for name in sorted(kwargs):
            self.in_args.append(kwargs[name])
            self.in_name.append(name)

        # check to see if user specified a filepath, that he also specified an image type
        if self.in_name[0] == 'filePath':
            if len(self.in_name) != 2:
                raise ValueError('Need two arguments <filePath> , <messageType> if not using XmlString')

            # if there are correct number of arguments for first case of initialization    
            self.filePath = self.in_args[0]
            self.messageType = self.in_args[1]

            # if it is a GrayImage
            if self.messageType is 'GrayImage':
                self.encoded, self.XmlString = self.file_to_xml(self.in_args[0], self.in_args[1])

            # if it is a ColorImage
            if self.messageType is 'ColorImage':
                self.encoded, self.encoded_red, self.encoded_green, self.encoded_blue, self.XmlString = self.file_to_xml(self.in_args[0], self.in_args[1])

            # check to see if messageType is valid
            if(self.messageType is not 'Text' and self.messageType is not 'GrayImage' and self.messageType is not 'ColorImage'):
                raise ValueError('messageType must be Text, GrayImage, ColorImage')
    
        # if user specified an XmlString, there is only one argument
        if self.in_name[0] == 'XmlString':
            if len(self.in_name) != 1:
                raise ValueError('If using XmlString, only supply one argument: XmlString')

            # if there are correct number of arguments for second case if initialization
            self.XmlString = self.in_args[0]

        # check to see that there is correct number of arguments
        #print(self.in_name[0])
        if len(self.in_name) > 2 or len(self.in_name) < 1 or (self.in_name[0] != 'XmlString' and self.in_name[0] != 'filePath'):
            raise ValueError("Usage: Message('filePath = <path>, messageType = <Text, GrayImage or ColorImage>') or Message('XmlString = <xmlstring>')")

        

    def getMessageSize(self):
        
        image = Image.open(self.filePath)
        # if message is GrayImage
        if self.messageType is 'GrayImage':
            return len(list(image.getdata()))
        
        # if message is ColorImage
        if self.messageType is 'ColorImage':
            return len(list(image.getdata())) * 3

        return len(self.XmlString)

    def getXmlString(self):
        # if message is not xml
        if self.in_name[0] == 'filePath':
            if self.encoded == '':
                raise Exception("No image data")             
            return self.XmlString

        # if message is xml
        if self.in_name[0] == 'XmlString':
            if self.XmlString == '':
                raise Exception("No image data")
            return self.XmlString

    def saveToImage(self, targetImagePath):

        # if the message is an image
        if self.messageType is not 'Text':
            if self.messageType is 'GrayImage':
                #print(base64.b64decode(self.encoded))
                data = base64.b64decode(self.encoded)
                #print(data)
                gray_image = Image.frombytes('L',(self.width, self.length), data)
                #gray_image.show()
                #print(self.encoded)
            # if the message is a ColorImage, we need to rejoin the bands 
            if self.messageType is 'ColorImage':
                
                # change the individual bands back to integer list
                red_data = list(bytearray(base64.b64decode(self.encoded_red)))
                green_data = list(bytearray(base64.b64decode(self.encoded_green)))
                blue_data = list(bytearray(base64.b64decode(self.encoded_blue)))
                
                # join them together
                data = []
                for i in range(len(red_data)):
                    data.append((red_data[i], green_data[i], blue_data[i]))

                #print(data[0:10])
                color_image = Image.new('RGB', (self.width, self.length))
                color_image.putdata(data)
                #color_image = Image.frombytes('RGB' , (self.width, self.length), data)
                #color_image.show()


    def saveToTextFile(self, targetTextFilePath):
        print('hi')

    def saveToTarget(self, targetPath):

        # invoke proper saving function, based on message type
        if self.messageType is 'Text':
            self.saveToTextFile(targetPath)
        else:
            self.saveToImage(targetPath)

    def file_to_xml(self, filePath, messageType):
        
        # perform the raster scan
        image = Image.open(filePath)

        # if the image is text
        if messageType is 'Text':
            print('hi')

        # if the image is not text
        else:

            # get the dimensions of the image
            right, lower = image.size
            self.width = right
            self.length = lower

            # perform the raster scan
            self.img_bytes = list(image.getdata())
            #print(self.img_bytes[0:10])
            
            ## change the scan to base 64
            
            # if its a GrayImage
            if self.messageType is'GrayImage':
                self.img_bytes64 = str(base64.b64encode(bytes(self.img_bytes)))[2:-1]            

                # write message in to xml string
                xml_string = '<?xml version="1.0" encoding="UTF-8"?>\n<message type="' + messageType + '" size="' + str(right) + ',' + str(lower) + '" encrypted="False">\n' + self.img_bytes64 + '\n</message>'
                open('testxml.xml', 'w').write(xml_string)

                return (self.img_bytes64, xml_string)

            # if its a ColorImage
            if self.messageType is 'ColorImage':

                # get the red, green , and blue channels
                self.red, self.green, self.blue = zip(*self.img_bytes)
                red_bytes64 = str(base64.b64encode(bytes(self.red)))[2:-1]
                green_bytes64 = str(base64.b64encode(bytes(self.green)))[2:-1]
                blue_bytes64 = str(base64.b64encode(bytes(self.blue)))[2:-1]

                # encoding is in order of red, green, blue
                img_bytes64 = red_bytes64 + green_bytes64 + blue_bytes64
                xml_string = '<?xml version="1.0" encoding="UTF-8"?>\n<message type="' + messageType + '" size="' + str(right) + ',' + str(lower) + '" encrypted="False">\n' + img_bytes64 + '\n</message>'
                open('testxml.xml', 'w').write(xml_string)

                return (img_bytes64, red_bytes64, green_bytes64, blue_bytes64, xml_string)
            return('', '')

class Steganography:

    def __init__(self, imagePath, direction='horizontal'):
        
        # check class initialization variables
        if type(imagePath) is not str or type(direction) is not str:
            raise ValueError('Usage: Steganography(imagePath = "string of imagePath", direction = "horizontal or vertical")')        

        # initialize class variables
        self.imagePath = imagePath
        self.direction = direction

        # open the image
        self.image = Image.open(imagePath)

        # check if medium is grayscale
        if self.image.mode is not 'L':
            raise TypeError('Image needs to be a grayscale image')

        # max image size is total number of pixels divided by 8
        self.width, self.height = self.image.size
        self.maxMessageSize = ((self.width*self.height)/8)



    def embedMessageInMedium(self, message, targetImagePath):

        # check if the medium can hold the message
        if message.getMessageSize() > self.maxMessageSize:
            raise ValueError("message size is too big for medium to hold")

        # get the byte values of the medium image as a list
        medium_bytes = list(self.image.getdata())
        
        # convert the xml string to a byte representation and convert it to a list of byte values
        message_bytes = "b'" + message.XmlString + "'"        
        message_bytes = list(bytearray(message_bytes, 'utf-8'))

        print(medium_bytes[90:100])
        if self.direction is 'vertical':
            vertical_bytes = []
            for i in range(self.width):
                vertical_bytes = vertical_bytes + medium_bytes[i::self.width]

            
        print(len(medium_bytes))
        # initialize variables for loop, j indexes through the message list 
        j = -1
        n = 0
        
        # set the first bit of each medium byte to be the corresponding bit of the message byte
        # each message byte will modify 8 medium bits
        # loop selects bit of message to check with by ANDing with a mask
        for i in range(len(medium_bytes)):
            n = 7 if n is 0 else n - 1
            j = j + 1 if n is 7 else j
            try:
                medium_bytes[i] = medium_bytes[i] | 1 if message_bytes[j] & 2**n else medium_bytes[i] & 254
            except:
                pass
            finally:
                pass

        print(vertical_bytes[90:100])        
        if self.direction is 'vertical':
            medium_bytes = []
            for i in range(self.height):
                medium_bytes = medium_bytes + vertical_bytes[i::self.height]
        print(medium_bytes[90:100])
            

        #print(medium_bytes[90:100])
            
        # set class variable to contain the modified original image
        self.stego_image = message_bytes
        
        gray_image = Image.new('L', (self.width, self.height))
        gray_image.putdata(medium_bytes)
        #gray_image.show()
        gray_image.save(targetImagePath)
        #print(medium_bytes[0:32])

            

            

def main():
    print("hi")
    myMessage = Message(filePath = "Phase1_tests/files/color_mona.png", messageType = "ColorImage")
    #myMessage.getMessageSize()
    #myMessage.getXmlString()
    #myMessage = Message(filePath = "Phase1_tests/files/bridge.png", messageType = "GrayImage")
    myMessage2 = Message(XmlString = "xml")
    #print(myMessage.getXmlString())
    myMessage.saveToImage('saved.png')
    mySteg = Steganography('Phase1_tests/files/bridge.png', 'vertical')
    mySteg.embedMessageInMedium(myMessage, 'testimageembed.png')

if __name__ == "__main__":
    main()