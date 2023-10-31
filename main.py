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
for index, code_line in enumerate(parsed_gsa_file):
    code_vars = execute(code_line, code_vars)