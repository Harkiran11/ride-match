import random
import time
import csv

from hash_table import HashTable
from trip_log import BST
from graph import Graph


def time_hash_table(n):
    table = HashTable()
    for i in range(n):
        table.put(i, i)
    start = time.perf_counter()
    for _ in range(1000):
        table.get(random.randrange(n))
    elapsed = time.perf_counter() - start
    return elapsed / 1000


def time_bst_sorted_insertion(n):
    tree = BST()
    for i in range(n):
        tree.insert(i, i)
    start = time.perf_counter()
    for _ in range(200):
        tree.search(random.randrange(n))
    elapsed = time.perf_counter() - start
    return elapsed / 200


def time_dijkstra(v_count):
    g = Graph()
    vertices = list(range(v_count))
    for v in vertices:
        g.add_vertex(v)
    for v in vertices:
        for _ in range(3):
            u = random.choice(vertices)
            if u != v:
                g.add_edge(v, u, random.randint(1, 20))

    start = time.perf_counter()
    g.dijkstra(0)
    elapsed = time.perf_counter() - start
    return elapsed


def main():
    sizes = [100, 500, 1000, 2000, 4000, 8000]
    rows = []
    for n in sizes:
        hash_time = time_hash_table(n)
        bst_time = time_bst_sorted_insertion(n)
        dijkstra_time = time_dijkstra(n)
        rows.append((n, hash_time, bst_time, dijkstra_time))
        print(f"n={n:>5}  hash_get={hash_time * 1e6:8.2f} us  "
              f"bst_search={bst_time * 1e6:8.2f} us  "
              f"dijkstra={dijkstra_time * 1e3:8.2f} ms")

    with open("benchmark_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "hash_get_seconds", "bst_search_seconds", "dijkstra_seconds"])
        writer.writerows(rows)


if __name__ == "__main__":
    main()
