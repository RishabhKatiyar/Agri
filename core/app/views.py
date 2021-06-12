from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from .tasks import get_latest_news
from datetime import datetime, timedelta
from .models import News


class NewsView(viewsets.ViewSet):
    def list(self, request):
        try:
            result = News.objects.all().order_by("-created_at")[:3]
            print(result)
            result_retry = False
            
            if result[0].created_at < (datetime.now() - timedelta(seconds=2)):
                get_latest_news.delay()
                result_retry = True
            
            response = [{'headline':_result.headline, 'content':_result.content} 
                        for _result in result]
            data = {'response':response, 'result_retry':result_retry}
            
            return Response(data=data, status=HTTP_200_OK)
        # Exception handling can be improved
        except Exception as ex:
            print(ex)
            get_latest_news.delay()
            return Response(status=HTTP_404_NOT_FOUND)