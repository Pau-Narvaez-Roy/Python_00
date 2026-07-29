def ft_count_harvest_iterative() -> None:
    harvest = int(input("Days until harvest: "))
    if harvest < 1:
        print("Error")
    for i in range(harvest):
        print(f"Day {i + 1}")
