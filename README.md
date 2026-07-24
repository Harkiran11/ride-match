# Ride Matching Engine

Code for my SFWRTECH 4DS3 final portfolio. Small ride matching and route
optimization engine, built using the data structures and algorithms from
the course, no external libraries.

Files:

- hash_table.py, chained hash table for the driver and rider registry
- min_heap.py, binary min heap used as Dijkstra's priority queue, plus heap sort
- graph.py, adjacency list graph with BFS, DFS, and Dijkstra
- sort_utils.py, merge sort used to rank candidate drivers by ETA
- trip_log.py, binary search tree for trip history
- ride_match_demo.py, runs one dispatch request end to end
- test_ridematch.py, correctness tests
- benchmark.py, timing experiment used for the growth chart in the report

Run with plain Python 3, no packages needed.

```
python ride_match_demo.py
python test_ridematch.py
python benchmark.py
```
