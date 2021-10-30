#Question: Easy
"""
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.
"""
import logging


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.myhash = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.myhash[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.myhash.keys():
            return self.myhash.get(key)
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.myhash.keys():
            self.myhash.pop(key)

if __name__ == "__main__":
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    hashMap = MyHashMap()
    hashMap.put(1, 1)
    hashMap.put(2, 2)
    hashMap.get(1)  # returns 1
    hashMap.get(3)  # returns - 1(not found)
    hashMap.put(2, 1)  # update the existing value
    hashMap.get(2)  # returns 1
    hashMap.remove(2)  # remove the mapping for 2
    hashMap.get(2)  # returns - 1(not found)
