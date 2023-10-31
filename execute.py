import re

def execute(code_line, vars = {}):
    # 각 줄이 저장됨. {type: 명령 타입, text: 코드 내용,line: 줄 번호}
    # 주석 0
    # 변수 선언 1
    # 입출력 2
    # 연산 3
    # 코드 시작 4
    # 코드 끝 5
    code = code_line["text"]
    if code_line["type"] == 0:
        return vars
    elif code_line["type"] == 1:
        # (숫자)호 (변수이름) 사감실로 오시기 바랍니다.
        # "(문자열)"한 (변수이름) 사감실로 오시기 바랍니다.
        if code.startswith('"'):
            string = re.search(r'"([^"]*)"', code)
            if string:
                vars[code.split(" ")[-4]] = string.group(1)
        else:
            vars[code.split(" ")[1]] = float(code.split(" ")[0][:-1])
        return vars
    elif code_line["type"] == 2:
        # (변수이름) 퇴사.
        # (변수이름) 너 뭐야.
        if code.endswith("퇴사."):
            if code.find("넘어갈 생각 말고") != -1:
                print(vars[code.split(" ")[0]], end="")
            else:
                print(vars[code.split(" ")[0]])
        elif code.endswith("너 뭐야."):
            temp_var_name = code.split(" ")[0]
            temp_var = input()
            vars[temp_var_name] = temp_var
        return vars
    elif code_line["type"] == 3:
        if code.endswith("로 이방하지마."):
            if code.split(" ")[1].endswith("방으로"):
                vars[code.split(" ")[0][0:-1]] = vars[code.split(' ')[0][0:-1]] + vars[code.split(" ")[1][0:-3]]
            else:
                vars[code.split(" ")[0][0:-1]] = vars[code.split(' ')[0][0:-1]] + vars[code.split(" ")[1][0:-2]]
        elif code.find("너 지금 이방만") != -1:
            vars[code.split(" ")[0][0:-1]] = vars[code.split(" ")[0][0:-1]] * float(code.split(" ")[4][0:-3])
        elif code.find("너 맨날") != -1:
            vars[code.split(" ")[0][0:-1]] = vars[code.split(" ")[0][0:-1]] * float(vars[code.split(" ")[3][0:-1]])
        return vars
    elif code_line["type"] == 4:
        return vars
    elif code_line["type"] == 5:
        return vars
