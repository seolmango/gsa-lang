def count_leading_spaces(s):
    count = 0
    for char in s:
        if char.isspace():
            count += 1
        else:
            break
    return count

def parser(file: str, option: bool = False):
    fin_result = []
    code_start = option
    # 각 줄이 저장됨. {type: 명령 타입, text: 코드 내용,line: 줄 번호}
    # 주석 0
    # 변수 선언 1
    # 입출력 2
    # 연산 3
    # 코드 시작 4
    # 코드 끝 5
    # 타입 변경 6
    # 조건문 7
    # while문 8
    line_data = file.split('\n')
    index = 0
    while index < len(line_data):
        line = line_data[index]
        if not code_start and not line == '사감실에서 알립니다.':
            index += 1
            continue
        elif line.endswith('.'):
            if line == "사감실에서 알립니다.":
                fin_result.append({'type': 4, 'text': line, 'line': index})
                code_start = True
                index += 1
            elif line.endswith("소등하고 취침하기 바랍니다."):
                fin_result.append({'type': 5, 'text': line, 'line': index})
                index += 1
                return fin_result
            elif line.endswith("사감실로 오시기 바랍니다."):
                fin_result.append({'type': 1, 'text': line, 'line': index})
                index += 1
            elif line.endswith("로 이방하지마."):
                fin_result.append({'type': 3, 'text': line, 'line': index})
                index += 1
            elif line.find("너 지금 이방만") != -1:
                fin_result.append({'type': 3, 'text': line, 'line': index})
                index += 1
            elif line.find("너 맨날") != -1:
                fin_result.append({'type': 3, 'text': line, 'line': index})
                index += 1
            elif line.endswith("퇴사."):
                fin_result.append({'type': 2, 'text': line, 'line': index})
                index += 1
            elif line.endswith("너 뭐야."):
                fin_result.append({'type': 2, 'text': line, 'line': index})
                index += 1
            elif line.endswith("너는 이방 횟수 계산도 못하니.") or line.endswith("너는 말이 말로 안들리니."):
                fin_result.append({'type': 6, 'text': line, 'line': index})
                index += 1
            elif line.endswith("수학처럼 국어도 공부해봐.") or line.endswith("국어도 수학이야."):
                fin_result.append({'type': 6, 'text': line, 'line': index})
                index += 1
            elif line.endswith("이렇게 만들었어."):
                fin_result.append({'type': 1, 'text': line, 'line': index})
                index += 1
            elif line.endswith("이게 사실이면."):
                code_level = count_leading_spaces(line)
                true_lines_start = index + 1
                true_lines_end = true_lines_start
                while true_lines_end < len(line_data) and count_leading_spaces(line_data[true_lines_end]) >= code_level+1:
                    true_lines_end += 1
                true_line_data = parser('\n'.join(line_data[true_lines_start:true_lines_end]),True)
                if line_data[true_lines_end].endswith("근데 아니면.") and count_leading_spaces(line_data[true_lines_end]) == code_level:
                    false_lines_start = true_lines_end + 1
                    false_lines_end = false_lines_start
                    while false_lines_end < len(line_data) and count_leading_spaces(line_data[false_lines_end]) >= code_level+1:
                        false_lines_end += 1
                    false_line_data = parser('\n'.join(line_data[false_lines_start:false_lines_end]),True)
                    fin_result.append({'type': 7, 'text': line, 'line': index, 'true': true_line_data, 'false': false_line_data})
                    index = false_lines_end
                else:
                    fin_result.append({'type': 7, 'text': line, 'line': index, 'true': true_line_data, 'false': None})
                    index = true_lines_end
            elif line.endswith("자꾸 했던 말 반복하게 할래."):
                code_level = count_leading_spaces(line)
                true_lines_start = index + 1
                true_lines_end = true_lines_start
                while true_lines_end < len(line_data) and count_leading_spaces(line_data[true_lines_end]) >= code_level+1:
                    true_lines_end += 1
                true_line_data = parser('\n'.join(line_data[true_lines_start:true_lines_end]),True)
                fin_result.append({'type': 8, 'text': line, 'line': index, 'true': true_line_data})
                index = true_lines_end
            else:
                fin_result.append({'type': 0, 'text': line, 'line': index})
                index += 1
        else:
            fin_result.append({'type': 0, 'text': line, 'line': index})
            index += 1
    if option:
        return fin_result