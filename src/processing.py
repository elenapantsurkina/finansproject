def filter_by_state(
    inform_state_list: list[dict[str, str | int]], state_id: str = "EXECUTED"
) -> list[dict[str, str | int]]:
    """Функция, которая принимает на вход список словарей и значение для ключа
    state и выдает новый список с заданным ключом"""

    list_state = []

    for key in inform_state_list:
        if key.get("state") == state_id:
            list_state.append(key)

    return list_state


def sort_by_date(inform_state_list: list[dict[str, str | int]], reverse: bool = True) -> list[dict[str, str | int]]:
    """Функция сортирующая исходные данные по дате"""

    sorted_inform = sorted(inform_state_list, key=lambda inform_state: inform_state["date"], reverse=reverse)

    return sorted_inform
