import subprocess
import send_files_aux_functions
import os

########################################################
# initial options
def initial_option_generate_new_rsa_key():
    print("New key will be generated in a moment...")
    subprocess.run(["python", "../rsa/generate_rsa.py"])
    send_files_aux_functions.update_Bens_received_public_key()

def initial_option_send_files():
    print("Send files option has been chosen. Now choose which file you want to send...")

########################################################
# files options
def send_file(filepath):
    print("Sending " + filepath + " to Bob...", )
    generated_hash = send_files_aux_functions.make_hash_from_file(filepath)
    output_sig_filepath = send_files_aux_functions.make_signature_with_private_key(filepath, generated_hash)
    send_files_aux_functions.send_original_file(filepath)
    send_files_aux_functions.send_signature_file(output_sig_filepath)

########################################################
# menu displays
def display_menu_initial():
    print("\n===== INITIAL MENU =====")
    print("1. Generate new rsa key")
    print("2. Sign and send files")
    print("=================")

# def display_menu_files():
#     print("\n===== FILES MENU =====")
#     print("1. Bigos recipe")
#     print("2. Cat photo")
#     print("3. University meme")
#     print("4. Secret info for Bob")
#     print("=================")

def display_menu_files(file_list):
    print("\n===== FILES MENU =====")
    for i, filename in enumerate(file_list):
        print(f"{i+1}. {filename}")

########################################################
# menus
def main():

    while True:
        display_menu_initial()
        initial_choice = input("Choose (1-2) options or write q to quit & exit: ")

        if initial_choice == '1':
            initial_option_generate_new_rsa_key()
        elif initial_choice == '2':
            initial_option_send_files()
            folder_path = './A/files_to_send'
            # check existing files in the folder
            file_list = os.listdir(folder_path)
            file_list = [f for f in file_list if os.path.isfile(os.path.join(folder_path, f))]
            if not file_list:
                print("No files in folder "+ folder_path)
                return
            while True:
                display_menu_files(file_list)
                choice = input("Choose a file to send or write q to quit & exit: ")
                choice_int = 0
                if choice != 'q':
                    choice_int = int(choice)

                if choice_int in range(1, len(file_list)+1):
                    # print(choice_int)
                    selected_file = file_list[choice_int - 1]
                    # print(selected_file)
                    file_path = os.path.join(folder_path, selected_file)
                    # print(file_path)
                    send_file(file_path)
                elif choice.lower() == 'q':
                    print("Program terminated.")
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif initial_choice.lower() == 'q':
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



