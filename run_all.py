import os
import json
from src.solver import solve_delivery_assignment


def run_all_testcases():
    input_folder = "data"
    output_folder = "output"

    # Create output folder if not exists
    os.makedirs(output_folder, exist_ok=True)

    # Get all JSON files in data folder
    json_files = [f for f in os.listdir(input_folder) if f.endswith(".json")]

    if not json_files:
        print("❌ No JSON test case files found inside 'data/' folder.")
        return

    print(f"✅ Found {len(json_files)} test cases.")
    print("Running all test cases...\n")

    for file_name in json_files:
        input_path = os.path.join(input_folder, file_name)

        # Load JSON file
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Solve assignment
        result = solve_delivery_assignment(data)

        # Output file name
        output_file_name = file_name.replace(".json", "_output.json")
        output_path = os.path.join(output_folder, output_file_name)

        # Save output
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4)

        print(f"✔ Processed: {file_name}  -->  {output_file_name}")

    print("\n🎉 All test cases completed successfully!")
    print(f"📌 Outputs saved in: {output_folder}/")


if __name__ == "__main__":
    run_all_testcases()
