"""
Title: CD_Inventory.py
Desc: Assignnment 08 - Working with classes
Change Log: (Who, When, What)
DBiesinger, 2030-Jan-01, created file
DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
NToulas, 2022-Jun-14, Modified file
"""

import pickle

# -- DATA -- #
STR_FILE_NAME = 'cdInventory.txt'
cd_objects_list = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # -- Fields -- #
    cd_id = 0
    cd_title = ''
    cd_artist = ''

    # TODO Add Code to the CD class
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

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODO Add code to process data from a file
    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.
        """
        table.clear()  # this clears existing data and allows to load data from file
        try:
            with open(file_name, 'rb') as file:
                data = pickle.load(file)
            for line in data:
                table.append(line)
            return table
        except FileNotFoundError:
            print('File does not exist')

    # TODO Add code to process data to a file
    @staticmethod
    def write_file(file_name, table):
        """Function to write data to file

        Writes the data to file identified by file_name into CSV format

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        with open(file_name, 'wb') as file:
            pickle.dump(table, file)
    pass

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling of input and output:

    properties:

    methods:


    """

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    @staticmethod
    def ask_for_cd_info():
        """Prompts user for CD info

        Returns:
            result: list of user input (ID, CD title, artist)

        """
        str_id = input('Enter ID: ').strip()
        str_title = input('What is the CD\'s title? ').strip()
        st_artist = input('What is the Artist\'s name? ').strip()
        return str_id, str_title, st_artist


# -- Main Body of Script -- #
# TODO Add Code to the main body
# Load data from file into a list of CD objects on script start
# Display menu to user
    # show user current inventory
    # let user add data to the inventory
    # let user save inventory to file
    # let user load inventory from file
    # let user exit program

