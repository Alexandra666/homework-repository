from typing import Callable


def cache(times=1) -> Callable:
    # num_of_calls = times

    def internal_decorator(func: Callable):
        cache_memo = {}

        def check_if_in_cache(*args, **kwargs):
            nonlocal times
            num_of_calls = times
            call_key = (args, tuple(sorted(kwargs.items())))
            if call_key not in cache_memo:
                result = func(*args, **kwargs)
                cache_memo[call_key] = [result, num_of_calls]
                if num_of_calls > times:
                    result = func(*args, **kwargs)
                    return result
                else:
                    cache_memo[call_key][1] -= 1
                    return result

        return check_if_in_cache

    return internal_decorator
