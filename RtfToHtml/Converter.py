import sys
import os,os.path
import comtypes.client
pdf_list = []

wdFormatPDF = 17

input_dir = r'C:\Users\kabil\Documents\pycharmprojects\RtfToHtml\input'
output_dir = 'C:\\Users\\kabil\\Documents\\pycharmprojects\\RtfToHtml\\output\\'

for subdir, dirs, files in os.walk(input_dir):
    for file in files:
        in_file = os.path.join(subdir, file)
        output_file = file.split('.')[0]
        out_file = output_dir+output_file+'.pdf'
        word = comtypes.client.CreateObject('Word.Application')

        doc = word.Documents.Open(in_file)
        doc.SaveAs(out_file, FileFormat=wdFormatPDF)
        doc.Close()
        word.Quit()
        pdf_list.append(out_file)



for i in range(len(pdf_list)):
	command = 'pdf2txt.py -o output'+str(i)+'.html -t html '+pdf_list[i]
	os.system(command)