class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "None"
        separator = "+|+%"
        return separator.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        separator = "+|+%"
        return s.split(separator)
