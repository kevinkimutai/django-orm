from core.models import Restaurant

def run():
    restaurants = [
      Restaurant(
        name="paparabuon place",
        website="https://www.paparabuon.com",
        town="nairobi",
        address_description="lunga lunga drive,opposite shell petrol station,nairobi,embakasi",
        restaurant_type=Restaurant.RestaurantTypeChoices.SOMALI,
        date_opened="1998-01-01",
        longitude=36.8285,
        latitude=1.2562
     ),
      Restaurant(
        name="The Urban Bites",
        website="https://www.urbanbites.co.ke",
        town="Nairobi",
        address_description="Westlands, Mpaka Road, Nairobi",
        restaurant_type=Restaurant.RestaurantTypeChoices.MEXICAN,
        date_opened="2012-05-10",
        longitude=36.8052,
        latitude=-1.2641
    ),
    Restaurant(
        name="Mama Oliech",
        website="https://www.mamaoliech.co.ke",
        town="Nairobi",
        address_description="Marcus Garvey Road, Kilimani, Nairobi",
        restaurant_type=Restaurant.RestaurantTypeChoices.JAPANESE,
        date_opened="2005-08-15",
        longitude=36.7984,
        latitude=-1.2955
    ),
    Restaurant(
        name="Habesha Restaurant",
        website="https://www.habesha.co.ke",
        town="Nairobi",
        address_description="Argwings Kodhek Rd, Hurlingham, Nairobi",
        restaurant_type=Restaurant.RestaurantTypeChoices.INDIAN,
        date_opened="2010-11-20",
        longitude=36.7850,
        latitude=-1.2910
    ),
    Restaurant(
        name="Tamarind Mombasa",
        website="https://www.tamarind.co.ke/mombasa",
        town="Mombasa",
        address_description="Silos Road, Nyali, Mombasa",
        restaurant_type=Restaurant.RestaurantTypeChoices.OTHER,
        date_opened="1980-02-14",
        longitude=39.6743,
        latitude=-4.0355
    ),
    Restaurant(
        name="Fogo Gaucho",
        website="https://www.fogogaucho.co.ke",
        town="Nairobi",
        address_description="Westlands, Waiyaki Way, Nairobi",
        restaurant_type=Restaurant.RestaurantTypeChoices.ARABIC,
        date_opened="2015-06-25",
        longitude=36.8056,
        latitude=-1.2643
    ),
    ]

    Restaurant.objects.bulk_create(restaurants)