from xml.dom.minidom import Document

# Create the minidom document 
doc = Document()

# Create the  base element 
wml = doc.createElement("wml") 
doc.appendChild(wml) 

# Create the main  element
maincard = doc.createElement("card") 
maincard.setAttribute("id", "main") 
wml.appendChild(maincard)  

#Create aelement 
paragraph1 = doc.createElement("p") 
maincard.appendChild(paragraph1)  

# Give theelemenet some text 
ptext = doc.createTextNode("This is a test!") 
paragraph1.appendChild(ptext)  

# Print our newly created XML 
print doc.toprettyxml(indent=" 1 ") 