from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()  # 使用有序字典
        self.capacity = capacity   # 设置缓存容量

    def get(self, key: int) -> int:
        if key not in self.cache:  # 如果不存在，返回 -1
            return -1
        # 如果存在，先将其移动到末尾 (标记为最近使用)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 如果键存在，更新值并移动到末尾
            self.cache.move_to_end(key)
        self.cache[key] = value
        # 如果缓存超过容量，弹出最早插入的元素
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)