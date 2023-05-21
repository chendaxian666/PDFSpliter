#需要安装python库pdfplumber pypdf2，使用pip install 命令
#需要的pdf不能是扫描版，需要用finereader等pdf工具的ocr功能，转化为文字版pdf
#文件命名成ocr.pdf放在同级目录下

import pdfplumber
import PyPDF2
import os
 
#提取当前页文字
def extract_text_onepage (filepath):
 
    pdf = pdfplumber.open(filepath)
    page = pdf.pages[0]
    print(page.extract_words())
 
#删除目录
def del_files(path_file):
    ls = os.listdir(path_file)
    for i in ls:
        f_path = os.path.join(path_file, i)
        # 判断是否是一个目录,若是,则递归删除
        if os.path.isdir(f_path):
            del_files(f_path)
        else:
            os.remove(f_path)
 
 
if __name__ == '__main__':
    path = os.getcwd()  #获取当前的操作目录
    dpfpath = path + '\\ocr.pdf' #文件名
    resultpath = path + "\\result"
    if(os.path.exists(resultpath)):
        del_files(resultpath)
        os.rmdir(resultpath)
    os.mkdir("result",)
    origindpf = pdfplumber.open(dpfpath)
    # pdf_writer = PyPDF2.PdfWriter()  # 创建一个空白 PDF 对象
    pdf_reader = PyPDF2.PdfReader(dpfpath)  # 用来保存每一页pdf
    pdf = pdfplumber.open(dpfpath)   #用来读取字符

    for n in range(len(origindpf.pages)):
        
        page_obj = pdf_reader.pages[n]
        pdf_writer = PyPDF2.PdfWriter()  # 创建一个空白 PDF 对象
        pdf_writer.add_page(page_obj)  # 向空白 PDF 对象中添加要复制的 PDF页面
        page = pdf.pages[n]
        words = page.extract_words()
        name = '!'+"fail"+ str(n);
        for index in range(len(words)):
            if((words[index]['text'] == '姓名')& (index+1<len(words))):
                name = words[index+1]['text']
        pdfnewpath = resultpath + '\\' + name + '.pdf'
        pdf_new_file = open(pdfnewpath, 'wb')  # 创建一个新文件
        pdf_writer.write(pdf_new_file)  # 将添加了内容的空白 PDF 对象，写入到新建文件中
        pdf_new_file.close()
    

