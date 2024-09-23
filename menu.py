def menu_option_1():
    print("Bạn đã chọn tùy chọn 1.")

def menu_option_2():
    print("Bạn đã chọn tùy chọn 2.")

def menu_option_3():
    print("Bạn đã chọn tùy chọn 3.")

def exit_menu():
    print("Thoát khỏi chương trình.")

def main_menu():
    options = {
        '1': menu_option_1,
        '2': menu_option_2,
        '3': menu_option_3,
        '4': exit_menu
    }

    while True:
        print("\nMenu:")
        print("1. Tùy chọn 1")
        print("2. Tùy chọn 2")
        print("3. Tùy chọn 3")
        print("4. Thoát")

        choice = input("Chọn một tùy chọn: ")

        if choice in options:
            options[choice]()  # Gọi hàm tương ứng với tùy chọn
            if choice == '4':
                break
        else:
            print("Tùy chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main_menu()



print("Hello")