from django.core.management.color import no_style
from django.db import connection
from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        sequence_sql = connection.ops.sequence_reset_sql(no_style(), [Category,Product])
        with connection.cursor() as cursor:
            for sql in sequence_sql:
                cursor.execute(sql)
