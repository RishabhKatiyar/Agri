from __future__ import absolute_import, unicode_literals
from django.db import transaction
from celery import shared_task
import requests
from .models import News


@shared_task(bind=True, max_retries=5)
def get_latest_news(self):
    try:
        response = requests.get('http://thirdpartyapi:8000/api/news/')
        data = response.json()
        with transaction.atomic():
            for item in data:
                News.objects.create(headline=item['headline'], content=item['content'])
    # Exception handling can be improved
    except Exception as e:
        raise self.retry(exc=e, countdown=2 + self.request.retries)