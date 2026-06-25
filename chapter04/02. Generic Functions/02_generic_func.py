from typing import Sequence, TypeVar, List, Any, Optional
 
# Declare Generic Type Variable
T = TypeVar('T')
 
# More descriptive TypeVar names based on the intended type constraints
Number = TypeVar('Number', int, float)
 
def first(seq: Sequence[T]) -> T:
    if not seq:
        raise ValueError("Sequence is empty")
    return seq[0]
 
 
def last(seq: Sequence[T]) -> T:
    if not seq:
        raise ValueError("Sequence is empty")
    return seq[-1]
 
def count_truthy(elements: List[Any]) -> int:
    return sum(1 for element in elements if element)
 
 
def len_str(s: Optional[str] = None) -> int:
    return len(s) if s is not None else 0
    # return 0 if None else len(s)
 
def main():
    # [1, "hello", 0, False, None, 100, 3.14]
    pass
 
if __name__ == "__main__":
    main()
 