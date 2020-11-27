import os
from lxml import etree

#把列表字典写入excel，每行是列表元素，每列是字典
def excelout(list_dic,title,path,filename):
	import xlsxwriter
	workbook = xlsxwriter.Workbook(path + filename)
	worksheet = workbook.add_worksheet('My Worksheet')

	for i in range(len(title)):
		worksheet.write(0,i,title[i])

	#excel_row是excel写入的起始行，row是list数据的每个子列表
	for row in range(len(list_dic)):	
		for col in range(len(title)):	
				worksheet.write(row+1,col,list_dic[row][title[col]])

	workbook.close()

resPath = __file__[:-11] 

inputPath = resPath + "/input.txt"
fo = open(inputPath, "r",encoding="utf-8")
t = fo.readlines()

ammFilePath = resPath + "/dmrl/"

shema_file = t[0]

# shema_file = "D:\\测试\\s1000d\\shema验证\\S1000D 4.1 Schema\\xml_schema_flat\\fault.xsd"

fileList =os.listdir(ammFilePath)
# shema_file = "C:\\winGit\\工作\\schema验证\\schema\\fault.xsd"
shema = etree.XMLSchema(etree.parse(shema_file))


list_dic = []   
for i in fileList:    
    task = ammFilePath + i
    data = etree.parse(task)
    shema.validate(data)
    if shema.validate(data) == False:
        for i in (shema.error_log):
            dic = {}
            dic["task"] = i.filename
            dic["path"] = i.path
            dic["message"] = i.message
            list_dic.append(dic)

filename = "fim_schemaTest.xlsx"
title =["task","path","message"]        
excelout(list_dic,title,resPath,filename)
