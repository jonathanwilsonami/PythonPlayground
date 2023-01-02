import re
import xml.etree.ElementTree as ET
import os

tree = ET.parse(cwd+'/DataFiles/astroXML.xml')
# print(type(tree))
root = tree.getroot()
# print(root)
#root.get('key') #returns val
#root.set('key', 'val')
#print(root.attrib) #return all atributes as dict
# tree.write(cwd+'/DataFiles/astroXML.xml') #save changes to xml file
# for c in root:
#     print(c.tag)
# print([elm.tag for elm in root.iter()])
# frameIds = []
# for frameId in root.findall("./frame/frameId"):
#     frameIds.append(frameId.text)

# print(len(frameIds))