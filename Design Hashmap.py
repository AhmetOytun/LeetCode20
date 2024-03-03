class MyHashMap:

    def __init__(self):
        self.key=[]
        self.value=[]
    def put(self, key: int, value: int) -> None:
        if key in self.key:
            i=self.key.index(key)
            self.value[i]=value
        else:
            self.key.append(key)
            self.value.append(value)

    def get(self, key: int) -> int:
        if key in self.key:
            return self.value[self.key.index(key)]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.key:
            i = self.key.index(key)
            self.key.pop(i)
            self.value.pop(i)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)