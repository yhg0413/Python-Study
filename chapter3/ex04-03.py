s = """어러 줄에 걸쳐 
정의하는 경우"""
#""" -> 보통은 엔터를 인식하지 않음 하지만 """을 사용할경우 엔터까지 인식
print(s)

linecontinue = 365 * 24 * \
                60 * 60
# \ 사용할시 개행으로 인식시킬수있음 긴 표현식 사용할떄 사용

print(linecontinue)

s = "korea" "japan" "2000"
print(s)
# 위 아래 둘다 사용가능
s = ("korea"
     "japan"
     "2002")

print(s)