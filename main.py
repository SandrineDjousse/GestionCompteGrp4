# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import string
import compte
from pip._vendor.distlib.compat import raw_input


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    choix = compte.choix()
    compte.traitement(choix)


    while choix != 8:
        choix = compte.choix()
        compte.traitement(choix)
    print("Merci Aurevoir")


