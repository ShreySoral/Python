import PyPDF2
readpdf=PyPDF2.PdfFileReader(open('file.pdf','rb'))
import pyttsx3
speaker=pyttsx3.init()
for pagenumber in range(readpdf.numPages):
    text=readpdf.getPage(pagenumber).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()
speaker.save_to_file(text,'audio.mp3')
speaker.runAndWait()