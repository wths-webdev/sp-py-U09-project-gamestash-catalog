games = {
    "GTA V": 2013,
    "Ratchet & Clank": 2021,
    "Spider-Man: Miles Morales": 2020,
    "God of War Ragnarok": 2022,
    "The Legend of Zelda: Tears of the Kingdom": 2023,
    "Super Mario Odyssey": 2017,
    "Princess Peach": 2024,
    "Mario Kart 8 Deluxe": 2017
}

# get_inventory_count(): Returns how many total games there are in a readable format.
    

# add_game(title, year): Adds a game to the inventory.


# remove_game(title): Removes a game from the inventory.


# display_inventory()


# search_year(year)


# search_title(title)



# Welcome message
print("\nWelcome to...")
print(" _____________________________  \n"
    "/        _____________        \\\n"
    "| == .  |             |     o |\n"
    "|   _   |             |    B  |\n"
    "|  / \\  |   Game      | A   O |\n"
    "| | O | |      Stash  |  O    |\n"
    "|  \\_/  |             |       |\n"
    "|  :::  |_____________| . . . |\n"
    "\\_____________________________/")

while True:
    # Display menu to user
    print()
    print("----------- Menu ----------")
    print("Add game (add)")
    print("Remove game (remove)")
    print("Show inventory (show)")
    print("Search by year (year)")
    print("Search for a title (title)")
    print("Quit (q)\n")
    user_selection = input("What would you like to do? ").lower()

    # Use conditional statements to call functions based on user input
    if user_selection == "add":
        print("What game would you like to add?")
        title = input("Title: ")
        year = input("Year released: ")

        # update() will add to the dictionary if the key does not exist
        games.update({title: year})

    elif user_selection == "remove":
        game = input("What title would you like to remove? ")

        games.pop(title)
        print(title + " was removed successfully.")
    
    elif user_selection == "show":
        # function 1:
        print("There are " + str(len(games)) + " games in your inventory.")

        # function 2:
        count = 1
        for game in games:
            # for key in games, games[key] returns the value
            print(f"   {str(count)}. {game} by {games[game]}")
            count += 1
        print()

    elif user_selection == "year":
        year = int(input("Which year would you like to seach for? "))

        print(f"All games from {year}:")
        for game in games:
            if games[game] == year:
                print(f"   {game}")

    elif user_selection == "title":
        title = input("Which title would you like to search for? ")

    elif user_selection == "q":
        print("Bye bye!")
        break # out of the loop

    else:
        print("Error: That was not an option.\n")

print("")