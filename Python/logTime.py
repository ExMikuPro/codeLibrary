import datetime

if __name__ == '__main__':
    now = datetime.datetime.now()
    otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    print("[" + otherStyleTime + "]")
