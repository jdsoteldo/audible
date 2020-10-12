import pyttsx3
import PyPDF2

book = open('py4e.pdf', 'rb')
reader = PyPDF2.PdfFileReader(book)
pages = reader.numPages
speaker = pyttsx3.init()

for num in range(12, pages):
    speaker.setProperty('rate', 200)
    startpage = reader.getPage(12)
    pageText = startpage.extractText()
    speaker.say(pageText)
    speaker.runAndWait()
