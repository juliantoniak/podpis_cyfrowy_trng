import os
import open_files_aux_functions

def display_menu(file_list):
    print("\n===== FILES MENU =====")
    for i, filename in enumerate(file_list):
        print(f"{i+1}. {filename}")
    # print("0. Exit")

# def show_file_content(filepath):
#     with open(filepath, 'r') as file:
#         content = file.read()
#         print(f"File: {filepath}\n")
#         print(content)

def show_file_content(filepath):
    _, file_extension = os.path.splitext(filepath)
    generated_hash = open_files_aux_functions.make_hash_from_file(filepath) # return hash
    authenticated = open_files_aux_functions.check_signature_if_valid(filepath, generated_hash)
    # authenticated = True
    
    if(authenticated):
        # if file_extension.lower() == '.txt':
        #     open_files_aux_functions.open_txt_file(filepath)
        # elif file_extension.lower() == '.jpg' or file_extension.lower() == '.jpeg':
        #     open_files_aux_functions.open_jpg_jpeg_file(filepath)
        # else:
        #     print(f"Unsupported file type: {file_extension}")

        print("All good! It is the same file with valid signature.")
    else:
        print("Not the same file or signature! Authentication failed.")

def main():
    folder_path = './B/received_files'

    # check existing files in the folder
    file_list = os.listdir(folder_path)
    file_list = [f for f in file_list if os.path.isfile(os.path.join(folder_path, f))]
    if not file_list:
        print("No files in folder "+ folder_path)
        return

    # Get user's choice
    while True:
        # Display menu
        display_menu(file_list)

        choice = input("Choose a file to open or write q to quit & exit: ")
        choice_int = 0
        if choice != 'q':
            choice_int = int(choice)

        if choice_int in range(1, len(file_list)+1):
            # print(choice_int)
            selected_file = file_list[choice_int - 1]
            # print(selected_file)
            file_path = os.path.join(folder_path, selected_file)
            # print(file_path)
            show_file_content(file_path)
        elif choice.lower() == 'q':
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
