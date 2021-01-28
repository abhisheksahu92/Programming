import xml.etree.ElementTree as ET

class XML:

    def __init__(self,file):
        self.file = file
        self.parsed_file = ET.parse(file)
        self.root = self.parsed_file.getroot()
        
    def getChild(self):
        #List of only child tags
        for elem in self.root:
            return elem.tag,elem.attrib

    def getAlltags(self):
        #List of all child tags
        return [ele.tag for ele in self.root.iter()]

    def verifyTag(self,tag):
        try:
            if tag in self.getAlltags():
                return True
            else:
                raise ValueError(f'{tag} is not present')
        except ValueError as e:
            return e


    def getTagValue(self,tag):
        __list = []
        verified_tag = self.verifyTag(tag)
        if verified_tag == True:
            for element in self.root.iter(tag):
                __list.append(element.text)
            return __list
        else:
            return verified_tag


    def getAttribute(self,tag):
        #attribute for a tag
        __list = []
        verified_tag = self.verifyTag(tag)
        if verified_tag == True:
            for element in self.root.iter(tag):
                __list.append(element.attrib)
            return __list
        else:
            return verified_tag

if __name__ == "__main__":
    xml_object = XML('sample.xml')
    print(xml_object.getChild())
    print(xml_object.getAlltags())
    print(xml_object.getAttribute('movie'))
    print(xml_object.getAttribute('abhi'))
    print(xml_object.getTagValue('description'))
    

    

    

    