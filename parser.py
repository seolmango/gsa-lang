def parser(file: str):
    fin_result = []
    code_start = False
    # 각 줄이 저장됨. {type: 명령 타입, text: 코드 내용,line: 줄 번호}
    # 주석 0
    # 변수 선언 1
    # 입출력 2
    # 연산 3
    # 코드 시작 4
    # 코드 끝 5
    # 타입 변경 6
    line_data = file.split('\n')
    for index, line in enumerate(line_data):
        if not code_start and not line == '사감실에서 알립니다.':
            continue
        elif line.endswith('.'):
            if line == "사감실에서 알립니다.":
                fin_result.append({'type': 4, 'text': line, 'line': index})
                code_start = True
            elif line.endswith("소등하고 취침하기 바랍니다."):
                fin_result.append({'type': 5, 'text': line, 'line': index})
                return fin_result
            elif line.endswith("사감실로 오시기 바랍니다."):
                fin_result.append({'type': 1, 'text': line, 'line': index})
            elif line.endswith("로 이방하지마."):
                fin_result.append({'type': 3, 'text': line, 'line': index})
            elif line.find("너 지금 이방만") != -1:
                fin_result.append({'type': 3, 'text': line, 'line': index})
            elif line.find("너 맨날") != -1:
                fin_result.append({'type': 3, 'text': line, 'line': index})
            elif line.endswith("퇴사."):
                fin_result.append({'type': 2, 'text': line, 'line': index})
            elif line.endswith("너 뭐야."):
                fin_result.append({'type': 2, 'text': line, 'line': index})
            elif line.endswith("너는 이방 횟수 계산도 못하니.") or line.endswith("너는 말이 말로 안들리니."):
                fin_result.append({'type': 6, 'text': line, 'line': index})
            elif line.endswith("수학처럼 국어도 공부해봐.") or line.endswith("국어도 수학이야."):
                fin_result.append({'type': 6, 'text': line, 'line': index})
            elif line.endswith("이렇게 만들었어."):
                fin_result.append({'type': 1, 'text': line, 'line': index})
            else:
                fin_result.append({'type': 0, 'text': line, 'line': index})
        else:
            fin_result.append({'type': 0, 'text': line, 'line': index})