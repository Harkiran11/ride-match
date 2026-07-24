from min_heap import MinHeap, heap_sort
from hash_table import HashTable
from graph import Graph
from sort_utils import merge_sort
from trip_log import BST


def test_min_heap_pop_order():
    heap = MinHeap()
    for priority in [5, 1, 8, 2, 9, 0, 3]:
        heap.push(priority, f"item-{priority}")
    popped = [heap.pop()[0] for _ in range(7)]
    assert popped == sorted(popped), f"heap did not pop in ascending order: {popped}"


def test_heap_sort_matches_builtin_sort():
    data = [9, 3, 7, 1, 5, 2, 8, 0, 6, 4]
    assert heap_sort(data) == sorted(data)


def test_hash_table_collisions():
    table = HashTable(capacity=2)
    for i in range(20):
        table.put(f"key-{i}", i)
    for i in range(20):
        assert table.get(f"key-{i}") == i
    assert len(table) == 20


def test_hash_table_delete():
    table = HashTable()
    table.put("a", 1)
    table.put("b", 2)
    assert table.delete("a") is True
    assert table.get("a") is None
    assert table.get("b") == 2


def test_dijkstra_shortest_path():
    g = Graph()
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 1)
    g.add_edge("C", "B", 1)
    g.add_edge("B", "D", 1)
    distances, previous = g.dijkstra("A")
    assert distances["D"] == 3
    path = Graph.build_path(previous, "D")
    assert path == ["A", "C", "B", "D"]


def test_bfs_hop_counts():
    g = Graph()
    g.add_edge("A", "B", 1)
    g.add_edge("B", "C", 1)
    g.add_edge("C", "D", 1)
    order = g.bfs("A")
    hops = dict(order)
    assert hops["A"] == 0
    assert hops["B"] == 1
    assert hops["C"] == 2
    assert hops["D"] == 3


def test_merge_sort_is_stable():
    data = [{"id": "x", "eta": 5}, {"id": "y", "eta": 5}, {"id": "z", "eta": 1}]
    ranked = merge_sort(data, key=lambda d: d["eta"])
    assert [d["id"] for d in ranked] == ["z", "x", "y"]


def test_bst_range_query():
    tree = BST()
    for key in [50, 30, 70, 20, 40, 60, 80]:
        tree.insert(key, f"trip-{key}")
    result = tree.range_query(35, 65)
    keys = [k for k, _ in result]
    assert keys == [40, 50, 60]


def run_all():
    tests = [
        test_min_heap_pop_order,
        test_heap_sort_matches_builtin_sort,
        test_hash_table_collisions,
        test_hash_table_delete,
        test_dijkstra_shortest_path,
        test_bfs_hop_counts,
        test_merge_sort_is_stable,
        test_bst_range_query,
    ]
    passed = 0
    for test in tests:
        test()
        passed += 1
        print(f"PASS: {test.__name__}")
    print(f"\n{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_all()
