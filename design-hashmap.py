"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 
"""

from typing import List
class MyHashMap:
    INITIAL_SIZE = 5
    mapped_array = []
    def __init__(self):
        self.rehashToSize(self.INITIAL_SIZE)
        self.size = self.INITIAL_SIZE
        self.items_count = 0

    def rehashToSize(self, new_size:int) -> None:
        self.size = new_size
        new_array = [None] * new_size
        for item in self.mapped_array:
            if not item:
                continue

            for k, v in item:
                new_idx = self.getIndex(k)
                if new_array[new_idx] == None:
                    new_array[new_idx] = []
                new_array[new_idx].append((k, v))

        self.mapped_array = new_array


    def put(self, key: int, value: int) -> None:
        self.items_count += 1
        if self.items_count >= len(self.mapped_array):
            self.rehashToSize((self.items_count * 2))

        target_idx = self.getIndex(key)
        if self.mapped_array[target_idx] == None:
            self.mapped_array[target_idx] = []

        # Need to handle update vs append
        update_idx = -1
        for i, v in enumerate(self.mapped_array[target_idx]):
            if v[0] == key:
                update_idx = i

        # If the above update code didn't return, simply append the new value
        if update_idx >= 0:
            self.mapped_array[target_idx][update_idx] = (key, value)
        else:
            self.mapped_array[target_idx].append((key, value))

    def getIndex(self, key: int) -> int:
        return key % self.size

    def get(self, key: int) -> int:
        target_idx = self.getIndex(key)
        if not self.mapped_array[target_idx]:
            return -1

        for k, v in self.mapped_array[target_idx]:
            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:
        self.items_count -= 1
        target_idx = self.getIndex(key)
        if self.mapped_array[target_idx]:
            self.mapped_array[target_idx] = [(k, v) for k, v in self.mapped_array[target_idx] if k != key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

x = MyHashMap()
x.put(1, 1)
x.put(2, 2)
x.put(2, 3)
x.put(3, 2)
x.put(5, 2)
x.put(100, 2)
print(x.get(100))