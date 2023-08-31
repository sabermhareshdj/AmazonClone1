import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from product.models import Brand , Product

def seed_brand(n):
    fake = Faker()
    images = ['1.jpg','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.jpg','11.png','12.jpg','13.jpg']
    for _ in range(n):
        Brand.objects.create (
            name = fake.name(),
            image = f'brands/{images[random.randint(0,11)]}'
        )
    print (f'seed {n} Brands Successfully')


def seed_product(n):
    pass




seed_brand(5)