# importing required modules 
import PyPDF2 
    
# creating a pdf file object 
pdfFileObj = open('sample.pdf', 'rb') 
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
# printing number of pages in pdf file 
# print(pdfReader.numPages) 
pageDict={}
# creating a page object 
for x in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(x)
    pageDict[x] = pageObj.extract_text()
    

# Created dictionary with page numbers and text
# Now I need to map the audio to get amount of time spent on page
    
# closing the pdf file object 
pdfFileObj.close() 