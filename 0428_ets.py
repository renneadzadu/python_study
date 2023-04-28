import xml.etree.ElementTree as ET
#import regex as re


tree= ET.parse('movies.xml')
root= tree.getroot()
print(root)
print(root.tag) #output is collection(root name)
print(root.attrib) # attribute = key value pair. root does not have attribute

for child in root:
    print(child.tag, child.attrib) # output genre {'category': 'Action'}, genre {'category': 'Thriller'}

#print([elem.tag for elem in root.iter()])
#print(ET.tostring(root, encoding='utf8').decode( 'utf8'))

for movie in root.iter("movie"):
    print(movie.attrib, movie.text)

for description in root.iter("description"):
    print(description.text)

for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(movie.attrib)

for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']..."):
    print(movie.attrib)

b2tf =root.find("./genre/decade/movie[@title='Back 2  the Future']")
print(b2tf)

b2tf.attrib["title"]= "Back to The Future"
print(b2tf.attrib)


for movie in root.findall("./genre/decade/movie"):
    print(movie.attrib)

#tree.write("movies.xml")

for movie in root.iter("movie"):
    print(movie.attrib, movie.text)


#for form in root.findall(" . / genre/ decade/movie/format"):
# Search for the commas in the format text
   # match = re.search(',' , form. text)
    #if match:
        #form. set('multiple' , 'Yes')
   # else:
       # form. set('multiple' ,'No')

