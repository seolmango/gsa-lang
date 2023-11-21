import re

def execute(code_line, index, vars = {}):
    # 각 줄이 저장됨. {type: 명령 타입, text: 코드 내용,line: 줄 번호}
    # 주석 0
    # 변수 처리 1
    # 입출력 2
    # 연산 3
    # 코드 시작 4
    # 코드 끝 5
    # 타입 변경 6
    code = code_line["text"].strip()
    if code_line["type"] == 0:
        return vars, index + 1
    elif code_line["type"] == 1:
        if code.endswith("사감실로 오시기 바랍니다."):
            # (숫자)호 (변수이름) 사감실로 오시기 바랍니다.
            # "(문자열)"한 (변수이름) 사감실로 오시기 바랍니다.
            if code.startswith('"'):
                string = re.search(r'"([^"]*)"', code)
                if string:
                    vars[code.split(" ")[-4]] = string.group(1)
            else:
                vars[code.split(" ")[1]] = float(code.split(" ")[0][:-1])
        elif code.endswith("이렇게 만들었어."):
            vars[code.split(" ")[2][:-1]] = vars[code.split(" ")[0][:-1]]
        return vars, index + 1
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
        return vars, index + 1
    elif code_line["type"] == 3:
        if code.endswith("로 이방하지마."):
            if code.split(" ")[1].endswith("방으로"):
                vars[code.split(" ")[0][0:-1]] = vars[code.split(' ')[0][0:-1]] + vars[code.split(" ")[1][0:-3]]
            else:
                vars[code.split(" ")[0][0:-1]] = vars[code.split(' ')[0][0:-1]] + float(code.split(" ")[1][0:-2])
        elif code.find("너 지금 이방만") != -1:
            vars[code.split(" ")[0][0:-1]] = vars[code.split(" ")[0][0:-1]] * float(code.split(" ")[4][0:-4])
        elif code.find("너 맨날") != -1:
            vars[code.split(" ")[0][0:-1]] = vars[code.split(" ")[0][0:-1]] * float(vars[code.split(" ")[3][0:-1]])
        return vars, index + 1
    elif code_line["type"] == 4:
        return vars, index + 1
    elif code_line["type"] == 5:
        return "EOF", index + 1
    elif code_line["type"] == 6:
        if code.endswith("너는 이방 횟수 계산도 못하니."):
            vars[code.split(" ")[0]] = str(vars[code.split(" ")[0]])
        elif code.endswith("너는 말이 말로 안들리니."):
            vars[code.split(" ")[0]] = int(vars[code.split(" ")[0]])
        elif code.endswith("수학처럼 국어도 공부해봐."):
            vars[code.split(" ")[0]] = chr(int(vars[code.split(" ")[0]]))
        elif code.endswith("국어도 수학이야."):
            temp = 0
            temp_string = vars[code.split(" ")[0]]
            for i in range(len(temp_string)):
                temp += ord(str(temp_string[i]))
            vars[code.split(" ")[0]] = temp
        return vars, index + 1
    elif code_line['type'] == 7:
        if_exp_res = False
        if_expression_count = code.count("?")
        if_expression = code.split("?")
        if_expression = list(map(lambda x: x.strip(), if_expression))
        for i in range(if_expression_count):
            multi_if_or = True
            if if_expression[i].startswith("그리고"):
                multi_if_or = False
                if_expression[i] = if_expression[i][4:]
            elif if_expression[i].startswith("또는"):
                if_expression[i] = if_expression[i][3:]
            if_expre = if_expression[i]
            if if_expre.endswith("호라고"):
                if_exp_res_temp = (vars[if_expre.split(" ")[0][:-2]] == int(if_expre.split(" ")[1][:-3]))
            elif if_expre.endswith("라고 했다고"):
                if_exp_res_temp = (vars[if_expre.split(" ")[0][:-1]] == str(if_expre.split(" ")[1][1:-3]))
            elif if_expre.endswith("랑 같은 짓을 했다고"):
                if_exp_res_temp = (vars[if_expre.split(" ")[0][:-1]] == vars[if_expre.split(" ")[1][:-1]])
            if multi_if_or:
                if_exp_res = if_exp_res or if_exp_res_temp
            else:
                if_exp_res = if_exp_res and if_exp_res_temp
        if_index = 0
        if if_exp_res:
            if_code_lines = code_line['true']
        elif not if_exp_res and not code_line['false'] == None:
            if_code_lines = code_line['false']
        else:
            if_code_lines = {}
        while if_index < len(if_code_lines):
            vars, if_index = execute(if_code_lines[if_index], if_index, vars)
        return vars, index+1