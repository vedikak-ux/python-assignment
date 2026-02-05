import math


def euclidean_distance(p1, p2):
    """
    Distance between two points [x, y]
    """
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def normalize_warehouses(warehouses):
    """
    Supports:
    - list: [{"id": "W1", "location": [0,0]}]
    - dict: {"W1": [0,0], "W2": [5,5]}
    """
    warehouse_map = {}

    if isinstance(warehouses, list):
        for w in warehouses:
            if isinstance(w, dict) and "id" in w and "location" in w:
                warehouse_map[w["id"]] = w["location"]

    elif isinstance(warehouses, dict):
        warehouse_map = warehouses

    else:
        raise ValueError("Invalid warehouses format")

    return warehouse_map


def normalize_agents(agents):
    """
    Supports:
    - list: [{"id": "A1", "location": [5,5]}]
    - dict: {"A1": [5,5], "A2": [10,10]}
    """
    agent_locations = {}

    if isinstance(agents, list):
        for a in agents:
            if isinstance(a, dict) and "id" in a and "location" in a:
                agent_locations[a["id"]] = a["location"]

    elif isinstance(agents, dict):
        agent_locations = agents

    else:
        raise ValueError("Invalid agents format")

    return agent_locations


def get_package_fields(package):
    """
    Handles package keys differences between test cases.
    """
    if not isinstance(package, dict):
        raise ValueError("Package must be an object/dict")

    package_id = package.get("id") or package.get("package_id")

    warehouse_id = (
        package.get("warehouse_id")
        or package.get("warehouse")
        or package.get("warehouseId")
    )

    destination = package.get("destination") or package.get("dest")

    if not package_id:
        raise ValueError("Package missing id")

    if not warehouse_id:
        raise ValueError(f"Package {package_id} missing warehouse_id")

    if destination is None:
        raise ValueError(f"Package {package_id} missing destination")

    return package_id, warehouse_id, destination


def solve_delivery_assignment(data):
    """
    Greedy solution:
    - For each package, assign to agent with minimum distance cost:
        agent -> warehouse + warehouse -> destination
    - After delivery, agent location becomes destination.

    Assumptions:
    - Unlimited package capacity per agent
    - Euclidean distance used
    - Tie-breaker: smallest agent id
    """

    warehouses = data.get("warehouses", [])
    agents = data.get("agents", [])
    packages = data.get("packages", [])

    warehouse_map = normalize_warehouses(warehouses)
    agent_locations = normalize_agents(agents)

    if not agent_locations:
        raise ValueError("No agents available")

    assignments = []
    total_distance = 0.0

    for package in packages:
        package_id, warehouse_id, destination = get_package_fields(package)

        if warehouse_id not in warehouse_map:
            raise ValueError(f"Warehouse {warehouse_id} not found for package {package_id}")

        warehouse_location = warehouse_map[warehouse_id]

        best_agent = None
        best_cost = float("inf")

        for agent_id, agent_loc in agent_locations.items():
            cost = euclidean_distance(agent_loc, warehouse_location) + euclidean_distance(
                warehouse_location, destination
            )

            if best_agent is None or cost < best_cost or (cost == best_cost and agent_id < best_agent):
                best_agent = agent_id
                best_cost = cost

        assignments.append({
            "agent_id": best_agent,
            "package_id": package_id,
            "warehouse_id": warehouse_id,
            "path": [
                agent_locations[best_agent],
                warehouse_location,
                destination
            ],
            "distance": round(best_cost, 2)
        })

        total_distance += best_cost
        agent_locations[best_agent] = destination

    return {
        "assignments": assignments,
        "total_distance": round(total_distance, 2)
    }


