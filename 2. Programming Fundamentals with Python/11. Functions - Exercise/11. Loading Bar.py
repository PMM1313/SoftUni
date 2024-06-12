def loading_bar(percentage):
    bar_length = percentage // 10
    loading_bar = f"[{'%' * bar_length}{'.' * (10 - bar_length)}]"
    if percentage == 100:
        print(f"{percentage}% Complete!\n{loading_bar}")
    else:
        print(f"{percentage}% {loading_bar}")
        print("Still loading...")

percentage = int(input())
loading_bar(percentage)