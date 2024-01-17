import sklearn as sk
import sklearn.preprocessing # 자동으로 import 안됨.

print(dir(sk)) # 패키지 안에 포함된 함수 출력

print("\n----------------------------------\n")

from numpy import arange # 선택적 import

print(arange(10))

print("\n----------------------------------\n")

import test_package as tp

tp.hello()