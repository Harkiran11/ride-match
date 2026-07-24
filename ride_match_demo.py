from hash_table import HashTable
from graph import Graph
from sort_utils import merge_sort
from trip_log import BST


def build_city_graph():
    city = Graph()
    roads = [
        ("Downtown", "Midtown", 6),
        ("Downtown", "Harbourside", 9),
        ("Midtown", "University", 4),
        ("Midtown", "Eastgate", 7),
        ("University", "Northside", 5),
        ("Eastgate", "Northside", 3),
        ("Harbourside", "Southpark", 8),
        ("Southpark", "Eastgate", 6),
        ("Northside", "Riverbend", 10),
        ("Eastgate", "Riverbend", 4),
    ]
    for source, destination, weight in roads:
        city.add_edge(source, destination, weight)
    return city


def build_driver_registry():
    drivers = HashTable()
    roster = [
        ("D-101", "Midtown"),
        ("D-102", "Harbourside"),
        ("D-103", "Northside"),
        ("D-104", "Eastgate"),
        ("D-105", "Downtown"),
        ("D-106", "Southpark"),
    ]
    for driver_id, zone in roster:
        drivers.put(driver_id, {"zone": zone, "available": True})
    return drivers


def find_available_drivers(drivers_by_zone, zones_in_range):
    candidates = []
    for zone, hops in zones_in_range:
        for driver_id, zone_of_driver in drivers_by_zone.get(zone, []):
            candidates.append((driver_id, zone_of_driver, hops))
    return candidates


def main():
    city = build_city_graph()
    drivers = build_driver_registry()

    drivers_by_zone = {}
    for driver_id in ["D-101", "D-102", "D-103", "D-104", "D-105", "D-106"]:
        record = drivers.get(driver_id)
        drivers_by_zone.setdefault(record["zone"], []).append((driver_id, record["zone"]))

    rider_zone = "University"
    print(f"Rider request received in zone: {rider_zone}\n")

    nearby_zones = city.bfs(rider_zone, max_hops=2)
    print("Zones within 2 hops of the rider (BFS order):")
    for zone, hops in nearby_zones:
        print(f"  {zone} ({hops} hop(s))")

    candidates = find_available_drivers(drivers_by_zone, nearby_zones)
    print(f"\nAvailable drivers found nearby: {[c[0] for c in candidates]}")

    distances, previous = city.dijkstra(rider_zone)

    ranked_input = []
    for driver_id, zone, _hops in candidates:
        eta = distances[zone]
        ranked_input.append({"driver_id": driver_id, "zone": zone, "eta": eta})

    ranked = merge_sort(ranked_input, key=lambda d: d["eta"])

    print("\nCandidates ranked by ETA (minutes):")
    for entry in ranked:
        print(f"  {entry['driver_id']} in {entry['zone']}, ETA {entry['eta']} min")

    best = ranked[0]
    path = city.build_path(previous, best["zone"])
    print(f"\nBest match: {best['driver_id']} from {best['zone']}")
    print(f"Route to rider: {' -> '.join(path)}")
    print(f"Total travel time: {best['eta']} minutes")

    trip_log = BST()
    trip_log.insert(1001, {"driver": best["driver_id"], "rider_zone": rider_zone, "eta": best["eta"]})
    trip_log.insert(1002, {"driver": "D-102", "rider_zone": "Harbourside", "eta": 0})
    trip_log.insert(1000, {"driver": "D-105", "rider_zone": "Downtown", "eta": 0})

    print("\nTrip log after logging this trip (sorted by timestamp):")
    for timestamp, record in trip_log.in_order():
        print(f"  {timestamp}: {record}")


if __name__ == "__main__":
    main()
