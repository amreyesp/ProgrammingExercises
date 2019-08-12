"""Frequency Queries"""
"""
You are given q queries. Each query is of the form two integers described below:
- 1x : Insert x in your data structure.
- 2y : Delete one occurence of y from your data structure, if present.
- 3z : Check if any integer is present whose frequency is exactly z. If yes,
print 1 else 0.

The queries are given in the form of a 2-D array queries of q size  where q[i][0]
contains the operation, and queries[i][1] contains the data element. For example,
you are given array queries = [(1,1),(2,2),(3,2),(1,1),(1,1),(2,1),(3,2)].
Credits: www.hackerrank.com
"""

class NewQuery:

    def __init__(self):
        self.queries = []
        self.array = []
        self.output = -1

    def read_input(self,queries):
        self.queries = queries

    def process_query(self,query):
        if query[0] == 1:
            self.array.append(query[1])
        if query[0] == 2 and query[1] in self.array:
            self.array.remove(query[1])
        if query[0] == 3:
            self.output = 0
            repeated = {x:self.array.count(x) for x in self.array}
            for element in repeated.values():
                if element == query[1]:
                    self.output = 1

    def frequency_queries(self):
        for element in self.queries:
            self.process_query(element)
