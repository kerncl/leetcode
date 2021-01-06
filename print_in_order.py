#Question: Easy
'''
Suppose we have a class:
public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().
'''
import threading
import logging
from typing import List
from collections import Callable
from concurrent.futures import ThreadPoolExecutor
from time import sleep

class Foo:
    def __init__(self):
        self.first_lock = threading.Lock()
        self.second_lock = threading.Lock()
        self.third_lock = threading.Lock()
        logging.info('Going to LOCK first lock, second lock, third lock')
        self.first_lock.acquire()
        self.second_lock.acquire()
        self.third_lock.acquire()


    def first(self, printFirst: 'Callable[[], None]', value) -> None:
        logging.info(f'Thread {value}: Entering foo.first ...... is about to RELEASE first lock')
        self.first_lock.release()
        logging.info(f'Thread {value}: .......................... RELEASED first lock')
        logging.info(f"Thread {value}: Going to executed first 'def'")
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        #sleep(3)
        logging.info(f'Thread {value}: ......................... is about to release LOCK second lock')
        self.second_lock.release()
        logging.info(f'Thread {value}: ......................... release second lock')
        logging.info(f'Finished Thread {value}')


    def second(self, printSecond: 'Callable[[], None]', value) -> None:
        logging.info(f'Thread {value}: Entering foo.second ...... is abort to LOCK second lock')
        self.second_lock.acquire()
        logging.info(f'Thread {value}: .......................... LOCKED second lock')
        logging.info(f"Thread {value}: Going to executed second 'def' ")
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        #sleep(3)
        logging.info(f'Thread {value}: .......................... is about to RELEASE third lock')
        self.third_lock.release()
        logging.info(f'Thread {value}: .......................... RELEASED third lock')
        logging.info(f'Finished Thread {value}')

    def third(self, printThird: 'Callable[[], None]', value) -> None:
        logging.info(f'Thread {value}: Entering foo.third ......... is abort to LOCK third lock')
        self.third_lock.acquire()
        logging.info(f'Thread {value}: .......................... LOCKED third lock')
        logging.info(f"Thread {value}: Going to executed third 'def' ")
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        #sleep(3)
        logging.info(f'Thread {value}: ............................. is about to RELEASE thrid lock')
        self.first_lock.release()
        logging.info(f'Thread {value}: .......................... RELEASED third lock')
        logging.info(f'Finished Thread {value}')


def process_sequence(call: List[int]):
    logging.info("Is about to executing")
    process = Foo()
    value = 1
    with ThreadPoolExecutor(max_workers=3) as executor:
        for sequence in call:
            logging.info("Starting executing thread %s", value)
            if sequence == 1:
                executor.submit(process.first, first, value)
            if sequence == 2:
                executor.submit(process.second, second, value)
            if sequence == 3:
                executor.submit(process.third, third, value)
            value += 1
        logging.info("Finishing activate 3 thread")
    logging.info("Ending ....")


def first():
    #print('first')
    logging.debug('FIRST')


def second():
    #print('second')
    logging.debug('SECOND')



def third():
    #print('third')
    logging.debug('THIRD')


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S", )
    logging.getLogger().setLevel(logging.DEBUG)
    #print('Right before executing')
    calling_sequence1 = [1, 2, 3]
    calling_sequence2 = [1, 3, 2]
    calling_sequence3 = [3, 2, 1]
    calling_sequence = calling_sequence3
    logging.debug(f'Right before executing {calling_sequence}')
    process_sequence(calling_sequence)
    #print(f'Output Calling Sequence: ')


