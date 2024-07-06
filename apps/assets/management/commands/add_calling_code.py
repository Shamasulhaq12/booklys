from django.core.management.base import BaseCommand
import pycountry
import phonenumbers
from apps.assets.models import CallingCodeWithName


class Command(BaseCommand):
    help = 'Adds all available Country to the database'

    def handle(self, *args, **options):

        for country in pycountry.countries:
            try:
                country_code = phonenumbers.country_code_for_region(country.alpha_2)
                CallingCodeWithName.objects.get_or_create(
                    calling_code=country_code,
                    name=country.name,)
                self.stdout.write(self.style.SUCCESS(
                    'Successfully added all country codes to the database.'))

            except phonenumbers.phonenumberutil.NumberParseException:
                # Ignore countries without calling codes
                pass
