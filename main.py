import json
import os
import sys

from src.solver import solve_delivery_assignment


def main():
    # Check if input file is provided
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_json_file>")
        print("Example: python main.py data/base_case.json")
        return

    input_file = sys.argv[1]

    # Validate input file exists
    if not os.path.exists(input_file):
        print(f"Error: File not found -> {input_file}")
        return

    # Load JSON input
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Solve assignment
    result = solve_delivery_assignment(data)

    # Create output folder
    os.makedirs("output", exist_ok=True)

    # Generate output filename
    input_filename = os.path.basename(input_file)
    output_filename = input_filename.replace(".json", "_output.json")
    output_file = os.path.join("output", output_filename)

    # Save output JSON
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)

    print("✅ Assignment solved successfully!")
    print(f"📌 Input file : {input_file}")
    print(f"📌 Output file: {output_file}")


if __name__ == "__main__":
    main()

