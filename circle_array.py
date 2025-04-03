class CycleArray:
    def __init__(self, size=1):
        self.arr = [None] * size
        self.count = 0  # 已占用的元素数目
        self.start = 0
        self.end = 0
        self.capacity = size  # 分配的空间数

    # 自动扩缩容辅助函数
    def resize(self, newSize):
        arr = [None] * newSize
        for i in range(self.count):
            arr[i] = self.arr[self.start]
            self.start = (self.start + 1) % self.count

        self.start = 0
        self.end = self.count
        self.arr = arr
        self.capacity = newSize

    # 在数组头部添加元素，时间复杂度 O(1)
    def add_first(self, val):
        if self.is_full():
            self.resize(self.capacity * 2)

        self.start = (self.start - 1 + self.count) % self.size
        self.arr[self.start] = val
        self.count += 1

    # 删除数组头部元素，时间复杂度 O(1)
    def remove_first(self):
        self.arr[self.start] = None
        self.start = (self.start + 1) % self.size
        self.count -= 1

        # 小于四分一，size改为二分一
        if self.count < self.capacity // 4:
            self.resize(self.capacity // 2)

    # 在数组尾部添加元素，时间复杂度 O(1)
    def add_last(self, val):
        if self.is_full():
            self.resize(self.capacity * 2)

        self.arr[self.end] = val
        self.end = (self.end + 1) % self.size
        self.count += 1

    # 删除数组尾部元素，时间复杂度 O(1)
    def remove_last(self):
        self.end = (self.end - 1 + self.count) % self.count
        self.arr[self.end] = None
        self.count -= 1

        # 小于四分一，size改为二分一
        if self.count < self.capacity // 4:
            self.resize(self.capacity // 2)

    # 获取数组头部元素，时间复杂度 O(1)
    def get_first(self):
        if self.is_empty():
            return None
        
        return self.arr[self.start]

    # 获取数组尾部元素，时间复杂度 O(1)
    def get_last(self):
        if self.is_empty():
            return None
        return self.arr[self.end - 1]

    def is_full(self):
        return self.count == len(self.arr)

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0
