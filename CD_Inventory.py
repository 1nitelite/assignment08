"""
Title: CD_Inventory.py
Desc: Assignnment 08 - Working with classes
Change Log: (Who, When, What)
DBiesinger, 2030-Jan-01, created file
DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
NToulas, 2022-Jun-14, Modified file
NToulas, 2022-Jun-19, Modified file
NToulas, 2022-Jun-20, Modified file
"""

import pickle

# -- DATA -- #
STR_FILE_NAME = 'cdInventory.dat'
cd_objects_list = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """


    # -- Constructor -- #
    def __init__(self, cd_id, cd_title, cd_artist):
        # -- Attributes -- #
        self._cd_id = cd_id
        self._cd_title = cd_title
        self._cd_artist = cd_artist

    @property
    def cd_id(self):
        return self._cd_id

    @cd_id.setter
    def cd_id(self, value):
        self._cd_id = value

    @property
    def cd_title(self):
        return self._cd_title

    @cd_title.setter
    def cd_title(self, value):
        self._cd_title = value

    @property
    def cd_artist(self):
        return self._cd_artist

    @cd_artist.setter
    def cd_artist(self, value):
        self._cd_artist = value

    def __str__(self):
        return f'this is str method {self._cd_id}  {self._cd_title} (by: {self._cd_artist})'


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:
        file_name: (string) with the name of the file

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """

    @staticmethod
    def read_file(file_name):
        """Function to read data from a file using pickle

        Args: file_name (string): name of file used to read the data from

        Returns:
            Data from file
        """
        try:
            with open(file_name, 'rb') as file:
                cd_info = pickle.load(file)
            return cd_info
        except FileNotFoundError:
            pass

    # TODO Add code to process data to a file
    @staticmethod
    def write_file(file_name, table):
        """Function to write data to file

        Writes the data to file using pickle

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        with open(file_name, 'wb') as file:
            pickle.dump(table, file)

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling of input and output:

    properties:

    methods:


    """

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        """

        print('Menu (please choose from the following):\n'
              '\t[l] Load inventory from file\n'
              '\t[a] Add CD to inventory\n'
              '\t[d] Display current inventory\n'
              '\t[s] Save inventory to file\n'
              '\t[x] Exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'd', 's', 'x']:
            choice = input('What would you like to do? [l, a, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for cd in table:
            print(f'{cd[0]} {cd[1]} (by: {cd[2]})')
        print('======================================')

    @staticmethod
    def add_cd():
        """Prompts user for CD info

        Returns:
            result: list of user input (ID, CD title, artist)

        """
        cid = input('Enter ID: ').strip()
        title = input('What is the CD\'s title? ').strip()
        artist = input('What is the Artist\'s name? ').strip()
        return cid, title, artist


# -- Main Body of Script -- #
# Load data from file into a list of CD objects on script start
try:
    init_file = FileIO.read_file(STR_FILE_NAME)
    for info in init_file:
        cd_objects_list.append(info)
except EOFError as error:
    pass

# start main loop
while True:
    # Display menu to user
    IO.print_menu()
    str_choice = IO.menu_choice()

    # Process menu selection
    # let user exit program
    if str_choice == 'x':
        break
    # let user load inventory from file
    if str_choice == 'l':
        try:
            data = FileIO.read_file(STR_FILE_NAME)
            for line in data:
                cd_objects_list.append(line)
            IO.show_inventory(data)
        except EOFError:
            pass
        continue
    # let user add data to the inventory
    elif str_choice == 'a':
        # Ask user for new ID, CD Title and Artist
        result = IO.add_cd()
        # Append result to table
        cd_objects_list.append(result)
        IO.show_inventory(cd_objects_list)
        continue
    # show user current inventory
    elif str_choice == 'd':
        IO.show_inventory(cd_objects_list)
        continue
    # let user save inventory to file
    elif str_choice == 's':
        # Display current inventory and ask user for confirmation to save
        IO.show_inventory(cd_objects_list)
        str_yes_no = input('Save this inventory to file? [y/n] ').strip().lower()
        # Process choice
        if str_yes_no == 'y':
            # save data
            FileIO.write_file(STR_FILE_NAME, cd_objects_list)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue
    # catch-all should not be possible, as user choice gets vetted in IO, but to be safe:
    else:
        print('General Error')
