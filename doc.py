from docx import  Document
import  re
 #选取题目 用正则表达式换掉题目中的答案 然后用变量保存答案作为判断依据

#题目类
class Topic:
    information="";
    answer="";
    option=""
    def __init__(self,information,answer,option):
        self.answer =answer
        self.information =information
        self.option=option
    def get_answer(self):
        return self.answer
    def get_information(self):
        return self.information
    def get_option(self):
        return self.option
    def show_Topic(self):
        print("题目:  "+ self.information)
        print("选项:  "+ self.option)
        print("答案:  "+ self.answer)

def getDocxContext(file):
    document = Document(file)
    fullText = []
    for context in document.paragraphs:
        fullText.append(context.text)
    return fullText


#有括号的都是题目 在碰到括号之前 的文本都作为答案
def clissfy():
    text = getDocxContext("E:\\Desktop\\kstk.docx")
    pattern = re.compile(r'[(|（]')      #题目的正则  。。写完才发现多余了因为偷懒了
    pattern_sub_num = re.compile('(.*?、)?')  #去掉题目前面标号的正则
    pattern_four = re.compile('[ABCDＡＢＣＤ].*?[ABCDＡＢＣＤ].*?[ABCDＡＢＣＤ].*?[ABCDＡＢＣＤ]') # 选项的正则   。。写完才发现多余了因为偷懒了  要补完有用，先留着
    pattern_sub_answer = re.compile('(（|[(]).*([)]|）)')     #去掉答案的正则
    pattern_save_answer = re.compile('[(（].*?([ABCD]).*?[)）]')  #选择答案的正则
    list =[]
    for i in range(0, len(text)-2,2):
        context = str(text[i])
        answer = pattern_save_answer.findall(context)
        answer ="".join(answer) #答案
        information = pattern_sub_num.sub("",context,1)       #去掉标号后的题目
        information = pattern_sub_answer.sub("( )",information)
        option = str(text[i+1]) #选项
        list.append(Topic(information,answer,option))
    return  list
def main():
    list = clissfy()
    for i in list:
        i.show_Topic()
main()
