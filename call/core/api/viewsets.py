from rest_framework import viewsets

from call.core.api.serializers import PersonSerializer
from call.core.models import Person


class PersonViewSets(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('name')
    serializer_class = PersonSerializer
