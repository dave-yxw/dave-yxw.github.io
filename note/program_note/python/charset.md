# 检测字符串字节编码

<pre>
import chardet

ret = chardet.detect(b"hello world")
print(ret)
# {'encoding': 'ascii', 'confidence': 1.0}

data = '离离原上草，一岁一枯荣'.encode('gbk')
ret = chardet.detect(data)
print(ret)
# {'encoding': 'GB2312', 'confidence': 0.7407407407407407}

data = '离离原上草，一岁一枯荣'.encode('utf-8')
ret = chardet.detect(data)
print(ret)
# {'encoding': 'utf-8', 'confidence': 0.99}

data = '最新の主要ニュース'.encode('euc-jp')
ret = chardet.detect(data)
print(ret)
# {'encoding': 'EUC-JP', 'confidence': 0.99}
</pre>