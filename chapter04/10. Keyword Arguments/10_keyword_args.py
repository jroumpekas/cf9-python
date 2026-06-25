from typing import List, Tuple, Dict, Optional
 
# [("lenovo", 100), ("lenovo", 40), ("ibm", 100)]
def get_results(products: List[Tuple[str, int]], **kwargs: Optional[Dict[str, str | int]]) -> List[Tuple[str, int]]:
    results = [
        # [ <expression> for <item> in <iterable> if <condition> ]
        (brand, price) for brand, price in products if kwargs.get('brand') == brand and kwargs.get('price') == price
    ]
    return results
 
def main():
    products = [("lenovo", 100), ("lenovo", 40), ("ibm", 100)]
    criteria = {"brand": "lenovo", "price" :100}
 
    print(get_results(products, **criteria))
 
if __name__ == "__main__":
    main()