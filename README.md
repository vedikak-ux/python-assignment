# python-assignment
# Nexgensis Technologies - Python Developer Assignment (2026)

## Problem Statement
This project solves the package delivery assignment problem where multiple agents deliver packages from warehouses to destination coordinates.

Each package must be picked up from its warehouse and delivered to its destination.

The goal is to assign packages to agents in an efficient way and generate the delivery route with total distance.

---

## Approach Used
For each package:
1. Compute delivery cost for each agent:
   - Distance(agent → warehouse) + Distance(warehouse → destination)
2. Assign the package to the agent with minimum cost.
3. Update the agent's location to the destination after completing delivery.

Distance is calculated using Euclidean distance formula.

---

## Assumptions
- Each agent can deliver unlimited packages.
- Packages are delivered sequentially.
- An agent must always go:
  Agent Location → Warehouse → Destination
- After delivery, agent location is updated to the destination.
- Euclidean distance is used because coordinates are given as [x, y].
- If multiple agents have the same cost, the agent with smaller ID is selected.
- Some test cases may have different key names (warehouse_id / warehouse / warehouseId),
  and fallback logic is added to handle such cases.

---

## Project Structure
Python assignment/
│── main.py
│── run_all.py
│── README.md
│
├── src/
│ ├── init.py
│ └── solver.py
│
├── data/
│ ├── base_case.json
│ ├── test_case_1.json
│ └── ...
│
└── output/
├── base_case_output.json
├── test_case_1_output.json
└── ...
