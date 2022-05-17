if __name__ == '__main__':
    # 判断文本里是否有string字符串的数据
    # 常用于机器人实现单次发送模块
    string = ""
    file = open("T.log", 'a+', encoding='utf-8')
    readFile = open("T.log", 'r', encoding='UTF-8')
    data = readFile.read()
    if string in data:
        file.close()
    else:
        file.write(str(string) + "\n")
        print("正在写入")
