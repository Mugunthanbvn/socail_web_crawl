from typing import Any, Optional, Callable, Tuple, TypeVar



T = TypeVar('T')  


def safe_execute(func: Callable[..., T], *args: Any, **kwargs: Optional[dict]) -> Tuple[Optional[T], bool ]:

    try:
        return (func(*args, **kwargs), True)
    except Exception as e:
        print(f"An error occurred: {e}")
        return (None, False)