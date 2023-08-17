from django.core.management import BaseCommand

from catalog.models import Category, Product
from django.core.management.color import no_style
from django.db import connection


class Command(BaseCommand):
    Category.objects.all().delete()
    Product.objects.all().delete()

    sequence_sql = connection.ops.sequence_reset_sql(no_style(), [Category, Product])
    with connection.cursor() as cursor:
        for sql in sequence_sql:
            cursor.execute(sql)

    def handle(self, *args, **options):
        products_list = [
            {'product_name': 'Chai', 'category_id': 1, 'description': '10 boxes x 30 bags', 'price': '1800'},
            {'product_name': 'Chang', 'category_id': 1, 'description': '24 - 12 oz bottles', 'price': '1900'},
            {'product_name': 'Aniseed Syrup', 'category_id': 2, 'description': '12 - 550 ml bottles', 'price': '1000'},
            {'product_name': 'Chef Anton Cajun Seasoning','category_id':2,'description':'48 - 6 oz jars','price':'2200'},
            {'product_name': 'Grandma Boysenberry Spread', 'category_id': 2, 'description': '12 - 8 oz jars','price': '2500'},
            {'product_name': 'Northwoods Cranberry Sauce', 'category_id': 2, 'description': '12 - 12 oz jars','price': '4000'},
            {'product_name': 'Mishi Kobe Niku', 'category_id': 6, 'description': '18 - 500 g pkgs.', 'price': '9700'},
            {'product_name': 'Ikura', 'category_id': 8, 'description': '12 - 200 ml jars', 'price': '3100'},
            {'product_name': 'Queso Cabrales', 'category_id': 4, 'description': '1 kg pkg.', 'price': '2100'},
            {'product_name': 'Queso Manchego La Pastora', 'category_id': 4, 'description': '10 - 500 g pkgs.',
             'price': '3800'},
            {'product_name': 'Konbu', 'category_id': 8, 'description': '2 kg box', 'price': '600'},
            {'product_name': 'Tofu', 'category_id': 7, 'description': '40 - 100 g pkgs.', 'price': '2300'},
            {'product_name': 'Genen Shouyu', 'category_id': 2, 'description': '24 - 250 ml bottles', 'price': '1300'},
            {'product_name': 'Pavlova', 'category_id': 3, 'description': '32 - 500 g boxes', 'price': '1700'},
            {'product_name': 'Alice Mutton', 'category_id': 6, 'description': '20 - 1 kg tins', 'price': '3900'},
            {'product_name': 'Carnarvon Tigers', 'category_id': 8, 'description': '16 kg pkg.', 'price': '6300'},
            {'product_name': 'Teatime Chocolate Biscuits', 'category_id': 3, 'description': '10 boxes x 12 pieces',
             'price': '3200'},
            {'product_name': 'Sir Rodneys Marmalade','category_id':3,'description':'30 gift boxes','price':'8100'},
            {'product_name': 'Sir Rodneys Scones','category_id':3,'description':'24 pkgs.x 4 pieces','price':'1000'},
            {'product_name': 'Gustaf', 'category_id': 5, 'description': '24 - 500 g pkgs.', 'price': '2100'},
            {'product_name': 'Tunnb', 'category_id': 5, 'description': '12 - 250 g pkgs.', 'price': '900'},
            {'product_name': 'Mascarpone Fabioli', 'category_id': 4, 'description': '24 - 200 g pkgs.','price': '3200'},
            {'product_name': 'Sasquatch Ale', 'category_id': 1, 'description': '24 - 12 oz bottles', 'price': '1400'},
            {'product_name': 'Steeleye Stout', 'category_id': 1, 'description': '24 - 12 oz bottles', 'price': '1800'},
            {'product_name': 'Inlagd Sill', 'category_id': 8, 'description': '24 - 250 g  jars', 'price': '1900'},
            {'product_name': 'Gravad lax', 'category_id': 8, 'description': '12 - 500 g pkgs.', 'price': '2600'},
            {'product_name': 'Chartreuse verte', 'category_id': 1, 'description': '750 cc per bottle', 'price': '1800'},
            {'product_name': 'Boston Crab Meat', 'category_id': 8, 'description': '24 - 4 oz tins', 'price': '4500'},
            {'product_name': 'Jacks New England Clam Chowder', 'category_id': 8, 'description': '12 - 12 oz cans','price': '2300'},
            {'product_name': 'Singaporean Hokkien Fried Mee', 'category_id': 5, 'description': '32 - 1 kg pkgs.','price': '1400'},
            {'product_name': 'Ipoh Coffee', 'category_id': 1, 'description': '16 - 500 g tins', 'price': '4600'},
            {'product_name': 'Gula Malacca', 'category_id': 2, 'description': '20 - 2 kg bags', 'price': '2000'},
            {'product_name': 'Rogede sild', 'category_id': 8, 'description': '1k pkg.', 'price': '4500'},
            {'product_name': 'Spegesild', 'category_id': 8, 'description': '4 - 450 g glasses', 'price': '1200'},
            {'product_name': 'Zaanse koeken', 'category_id': 3, 'description': '10 - 4 oz boxes', 'price': '6900'},
            {'product_name': 'Chocolade', 'category_id': 3, 'description': '10 pkgs.', 'price': '2300'},
            {'product_name': 'Maxilaku', 'category_id': 3, 'description': '24 - 50 g pkgs.', 'price': '2000'},
            {'product_name': 'Valkoinen suklaa', 'category_id': 3, 'description': '12 - 100 g bars', 'price': '1600'},
            {'product_name': 'Manjimup Dried Apples', 'category_id': 7, 'description': '50 - 300 g pkgs.',
             'price': '5300'},
            {'product_name': 'Filo Mix', 'category_id': 5, 'description': '16 - 2 kg boxes', 'price': '700'},
            {'product_name': 'Perth Pasties', 'category_id': 6, 'description': '48 pieces', 'price': '3300'},
            {'product_name': 'Tourtiere', 'category_id': 6, 'description': '16 pies', 'price': '2200'},
            {'product_name': 'Pate chinois', 'category_id': 6, 'description': '24 boxes x 2 pies', 'price': '2400'},
            {'product_name': 'Gnocchi di nonna Alice', 'category_id': 5, 'description': '24 - 250 g pkgs.',
             'price': '3800'},
            {'product_name': 'Ravioli Angelo', 'category_id': 5, 'description': '24 - 250 g pkgs.', 'price': '1100'},
            {'product_name': 'Escargots de Bourgogne', 'category_id': 8, 'description': '24 pieces', 'price': '13000'},
            {'product_name': 'Raclette Courdavault', 'category_id': 4, 'description': '5 kg pkg.', 'price': '5500'},
            {'product_name': 'Camembert Pierrot', 'category_id': 4, 'description': '15 - 300 g rounds',
             'price': '3400'},
            {'product_name': 'Sirop derable', 'category_id': 2, 'description': '24 - 500 ml bottles', 'price': '4500'},
            {'product_name': 'Tarte au sucre', 'category_id': 3, 'description': '48 pies', 'price': '300'},
            {'product_name': 'Vegie-spread', 'category_id': 2, 'description': '15 - 625 g jars', 'price': '700'},
            {'product_name': 'Wimmers gute Semmelknodel', 'category_id': 5, 'description': '20 bags x 4 pieces',
             'price': '900'},
            {'product_name': 'Louisiana Fiery Hot Pepper Sauce', 'category_id': 2, 'description': '32 - 8 oz bottles',
             'price': '1200'},
            {'product_name': 'Louisiana Hot Spiced Okra', 'category_id': 2, 'description': '24 - 8 oz jars',
             'price': '1700'},
            {'product_name': 'Laughing Lumberjack Lager', 'category_id': 1, 'description': '24 - 12 oz bottles',
             'price': '1400'},
            {'product_name': 'Scottish Longbreads', 'category_id': 3, 'description': '10 boxes x 8 pieces',
             'price': '200'},
            {'product_name': 'Gudbrandsdalsost', 'category_id': 4, 'description': '10 kg pkg.', 'price': '3600'},
            {'product_name': 'Outback Lager', 'category_id': 1, 'description': '24 - 355 ml bottles', 'price': '1500'},
            {'product_name': 'Flotemysost', 'category_id': 4, 'description': '10 - 500 g pkgs.', 'price': '2300'},
            {'product_name': 'Mozzarella di Giovanni', 'category_id': 4, 'description': '24 - 200 g pkgs.',
             'price': '6500'},
            {'product_name': 'Rod Kaviar', 'category_id': 8, 'description': '24 - 150 g jars', 'price': '1500'},
            {'product_name': 'Longlife Tofu', 'category_id': 7, 'description': '5 kg pkg.', 'price': '1000'},
            {'product_name': 'Rhonbrau Klosterbier', 'category_id': 1, 'description': '24 - 0.5 l bottles',
             'price': '3400'},
            {'product_name': 'Lakkalikoori', 'category_id': 1, 'description': '500 ml', 'price': '1800'},
            {'product_name': 'Original Frankfurter', 'category_id': 2, 'description': '12 boxes', 'price': '1300'},

        ]

        category_list = [
            {'name': 'Beverages', 'description': 'Soft drinks, coffees, teas, beers, and ales'},
            {'name': 'Condiments', 'description': 'Sweet and savory sauces, relishes, spreads, and seasonings'},
            {'name': 'Confections', 'description': 'Desserts, candies, and sweet breads'},
            {'name': 'Dairy Products', 'description': 'Cheeses'},
            {'name': 'Grains/Cereals', 'description': 'Breads, crackers, pasta, and cereal'},
            {'name': 'Meat/Poultry', 'description': 'Prepared meats'},
            {'name': 'Produce', 'description': 'Dried fruit and bean curd'},
            {'name': 'Seafood', 'description': 'Seaweed and fish'},
        ]

        categories_for_DB = []
        for category in category_list:
            categories_for_DB.append(Category(**category))

        Category.objects.bulk_create(categories_for_DB)

        products_for_DB = []
        for product in products_list:
            products_for_DB.append(Product(**product))

        Product.objects.bulk_create(products_for_DB)


