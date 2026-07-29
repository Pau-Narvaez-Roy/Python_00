def printer(day) -> None:
    if day > 1:
        printer(day - 1)
    print(f"Day {day}")


def ft_count_harvest_recursive() -> None:
    harvest = int(input("Days until harvest: "))
    if harvest < 1:
        print("Error")
    printer(harvest)
