from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import SuspectList, MurderStat, Detective, Trait, SuspectTrait, Statement, Location
from .serializer import (
    SuspectSerializer,
    MurderSerializer,
    DetectiveSerializer,
    TraitSerializer,
    SuspectTraitSerializer,
    StatementSerializer,
    LocationSerializer,
)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'suspects': reverse('suspect-list', request=request, format=format),
        'murder-stats': reverse('murderstat-list', request=request, format=format),
        'detectives': reverse('detective-list', request=request, format=format),
        'traits': reverse('trait-list', request=request, format=format),
        'suspect-traits': reverse('suspecttrait-list', request=request, format=format),
        'statements': reverse('statement-list', request=request, format=format),
        'locations': reverse('location-list', request=request, format=format),
    })


class SuspectViewSet(ListCreateAPIView):
    queryset = SuspectList.objects.all()
    serializer_class = SuspectSerializer

class SuspectViewSetId(RetrieveUpdateDestroyAPIView):
    queryset = SuspectList.objects.all()
    serializer_class = SuspectSerializer

class MurderStatViewSet(ListCreateAPIView):
    queryset = MurderStat.objects.all()
    serializer_class = MurderSerializer

class MurderStatViewSetId(RetrieveUpdateDestroyAPIView):
    queryset = MurderStat.objects.all()
    serializer_class = MurderSerializer

class DetectiveViewSet(ListCreateAPIView):
    queryset = Detective.objects.all()
    serializer_class = DetectiveSerializer

class DetectiveViewSetId(RetrieveUpdateDestroyAPIView):
    queryset = Detective.objects.all()
    serializer_class = DetectiveSerializer

class TraitViewSet(ListCreateAPIView):
    queryset = Trait.objects.all()
    serializer_class = TraitSerializer

class TraitViewSetId(RetrieveUpdateDestroyAPIView):
    queryset = Trait.objects.all()
    serializer_class = TraitSerializer

class SuspectTraitViewSet(ListCreateAPIView):
    queryset = SuspectTrait.objects.all()
    serializer_class = SuspectTraitSerializer

class SuspectTraitViewSetId(RetrieveUpdateDestroyAPIView):
    queryset = SuspectTrait.objects.all()
    serializer_class = SuspectTraitSerializer

class StatementViewSet(ListCreateAPIView):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer

class StatementViewSetId(RetrieveUpdateDestroyAPIView):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer

class LocationViewSet(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationViewSetId(RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
