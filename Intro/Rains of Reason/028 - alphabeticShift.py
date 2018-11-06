def alphabeticShift(inputString):
  res = ''
  for c in list(inputString) :
    res += chr(97) if ord(c)==122 else chr(ord(c)+1)
  return "".join(res)
