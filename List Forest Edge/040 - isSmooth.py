def isSmooth(arr):
    return False if arr[0] != arr[-1] else arr[0] == ( arr[len(arr) // 2] + arr[(len(arr) // 2) - 1] if len(arr) % 2 == 0 else arr[len(arr) // 2] )
