# ****************
# SUMA HETEROGÉNEA
# ****************


def run(items: list) -> int:
    to_dec = [int(i) for i in items]
    sum_items = sum(to_dec)

    return sum_items


if __name__ == '__main__':
    run([1, '2', 3, '4', 5])