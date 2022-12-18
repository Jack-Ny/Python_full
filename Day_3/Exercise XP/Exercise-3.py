# Exercice 3 : Zara
#  brand's dictionary creation
brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': ['blue'],
        'Spain': ['red'],
        'US': ['pink', 'green']
    }
}

# 3. Edit store's number
brand['number_stores'] = 2

# 4. explanation of zara clients
print(f"Zara's customers are men, women, children and those looking for home furnishings.")

# 5. Adding a key
brand['country_creation'] = 'Spain'

# 6. Checking for the presence of the international_competitors key and adding Desigual
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')

# 7. Delete informations about the date of creation
del brand['creation_date']

# 8. Printing of the latest international competitor
print(f"The last international competitor's is {brand['international_competitors'][-1]}.")

# 9. Printing of the main colors of clothing in the United States
print(f"The major colors in the US are {', '.join(brand['major_color']['US'])}.")

# 10. Printing of the amount of key value pairs
print(f"The amount of key value pairs is {len(brand)}")

# 11. Printing te keys of dictionary
print(f"The keys of the dictionary are : {', '.join(brand.keys())}.")

# 12. creation of another dictonary
more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}

# 13. Add information into brand's dictionary
brand.update(more_on_zara)

# 14. Printing de la valeur de la clé number_stores
print(f"The number of Zara stores is now {brand['number_stores']}.")