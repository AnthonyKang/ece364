from PIL import Image
import base64
import re

class Message:

    def __init__(self, **kwargs):
        self.in_args = []
        self.in_name = []

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

            # if it is Text
            if self.messageType is 'Text':
                self.file_to_xml(self.in_args[0], self.in_args[1])

            # check to see if messageType is valid
            if(self.messageType is not 'Text' and self.messageType is not 'GrayImage' and self.messageType is not 'ColorImage'):
                raise ValueError('messageType must be Text, GrayImage, ColorImage')
    
        # if user specified an XmlString, there is only one argument
        if self.in_name[0] == 'XmlString':
            if len(self.in_name) != 1:
                raise ValueError('If using XmlString, only supply one argument: XmlString')

            # if there are correct number of arguments for second case for initialization
            self.XmlString = self.in_args[0]

            # get the message type from the xmlstring
            type_match = re.search(r'(type="(\w+)")', self.XmlString)
            self.messageType = type_match.groups()[1]

            # get the width and height if its a picture
            m = re.search(r'(size="(\d+),(\d+)")', self.XmlString)
            if m:
                self.width = m.groups()[1]
                self.height = m.groups()[2]
            
            # get the width and height if its just text
            m = re.search(r'(size="(\d+)")', self.XmlString)
            if m:
                self.text_length = len(m.groups()[1])
                

        # check to see that there is correct number of arguments
        #print(self.in_name[0])
        if len(self.in_name) > 2 or len(self.in_name) < 1 or (self.in_name[0] != 'XmlString' and self.in_name[0] != 'filePath'):
            raise ValueError("Usage: Message('filePath = <path>, messageType = <Text, GrayImage or ColorImage>') or Message('XmlString = <xmlstring>')")

        

    def getMessageSize(self):
        
        # if message is text
        if self.messageType is 'Text':
            return self.text_length
        else:
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
            if self.messageType == 'GrayImage':
                #print(base64.b64decode(self.encoded))
                if self.in_name[0] == 'XmlString':
                    m = re.match(r'(.*\n.*\n(.*)\n</message>)', self.XmlString)
                    
                    data = base64.b64decode(m.groups()[1])
                    #print(data[0:10])                   
                    #print(len(data))         
                    gray_image = Image.new('L', (int(self.width), int(self.height)))
                    #print(len(data))
                    gray_image.putdata(data)
                    gray_image.save(targetImagePath)
                else:
                    data = base64.b64decode(self.encoded)
                    '''
                except:
                    m = re.match(r'(.*\n.*\n(.*)\n</message>)', self.XmlString)
                    
                    data = base64.b64decode(m.groups()[1])
                    #print(data[0:10])                   
                    #print(len(data))         
                    gray_image = Image.new('L', (int(self.width), int(self.height)))
                    #print(len(data))
                    gray_image.putdata(data)
                    gray_image.save(targetImagePath)

                    return None
                    '''
                #print(data)           
                    gray_image = Image.frombytes('L',(self.width, self.height), data)
                    gray_image.show()
                
                    gray_image.save(targetImagePath)
            # if the message is a ColorImage, we need to rejoin the bands 
            if self.messageType == 'ColorImage':

                if self.in_name[0] == 'XmlString':

                    #extract the bands from the xml
                    red_data, green_data, blue_data = self.rgb_xml_extract()
                else:                
                    # change the individual bands back to integer list
                    red_data = list(bytearray(base64.b64decode(self.encoded_red)))
                    green_data = list(bytearray(base64.b64decode(self.encoded_green)))
                    blue_data = list(bytearray(base64.b64decode(self.encoded_blue)))
                    
                # join them together
                data = []
                for i in range(len(red_data)):
                    data.append((red_data[i], green_data[i], blue_data[i]))

                #print(data[0:10])
                color_image = Image.new('RGB', (int(self.width), int(self.height)))
                color_image.putdata(data)
                #color_image = Image.frombytes('RGB' , (self.width, self.length), data)
                #color_image.show()\
                color_image.save(targetImagePath)

    def rgb_xml_extract(self):
        m = re.match(r'(.*\n.*\n(.*)\n</message>)', self.XmlString)
        if m:
            rgb = list(base64.b64decode(m.groups()[1]))
            #print(len(rgb)/3)
            r = rgb[:int((len(rgb)/3))]
            g = rgb[int((len(rgb)/3)):int(len(rgb)*2/3)]
            b = rgb[int(len(rgb)*2/3):]
            return (r,g,b)


    def saveToTextFile(self, targetTextFilePath):
        
        outfile = open(targetTextFilePath, 'w')

        
        m = re.search(r'(\w+=*\n<)', self.XmlString)
        #print(m)
        #print(m.groups()[0][0:-2])
        #print(str(base64.b64decode((m.groups()[0][0:-2])))[2:-1].split('\\n'))
        output_string = str(base64.b64decode((m.groups()[0][0:-2])))[2:-1].split('\\n')
        if len(output_string) > 1:
            output_string = output_string[:-1]      
            for line in output_string:
                outfile.write(line + '\n')
        else:
            outfile.write(output_string[0])
        
        

    def saveToTarget(self, targetPath):

        # invoke proper saving function, based on message type
        print(self.messageType)
        if self.messageType == 'Text':
            self.saveToTextFile(targetPath)
        else:
            self.saveToImage(targetPath)

    def file_to_xml(self, filePath, messageType):
        
        # if the image is text
        if messageType == 'Text':
            input_file = open(filePath, 'r')
            self.text_bytes = list(bytearray(input_file.read(), 'utf-8'))
            self.text64 = base64.b64encode(bytes(self.text_bytes))
            self.text_length = len(input_file.read())
            #print(self.text64)

            self.XmlString = '<?xml version="1.0" encoding="UTF-8"?>\n<message type="' + messageType + '" size="' + str(self.text_length) + '" encrypted="False">\n' + str(self.text64)[2:-1] + '\n</message>'           
            #open('test_text.xml', 'w').write(self.XmlString)

        # if the image is not text
        else:

            # perform the raster scan
            image = Image.open(filePath)

            # get the dimensions of the image
            right, lower = image.size
            self.width = right
            self.height = lower

            # perform the raster scan
            self.img_bytes = list(image.getdata())
            #print(self.img_bytes[0:10])
            
            ## change the scan to base 64
            
            # if its a GrayImage
            if self.messageType =='GrayImage':
                self.img_bytes64 = str(base64.b64encode(bytes(self.img_bytes)))[2:-1]            

                # write message in to xml string
                xml_string = '<?xml version="1.0" encoding="UTF-8"?>\n<message type="' + messageType + '" size="' + str(right) + ',' + str(lower) + '" encrypted="False">\n' + self.img_bytes64 + '\n</message>'
                open('testxml.xml', 'w').write(xml_string)

                return (self.img_bytes64, xml_string)

            # if its a ColorImage
            if self.messageType == 'ColorImage':

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
        message_bytes = list(bytearray(message_bytes, 'utf-8'))[2:-1]

        #print(medium_bytes[90:100])
        if self.direction is 'vertical':
            vertical_bytes = []
            for i in range(self.width):
                vertical_bytes = vertical_bytes + medium_bytes[i::self.width]

            medium_bytes = vertical_bytes

        #print(len(medium_bytes))
        # initialize variables for loop, j indexes through the message list 
        j = -1
        n = 0
        print(message_bytes[0:2])
        print(medium_bytes[0:8])
        print(len(message_bytes))
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

        
        #print(vertical_bytes[90:100])        
        if self.direction is 'vertical':
            vertical_bytes = medium_bytes
            medium_bytes = []
            for i in range(self.height):
                medium_bytes = medium_bytes + vertical_bytes[i::self.height]
        #print(medium_bytes[90:100])
        print(message.messageType)

        #print(medium_bytes[90:100])
            
        # set class variable to contain the modified original image
        self.stego_image = medium_bytes
        
        gray_image = Image.new('L', (self.width, self.height))
        gray_image.putdata(medium_bytes)
        #gray_image.show()
        gray_image.save(targetImagePath)
        #print(medium_bytes[0:32])

    def extractMessageFromMedium(self):
        # Extracts the message from the medium
        # If data is valid, return an instance of the Message class
        # Otherwise, return None
        
        # get data from picture
        medium_bytes = list(self.image.getdata())

        if self.direction is 'vertical':
            vertical_bytes = []
            for i in range(self.width):
                vertical_bytes = vertical_bytes + medium_bytes[i::self.width]
            medium_bytes = vertical_bytes

        # extract message by getting the last bit of each set of 8 bytes and creating the message byte
        extracted_message = []
        #print(len(self.stego_image))
        for i in range(int(len(medium_bytes)/8)):
            message_byte = 0
            message_byte = message_byte + 128 if medium_bytes[i*8] & 1 else message_byte
            message_byte = message_byte + 64 if medium_bytes[i*8+1] & 1 else message_byte
            message_byte = message_byte + 32 if medium_bytes[i*8+2] & 1 else message_byte
            message_byte = message_byte + 16 if medium_bytes[i*8+3] & 1 else message_byte
            message_byte = message_byte + 8 if medium_bytes[i*8+4] & 1 else message_byte
            message_byte = message_byte + 4 if medium_bytes[i*8+5] & 1 else message_byte
            message_byte = message_byte + 2 if medium_bytes[i*8+6] & 1 else message_byte
            message_byte = message_byte + 1 if medium_bytes[i*8+7] & 1 else message_byte
            extracted_message.append(message_byte)
        print(len(extracted_message))
        

        # create a string of the extracted bytes
        extracted_message_string = ''.join(chr(byte) for byte in extracted_message)
        
        # search for the message in the string, the message could be shorter than all the extracted bytes
        m = re.match(r'(.*\n.*\n.*\n</message>)', extracted_message_string)
        
        # if the data is valid, return the Message, otherwise return None
        if m:           
            xml_string = m.groups()[0]
            open('xml_string_test', 'w').write(xml_string)
            #print(xml_string)
            #print(xml_string)

            # fuck why did i just do these 3 lines
            #type_match = re.search(r'(type="(\w+)")', xml_string)
            #message_type = type_match.groups()[1]
            
            return Message(XmlString = xml_string)
        else:
            return None



            

            

