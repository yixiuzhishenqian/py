# try:
#     print(5 / 0)
# except ZeroDivisionError as z:
#     print(z.args)
import traceback

try:
    msg = 'You raise me up, to walk on stormy seas'
    raise ZeroDivisionError(msg, 123456)
except ZeroDivisionError as z:
    print("异常出现了")
    print(z)
    # 加上追踪之后,就可以方便的定位异常出错的语句了
    traceback.print_exc()
