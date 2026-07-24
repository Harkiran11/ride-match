# Ride Matching Engine

A small ride matching and route optimization engine, the kind of dispatch logic behind an app like Uber. Given a rider's location and a live set of drivers, it finds nearby drivers, computes real travel time to each of them, and ranks candidates for dispatch.

Built for a data structures and algorithms course project. Every core structure is implemented from scratch in plain Python, no `heapq`, no `dict` shortcuts standing in for the real mechanics, to actually show how each one works instead of calling a library.

## What it does

A single dispatch request runs through five stages:

1. Look up drivers by id in a hash table with chaining
2. Search nearby zones with breadth first search, bounded to a small hop radius
3. Compute exact travel time to each candidate with Dijkstra's algorithm, using a binary min heap as the priority queue
4. Rank candidates by ETA with merge sort
5. Log the completed trip into a binary search tree keyed by timestamp

## Why these choices

- **Hash table over a tree** for the driver registry, since lookups happen on every request and need to be close to O(1)
- **Adjacency list over a matrix** for the road network, since real road graphs are sparse
- **Dijkstra over Bellman Ford**, since travel times are never negative, so the faster algorithm is safe to use
- **Merge sort over quick sort**, for guaranteed O(n log n) and stable ordering when two drivers tie on ETA
- **Plain BST for trip history**, with a red black tree noted as the production upgrade, since sorted timestamp inserts are the exact case a plain BST handles worst

## Performance

| Component | Approach | Average case | Worst case |
|---|---|---|---|
| Driver lookup | Hash table, chaining | O(1) | O(n) |
| Nearby zone search | BFS, bounded | O(V + E) | O(V + E) |
| Fastest route | Dijkstra, min heap | O((V+E) log V) | O((V+E) log V) |
| Candidate ranking | Merge sort | O(n log n) | O(n log n) |
| Trip history | Binary search tree | O(log n) | O(n) |

Measured with a benchmark script comparing hash table lookups against BST lookups from 100 to 8000 records: hash table stays flat around 1 microsecond per lookup, BST search grows to roughly 150 microseconds at 8000 records, which matches the theory.

## Running it

Plain Python 3, no installs needed.

```
python ride_match_demo.py
python test_ridematch.py
python benchmark.py
```

## Files

- `hash_table.py`, chained hash table
- `min_heap.py`, binary min heap and heap sort
- `graph.py`, adjacency list graph, BFS, DFS, Dijkstra
- `sort_utils.py`, merge sort
- `trip_log.py`, binary search tree
- `ride_match_demo.py`, end to end example
- `test_ridematch.py`, correctness tests
- `benchmark.py`, timing experiment
