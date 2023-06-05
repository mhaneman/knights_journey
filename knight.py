import matplotlib.pyplot as plt

class Knight:
    def __init__(self) -> None:
        self.position_history = [(0, 0)]
        self.stuck_positions = []
        
        self.position = [0, 0]
        self.moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]


    def move(self, pos):
        self.position = pos


    def find_next_square(self, board):
        next_pos = None
        next_val = None
        for i in self.moves:
            pos = [sum(i) for i in zip(self.position, i)]
            val = board.grid[tuple(pos)]

            if (next_val is None or val < next_val) and val > 0 and val not in self.stuck_positions:
                next_val = val
                next_pos = pos

        if next_pos is None:
            # print("no more valid squares!", len(self.position_history), self.position)
            self.stuck_positions.append(self.position)
            self.position_history.pop()
            self.position = self.position_history.pop()
            return self.find_next_square(board)

        
        self.position_history.append(tuple(next_pos))
        return next_pos
    

    def show(self):
        plt.plot(*zip(*self.position_history), color="gray")
        x, y = self.position_history[-1]
        plt.plot(x, y, marker="o", markersize=5, markerfacecolor="green")

        for i in self.stuck_positions:
            plt.plot(i[0], i[1], marker="o", markeredgecolor="red", markersize=5, markerfacecolor="red")
            
