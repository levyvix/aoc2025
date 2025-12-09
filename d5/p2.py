from icecream import ic

ranges, products = open(0).read().split("\n\n")
ranges = [r for r in ranges.splitlines()]
products = [p for p in products.splitlines()]


def merge_and_count(intervalos):
    if not intervalos:
        return 0

    # 1. Ordena pelos valores de início
    intervalos = sorted(intervalos)  # ordena por [start, end]

    total = 0
    atual_inicio = intervalos[0][0]
    atual_fim = intervalos[0][1]

    for inicio, fim in intervalos[1:]:
        if inicio <= atual_fim + 1:  # tem sobreposição ou encosta
            atual_fim = max(atual_fim, fim)
        else:
            # termina o intervalo atual
            tamanho = atual_fim - atual_inicio + 1
            total += tamanho
            # começa novo
            atual_inicio = inicio
            atual_fim = fim

    # não esquece do último!
    tamanho = atual_fim - atual_inicio + 1
    total += tamanho
    return total


# sort the ranges by first number
ranges_sorted = sorted(ranges, key=lambda x: int(x.split("-")[0]))
intervalos = []
for r in ranges_sorted:
    init, end = r.split("-")
    init, end = int(init), int(end)
    intervalos.append([init, end])
ic(merge_and_count(intervalos))
