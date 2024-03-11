import json

def json_reader():
    """
    Function to read JSON file.
    
    Args:
    None

    Returns:
    JSON data as string
    """
    # Opening JSON file
    with open('json/data.json', 'r') as jsonfile:
 
        # Reading from json file
        json_data = json.load(jsonfile)
    
    return json_data


def json_writer(new_data):
    """
    Function to write JSON file.
    
    Args:
    new_data: dict

    Returns:
    None
    """
    with open('json/data.json', 'w') as jsonfile:
        
        # Writing the json file
        json.dump(new_data, jsonfile)

def main() -> None:
    print(json_reader())
    data = {
        "id": 1,
        "name": "Alex"
    }
    print(json_writer(data))
    print(json_reader())

if __name__ == '__main__':
    main()