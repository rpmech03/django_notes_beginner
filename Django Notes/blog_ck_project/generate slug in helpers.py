from django.utils.text import slugify
from .models import *

import string
import random

# using random.choices()
# generating random strings
def gen_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=N))
    return res

def gen_slug(text):
    new_slug = slugify(text)
    if blog.objects.filter(slug = new_slug).exists():
        gen_slug(text + gen_random_string(5))
    return new_slug