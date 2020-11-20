#get_volleyball_player
#get_team
#get_height_Alessia Zhou

#I create a dictionary containing the "NAME" and "HEIGHT" columns as keys and values respectively:
dict_height = dict(zip(df.NAME, df.HEIGHT))
#Ask the user to provide the name and surname of the player:
search_height = input("provide name and surname")

def give_height(name):
    for name,height in dict_height.items():
        if name == search_height:
            print(height)

#get_year
#get_nationality
#choose_team
#get_members
