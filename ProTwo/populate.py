import os, faker, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()
from AppTwo.models import User

fakegen = faker.Faker()


def populate(N=5):
    for entry in range(N):
        name = fakegen.name().split()
        firstName = name[0]
        lastName = name[1]
        email = fakegen.email()

        user = User.objects.get_or_create(firstName=firstName,
                                          lastName=lastName,
                                          email=email)[0]

if __name__ == '__main__':
    print("Populating!")
    populate(20)
    print("Populated!")
