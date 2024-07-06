from django.core.management.base import BaseCommand
from apps.assets.models import CountryTimeZone
from apps.assets.models import Countries
import pycountry
import pytz


class Command(BaseCommand):
    help = 'Adds all available timezones to the database'

    def handle(self, *args, **options):
        
       


        for country in pycountry.countries:
            try:
                timezone = pytz.country_timezones[country.alpha_2][0]
                
                country_obj, _ = Countries.objects.get_or_create(common_name=country.name,flag_png=country.flag)
             
                country_timezone = CountryTimeZone(timezone=timezone, country=country_obj)
                country_timezone.save()
                self.stdout.write(self.style.SUCCESS(
                'Successfully added all timezones to the database.'))

            except Exception as e:
                print(e)
        
                pass