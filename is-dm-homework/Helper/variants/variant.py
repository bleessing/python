import random


def generate_variants(tasks, total):
    counts = []
    for i in tasks:
        counts.append(len(i))
    result = set()
    while len(result) < total:
        result.add(generate_variant(counts))
    return list(result)


def generate_variant(counts):
    result = []
    for i in range(len(counts)):
        result.append(random.randint(1, counts[i]))
    return tuple(result)
