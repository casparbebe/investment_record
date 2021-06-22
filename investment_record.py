import os # operating system

# 讀取檔案
def read_file(filename):
	records = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '買入日期,股票代號,買入價格,股數,手續費,淨收付,,賣出日期,股票代號,賣出價格,交易股數,手續費,淨收付,淨賺美金,淨賺台幣,報酬率' in line:
				continue
			date1, code_name1, price1, quantity1, handling_charge1, net_income1, space, date2, code_name2, price2, quantity2, handling_charge2, net_income2, USD, NTD, ROI = line.strip().split(',')
			records.append([date1, code_name1, price1, quantity1, handling_charge1, net_income1, space, date2, code_name2, price2, quantity2, handling_charge2, net_income2, USD, NTD, ROI])
	print(records)

	return records


# 輸入交易紀錄
def user_input(records):
	while True:
		date1 = input('請輸入買入日期: ')
		if date1 == 'q':
			break
		code_name1 = input('請輸入股票代號: ')
		price1 = input('請輸入買入價格:  ')
		quantity1 = input('請輸入交易股數: ')
		handling_charge1 = input('請輸入手續費: ')
		net_income1 = input('請輸入淨收付: ')

		date2 = input('請輸入賣出日期: ')
		if date2 == 'q':
			break
		code_name2 = input('請輸入股票代號: ')
		price2 = input('請輸入賣出價格: ')
		quantity2 = input('請輸入交易股數: ')
		handling_charge2 = input('請輸入手續費: ')
		net_income2 = input('請輸入淨收付: ')
		USD = input('請輸入淨賺美金: ')
		NTD = input('請輸入淨賺台幣: ')
		ROI = input('請輸入報酬率: ')
		records.append([date1, code_name1, float(price1), int(quantity1), handling_charge1, float(net_income1)
			, date2, code_name2, float(price2), int(quantity2), handling_charge2, float(net_income2), float(USD), float(NTD), float(ROI)])

	return records
	print(records)

def print_records(records):
    for record in records:
        print(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12], record[13], record[14])


# 建立檔案並寫入
def write_file(filename, records): 
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('買入日期,股票代號,買入價格,股數,手續費,淨收付,,賣出日期,股票代號,賣出價格,交易股數,手續費,淨收付,淨賺美金,淨賺台幣,報酬率\n')
		for r in records:
			f.write(r[0] + ',' + r[1] + ',' + str(r[2]) + '元' + ',' + str(r[3]) + '股' + ',' + r[4] + ',' + str(r[5]) + '美元' + ',' + ','
			  + r[6] + ',' + r[7] + ',' + str(r[8]) + '元' + ',' + str(r[9]) + '股' + ',' + r[10] + ',' + str(r[11]) + '美元' + ',' +
			 str(r[12]) + '美金' + ',' + str(r[13]) + '元' + ',' + str(r[14]) + '%' + '\n')

def main():
	filename = 'investment_records.csv'
	if os.path.isfile(filename):
		print('找到檔案了')
		records = read_file(filename)
	else:
		records = []
		print('檔案不存在')
	print_records(records)
	records = user_input(records)
	write_file(filename, records)


main()