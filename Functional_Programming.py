def apply_all_func(int_list, *functions):
    # Создаем пустой словарь для результатов
    results = {}

    # Перебираем все переданные функции
    for func in functions:
        try:
            # Применяем функцию к списку и сохраняем результат под её именем
            results[func.__name__] = func(int_list)
        except Exception as e:
            # Если функция вызвала ошибку, можно сохранить информацию об ошибке
            results[func.__name__] = f"Error: {str(e)}"

    return results


# Пример использования
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

# Вывод на консоль:
# {'max': 20, 'min': 6}
# {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}