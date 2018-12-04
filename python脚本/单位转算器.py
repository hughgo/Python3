#字节转B KB MB GB
def  zhuan(size):
    if (size < 1024) :
        return str(size) + " B"
    elif 1024<size<1048576 :
        size = round(size / 1024,2)
        return str(size) + " KB"
    elif 1048576<size<1073741824:
        size=round(size/1048576,2)
        return str(size) +" MB"
    elif size>107374824:
        size=round(size/1073741824,2)
        return str(size)+" GB"



stra = "-24556455555"
data = abs(int(stra))

print(zhuan(data))