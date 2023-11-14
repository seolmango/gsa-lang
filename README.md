# GSA-Lang

GSA-Lang은 강력한 라이브러리가 없고 복잡하고 직관적이지 않은 프로그래밍 언어입니다. 
그러나 광곽(Gwangju Science Academy, GSA) 학생들은 평소 자연스럽게 접하는 언어들로 구성되어 있어,
 ~~쉽고~~어렵고 ~~간편하게~~복잡하게 ~~다양한~~ 쓸 곳도 없는 프로그래밍이 가능합니다.

GSA-Lang은 ***읽기 쉬운 코드보단, 읽기 찰진 코드***라는 철학을 가지고 개발되고 있습니다.

## 사용방법

이 repo의 코드를 clone 한 뒤 gsa 파일을 작성하세요. 아래는 예시 gsa 파일입니다.

```gsa
test.gsa

사감실에서 알립니다.
12호 설망고 사감실로 오시기 바랍니다.
설망고 퇴사.
설망고! 설망고방으로 이방하지마.
설망고 퇴사.
"문자열을 입력하세요 > "한 삽동부 사감실로 오시기 바랍니다.
삽동부 넘어갈 생각 말고 퇴사.
설망고 너 뭐야.
설망고 퇴사.
소등하고 취침하기 바랍니다.
```

이후 

```bash
python main.py test.gsa
```

를 통해 파일을 실행하세요. 아래는 예시 결과입니다.

```bash
C:\Example\gsa-lang>python main.py test.gsa
12.0
24.0
문자열을 입력하세요 > 12
12
```

더 많은 예시를 확인하려면 [예시 폴더](examples)을 참고하세요.

이제 GSA-Lang을 이용하여 **유한한** 프로그래밍을 즐기세요!

## 문법

### 기본 숙지 사항

1. 모든 gsa 코드의 시작은 "**사감실에서 알립니다.**"로 시작해야 합니다.
2. 모든 gsa 코드의 끝은 "**소등하고 취침하기 바랍니다.**"로 끝나야 합니다.
3. 모든 gsa 코드는 **줄넘김**을 통해 구분됩니다.
4. 모든 gsa 코드의 각 줄은 **마침표('.')** 로 끝나야 합니다. 만약 마침표가 없다면 그 줄은 실행되지 않습니다.
5. 주석은 따로 없습니다. 위의 4번을 응용하여 _마침표를 찍지 않으면 그 줄은 주석이 됩니다._
6. 변수의 이름은 사람의 이름으로 짓는 것을 권장합니다. ~~그래야 찰집니다.~~
7. 들여쓰기는 스페이스 한개로 합니다. Tab이 아닙니다.

### 변수

1. 숫자는 **'(숫자)호'** 로 표현합니다.
2. 문자는 **'"(문자)"한'** 으로 표현합니다.

#### 변수 선언

변수를 선언할 때는 아래와 같이 적습니다.

```gsa
(값) (변수이름) 사감실로 오시기 바랍니다.
```

아래는 예시입니다.

```gsa
숫자 39를 변수 설망고에 대입한다
39호 설망고 사감실로 오시기 바랍니다.

문자 Hello World를 변수 설망고에 대입한다
"Hello World"한 설망고 사감실로 오시기 바랍니다.
```

#### 타입 변경

타입 변경은 아래와 같이 합니다.

```gsa
변수 설망고를 문자열로 변경한다
설망고 너는 이방 횟수 계산도 못하니.

변수 설망고를 숫자로 변경한다
설망고 너는 말이 말로 안들리니.
```

유니코드 변환은 아래와 같이 합니다.

> **주의**
>
> 문자열을 숫자로 유니코드 변환하는 경우, 문자열의 각 문자들의 **숫자를 모두 더한 결과**를 반환합니다.

```gsa
변수 설망고에 99를 대입한다
99호 설망고 사감실로 오시기 바랍니다.

설망고에 대입된 99를 유니코드로 바꾸어 출력한다
설망고 수학처럼 국어도 공부해봐.
c가 출력된다
설망고 퇴사.

변수 설망고에 문자열 "c+"를 대입한다
"c+"한 설망고 사감실로 오시기 바랍니다.

설망고에 대입된 "c+"를 바꾸어 출력한다
설망고 국어도 수학이야.
142(99+43)이 출력된다
설망고 퇴사.

소등하고 취침하기 바랍니다.
```

