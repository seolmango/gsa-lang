import sys

# 컴파일할 gsa 파일의 경로를 파라미터로 받는다.
gsa_file_path = sys.argv[1]

# gsa 파일을 읽어서 파싱한다.
with open(gsa_file_path, 'r', encoding='UTF-8') as f:
    gsa_file = f.read()

# 파싱한 gsa 파일을 컴파일한다.
line_data = gsa_file.split('\n')
code_var = {}
program_start = False
now_level = 0
now_line = 0

if line_data[0] != "사감실에서 알립니다.":
    raise Exception("파일 컴파일러를 지정할 수 없습니다.")

while line_data[now_line] != "소등하고 취침하기 바랍니다.":
    if line_data[now_line].endswith('.'):
        if line_data[now_line].find("사감실로 오시기 바랍니다") != -1:
            # 변수 선언
            # (변수 이름) 사감실로 오시기 바랍니다. ==> 변수에 0대입
            # (숫자)호 (뼌수이름) 사감실로 오시기 바랍니다. ==> 변수에 숫자 대입
            temp = line_data[now_line].split(' ')
            if temp[0][0:-1].isdigit() and len(temp) == 5:
                code_var[temp[1]] = int(temp[0][0:-1])
            elif len(temp) == 4:
                code_var[temp[0]] = 0
            now_line += 1
        elif line_data[now_line].find("로 이방") != -1:
            # 변수 덧셈
            temp = line_data[now_line].split(' ')
            if temp[1].endswith("호로"):
                code_var[temp[0][0:-1]] += int(temp[1][0:-2])
            else:
                code_var[temp[0][0:-1]] += code_var[temp[1][0:-1]]
            now_line += 1
        elif line_data[now_line].find("너 지금 이방만") != -1 or line_data[now_line].find("너 맨날") != -1:
            temp = line_data[now_line].split(' ')
            if line_data[now_line].find("번째야") != -1:
                code_var[temp[0][0:-1]] = int(temp[4][0:-4]) * code_var[temp[0][0:-1]]
            else:
                code_var[temp[0][0:-1]] = code_var[temp[3][0:-1]] * code_var[temp[0][0:-1]]
            now_line += 1
        elif line_data[now_line].find("입니다") != -1 or line_data[now_line].find("퇴사") != -1:
            # 입출력
            if line_data[now_line].find("입니다") != -1:
                # 입력
                # (기본값)반 (변수 이름)입니다.
                variable_name = line_data[now_line].split(' ')[1].split('입니다')[0]
                temp = input()
                if temp != '':
                    code_var[variable_name] = temp
                else:
                    code_var[variable_name] = int(str(line_data[now_line].split(' ')[0])[0:-1])
                now_line += 1
            else:
                # 출력
                # (변수 이름) 퇴사.
                variable_name = line_data[now_line].split(' ')[0]
                print(code_var[variable_name])
                now_line += 1
        else:
            now_line += 1
    else:
        now_line += 1