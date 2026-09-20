from collections import defaultdict

class Solution:
    def hasNoDuplicate(self, search_space: dict[str, int]) -> bool:
        for digit, count in search_space.items():
            if digit == '.':
                continue
            
            if count != 1:
                return False
        return True
    
    def squareTest(self, board: List[List[str]]) -> bool:
        for c in range(len(board) // 3):
            for r in range(len(board[0]) // 3):
                seen = defaultdict(int)
                for i in range(3):
                    for j in range(3):
                        seen[board[c * 3 + i][r * 3 + j]] += 1
                if not self.hasNoDuplicate(seen):
                    return False
        return True
    
    def columnTest(self, board: List[List[str]]) -> bool:
        for r in range(len(board[0])):
            seen = defaultdict(int)
            for c in range(len(board)):
                seen[board[c][r]] += 1
            if not self.hasNoDuplicate(seen):
                return False
        return True
    
    def rowTest(self, board: List[List[str]]) -> bool:
        for c in range(len(board)):
            seen = defaultdict(int)
            for r in range(len(board[0])):
                seen[board[c][r]] += 1
            if not self.hasNoDuplicate(seen):
                return False
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.squareTest(board) and self.columnTest(board) and self.rowTest(board)