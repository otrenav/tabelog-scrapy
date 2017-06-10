# -*- coding: utf-8 -*-

prefectures = [
    'aichi',
    'akita',
    'aomori',
    'chiba',
    'ehime',
    'fukui',
    'fukuoka',
    'fukushima',
    'gifu',
    'gunma',
    'hiroshima',
    'hokkaido',
    'hyogo',
    'ibaraki',
    'ishikawa',
    'iwate',
    'kagawa',
    'kagoshima',
    'kanagawa',
    'kochi',
    'kumamoto',
    'kyoto',
    'mie',
    'miyagi',
    'miyazaki',
    'nagano',
    'nagasaki',
    'nara',
    'niigata',
    'oita',
    'okayama',
    'okinawa',
    'osaka',
    'saga',
    'saitama',
    'shiga',
    'shimane',
    'shizuoka',
    'tochigi',
    'tokushima',
    'tokyo',
    'tottori',
    'toyama',
    'wakayama',
    'yamagata',
    'yamaguchi',
    'yamanashi'
]

categories = [
    # "washoku",         ### Washoku (Japanese food)
    # "japanese",        ##  Japanese Cuisine
    # "RC010101",        #   Kaiseki (Traditional Japanese)
    # "RC010103",        #   Kappo (Traditional Japanese)
    # "RC010105",        #   Shojin Cuisine (Buddhist Cuisine)
    # "RC010104",         #   Kyoto Cuisine
    # "sushi",           ##  Sushi
    # "RC010201",        #   Sushi

    "RC010202",        #   Kaitenzushi (Sushi Train)
    "RC010203",        #   Standing style sushi
    "seafood",         ##  Seafood
    "RC011211",        #   Seafood
    "RC011212",        #   Fugu (Blowfish)
    "RC011213",        #   Crab
    "RC011214"         #   Suppon (Soft-shelled Turtle)

    # "RC011215",        #   Angler
    # "RC0103",          ##  Tempura, Fried Foods
    # "tempura",         #   Tempura
    # "tonkatsu",        #   Tonkatsu (Pork cutlet)
    # "kushiage",        #   Kushi-age (Fried Skewer)
    # "RC010304",        #   Boneless deep-fried chicken
    # "RC010399",        #   Fried Foods (other)
    # "RC0104",          ##  Soba, Udon, Noodles
    # "soba",            #   Soba
    # "RC010408",        #   Standing style soba
    # "udon",            #   Udon
    # "RC010407",        #   Curry Udon
    # "RC010406",        #   Chow Mein Noodle
    # "RC010404",        #   Okinawa Soba (Okinawa Noodle)
    # "RC010403",        #   Hoto (Noodle)
    # "RC010405",        #   Champon Noodle
    # "RC010499",        #   Noodles (other)
    # "RC0105",          ##  Unagi (Fleshwater eel), Dojo (Loach)
    # "unagi",           #   Unagi (Freshwater eel)
    # "RC010502",        #   Dojo (Loach)
    # "RC010503",        #   Anago (Sea eel)
    # "RC0106",          ##  Yakitori (Grilled chicken), Kushiyaki (Satay)
    # "yakitori",        #   Yakitori (Grilled chicken)
    # "RC010602",        #   Kushiyaki (Grilled skewer)
    # "RC010604",        #   Grilled tripe
    # "RC010605",        #   Grilled pork
    # "RC010603",        #   Fowl
    # "RC010606",        #   Chicken wings
    # "RC0107",          ##  Sukiyaki, Shabu Shabu
    # "RC010701",        #   Sukiyaki
    # "syabusyabu",      #   Shabu Shabu (Japanese Steamboat)
    # "RC010703",        #   Pork Shabu Shabu
    # "RC0108",          ##  Oden
    # "RC0109",          ##  Okonomiyaki, Takoyaki
    # "okonomiyaki",     #   Okonomiyaki
    # "monjya",          #   Monjya yaki
    # "RC010911",        #   Takoyaki
    # "RC010912",        #   Akashi yaki
    # "RC010999",        #   Okonomiyaki and takoyaki baked (other)
    # "RC0110",          ##  Regional Cuisine
    # "okinawafood",     #   Okinawan Cuisine
    # "RC011002",        #   Kiritanpo (pounded rice skewer)
    # "RC011099",        #   Regional Cuisine (Other)
    # "RC0111",          ##  Donburi
    # "RC011101",        #   Gyu-don (Beef Bowl)
    # "RC011102",        #   Oyako-don (Chicken Bowl)
    # "RC011103",        #   Ten-don (Tempura Bowl)
    # "RC011104",        #   Katsu-don (Pork Cutlet Bowl)
    # "RC011105",        #   Seafood rice bowl
    # "RC011106",        #   Buta-don (Pork Bowl)
    # "RC011199",        #   Donburi (other)
    # "RC0199",          ##  Japanese food (other)
    # "RC019910",        #   Tofu, Yuba
    # "RC019908",        #   Mugitoro (Grated yam and brown rice)
    # "RC019909",        #   Kamameshi (Clay pot rice)
    # "RC019912",        #   Tripe related dishes
    # "RC019911",        #   Whale dishes
    # "RC019907",        #   Gyutan (Beef tongue)
    # "RC019903",        #   Robatayaki
    # "RC019999",        #   Japanese food (other)
    # "RC02",            ### Western food(European food)
    # "RC0201",          ##  Steak Hamburger
    # "steak",           #   Steak
    # "hamburgersteak",  #   Hamburger Steak
    # "RC0203",          ##  Teppan-yaki
    # "RC0202",          ##  Pasta, Pizza
    # "pasta",           #   Pasta
    # "pizza",           #   Pizza
    # "hamburger",       ##  Burger
    # "RC0209",          ##  Western, Continental Cuisine
    # "yoshoku",         #   Western Cuisine
    # "RC020911",        #   Hashed Beef Rice
    # "RC020912",        #   Omurice
    # "RC020913",        #   Stew
    # "RC020914",        #   Soup
    # "RC020915",        #   Croquette
    # "RC020999",        #   Western Food (Other)
    # "french",          ##  French
    # "RC021101",        #   French
    # "RC021102",        #   Bistro
    # "RC021103",        #   Modern French
    # "italian",         ##  Italian
    # "spain",           ##  Spain
    # "RC021301",        #   Spain
    # "RC021302",        #   Modern Spanish
    # "RC0219",          ##  Western Cuisine
    # "RC021902",        #   Mediterranean
    # "RC021903",        #   German
    # "RC021904",        #   Russian
    # "RC021905",        #   American
    # "RC021906",        #   California
    # "RC021907",        #   Oceanic Cuisine
    # "RC021908",        #   Hawaiian cuisine
    # "RC021999",        #   Western (Others)
    # "chinese",         ### Chinese
    # "RC0301",          ##  Chinese Cuisine
    # "RC030101",        #   Chinese
    # "RC030102",        #   Dim sum
    # "RC030103",        #   Beijing Cuisine
    # "RC030104",        #   Shanghai Cuisine
    # "RC030105",        #   Cantonese Cuisine
    # "RC030106",        #   Sichuan Cuisine
    # "RC030107",        #   Taiwan Cuisine
    # "RC0302",          ##  Dumplings, Pork Buns
    # "gyouza",          #   Dumplings
    # "RC030202",        #   Meat Buns, Chinese Buns
    # "RC0303",          ##  Chinese Rice Porridge
    # "RC0304",          ##  Chinese Noodles
    # "RC030401",        #   Dandan noodles
    # "RC030402",        #   Knife cut noodles
    # "RC030403",        #   Chinese noodles (other)
    # "RC04",            ### Asian, Ethnic
    # "korea",           ##  Korean Cuisine
    # "RC040101",        #   Korean cuisine
    # "RC040102",        #   Cold noodles
    # "RC0402",          ##  Southeast Asian Cuisine
    # "thai",            #   Thailand cooking
    # "RC040202",        #   Viet Nam cuisine
    # "RC040203",        #   Indonesia cuisine
    # "RC040204",        #   Singaporean cuisine
    # "RC040299",        #   Southeast Asian cuisine (and others)
    # "RC0403",          ##  South Asian Cuisine
    # "RC040301",        #   India cuisine
    # "RC040302",        #   Nepal cuisine
    # "RC040303",        #   Pakistani cuisine
    # "RC040304",        #   Sri Lanka cuisine
    # "RC040399",        #   South Asian cuisine (and others)
    # "RC0404",          ##  West Asian Cuisine
    # "RC040401",        #   Turkish dishes
    # "RC040499",        #   West Asian (other)
    # "RC0411",          ##  Latin American Cuisine
    # "RC041101",        #   Mexico cuisine
    # "RC041102",        #   Brazil cuisine
    # "RC041199",        #   Latin American cuisine (and others)
    # "RC0412",          ##  African Cuisine
    # "RC0499",          ##  Asian Cuisine, Ethnic Cuisine (others)
    # "curry",           ### Curry
    # "RC1201",          ##  Curry Rice
    # "RC1202",          ##  European-style Curry
    # "RC1203",          ##  Indian Curry
    # "RC1204",          ##  Thai Curry
    # "RC1205",          ##  Soup Curry
    # "RC1299",          ##  Curry (other)
    # "RC13",            ### Yakiniku (Grilled beef), Hormones (Offel)
    # "RC1301",          ##  Yakiniku (BBQ Beef), Hormone (Offel)
    # "yakiniku",        #   Yakiniku (BBQ Beef)
    # "horumon",         #   Horumon (BBQ Offel)
    # "RC1302",          ##  Genghis Khan
    # "nabe",            ### Hot Pot
    # "RC1401",          ##  Chanko-Nabe (Sumo Wrestlers Hot Pot)
    # "RC1402",          ##  Udon Suki
    # "motsu",           ##  Motsu-Nabe (Offel Hot Pot)
    # "RC1404",          ##  Mizutaki
    # "RC1405",          ##  Chiritori-Nabe, Tecchyan-Nabe
    # "RC1406",          ##  Chinese Hot Pot / Fire Pot
    # "RC1407",          ##  Korean Hot Pot
    # "RC1409",          ##  Thai suki
    # "RC1408",          ##  Hot Pot (other)
    # "RC21",            ### Izakaya (Tavarn), Dining Bar
    # "izakaya",         ##  Izakaya (Tavern)
    # "RC2102",          ##  Dining bar
    # "RC2199",          ##  Izakaya (other)
    # "RC219902",        #   Stand Bar
    # "RC219903",        #   Bar
    # "RC219904",        #   Beer, beer restaurant
    # "RC219999",        #   Izakaya (other)
    # "RC22",            ### Creative Cuisine, Fusion food
    # "RC2201",          ##  Creative cuisine
    # "RC2202",          ##  Innovative cuisine, Fusion cuisine
    # "RC2203",          ##  Fusion food
    # "RC23",            ### casual dining
    # "RC99",            ### Restaurants (other)
    # "RC9901",          ##  table d&#39;hôte
    # "RC990101",        #   table d&#39;hôte
    # "RC990102",        #   School cafeteria
    # "RC990103",        #   Company cafeteria
    # "RC9903",          ##  Natural food, Medicinal Food
    # "RC990301",        #   Natural food
    # "RC990302",        #   medicinal foods
    # "RC9904",          ##  Bento (Lunch Box), Onigiri (Rice Ball)
    # "RC990401",        #   Bento (Lunch box)
    # "RC990402",        #   Onigiri (Rice ball)
    # "RC9999",          ##  Restaurants (other)
    # "viking",          #   Buffet style
    # "RC999903",        #   Delicatessen
    # "RC999901",        #   Seafood
    # "RC999913",        #   Oyster Bar
    # "RC999902",        #   Garlic dishes
    # "RC999905",        #   Vegetable dishes
    # "RC999907",        #   Beef dishes
    # "RC999908",        #   Pork dishes
    # "RC999909",        #   Meat dishes
    # "RC999910",        #   Sumibiyaki
    # "RC999911",        #   BBQ
    # "RC999912",        #   Other meat dishes
    # "RC999914",        #   Houseboat and cruising
    # "RC999999",        #   Restaurants (other)
    # "ramen",           ### Ramen
    # "MC21",            ### Soupless ramen
    # "MC2101",          ##  Abura soba
    # "MC2102",          ##  Taiwan style mixed noodles
    # "MC2103",          ##  Soupless Dandan noodles
    # "MC11",            ### Tsukemen
    # "CC01",            ### Cafe
    # "CC02",            ### Authentic Café
    # "CC03",            ### Coffee Shoppe
    # "CC04",            ### Tea Shoppe
    # "CC05",            ### China tea Shoppe
    # "CC06",            ### Japan tea Shoppe
    # "CC99",            ### Café (other)
    # "pan",             ### Bakery, Sandwich
    # "SC0101",          ##  Bakery
    # "SC0102",          ##  Sandwich Shop
    # "SC0103",          ##  Bagel
    # "SC0199",          ##  Bakery (other)
    # "sweets",          ### Sweets
    # "SC0201",          ##  Sweets
    # "cake",            #   Cake
    # "SC020102",        #   Chocolate
    # "SC020103",        #   Macaroon
    # "SC020104",        #   Baumkuchen
    # "SC020199",        #   Sweets (other)
    # "SC0202",          ##  Japanese Sweets
    # "SC020201",        #   Japanese sweets
    # "SC020202",        #   Sweets
    # "SC020203",        #   Taiyaki &amp; Oobanyaki
    # "SC020204",        #   Dorayaki
    # "SC020205",        #   Daifuku
    # "SC020206",        #   Senbei (Rice cracker)
    # "SC0203",          ##  Chinese Pastry
    # "SC0299",          ##  Sweets (others)
    # "SC029901",        #   Ice cream
    # "SC029909",        #   Soft serve ice cream
    # "SC029907",        #   Shaved ice (snow cone)
    # "SC029903",        #   Crepes
    # "SC029904",        #   Parfait
    # "SC029902",        #   Fruit parlour
    # "SC029905",        #   Juice bar
    # "SC029906",        #   Pancake
    # "SC029908",        #   Donut
    # "SC029910",        #   French toast
    # "SC029911",        #   Acai bowl
    # "SC029999",        #   Sweets (and others)
    # "BC01",            ### Bar
    # "BC02",            ### Pub
    # "BC03",            ### Lounge
    # "BC04",            ### Wine bar
    # "BC05",            ### Beer garden
    # "BC06",            ### Beer Bar
    # "BC07",            ### Sports Bar
    # "BC99",            ### Bar (other)
    # "BC9901",          ##  Nihonshu, Shochu
    # "BC990101",        #   Nihonshu (Japanese sake)
    # "BC990102",        #   Shochu (Japanese spirits)
    # "BC9999",          ##  Bar (other)
    # "ryokan",          ### Ryokan
    # "YC02",            ### Auberge
    # "YC99",            ### Auberge (other)
    # "ZZ99"             ### Other
]
