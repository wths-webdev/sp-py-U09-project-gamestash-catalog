# Game Stash!
<img src="./images/game-stash-logo.png" width=120>  

The Game Stash codebase needs some updates and you are up for the challenge! You are given starter code and need to function-ize it:

1. First, take 3 minutes to become familiar with the given code. Take note of the dictionary of gaes and the conditional statements.
2. Turn each conditional statement into its own function:
    * Create the add_game() function: we're going to start this as a group.
    * Create the remove_game() function.
    * Break the "show" conditional into two functions: 
        * one function for the inventory count
        * the other function for printing the games
    * Create the search_year() function.
    * Make sure to only print games if the year exists in the dictionary
    * search_title(): implement your own search  
    
There are extra challenges at the bottom.

### Sample Runs
```
Welcome to...
 _____________________________   
/        _____________        \  
| == .  |             |     o |
|   _   |             |    B  |
|  / \  |   Game      | A   O |
| | O | |      Stash  |  O    |
|  \_/  |             |       |
|  :::  |_____________| . . . |
\_____________________________/

----------- Menu ----------
Add game (add)
Remove game (remove)
Show inventory (show)
Search by year (year)
Search for a title (title)
Quit (q)

What would you like to do? add
What game would you like to add?
Title: Red Dead Redemption 2
Year released: 2018
Red Dead Redemption 2 was added successfully.
```
```
What would you like to do? remove
What title would you like to remove? fsdfds
Error: fsdfds not in inventory.
```
```
What would you like to do? year
Which year would you like to seach for? 2017
All games from 2017:
   1. The Legend of Zelda: Breath of the Wild
   2. Super Mario Odyssey
   3. Mario Kart 8 Deluxe

----------- Menu ----------
Add game (add)
Remove game (remove)
Show inventory (show)
Search by year (year)
Search for a title (title)
Quit (q)

What would you like to do? show
There are 9 games in your inventory.
   1. GTA V by 2013
   2. Spider-Man: Miles Morales by 2020
   3. The Legend of Zelda: Breath of the Wild by 2017
   4. God of War by 2022
   5. The Legend of Zelda: Tears of the Kingdom by 2023
   6. Super Mario Odyssey by 2017
   7. Princess Peach by 2024
   8. Mario Kart 8 Deluxe by 2017
   9. Red Dead Redemption 2 by 2018
```

## Extra Challenge
* add_game: if the game is already in the dictionary, don't add it.
* remove_game(): if the game isn't found, let the user know.
* Allow the title search feature to include any game containing the searched word(s).

### Extra Challenge Sample Run
```
Which title would you like to search for? mario

There are 2 game(s) found containing mario:
   1. Super Mario Odyssey - 2017
   2. Mario Kart 8 Deluxe - 2017
```

## The menu
```
print(" _____________________________  \n"
    "/        _____________        \\\n"
    "| == .  |             |     o |\n"
    "|   _   |             |    B  |\n"
    "|  / \\  |   Game      | A   O |\n"
    "| | O | |      Stash  |  O    |\n"
    "|  \\_/  |             |       |\n"
    "|  :::  |_____________| . . . |\n"
    "\\_____________________________/")
```