import requests
import json

def fetch_api_data(url, payload, output_file):
    try:
        # Send a POST request to the API endpoint with the JSON payload
        response = requests.post(url, json=payload)
        
        # Raise an exception for HTTP errors (status codes 4xx or 5xx)
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Print the JSON data
        print("Response JSON:")
        print(json.dumps(data, indent=4))  # Pretty-print the JSON
        
        # Dump the JSON data to a file
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)  # Pretty-print the JSON to the file
        
        print(f"JSON data has been written to {output_file}")
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error occurred: {req_err}")
    except ValueError as json_err:
        print(f"Error parsing JSON: {json_err}")

if __name__ == "__main__":
    # Replace with the API URL you want to call
    api_url = "https://5ef3-110-224-127-85.ngrok-free.app/permit-list/"
    
    # Define the JSON payload
    payload = {
        "paths": [
            "/mnt/c/Users/Shreyansh/Desktop/tidbtestfolder"
        ]
    }
    
    # Define the output file path
    output_file = "response.json"
    
    # Fetch and print the API data, and save to file
    fetch_api_data(api_url, payload, output_file)
