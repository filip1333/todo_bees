from django.conf.urls import url
from django.urls import include
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from ToDoBeesBzzz.views import ToDoListView

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^To-Do-List-View/', ToDoListView.as_view()),
    url(r'^docs/', include_docs_urls(title='My API title')),
]