from docx import  Document
import  re
 #选取题目 用正则表达式换掉题目中的答案 然后用变量保存答案作为判断依据

#题目类
class Topic:
    num ="";
    information="";
    answer="";
    option=""
    def __init__(self,num,information,answer,option):
        self.num = num
        self.answer =answer
        self.information =information
        self.option=option
    def get_answer(self):
        return self.answer
    def get_information(self):
        return self.information
    def get_num(self):
        return self.num
    def get_option(self):
        return self.option

#获取答案
# def regex_get_answer():


def getDocxContext(file):
    document = Document(file)
    fullText = []
    for context in document.paragraphs:
        fullText.append(context.text)
    return fullText


#有括号的都是题目 在碰到括号之前 的文本都作为答案
def clissfy():
    text = getDocxContext("E:\\Desktop\\kstk.docx")
    pattern = re.compile(r'[(|（]')      #题目的正则
    pattern_four = re.compile('[ABCDＡＢＣＤ].*?[ABCDＡＢＣＤ].*?[ABCDＡＢＣＤ].*?[ABCDＡＢＣＤ]') # 选项的正则  偷懒只选择一行四个的
    pattern_sub_num = re.compile('(.*?、?)')  #去掉前面标号的正则
    # pattern_sub_answer = re.compile('(（|[(]).*([)]|）)')     #去掉答案的正则
    pattern_save_answer = re.compile('[(（].*?([ABCD]).*?[)）]')  #选择答案的正则
    for i in range(0, len(text)):
        if (pattern.findall(text[i])):
            context = str(text[i])
            context = pattern_sub_num.sub("",context)
            context = pattern_save_answer.findall(context)
            # context = pattern_select_answer.match(context)
            # context = pattern_sub_answer.sub("( )",context)
            print(context)



def main():
    clissfy()

main()
