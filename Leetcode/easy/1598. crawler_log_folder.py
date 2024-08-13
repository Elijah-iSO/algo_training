"""
The Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:

"../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
"./" : Remain in the same folder.
"x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder after the change folder operations.
"""


class Solution:
    def min_operations(self, logs: list[str]) -> int:
        steps_to_main = 0
        for operation in logs:
            if '../' in operation and steps_to_main > 0:
                steps_to_main -= 1
            elif not operation.startswith('.'):
                steps_to_main += 1

        return steps_to_main


result = Solution()
