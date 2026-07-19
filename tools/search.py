from serpapi import GoogleSearch
import os

def search_products(query):
    params = {
        "engine": "google_shopping",
        "q": query,
        "api_key": os.getenv("SERPAPI_API_KEY")
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    return results["shopping_results"]


if __name__ == "__main__":
    search_query = input("Enter a product name to search: ")
    results = search_products(search_query)
    print(results)