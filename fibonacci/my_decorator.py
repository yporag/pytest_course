from typing import List, Tuple, Callable

Decorator = Callable


def parse_kwargs(
    identifiers: str, values: List[Tuple[str, str]]
) -> List[Tuple[str, str]]:
    identifiers_list = identifiers.split(",")
    list_of_kwargs = []
    for tuple_values in values:
        kwargs = {}
        for i, keyword in enumerate(identifiers_list):
            kwargs[keyword] = tuple_values[i]
        list_of_kwargs.append(kwargs)

    return list_of_kwargs


def my_parameterize(identifiers: str, values: List[Tuple[int, int]]) -> Decorator:
    def my_parameterized_decorator(function: Callable) -> Callable:
        def run_func_parameterized() -> None:
            list_of_kwargs = parse_kwargs(identifiers, values)
            for kwargs in list_of_kwargs:
                print(f"calling function {function.__name__} with {kwargs=}")
                function(**kwargs)

        return run_func_parameterized

    return my_parameterized_decorator
