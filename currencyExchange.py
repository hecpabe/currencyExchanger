

# ========== Preprocess Instructions ==========
# Request to get the exchanges data JSON
import requests
import os

# ========== Global Declarations ==========
# Constants
EXCHANGE_CURRENCY = 1
SHOW_CURRENCIES = 2
EXIT = 3

# URL Where the data is collected
currenciesURL = "https://api.vatcomply.com/currencies"
ratesURL = "https://api.vatcomply.com/rates"

# ========== Main Function ==========
# Name: Main
# Description: Starts the program
# Parameters: None
# Return: None
def main():

    # Needed variables
    execution = True

    # Print welcome message
    clearScreen()
    print("Bienvenido al convertidor de monedas...")
    makePause()
    clearScreen()

    # Execute the program
    while execution:
        showMainMenu()
        execution = makeSelection()

# ========== Functions Coding ==========
# Name: Make Pause
# Description: Function to wait until the user press ENTER
# Paramters: None
# Return: None
def makePause():
    
    input("Pulse 'ENTER' para continuar...")

# Name: Clear Screen
# Description: Function to clear the terminal output
# Paramters: None
# Return: None
def clearScreen():
    
    # NT = Windows / Else = Linux
    os.system('cls' if os.name=='nt' else 'clear')

# Name: Show Main Menu
# Description: Function wich shows the main menu to the user
# Parameters: None
# Return: None
def showMainMenu():
    
    print("----- Menu Principal -----")
    print("1.- Intercambiar monedas.")
    print("2.- Mostrar divisas disponibles.")
    print("3.- Salir")

# Name: Make Selection
# Description: Function to get and execute the user selection
# Parameters: None
# Return: Boolean (True if the program continues and false if the user wants to leave)
def makeSelection():
    
    # Needed variables
    userKeeps = True      # Variable to know if the program should keep running (The user does not leaves)
    selection = 0

    # Get users selection and see what it is
    try:
        selection = int(input("Selección: "))
        if selection == EXCHANGE_CURRENCY:
            exchangeCurrency()
        elif selection == SHOW_CURRENCIES:
            showCurrencies()
        elif selection == EXIT:
            userKeeps = False
        else:
            print("ERROR: La selección introducida no se encuentra en el menú.")
            makePause()
    except:
        print("ERROR: Ha ocurrido un error al realizar la selección, inténtelo de nuevo")
        makePause()
    
    clearScreen()
    
    return userKeeps

# Name: Exchange Currency
# Description: Function to exchange currency (user selects wich currencies)
# Parameters: None
# Return: None
def exchangeCurrency():
    
    # Needed Variables
    currencyFrom = ""
    currencyTo = ""
    amountToExchange = 0
    dataJSON = ""

    clearScreen()

    try:
        # Get user's exchange data
        currencyFrom = input("Introduzca el codigo de la divisa a convertir: ")
        currencyTo = input("Introduzca el codigo de la divisa a la que quiere convertir: ")
        amountToExchange = float(input("Introduzca la cantidad a convertir: "))

        # Get the data from the API with the exchanges for the first currency
        dataJSON = requests.get(ratesURL + "?base=" + currencyFrom).json()

        if len(dataJSON) == 1:
            # The JSON sends error
            print("ERROR: La divisa introducida no existe...")
        else:
            # Print " AMOUNT_TO_EXCHANGE CURRENCY_TO_EXCHANGE = AMMOUNT_EXCHANGED CURRENCY_EXCHANGED"
            print(str(round(amountToExchange, 2)) + " " + currencyFrom + " = " + str(round(amountToExchange * dataJSON["rates"][currencyTo], 2)) + " " + currencyTo)

    except:
        print("ERROR: No has introducido correctamente los datos solicitados")

    makePause()


# Name: Show Currencies
# Description: Function to show all currencies codes
# Paramters: None
# Return: None
def showCurrencies():

    # Needed Variables
    availableCurrencies = ""

    clearScreen()

    print("----- Divisas Disponibles -----")
    print("CODIGO\t| SIMBOLO\t| NOMBRE")
    availableCurrencies = requests.get(currenciesURL).json()
    for i in availableCurrencies:
        print(i + "\t| " + availableCurrencies[i]["symbol"] + "\t\t| " + availableCurrencies[i]["name"])

    makePause()





# ========== Main Function Execution ==========
main()
