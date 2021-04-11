# SQ数据管理

## 生成instrument时几个选项意义

## 数据从csv文件中导入
- 在data tab中创建一个data set: file import -> add symbol
- file import -> import file
    - 全删数据
    - 不重叠的情况下增加数据
    - 同时间鹾下，新数据会覆盖旧数据。据此可以进行数据修正。
    - 数据导入有重叠时，会有重复数据发生。
    - 导入数据会删除覆盖时间段内的原有数据。但有时也会不覆盖，不擦除。造成大量冗余或错误数据
    - 所以保险的方式，不要有重复数据输入。
    - 如果要修改，需要先导出正确的数据，错误的数据。再删除数据，重新导入。
    - 有能力的话，保留导入前的数据。非常大啊。
    - 导入的数据文件中，每行的时间要求是递增的。这样发现错误时可以全量重导入

## 数据导出
- 导出时显示有tick value，在mt every tick测试时，getTickValue会得到这个值(不是broker的当前值)
- 导出时的tick value值与实际订单计算的值一致，lot比较小时有计算误差
- 所以要保持数据计算的完全正确性，最好生成tick数据后永远不要让mt联网更新
- 每次导出都有重新选一遍mt properties，否则进去都是默认值，不会变
- 默认property最小仓位0.1，设置mt properties后最小可建仓0.01
- 导出时要选择timeframe，否则会导出全timeframe的数据，占用很多空间。但只选
一个timeframe，其他timeframe的bar数据不会导出(tickstory中是默认会导出的)，
要么不看要么另想办法

## ducascopy数据解析
- 用py lib解析有时会出错，可以用7z先解压，再读取。
- 7z解压命令：7z e {filename} -o{target_dir}
- bi5中价格以整数形式保存，需要除以100000, 1000(与digit相关)
