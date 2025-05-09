import json
import sys

def convert_trust_values(json_obj, type_mapping, direction_mapping):
    if isinstance(json_obj, dict):
        for key, value in list(json_obj.items()):
            if key == "TrustType" and isinstance(value, int) and value in type_mapping:
                json_obj[key] = type_mapping[value]
            elif key == "TrustDirection" and isinstance(value, int) and value in direction_mapping:
                json_obj[key] = direction_mapping[value]
            elif isinstance(value, (dict, list)):
                convert_trust_values(value, type_mapping, direction_mapping)
    elif isinstance(json_obj, list):
        for item in json_obj:
            convert_trust_values(item, type_mapping, direction_mapping)
    
    return json_obj

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_json_file> [output_json_file]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else input_file
    

    trust_type_mapping = {
        0: "ParentChild",
        1: "CrossLink",
        2: "Forest",
        3: "External",
        4: "Unknown"
    }
    
    trust_direction_mapping = {
        0: "Disabled",
        1: "Inbound",
        2: "Outbound",
        3: "Bidirectional"
    }
    
    try:
        with open(input_file, 'r') as f:
            data = json.load(f)
        
        updated_data = convert_trust_values(data, trust_type_mapping, trust_direction_mapping)
        
        with open(output_file, 'w') as f:
            json.dump(updated_data, f, separators=(',', ':'))

            
        print(f"Successfully processed JSON file. Output saved to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except json.JSONDecodeError:
        print(f"Error: '{input_file}' is not a valid JSON file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()