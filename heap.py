import heapq
import game2

class Heap:
    def __init__(self):
        self.heap_ = []

    def game(self):
        game_ = game2.Game()
        game_.go()
        record = game_.attempt
        name = game_.name
        heapq.heappush(self.heap_, (-record, name))
        if len(self.heap_) > 10:
            heapq.heappop(self.heap_)

    def __str__(self):
        str_ = '№\tName\tIterations\n'
        i = 1
        for (record, name) in reversed(sorted(self.heap_)):
            str_ = str_ + '{0}.\t{1}\t{2}\n'.format(i, name, -record)
            i += 1
        return str_
