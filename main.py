print("=== КРЕСТИКИ-НОЛИКИ ===")

game_active = True

while game_active:
    
    print("\nГлавное меню:")
    print("1. Начать новую игру")
    print("2. Правила игры")
    print("3. Выйти")
    
    menu_choice = input("Выберите пункт меню (1-3): ")
    
    if menu_choice == "1":
        
        # Выбор размера поля
        print("\nВыберите размер поля:")
        print("1. 3×3 (классика)")
        print("2. 4×4")
        size_choice = input("Ваш выбор (1 или 2): ")
        
        if size_choice == "1":
            size = 3
        elif size_choice == "2":
            size = 4
        else:
            print("Неверный выбор. По умолчанию 3×3.")
            size = 3
        
        # Создание пустого поля
        field = []
        for _ in range(size):
            row = []
            for _ in range(size):
                row.append(" ")
            field.append(row)
        
        current_player = "X"
        game_finished = False
        move_count = 0
        
        print(f"\n=== НАЧАЛО НОВОЙ ИГРЫ {size}×{size} ===")
        print(f"Игроки поочередно вводят координаты от 1 до {size}")
        print("Формат ввода: строка столбец (например: 1 2)")
        
        # Функция проверки победителя
        def check_winner(board, size):
            # Проверка строк
            for i in range(size):
                for j in range(size - 3):
                    if board[i][j] != " " and board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3]:
                        return board[i][j]
            
            # Проверка столбцов
            for i in range(size - 3):
                for j in range(size):
                    if board[i][j] != " " and board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j]:
                        return board[i][j]
            
            # Проверка главных диагоналей (вниз-вправо)
            for i in range(size - 3):
                for j in range(size - 3):
                    if board[i][j] != " " and board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3]:
                        return board[i][j]
            
            # Проверка побочных диагоналей (вниз-влево)
            for i in range(size - 3):
                for j in range(3, size):
                    if board[i][j] != " " and board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3]:
                        return board[i][j]
            
            return None
        
        while not game_finished:
            
            print("\nТекущее поле:")
            
            # Вывод номеров столбцов
            print("  ", end="")
            for i in range(size):
                print(f" {i+1}", end="")
            print()
            
            # Вывод поля
            for i in range(size):
                print(f"{i+1} ", end="")
                for j in range(size):
                    print(field[i][j], end="")
                    if j < size - 1:
                        print("|", end="")
                print()
                if i < size - 1:
                    print("  ", end="")
                    for _ in range(size * 2 - 1):
                        print("-", end="")
                    print()
            
            # Ввод координат
            valid_input = False
            while not valid_input:
                try:
                    player_input = input(f"\nИгрок {current_player}, ваш ход (строка столбец): ")
                    parts = player_input.split()
                    
                    if len(parts) != 2:
                        print(f"Нужно ввести 2 числа! Пример: 1 2")
                        continue
                    
                    row = int(parts[0]) - 1
                    col = int(parts[1]) - 1
                    
                    if row < 0 or row >= size or col < 0 or col >= size:
                        print(f"Ошибка! Координаты должны быть от 1 до {size}")
                        continue
                    
                    if field[row][col] != " ":
                        print("Эта клетка уже занята! Выберите другую.")
                        continue
                    
                    field[row][col] = current_player
                    move_count += 1
                    valid_input = True
                    
                except ValueError:
                    print("Ошибка! Введите два целых числа через пробел")
            
            # Проверка победы
            winner = check_winner(field, size)
            
            if winner is not None:
                print("\n=== ИГРА ОКОНЧЕНА ===")
                print("Финальное поле:")
                print("  ", end="")
                for i in range(size):
                    print(f" {i+1}", end="")
                print()
                for i in range(size):
                    print(f"{i+1} ", end="")
                    for j in range(size):
                        print(field[i][j], end="")
                        if j < size - 1:
                            print("|", end="")
                    print()
                    if i < size - 1:
                        print("  ", end="")
                        for _ in range(size * 2 - 1):
                            print("-", end="")
                        print()
                print(f"\n🏆 ПОБЕДИЛ ИГРОК {winner}! 🏆")
                game_finished = True
                
            elif move_count == size * size:
                print("\n=== ИГРА ОКОНЧЕНА ===")
                print("Финальное поле:")
                print("  ", end="")
                for i in range(size):
                    print(f" {i+1}", end="")
                print()
                for i in range(size):
                    print(f"{i+1} ", end="")
                    for j in range(size):
                        print(field[i][j], end="")
                        if j < size - 1:
                            print("|", end="")
                    print()
                    if i < size - 1:
                        print("  ", end="")
                        for _ in range(size * 2 - 1):
                            print("-", end="")
                        print()
                print("\n🤝 НИЧЬЯ! 🤝")
                game_finished = True
            else:
                # Смена игрока
                if current_player == "X":
                    current_player = "O"
                else:
                    current_player = "X"
        
        input("\nНажмите Enter чтобы вернуться в меню...")
    
    elif menu_choice == "2":
        
        print("\n=== ПРАВИЛА ИГРЫ ===")
        print("1. Игроки по очереди ставят X и O на свободные клетки")
        print("2. Побеждает тот, кто первым соберет 4 своих знака в ряд:")
        print("   - По горизонтали")
        print("   - По вертикали")
        print("   - По диагонали")
        print("3. Для поля 3×3 достаточно собрать 3 знака в ряд")
        print("4. Координаты вводятся через пробел: строка столбец")
        print("5. Пример: '1 2' - первая строка, второй столбец")
        
        print("\nПример поля 4×4:")
        print("   1 2 3 4")
        print("1   | | | ")
        print("  --------")
        print("2   | | | ")
        print("  --------")
        print("3   | | | ")
        print("  --------")
        print("4   | | | ")
        
        input("\nНажмите Enter чтобы вернуться в меню...")
    
    elif menu_choice == "3":
        print("\nСпасибо за игру! До свидания!")
        game_active = False
    
    else:
        print("Неверный выбор! Введите цифру от 1 до 3.")
