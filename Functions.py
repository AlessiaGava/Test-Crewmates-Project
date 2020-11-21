#get_volleyball_player
#get_team
#get_height
#get_year

#get_year Luisa Yang

#Create a dictionary matching "NAME" and "BIRTH_YEAR" columns:
dict_year = dict(zip(df.NAME, df.BIRTH_YEAR))

#Kindly ask user the inputs specificly for the BIRTH_YEAR
search_birth_year = input("Whose birthday year do you wish to know? Write SURNAME NAME: ")

def get_year(name):
    for name, birth_year in dict_year.items():
        if name == search_birth_year:
            print(birth_year)
        else:
            print("Apologies, the birth year of the person you are looking for may not be available or it may be written in the wrong way. Try again."

#get_nationality
#choose_team
#get_members
