from cache import get_cached_result, store_result

text = "I am very happy today"

result = {"joy": 0.82}

store_result(text, result)

cached = get_cached_result(text)

print(cached)