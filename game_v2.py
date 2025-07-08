"""Игра 'Угадай число'
Компьютер сам загадывает и сам угадывает число
Сравнение алгоритмов: случайный поиск vs бинарный поиск
"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """Угадываем число случайным образом
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    
    Returns:
        int: Число попыток
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            return count

def game_core_v3(number: int = 1) -> int:
    """Угадываем число методом бинарного поиска
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    
    Returns:
        int: Число попыток
    """
    count = 0
    low, high = 1, 100
    
    while low <= high:
        count += 1
        predict = (low + high) // 2
        if number == predict:
            return count
        elif number > predict:
            low = predict + 1
        else:
            high = predict - 1
    return count

def score_game(predict_func, n_iter=1000) -> int:
    """Тестируем алгоритм угадывания
    
    Args:
        predict_func: Функция угадывания
        n_iter: Количество тестовых прогонов
    
    Returns:
        int: Среднее количество попыток
    """
    np.random.seed(1)  # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=n_iter)
    counts = [predict_func(number) for number in random_array]
    score = int(np.mean(counts))
    print(f"Алгоритм {predict_func.__name__} угадывает число в среднем за: {score} попыток")
    return score

if __name__ == "__main__":
    # Сравниваем алгоритмы
    score_game(random_predict)
    score_game(game_core_v3)