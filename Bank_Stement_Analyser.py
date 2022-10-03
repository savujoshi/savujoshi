from webbrowser import get
import PyPDF2
  

def main_function():
    # creating a pdf file object
    pdfFileObj = open('statement-34.pdf', 'rb')
    
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    
    # printing number of pages in pdf file
    # print("Number of pages:"+str(pdfReader.numPages))
    text = ""
    # creating a page object
    for pageNo in range(0, pdfReader.numPages):
        # print(pageNo)
        
        if pageNo != 1:
            pageObj = pdfReader.getPage(pageNo)
            print("\n")
            text = text + pageObj.extractText()
            
    
    # the main string split into the 2 parts using 2 key words "Statement Period" and "Statement date"
    Statement_period = (text.split("Statement Period")[1]).split("Statement date")[0]
    print("The Period of the statement is" +  Statement_period)

    Transactions = (text.split("Transactions since your last statement")[1]).split("If you have any questions about this")[0]
    



    # extracting text from page
    # print(pageObj.extractText())
    
    # closing the pdf file object
    pdfFileObj.close()






if __name__=='__main__':

    main_function()