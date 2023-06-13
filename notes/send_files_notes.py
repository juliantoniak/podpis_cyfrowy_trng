# def handle_initial_menu():
#     while True:
#         display_menu_initial()
#         initial_choice = input("Choose (1-2) options or write q to quit & exit: ")
        
#         if initial_choice == '1':
#             initial_option_generate_new_rsa_key()
#         elif initial_choice == '2':
#             initial_option_send_files()
#             break
#         elif initial_choice.lower() == 'q':
#             print("Program ended.")
#             break
#         else:
#             print("Invalid choice. Try again.")

# def handle_files_menu():
#     while True:
#         display_menu_files()
#         file_choice = input("Choose (1-4) options or write q to quit & exit: ")
#         if file_choice == '1':
#             send_file("./files_to_send/bigos_recipe.txt")
#         elif file_choice == '2':
#             send_file("./files_to_send/cat.jpg")
#         elif file_choice == '3':
#             send_file("./files_to_send/meme.jpg")
#         elif file_choice == '4':
#             send_file("./files_to_send/secret_info_for_Bob.txt")