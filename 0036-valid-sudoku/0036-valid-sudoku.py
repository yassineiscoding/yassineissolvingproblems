class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we'll create three dictionaries
        # rows, columns and subboxes
        # each dictionary will have (key = div_number, value = set with values)
        # check will be performed after inserting each row, or column

        rows = defaultdict(set)
        for i in range(9):
            for element in board[i]:
                if element in rows[i]:
                    return False
                elif element != '.':
                    rows[i].add(element)

        columns = defaultdict(set)
        for c in range(9):
            for r in range(9):
                if board[r][c] in columns[c]:
                    return False
                elif board[r][c] != '.':
                    columns[c].add(board[r][c])

        sub_boxes = defaultdict(set)
        for i in range(9):
            for j in range(9):
                # Calculate which sub-box this cell belongs to (0-8)
                box_idx = (i // 3) * 3 + (j // 3)
                if board[i][j] in sub_boxes[box_idx]:
                    return False
                elif board[i][j] != '.':
                    sub_boxes[box_idx].add(board[i][j])
        return True


        
                
                