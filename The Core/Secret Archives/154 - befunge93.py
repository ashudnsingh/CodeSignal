def befunge93(prog):
    class Stack(list):
        def pop(self):
            if self:
                return super().pop()
            return 0

        def popn(self):
            v = self.pop()
            if not isinstance(v, int):
                return ord(v)
            return v

        def __getitem__(self, idx):
            try:
                return super().__getitem__(idx)
            except IndexError:
                return 0

    stk = Stack()
    res = ''
    y = 0
    x = 0
    string_mode = False
    dy = 0
    dx = 1
    for i in range(10**5):
        y = y % len(prog)
        x = x % len(prog[0])
        p = prog[y][x]

        if string_mode and p != '"': stk.append(p)
        elif p == '>': dy, dx = 0, 1
        elif p == '<': dy, dx = 0, -1
        elif p == 'v': dy, dx = 1, 0
        elif p == '^': dy, dx = -1, 0
        elif p == '#': dx *= 2; dy *= 2
        elif p == '_': dy, dx = 0, (1 if stk.popn() == 0 else -1)
        elif p == '|': dy, dx = (1 if stk.popn() == 0 else -1), 0
        elif p == '+': stk.append(stk.popn() + stk.popn())
        elif p == '-': a, b = stk.popn(), stk.popn(); stk.append(b - a)
        elif p == '*': stk.append(stk.popn() * stk.popn())
        elif p == '/': a, b = stk.popn(), stk.popn(); stk.append(b // a)
        elif p == '%': a, b = stk.popn(), stk.popn(); stk.append(b % a)
        elif p == '!': stk.append(1 if stk.pop() == 0 else 0)
        elif p == '`': a, b = stk.popn(), stk.popn(); stk.append(1 if b > a else 0)
        elif p == ':' and stk: stk.append(stk[-1])
        elif p == '\\': a, b = stk.pop(), stk.pop(); stk.append(a); stk.append(b)
        elif p == '$': stk.pop()
        elif p == '.': v = stk.pop(); res += (str(v) if isinstance(v, int) else ord(v)) + ' '
        elif p == ',': v = stk.pop(); res += (v if isinstance(v, str) else chr(v))
        elif p.isdigit(): stk.append(int(p))
        elif p == '@': break
        elif p == '"': string_mode = not string_mode

        x += dx
        y += dy

        if abs(dy) > 1:
            dy = -1 if dy < 0 else 1
        if abs(dx) > 1:
            dx = -1 if dx < 0 else 1

        if len(res) >= 100:
            break

    return res
