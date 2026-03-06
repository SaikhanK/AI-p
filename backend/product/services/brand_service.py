from ..models import AttributeValue
from typing import List
def get_brands() -> List:
    query_set = [val for val in AttributeValue.objects.filter(attribute__name='Brand')]
    brands = [att.value for att in query_set]
    return brands