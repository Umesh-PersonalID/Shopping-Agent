from typing import Any

from tools.compare import call_llm
from tools.search import search_products


def normalize_product(product: dict[str, Any]) -> dict[str, Any]:
    return {
        "title": product.get("title", "Untitled product"),
        "price": product.get("price", "N/A"),
        "source": product.get("source", "Unknown"),
        "link": product.get("link") or product.get("product_link", ""),
        "thumbnail": product.get("thumbnail", ""),
        "rating": product.get("rating"),
        "reviews": product.get("reviews"),
    }


def parse_price(price_text: str) -> float | None:
    digits = "".join(character for character in price_text if character.isdigit() or character == ".")
    if not digits:
        return None
    try:
        return float(digits)
    except ValueError:
        return None


def filter_products_by_budget(products: list[dict[str, Any]], budget: float) -> list[dict[str, Any]]:
    filtered_products: list[dict[str, Any]] = []
    for product in products:
        price = parse_price(str(product.get("price", "")))
        if price is None:
            continue
        if price <= budget:
            filtered_products.append(product)
    return filtered_products


def build_recommendation(query: str, budget: float) -> dict[str, Any]:
    search_results = search_products(query)
    normalized_results = [normalize_product(product) for product in search_results]
    filtered_results = filter_products_by_budget(normalized_results, budget)
    recommendation = call_llm(filtered_results) if filtered_results else "No products matched your budget."

    return {
        "query": query,
        "budget": budget,
        "search_count": len(normalized_results),
        "filtered_count": len(filtered_results),
        "recommendation": recommendation,
        "products": filtered_results,
    }
