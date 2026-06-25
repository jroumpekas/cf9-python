from typing import List, Any

my_list = [1, 2, "hello", [3,4,5]]

def append_to_list(li: List[Any], element: Any) -> None:
    li.append(element)

append_to_list(my_list, 'CF9 friends')


for item in my_list:
    print(item, end=", ")

