class BException(Exception):
    pass


class CException(BException):
    pass


class DException():
    pass


# for exc in [BException, CException, DException]:
#     try:
#         raise exc()  # 抛出异常
#     except DException:
#         print("D")
#     except CException:
#         print("C")
#     except BException:
#         print("B")

for exc1 in [BException, CException, DException]:
    try:
        raise exc1()  # 抛出异常
    except (BException, CException):
        print("B")
    except:
        print("D")
    else:
        print("没有异常")
    finally:
        print("都会执行")