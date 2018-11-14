import xlrd

workbook = xlrd.open_workbook('myfile2.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')
num_rows = worksheet.nrows - 1
curr_row = -1
column = 0
rEdge = False
count = 0 
while curr_row < num_rows:
        curr_row += 1
        valueStr = str(worksheet.cell(curr_row, column))
	value = float(valueStr[7:])
        print value
	if value > 0.1 and rEdge == False:
		rEdge = True 
		count += 1
	if value < 0.1 and rEdge == True:
		rEdge = False
	print("count is " + str(count))
	
