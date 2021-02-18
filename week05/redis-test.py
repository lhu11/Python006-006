"""
在社交类网站中，经常需要对文章、视频等元素进行计数统计功能，热点文章和视频多为高并发请求，因此采用 redis 做为文章阅读、视频播放的计数器。
请实现以下函数：

复制代码
counter()
def counter(video_id: int):
    ...
    return count_number
函数说明:

counter 函数为统计视频播放次数的函数，每调用一次，播放次数 +1
参数 video_id 每个视频的 id，全局唯一
基于 redis 实现自增操作，确保线程安全
"""
from redis import Redis

def __init__(self,client:Redis,key:str):
    self.client=client
    self.key=key

client=Redis(host="192.168.43.6",password="")

def counter(self,video_id: int):
    if client.exists(str(video_id))==False:
        client.set(str(video_id),0)
    count_number=client.incr(str(video_id))
    return count_number

if __name__ == '__main__':
    print(counter(1001))
    print(counter(1002))
    print(counter(1001))