#### 변수 복사

변수를 복사하려면 아래와 같이 작성한다. 복사된 변수는 타입, 값이 모두 같다.

```gsa
변수 설망고를 삽동부로 복사한다
설망고! 너가 삽동부(을/를) 이렇게 만들었어.
```

### 연산

1. 덧셈

```gsa
변수 설망고에 변수 삽동부를 더한다
설망고! 삽동부방으로 이방하지마.

변수 설망고에 숫자 39를 더한다
설망고! 39호로 이방하지마.
```

2. 곱셈

```gsa
변수 설망고에 숫자 39를 곱한다
설망고! 너 지금 이방만 39번째야.

변수 설망고에 변수 삽동부를 곱한다
설망고! 너 맨날 삽동부랑 이방하지.
```

### 입출력

1. 입력

```gsa
변수 설망고에 사용자가 입력한 값을 대입한다
설망고 너 뭐야.
```

2. 출력

```gsa
변수 설망고를 출력한다
설망고 퇴사.

줄넘김없아 변수 설망고를 출력한다
설망고 넘어갈 생각 말고 퇴사.
```

### 흐름 제어

#### 조건문

변수와 숫자를 비교할 때는 아래와 같이 작성합니다.

```gsa
설망고 너 뭐야.
"사실입니다"한 삽동부 사감실로 오시기 바랍니다.
"거짓입니다"한 김광곽 사감실로 오시기 바랍니다.
"프로그램 종료"한 박광곽 사감실로 오시기 바랍니다.

설망고 너는 말이 말로 안들리니.
변수 설망고와 39가 같은지 비교한다
설망고방이 39호라고? 이게 사실이면.
 삽동부 퇴사.
근데 아니면.
 김광곽 퇴사.


박광곽 퇴사.
소등하고 취침하기 바랍니다.
```

변수와 문자열을 비교할 때는 아래와 같이 작성합니다.

```gsa
설망고 너 뭐야.
"사실입니다"한 삽동부 사감실로 오시기 바랍니다.
"거짓입니다"한 김광곽 사감실로 오시기 바랍니다.
"프로그램 종료"한 박광곽 사감실로 오시기 바랍니다.

변수 설망고와 문자열 "안녕하세요"가 같은지 비교한다
설망고가 "안녕하세요"라고 했다고? 이게 사실이면.
 삽동부 퇴사.
근데 아니면.
 김광곽 퇴사.


박광곽 퇴사.
소등하고 취침하기 바랍니다.
```

변수끼리 비교할 때는 아래와 같이 작성합니다.

```gsa
설망고 너 뭐야.
추석망고 너 뭐야.
"사실입니다"한 삽동부 사감실로 오시기 바랍니다.
"거짓입니다"한 김광곽 사감실로 오시기 바랍니다.
"프로그램 종료"한 박광곽 사감실로 오시기 바랍니다.

변수 설망고와 변수 추석망고가 같은지 비교한다
설망고가 추석망고랑 같은 짓을 했다고? 이게 사실이면.
 삽동부 퇴사.
근데 아니면.
 김광곽 퇴사.

박광곽 퇴사.
소등하고 취침하기 바랍니다.
```

#### if문

if문은 아래와 같이 작성합니다. if문을 작성할 때는 주의할 점은 들여쓰기를 해야한다는 점입니다.

```gsa
(조건문)? 이게 사실이면.
 (참이면 실행할 코드)
근데 아니면.
 (거짓이면 실행할 코드)
```

## 버전 정보

### 0.0.1

1. 기본적 기틀 마련
2. 변수 선언, 입출력, 연산 구현
3. 문법 문서화

### 0.0.2

1. 타입 변경 추가
2. 유니코드 변환 추가
3. 변수 복사 추가
4. repo에 예시 코드 추가

### 0.1.0

1. if문 추가
2. goto 문 삭제

## 기여하기

1. PR은 언제든 환영입니다.
2. 새로운 문법을 제안하시려면 issue를 남겨주세요.

## 라이센스

GSA-Lang은 GSA 라이센스를 따릅니다. 자세한 내용은 [LICENSE](LICENSE)를 참고하세요.