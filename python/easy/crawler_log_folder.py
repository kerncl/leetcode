# Question: Easy
'''
The Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:

"../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
"./" : Remain in the same folder.
"x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder after the change folder operations.
'''
from typing import List
import logging


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        if logs[0] == '../':
            logs.pop(0)
        orig_logs = logs.copy()
        logs.reverse()
        stop_operate_index = len(logs) - logs.index('../') if '../' in logs else 0
        num_operator = stop_operate_index - orig_logs[:stop_operate_index].count('./') - orig_logs[:stop_operate_index].count('../') * 2
        logs = orig_logs[stop_operate_index:]
        if './' in orig_logs[stop_operate_index:]:
            for _ in range (orig_logs[stop_operate_index:].count('./')):
                logs.remove('./')
        return num_operator+len(logs) if num_operator > 0 else len(logs)

class Solution2:
    def minOperations(self, logs: List[str]) -> int:
        operation = 0
        if './' in logs:
            for _ in range(logs.count('./')):
                logs.remove('./')
        for index in logs:
            if index == '../':
                operation -= 1
            else:
                if operation < 0:
                    operation = 0
                operation +=1
        return operation


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.DEBUG)
    logs = ["d1/", "d2/", "../", "d21/", "./"]
    logs2 = ["./", "wz4/", "../", "mj2/", "../", "../", "ik0/", "il7/"]
    logs3 = ["./", "../", "./"]
    logs4 = ["vv1/","../","./"]
    logs5 = ["d1/","d2/","./","d3/","../","d31/"]
    logs6 = ["./","ho3/","tl8/"]
    logs7 = ["../","pb3/","w1/","q2/","j4/","k0/","../","./","rm6/"]
    logs8 = ["../","zp8/","../","./","../","../","np9/","i4/","./","sv9/","cl9/","../","../","qf5/","hr6/","s8/","w8/","./","../","./","i3/","bj9/","./","qi9/","./","../"]
    #result = Solution()
    #logging.info(f'Number of operation: {result.minOperations(logs8)}')
    result2 = Solution2()
    logging.info(f'Number of operation: {result2.minOperations(logs8)}')
