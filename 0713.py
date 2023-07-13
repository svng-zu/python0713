# msg = "Korea"
#
# print(msg[::]) #전체
# print(msg[:-1:]) #뒤에서 첫번째 앞까지
# print(msg[::-1]) #뒤에서 부터 출력

# a = 10
# #a = 10 의 형태로 문자열 만들기
# s = "a = %d"%(a) #메모리 내에 원본을 남겨놓지 않게 됨.
# print(s)
#
# s = "a = {0:d}".format(a)
# print(s)

#gccg 문자열 위치 전부 찾아보기
#이미 찾은건 제외하고 찾아야함.
# gc = "gccgccgsgccgccgccgjcgccgcgdcjha"
# ar = gc.replace("gccg", "!!!!")
# idx = []
# aa = '!!!!'
# for i in range(0,len(ar)) :
#     if ar[i:i+4] == aa :
#         idx.append(i)
#
#
# print(idx)
# print(ar)



# import re
# # : 이나 | 를 , 로 치환
#
# testStr = "apple:samsung google|kakao"
# Str = re.sub("[:|]", ",",testStr) #replace 함수는 1대1 매치인데, re.sub를 이용하면 한줄 코드로 여러개를 바꿀 수가 있다.(다대 1대응)
# print(Str)

#email 이 유효한 이메일 인지 검사

# import re
# a = re.compile('^[a-zA-Z0-9+-\_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
#
# emails = ["tkdks@kakao.com", "zztisdudoo@gmail.com", "dfdf@dfka"]
# for email in emails :
#     print(a.match(email) != None)


# #list의 메서드 활용
# li1 = ["hello", "vision", "dxdata", "school", "1기"]
# li2 = list(range(10))
#
# #데이터 추가
# li1.append("합격")
#
# #한개 데이터 출력
# print(li1[0])
#
# #슬라이싱 (범위로 출력)
# print(li1[0:-2])
#
# #리스트 데이터 삭제
# del li1[3]
#
# #데이터 순회
# for item in li1 :
#     print(item)

# # list의 정렬
# li = ["Hello", "vision", "dxdata", "school", "1기"]
# li.sort() #오름차순 정렬
# print(li)
#
# li.sort(reverse = True) #내림차순 정렬
# print(li)
#
# result = sorted(li) #sorted()는 return을 해주기 때문에 변수로 받아야함.
# print(result)
#
# #영문 대소문자 구분없이 정렬
# li.sort(key = str.lower)
# print(li)
#
#  ['1기', 'Hello', 'dxdata', 'school', 'vision']
#  ['vision', 'school', 'dxdata', 'Hello', '1기']
#  ['1기', 'Hello', 'dxdata', 'school', 'vision']
#  ['1기', 'dxdata', 'Hello', 'school', 'vision']

# record = ("hello", "dxdata", "school", "vision", 1) #튜플 생성
# print(record)
# print(record[0])
# #record[0] = "Hello" # ERROR, 수정이 불가능 함.
#
# #list와 tuple은 unpacking 이 가능함.
#
# company, edu, job, name, st = record
# print(company)
#
# *etc, company = record # *을 이용하면 나머지 모두를 list로 생성
# print(etc)
#
# #swap : 2개의 데이터의 값을 치환
# a = 10
# b = 20
#
# a , b = b , a
# print(a, b)


# #테이블 구조의 데이터를 생성
# data = [('adam', '010'), ('jessica', '011')]
#
# #이름만 출력
# for row in data :
#     print(row[0]) #이름이 없어 index로 찍어야함.
#
# 컬럼에 이름을 사용하는 튜플
# from collections import namedtuple
#
# #자료구조 생성 - 튜플의 각 컬럼 이름 만들기
# Person = namedtuple("Person", "name mobile")
# persons = [Person('adam', '010'), Person('jesscia', '011')]
# for person in persons :
#     print(person.name) #이름이 있어서 name으로 값을 얻을 수 있다.
#     print(person.mobile) #이건 번호

#set은 데이터의 순서와 상관없이 저장되므로 출력되는 순서는 예측할 수 없습니다.
# s = {"adam", "genesis", "exodus" , "genesis"}
# print(s) # 중복이 제거 + 순서는 알 수가 없음.
# s.add("numbers")
#
# for d in s :
#     print(d) #매 실행마다 결과값의 순서가 달라짐.

