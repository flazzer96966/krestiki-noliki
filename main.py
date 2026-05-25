print("=== КРЕСТИКИ-НОЛИКИ ===")

game_active = True

while game_active:
    
    print("\nГлавное меню:")
    print("1. Начать новую игру")
    print("2. Правила игры")
    print("3. Выйти")
    
    menu_choice = input("Выберите пункт меню (1-3): ")
    
    if menu_choice == "1":
        
        field = [
            [" ", " ", " "],
            [" ", " ", " "], 
            [" ", " ", " "]
        ]
        
        current_player = "X"
        game_finished = False
        move_count = 0
        
        print("\n=== НАЧАЛО НОВОЙ ИГРЫ ===")
        print("Игроки поочередно вводят координаты от 1 до 3")
        print("Формат ввода: строка столбец (например: 1 2)")
        
        while not game_finished:
            
            print("\nТекущее поле:")
            print("  1 2 3")
            row_num = 1
            while row_num <= 3:
                print(f"{row_num} {field[row_num-1][0]}|{field[row_num-1][1]}|{field[row_num-1][2]}")
                if row_num < 3:
                    print("  -----")
                row_num += 1
            
            valid_input = False
            while not valid_input:
                player_input = input(f"\nИгрок {current_player}, ваш ход: ")
                
                if len(player_input) == 3 and player_input[1] == " ":
                    row_char = player_input[0]
                    col_char = player_input[2]
                    
                    if row_char in "123" and col_char in "123":
                        row = int(row_char) - 1
                        col = int(col_char) - 1
                        
                        if field[row][col] == " ":
                            field[row][col] = current_player
                            move_count += 1
                            valid_input = True
                        else:
                            print("Эта ячейка уже занята! Выберите другую.")
                    else:
                        print("Координаты должны быть от 1 до 3!")
                else:
                    print("Неверный формат! Введите две цифры от 1 до 3 через пробел.")
            
            # Проверка победителя по строкам
            i = 0
            winner = None
            while i < 3:
                if field[i][0] == field[i][1] == field[i][2] != " ":
                    winner = field[i][0]
                i += 1
            
            # Проверка по столбцам
            i = 0
            while i < 3:
                if field[0][i] == field[1][i] == field[2][i] != " ":
                    winner = field[0][i]
                i += 1
            
            # Проверка диагоналей
            if field[0][0] == field[1][1] == field[2][2] != " ":
                winner = field[0][0]
            
            if field[0][2] == field[1][1] == field[2][0] != " ":
                winner = field[0][2]
            
            if winner is not None:
                print("\nФинальное поле:")
                print("  1 2 3")
                row_num = 1
                while row_num <= 3:
                    print(f"{row_num} {field[row_num-1][0]}|{field[row_num-1][1]}|{field[row_num-1][2]}")
                    if row_num < 3:
                        print("  -----")
                    row_num += 1
                print(f"\nПобедил игрок {winner}!")
                game_finished = True
            elif move_count == 9:
                print("\nФинальное поле:")
                print("  1 2 3")
                row_num = 1
                while row_num <= 3:
                    print(f"{row_num} {field[row_num-1][0]}|{field[row_num-1][1]}|{field[row_num-1][2]}")
                    if row_num < 3:
                        print("  -----")
                    row_num += 1
                print("\nНичья!")
                game_finished = True
            else:
                # Смена игрока
                if current_player == "X":
                    current_player = "O"
                else:
                    current_player = "X"
        
        print("\nИгра завершена!")
        back_to_menu = input("Нажмите Enter чтобы вернуться в меню...")
    
    elif menu_choice == "2":
        
        print("\n=== ПРАВИЛА ИГРЫ ===")
        print("1. Игроки по очереди ставят на свободные клетки поля 3×3 знаки")
        print("2. Один игрок играет 'X', другой - 'O'")
        print("3. Первый, выстроивший в ряд 3 своих фигуры, выигрывает")
        print("4. Игроки вводят координаты в формате: СТРОКА СТОЛБЕЦ")
        print("5. Например: '1 2' - первая строка, второй столбец")
        print("6. Если все клетки заполнены, но нет победителя - ничья")
        
        print("\nПример поля с координатами:")
        print("  1 2 3")
        print("1  | | ")
        print("  -----")
        print("2  | | ")
        print("  -----")
        print("3  | | ")
        
        back_to_menu = input("\nНажмите Enter чтобы вернуться в меню...")
    
    elif menu_choice == "3":
        
        print("\nСпасибо за игру! До свидания!")
        game_active = False
    
    else:
        print("Неверный выбор! Введите цифру от 1 до 3.")