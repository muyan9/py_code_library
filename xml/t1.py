import sys

print "Content-type:text/xml\n"

#write XML declaration and processing instruction
print """<?xml version = "1.0"?>
<?xml:stylesheet type = "text/xsl"
href = "name.xsl"?>"""

#open data file
try:
    file = open( "names.txt","r" )
except IOError:
    sys.exit( "Error opening file" )

print "<contacts>"  #write root element

#list of tuples:(special character,entity reference)
replaceList = [ ( "&", "&amp;" ),
                ( "<", "&lt;" ),
                ( ">", "&gt;" ),
                ( '"', "&quot;" ),
                ( "'", "&apos;" ) ]

#replace special characters with entity reference
for currentLine in file.readlines():

    for oldValue, newValue in replaceList:
        currentLine = currentLine.replace( oldValue, newValue )

    #extract lastname and firstname
    last, first = currentLine.split( "," )
    first = first.strip()   #remove carriage return

    #write contact element
    print """ <contact>
    <LastName>%s</LastName>
    <FirstName>%s</FirstName>
    </contact>""" % ( last, first )

file.close()

print "</contacts>"
