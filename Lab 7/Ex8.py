celeb = ("Talor Swift", "Christiano Ronaldo", "Trevor Noah", "Dua Lipa", "Jungkook")
ages = (34, 38, 39, 27, 26)

celeb_list = []
for person in celeb:
    celeb_list.append(person)

age_list = [age for age in ages]

celeb_dictionary = {"celebs": celeb_list, "ages": age_list}
    print(celeb_dictionary)