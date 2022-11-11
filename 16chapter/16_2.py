#패키지
#모듈들을 모아놓은 디렉토리
#반드시 __init__.py가 존재해야 함
#일반적으로 내용은 없음

#__init__.py 안의 내용을 전부 공개하겠다
#__all__ = ["add", "multi"] 공개할 함수명을 적으면 공개됌
import sys
import math


print(sys.builtin_module_names)
print()
dir(math)

help(math.hypot)