import sys
import utils

def main():
    while True:
        print("\n")
        files = utils.print_inputs_menu()
        if not files:
            return
        try:
            choice = input()
            index = int(choice)
            if index == 0:
                return
            if 1 <= index <= len(files):
                selected_file = files[index - 1]
                print(f"{selected_file}...")
                content = utils.read_text_file(selected_file)
                print("----------------------------------------\n")
                print(content)
                print("----------------------------------------\n")
            else:
                print(f"Invalid choice. Please enter a number between 0 and {len(files)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")        
    

if __name__ == "__main__":
    main()