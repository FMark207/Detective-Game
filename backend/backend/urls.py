from django.contrib import admin
from django.urls import path, include
from api.views import (
    api_root,
    SuspectViewSet, SuspectViewSetId,
    MurderStatViewSet, MurderStatViewSetId,
    DetectiveViewSet, DetectiveViewSetId,
    TraitViewSet, TraitViewSetId,
    SuspectTraitViewSet, SuspectTraitViewSetId,
    StatementViewSet, StatementViewSetId,
    LocationViewSet, LocationViewSetId,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('api/', api_root, name='api-root'),

    path('api/suspects/', SuspectViewSet.as_view(), name='suspect-list'),
    path('api/suspects/<int:pk>/', SuspectViewSetId.as_view(), name='suspect-detail'),

    path('api/murder-stats/', MurderStatViewSet.as_view(), name='murderstat-list'),
    path('api/murder-stats/<int:pk>/', MurderStatViewSetId.as_view(), name='murderstat-detail'),

    path('api/detectives/', DetectiveViewSet.as_view(), name='detective-list'),
    path('api/detectives/<int:pk>/', DetectiveViewSetId.as_view(), name='detective-detail'),

    path('api/traits/', TraitViewSet.as_view(), name='trait-list'),
    path('api/traits/<int:pk>/', TraitViewSetId.as_view(), name='trait-detail'),

    path('api/suspect-traits/', SuspectTraitViewSet.as_view(), name='suspecttrait-list'),
    path('api/suspect-traits/<int:pk>/', SuspectTraitViewSetId.as_view(), name='suspecttrait-detail'),

    path('api/statements/', StatementViewSet.as_view(), name='statement-list'),
    path('api/statements/<int:pk>/', StatementViewSetId.as_view(), name='statement-detail'),

    path('api/locations/', LocationViewSet.as_view(), name='location-list'),
    path('api/locations/<int:pk>/', LocationViewSetId.as_view(), name='location-detail'),
]
