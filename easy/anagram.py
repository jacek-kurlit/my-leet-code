from collections import defaultdict


class Solution:
    def isAnagram_first_solution(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        occurences = defaultdict(lambda: 0)
        for c in s:
            occurences[c] = occurences[c] + 1

        for c in t:
            chars_left = occurences[c] - 1
            if chars_left < 0:
                return False
            occurences[c] = chars_left

        return True

    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
