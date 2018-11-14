def greatRenaming(roadRegister):
    swap = lambda x: [x[-1]] + x[:-1]
    return swap([swap(row) for row in roadRegister])
