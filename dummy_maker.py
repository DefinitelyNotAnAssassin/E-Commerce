from Models.models import Category, Product
import os

from django.core.wsgi import get_wsgi_application

def main():
    
    print(f"There are {Product.count()} products in the database")
 
 
if __name__ == "__main__":

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ECommerce.settings")
    application = get_wsgi_application()

    main()