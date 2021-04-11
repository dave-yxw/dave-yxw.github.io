# 音频处理

## [pydub库](https://github.com/jiaaro/pydub)
安装
<pre>pip install pyhub</pre>

pydub后端使用FFmpeg，需要先安装FFmpeg
<pre>apt-get install ffmpeg</pre>

格式转换
<pre>AudioSegment.from_file("test.m4a",format="m4a")
    .export("test.mp3",format="mp3")
</pre>

还可以做切片，淡入淡出等。更细致的操作需要检查流数据

[pydub api](https://github.com/jiaaro/pydub/blob/master/API.markdown)
一个示例
- frame_rate 44100 44.1kHz
- frame_count: # frames, 420273 = frame_rate * duration_seconds
- sample_width: # bytes/frame, 2
- frame_width: # bytes/frame of all channels, 4
- duration_seconds: 9.53
- channels: 2
- len(adf_ad): 9530 = duration_seconds*1000 
- len(adf_ad_raw): 1681092 = frame_count * frame_width
- len(adf_ad_arr): 840546, 两个channels, 每个channel有frame_count个数据. 
- adf.split_to_mono(), 得到左右声道两个Segment
    - 声道1 arr=[-983, -970, ...]
    - 声道2 arr=[-748, -770, ...]
    - 源数据arr=[-983, -748, -970, -770, ...]
