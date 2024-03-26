def read_text_file_to_list(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            # Remove newline characters and create a list
            word_list = [line.strip() for line in lines]
            return word_list
    except Exception as e:
        print(f"File '{file_path}' not found. Error {e}")
        return []
# Example usage: Read words from "words.txt" and store them in a list
file_path = "words.txt"
word_list = read_text_file_to_list(file_path)


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = '''
 __    __                                                                 
/  |  /  |                                                                
$$ |  $$ |  ______   _______    ______   _____  ____    ______   _______  
$$ |__$$ | /      \ /       \  /      \ /     \/    \  /      \ /       \ 
$$    $$ | $$$$$$  |$$$$$$$  |/$$$$$$  |$$$$$$ $$$$  | $$$$$$  |$$$$$$$  |
$$$$$$$$ | /    $$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ | /    $$ |$$ |  $$ |
$$ |  $$ |/$$$$$$$ |$$ |  $$ |$$ \__$$ |$$ | $$ | $$ |/$$$$$$$ |$$ |  $$ |
$$ |  $$ |$$    $$ |$$ |  $$ |$$    $$ |$$ | $$ | $$ |$$    $$ |$$ |  $$ |
$$/   $$/  $$$$$$$/ $$/   $$/  $$$$$$$ |$$/  $$/  $$/  $$$$$$$/ $$/   $$/ 
                              /  \__$$ |                                  
                              $$    $$/                                   
                               $$$$$$/                                    '''

                                                                    
                                                                    

