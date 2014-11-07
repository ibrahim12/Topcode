# class GreaterGameDiv2:
#     def calc(self, snuke, sothe ):
#
#         n = len(snuke)
#
#         point = 0
#         for index in xrange(n):
#             if snuke[index] > sothe[index]:
#                 point =+ 1
#
#         return point


class PathGameDiv2:

    def _has_left_to_right_path(self, board, index_i, index_j ):
        print(index_i, index_j)

        n = len(board[0])


        if index_i == n - 1:
            if board[0][index_i] == '.':
                print(index_i)
                return 1
            else:
                return 0

        if index_j == n - 1 :
            if board[1][index_j] == '.':
                print(index_j)
                return 1
            else:
                return 0

        if board[0][index_i]  == '#' and board[1][index_j] == '#':
            return 0

        fwd = 0
        if board[0][index_i + 1] == '.':
            fwd = self._has_left_to_right_path(board, index_i+1, index_j )

        dwn = 0
        if board[1][index_j + 1] == '.':
            dwn = self._has_left_to_right_path(board, index_i, index_j + 1 )

        if fwd:
            print('f')

        if dwn:
            print('d')

        return fwd or dwn

    def calc(self, board):

        n = len(board[0])

        has_path = self._has_left_to_right_path(board, 0, 0)

        print(has_path)


s = PathGameDiv2()
s.calc(("#...#","..#.."))