# -*- coding: utf-8 -*-
# 在文件末尾添加一个空行

def lines(file):
	for line in file:
		yield line
	yield '\n'

# 文本块生成器，得到一个文本块的生成器
def blocks(file):
	block = []
	for line in lines(file):
		if line.strip():
			block.append(line)
		elif block:
			yield ''.join(block).strip()
			block = []


