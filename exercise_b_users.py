users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print("Johnathan's Twitter handle is " + str(users["Jonathan"]["twitter"]))

# 2. Get Erik's hometown
print("Erik's hometown is " + str(users["Erik"]["home_town"]))

# 3. Get the list of Erik's lottery numbers
print("Eric's lottery numbers are: " + str(users["Erik"]["lottery_numbers"]))

# 4. Get the species of Avril's pet Monty
print("The species of Avril's pet Monty is " + str(users["Avril"]["pets"][0]["species"]))

# 5. Get the smallest of Erik's lottery numbers
erik_numbers = users["Erik"]["lottery_numbers"]
erik_min = min(erik_numbers)
print("Erics smallest lottery number is " + str(erik_min))

# 6. Return an list of Avril's lottery numbers that are even
print("Avril's even lottery numbers are as follows:")
avril_numbers = users["Avril"]["lottery_numbers"]
for number in avril_numbers:
  if number % 2 == 0:
    print(number)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]["lottery_numbers"].append(7)

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"

# 9. Add a pet dog to Erik called "fluffy"
users["Erik"]["pets"].append({"name" : "fluffy" , "species" : "dog"})

# 10. Add another person to the users dictionary

users["Ewan"] = {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "bonnie",
        "species": "dog"
      }
    ]
  }

# print(users["Ewan"]["pets"][0]["species"])


