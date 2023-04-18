#coding=utf-8
from django.test import TestCase

# Create your tests here.

import os
from hellodjango import settings
# if __name__ == '__main__':
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hellodjango.settings')
#     import django
#     django.setup()
#     from first.models import TbSubject
#     subject1 = TbSubject(name='Python全栈开发' ,intro='当前最热门的学科',is_hot=True)
#     subject1.save()
#     subject2 = TbSubject(name='全站软件测试',intro=' 学习自动化测试的学科',is_hot=False)
#     subject2.save()
#     subject3 = TbSubject(name='JaveEE分布式开发',intro='基于java语言的服务器应用开发',is_hot=True)
#     print('ok')

# print(os.path.join(settings.BASE_DIR,'first\static'))
# def pascal_row(n=0):
#     """生成毕达哥拉斯三角形（杨辉三角）"""
#     result = [1]
#     x,numerator = 1,n
#     for denominator in range(1,n // 2 + 1):
#         x *= numerator
#         x /= denominator
#         result.append(x)
#         numerator-=1
#     if n & 1 == 0:
#         result.extend(reversed(result[:-1]))
#     else:
#         result.extend(reversed(result))
#     return result
# tsequense = tuple([t/20.0 for t in range(21)])
# print(pascal_row(4))
# print(tsequense)
# r = []
# for t in tsequense:
#     tpowers = (t**i for i in range(5))
#     upowers = ((1 - t) ** i for i in range(5 -1,-1,-1))
#     coefs = [c * a * b for c,a,b in zip(pascal_row(4),tpowers,upowers)]
#     r.append(coefs)
# print(r)
# res = [1,2,3,4,5]
# print(res[:-1])
# print(2&1)
# print(3&1)
# print(list(range(1,3)))

import base64

t = base64.b64decode('ODkxNDQ4YzAwOTBlNzI0NGIxNmU3OTI1Zjc4MzE5ZmE2NmRmZjBiMTp7ImNhcHRjaGEiOiJpdG9oIiwidXNlcmlkIjoyLCJ1c2VybmFtZSI6ImhlbGxva2l0dHkifQ==')
print(t)