import json

def clean_json(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    print(f"Data: {data}")  # Add this line to print the data

    cleaned_data = []

    for item in data:
        cleaned_item = {
            'title': item.get('title', None),
            'keywords': item.get('keywords', None),
            'creator': item.get('creator', None),
            'full_description': item.get('full_description', None),
            'pubDate': item.get('pubDate', None),
            'image_url': item.get('image_url', None),
            'category': item.get('category', None),
        }

        cleaned_data.append(cleaned_item)

    with open(output_file, 'w') as f:
        json.dump(cleaned_data, f, indent=2)

if __name__ == "__main__":
    input_file = 'input_file.json'
    output_file = 'output_file.json'
    clean_json(input_file, output_file)
