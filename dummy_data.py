import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from product.models import Brand , Product , ProductImages

def seed_brand(n):
    fake = Faker()
    images = ['1.jpg','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.jpg','11.png','12.jpg','13.jpg']
    for _ in range(n):
        Brand.objects.create (
            name = fake.name(),
            image = f'brands/{images[random.randint(0,10)]}'
        )
    print (f'seed {n} Brands Successfully')


def seed_product(n):
    fake = Faker()
    images = ['2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.jpg','11.png','12.jpg','13.jpg']
    flags = ['New','Sale','Feature']

    for _ in range(n):

        Product.objects.create(
            name = fake.name() ,
            image = f'brands/{images[random.randint(0,11)]}' ,
            flag = flags[random.randint(0,2)] ,
            price = round(random.uniform(20.99,99.99),2) ,
            sku = random.randint(1000,1000000) , 
            subtitle = fake.text(max_nb_chars=250) ,
            description = fake.text(max_nb_chars=2500) ,
            quantity = random.randint(0,30),
            brand = Brand.objects.get(id=random.randint(1,105))
           
        )

        print (f'seed {n} Product Successfully')


#seed_brand(500)
seed_product(500)