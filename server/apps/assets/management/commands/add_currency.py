from django.core.management.base import BaseCommand
import requests
from apps.assets.models import Currency


class Command(BaseCommand):
    help = 'Adds all available currencies to the database'

    def handle(self, *args, **options):

        # Make a GET request to the API endpoint
        response = requests.get("https://openexchangerates.org/api/currencies.json")

        # Retrieve the response content as a JSON object
        currencies = response.json()

        for code, details in currencies.items():

            Currency.objects.get_or_create(

                name=details,
                code=code,
            )
            self.stdout.write(self.style.SUCCESS(
                'Successfully added all currencies to the database.'))
