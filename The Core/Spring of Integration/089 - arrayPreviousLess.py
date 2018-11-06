def arrayPreviousLess(items):
    return [next((b for b in items[:i][::-1] if b < a), -1) for i, a in enumerate(items)]
