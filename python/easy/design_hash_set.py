#Question: Easy
'''
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet.
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.
'''
import logging


class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_list = []

    def add(self, key: int) -> None:
        self.hash_list.append(key)

    def remove(self, key: int) -> None:
        if key in self.hash_list:
            count = self.hash_list.count(key)
            for _ in range(count):
                self.hash_list.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.hash_list:
            return True
        else:
            return False


if __name__ == "__main__":
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    hashSet = MyHashSet()
    hashSet.add(1)
    hashSet.add(2)
    print(f'{hashSet.contains(1)}')
    print(f'{hashSet.contains(3)}')
    hashSet.add(2)
    print(f'{hashSet.contains(2)}')
    hashSet.remove(2)
    print(f'{hashSet.contains(2)}')