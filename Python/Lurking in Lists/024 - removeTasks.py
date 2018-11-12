def removeTasks(k, toDo):
    del (toDo[k-1::k])
    return toDo
