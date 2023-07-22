from collections.abc import Callable
from typing import List
from ast import literal_eval


def extract(prop: str) -> Callable[[object], List[str]]:
    def wrapper(obj):
        return [i[prop] for i in literal_eval(obj)]
    return wrapper


def extract_cast(obj) -> List[str]:
    lst: List[str] = []
    counter = 0
    for i in literal_eval(obj):
        if counter != 3:
            lst.append(i["name"])
            counter += 1
        else:
            break
    return lst
