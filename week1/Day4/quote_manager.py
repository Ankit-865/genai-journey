# Day 4: Quote Manager App
import random  
def add_quote(quote, quote_list):  
    if quote.strip() == "":  
        return "Error: Quote cannot be empty!"  
    if quote in set(quote_list):  
        return "Error: Quote already exists!"  
    quote_list.append(quote)  
    return "Quote added successfully!" 

def view_quotes(quote_list):  
    if not quote_list: 
        return "No quotes yet!"  
    return "\n".join(f"{i+1}. {q}" for i, q in enumerate(quote_list)) 

def delete_quote(index, quote_list):  
    if not quote_list:  
        return "Error: No quotes to delete!"  
    if 1 <= index <= len(quote_list):  
        return f"Deleted quote: {quote_list.pop(index-1)}"  
    return "Error: Invalid index!"  

def random_quote(quote_list):  
    if not quote_list:  
        return "Error: No quotes available!"  
    return random.choice(quote_list) 

quotes = []  
while True: 
    print("\nQuote Manager Menu:")  
    print("1. Add Quote")  
    print("2. View Quotes")  
    print("3. Delete Quote")  
    print("4. Random Quote")  
    print("5. Quit")  
    choice = input("Choose (1-5): ")  

    if choice == "1":  
        quote = input("Enter quote: ")  
        print(add_quote(quote, quotes))  
    elif choice == "2":  
        print(view_quotes(quotes))  
    elif choice == "3":  
        try:  
            index = int(input("Enter quote number to delete: "))  
            print(delete_quote(index, quotes))  
        except ValueError:  
            print("Error: Enter a valid number!") 
    elif choice == "4":  
        print(random_quote(quotes))   
    elif choice == "5":  
        print("Goodbye!")  
        break  
    else:  
        print("Invalid choice! Choose 1-5.")  