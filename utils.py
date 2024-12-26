import json
from book import Book
FILE = "books.json"

def Wbook(books):
    try:   
        with open(FILE, "w") as f:
            json.dump(books, f, indent=4)  # indent for pretty printing
        print(f"JSON data written to {FILE}")
    except IOError as e:
        print(f"Error writing to file: {e}")
        
        
def Rbook():
    try:
        with open(FILE, "r") as f:
            loaded_data = json.load(f)
        print(f"JSON data read from {FILE}:")
        return loaded_data
    except FileNotFoundError:
        print("File data.json not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except IOError as e:
        print(f"Error reading from file: {e}")
