from rest_framework import mixins, viewsets


class CreateAndListViewSet(mixins.CreateModelMixin,
                           mixins.ListModelMixin,
                           viewsets.GenericViewSet):

    pass
