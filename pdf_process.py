import glob
import fitz  # 导入本模块需安装pymupdf库
import os
#pip3 install fitz -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
#pip3 install PyMuPDF -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

# 将文件夹中所有jpg图片全部转换为一个指定名称的pdf文件，并保存至指定文件夹
def pic2pdf_1(img_path, pdf_path, pdf_name):
    doc = fitz.open()
    for img in sorted(glob.glob(img_path + "\*.jpg")):
        imgdoc = fitz.open(img)
        pdfbytes = imgdoc.convert_to_pdf()
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insert_pdf(imgpdf)
    doc.save(os.path.join(pdf_path, pdf_name))
    doc.close()

# 将文件夹中指定jpg图片转换为指定名称的pdf文件，并保存至指定文件夹
def pic2pdf_2(img_path, pdf_path, img_list, pdf_name):
    doc = fitz.open()
    pic_list = [img_path+i for i in img_list]
    for img in sorted(pic_list):
        imgdoc = fitz.open(img)
        pdfbytes = imgdoc.convertToPDF()
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insert_pdf(imgpdf)
    doc.save(os.path.join(pdf_path, pdf_name))
    doc.close()

# 将文件夹中所有jpg图片分别转换为同一名称的pdf文件，并保存至指定文件夹

def pic2pdf_3(img_path, pdf_path):

    for img in glob.glob(img_path + "\*.jpg"):
        file_name = os.path.basename(img).replace('jpg', 'pdf')
        doc = fitz.open()
        imgdoc = fitz.open(img)
        pdfbytes = imgdoc.convertToPDF()
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insert_pdf(imgpdf)
        doc.save(pdf_path + '\\' + file_name) 
        doc.close()


if __name__ == '__main__':

    # img_path = r'C:\Users\Wu-Junyan\OneDrive\文档\huh\IP\WDFS\temp'
    # pdf_path = r'C:\Users\Wu-Junyan\Desktop\WDFS'
    # pdf_name = r'WDFS.pdf'
    # pic2pdf_1(img_path=img_path, pdf_path=pdf_path, pdf_name=pdf_name)
    path=r"C:\Users\Wu-Junyan\OneDrive\文档\huh\IP\WDFS\漫画"
    dirnames=os.listdir(path)
    for dn in dirnames:
        img_path = os.path.join(path,dn)
        pdf_path = r'C:\Users\Wu-Junyan\Desktop\WDFS'
        pdf_name = '%s.pdf'%dn
        pic2pdf_1(img_path=img_path, pdf_path=pdf_path, pdf_name=pdf_name)


    
    # img_path = r'E:\test\jpg'
    # pdf_path = r'E:\test\jpg'
    # pdf_name = r'1.pdf'
    # img_list1, pdf_name1 = [r'\001.jpg', r'\002.jpg'], r'\2.pdf'
    # pic2pdf_1(img_path=img_path, pdf_path=pdf_path, pdf_name=pdf_name)
    # pic2pdf_2(img_path=img_path, pdf_path=pdf_path, img_list=img_list1, pdf_name=pdf_name1)
    # pic2pdf_3(img_path=img_path, pdf_path=pdf_path)