def main():
    #print("hi")
    myMessage = Message(filePath = "Phase1_tests/files/bridge_dog_h.png", messageType = "GrayImage")
    print(myMessage.getMessageSize())
    #myMessage3 = Message(filePath = "Phase1_tests/files/full.txt", messageType = "Text")
    #myMessage3.saveToTextFile('test_text_save.xml')
    #myMessage.getMessageSize()
    #myMessage.getXmlString()
    #myMessage = Message(filePath = "Phase1_tests/files/bridge.png", messageType = "GrayImage")
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<message type="Text" size="890" encrypted="False">TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNldGV0dXIgc2FkaXBzY2luZyBlbGl0ciwgIHNlZCBkaWFtIG5vbnVteSBlaXJtb2QgdGVtcG9yIGludmlkdW50IHV0IGxhYm9yZSBldCBkb2xvcmUgbWFnbmEgYWxpcXV5YW0gZXJhdCwgc2VkIGRpYW0gdm9sdXB0dWEuIEF0IHZlcm8gZW9zIGV0IGFjY3VzYW0gZXQganVzdG8gZHVvIGRvbG9yZXMgZXQgZWEgcmVidW0uIFN0ZXQgY2xpdGEga2FzZCBndWJlcmdyZW4sIG5vIHNlYSB0YWtpbWF0YSBzYW5jdHVzIGVzdCBMb3JlbSBpcHN1bSBkb2xvciBzaXQgYW1ldC4gTG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNldGV0dXIgc2FkaXBzY2luZyBlbGl0ciwgIHNlZCBkaWFtIG5vbnVteSBlaXJtb2QgdGVtcG9yIGludmlkdW50IHV0IGxhYm9yZSBldCBkb2xvcmUgbWFnbmEgYWxpcXV5YW0gZXJhdCwgc2VkIGRpYW0gdm9sdXB0dWEuIEF0IHZlcm8gZW9zIGV0IGFjY3VzYW0gZXQganVzdG8gZHVvIGRvbG9yZXMgZXQgZWEgcmVidW0uIFN0ZXQgY2xpdGEga2FzZCBndWJlcmdyZW4sIG5vIHNlYSB0YWtpbWF0YSBzYW5jdHVzIGVzdCBMb3JlbSBpcHN1bSBkb2xvciBzaXQgYW1ldC4gTG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNldGV0dXIgc2FkaXBzY2luZyBlbGl0ciwgIHNlZCBkaWFtIG5vbnVteSBlaXJtb2QgdGVtcG9yIGludmlkdW50IHV0IGxhYm9yZSBldCBkb2xvcmUgbWFnbmEgYWxpcXV5YW0gZXJhdCwgc2VkIGRpYW0gdm9sdXB0dWEuIEF0IHZlcm8gZW9zIGV0IGFjY3VzYW0gZXQganVzdG8gZHVvIGRvbG9yZXMgZXQgZWEgcmVidW0uIFN0ZXQgY2xpdGEga2FzZCBndWJlcmdyZW4sIG5vIHNlYSB0YWtpbWF0YSBzYW5jdHVzIGVzdCBMb3JlbSBpcHN1bSBkb2xvciBzaXQgYW1ldC4=\n</message>'
    myMessage2 = Message(XmlString = xml)
    #print(myMessage.getXmlString())
    myMessage.saveToImage('saved.png')
    mySteg = Steganography('Phase1_tests/files/nature_sunflower_h.png', 'horizontal')
    #mySteg.embedMessageInMedium(myMessage3, 'testimageembed.png')
    myMessage4 = mySteg.extractMessageFromMedium()
    #print(myMessage4.XmlString)
    myMessage4.saveToTarget('test_extract_text.png')
    #print('hi')

if __name__ == "__main__":
    main()