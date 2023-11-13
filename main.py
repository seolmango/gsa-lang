import sys
from parser import parser
from execute import execute

# 컴파일할 gsa 파일의 경로를 파라미터로 받는다.
gsa_file_path = sys.argv[1]

# gsa 파일을 읽어서 파싱한다.
with open(gsa_file_path, 'r', encoding='UTF-8') as f:
    gsa_file = f.read()

parsed_gsa_file = parser(gsa_file)

code_vars = {}
index = 0
while code_vars != "EOF":
    code_vars, new_index = execute(parsed_gsa_file[index], index, code_vars)
    index = new_index