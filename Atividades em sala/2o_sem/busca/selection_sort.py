def menor(lista: list, pos: int) -> int:
    aux = lista[pos]
    aux_pos = pos
    pos += 1

    while pos < len(lista):
        if lista < pos:
            print()