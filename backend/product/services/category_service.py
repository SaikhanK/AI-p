from typing import List
from ..models import Category

def get_categories()-> List:

    categories = Category.objects.all()
    category_list = [cat.name for cat in categories]
    return category_list