# #dict 생성
#
# dic = {}
# #데이터 추가
# dic['name'] = 'adam'
# dic['job'] = 'singer'
# dic['father'] = 'pms'
# dic['father'] = 'pjm'
#
# print(dic)
# print(dic["job"])
# print(dic.get("job", "nojob"))
# # print(dic["score"]) #존재하지 않는 key를 사용하면 keyError 발생
# print(dic.get("score", 0)) #존재하지 않는 key를 사용하면 두번째 매개변수가 리턴
#
# #순회
# for key in dic :
#     print(key,":", dic[key])


#dict 를 이용한 MVC

# #DTO 역할을 수행하는 클래스 생성 - 최근에는 더 권장
#
# class DTO :
#     def __init__(self, name="noname", tel="전화없음"):
#         self.name = name
#         self.tel = tel
#
# #데이터 목록 출력
# datas = [DTO("adam", "010"), DTO("jessica", "011")]
#
# #이름과 전화번호 출력
# for data in datas :
#     print(data.name, data.tel)
#
# datas = [{"name":"adam", "tel":"010"}, {"name":"jessica", "tel":"011"}]
# for data in datas :
#     for key in data :
#         print(key, ":", data[key])


# #이차원 배열 대신에 dict 사용
# kia =["윤영철", "최형우", "이의리"]
# lg = ["켈리", '플럿코']
# han = ["노시환"]
# kbo = [kia,lg, han] #list의 list
# #list는 index를 이용해서 접근하고 dict는 key를 이용해서 접근한다.
#
# #enumerate 는 index와 data를 tuple로 리턴합니다.
# for idx, baseball in enumerate(kbo) :
#     if idx == 0 :
#         print("기아", end='\t')
#     else :
#         print("엘지", end="\t")
#
#     for player in baseball :
#         print(player, end="\t")
#     print()


# kia =["윤영철", "최형우", "이의리"]
# lg = ["켈리", '플럿코']
# han = ["노시환"]
#
# kbo = [{"team" : "기아", "data" :kia}, {"team" : "엘지", "data" : lg}, {"team" : "한화", "data" : han}]
#
# for dic in kbo :
#     print(dic.get("team"), end=":")
#     for player in dic.get("data"):
#         print(player, end = "\t")
#         print()\



# li = list(range(10))
# a = []
# #li의 모든 데이터를 제곱한 list 생성
# #1번
# for i in li :
#     i = i*i
#     a.append(i)
#
#     result = a
# print(result)
#
# #2번
# # map 함수 이용
# # def mul_one(n):
# #     return n * n
# #함수 정의 혹은
# #lambda 사용
#
# result2 = list(map(lambda x : x*x, li))  # map반환을 list 로 변환
# print(f'result2 : {result2}')
#
# #3번 list comprehension 이용
# #[연산식 순회할문장
# result3 = [i*i for i in li]
# print(result3)
#
# #for 2개 사용
# li1 = [1, 2, 3]
# li2 = [4, 5, 6, 7]
# result= [x*y for x in li1 for y in li2]
# print(result)
#
# #list의 활용
# #for 와 if 사용 가능 - filtering
# singers = ["태연", "수지", "아이유","유나", "장원영"]
#
# #글자 수가 3이상인 데이터만 추출
# result = list(filter(lambda x : len(x)>=3, singers))
# print(result)
#
# result = [x for x in singers if len(x) >= 3]
# print(result)

#if else for 활용
# result = [x if len(x) >= 3 else x + "_" for x in singers]
# print(result)


# #개수 쓸 때 유용한 팁!
# from collections import Counter
# data = ["한식", "중식", "분식", "한식", "일식", "양식","중식", "분식", "인식", "한식"]
# counter = Counter(data)
# print(counter)
# print(counter.keys())#dict 으로 활용 가능
# print(counter["한식"])
#
# #상위 2개만 추출
# print(counter.most_common(1))
#
# #튜플의 목록
# data = [("APPLE", 3), ("APPLE", 2), ("ORANGE", 3), ("MANGO", 3), ("ORANGE", 5)]
# counter = Counter()
# #데이터의 합계 구하기
# for name, count in data :
#     counter[name] += counter #개수 , count면
# print(counter)
#
# #데이터의 개수 구하기
# for name, count in data :
#     counter[name] += 1
# print(counter)

# def div(x) :
#     return 10 / x
#
# try :
#     print(div(20))
#     print(div(0)) #프로그램 에러 발생시키는 요소
#
#
# except :
#     #try 절에서 문제가 발생하면 수행되는 구문
#     print("HI")
#     print("프로그램 종료")