from django.shortcuts import render
from rest_framework.views import APIView
from .models import Proposal
from rest_framework import generics
from .serializers import ProposalSerializer
# Create your views here.

class ProposalView(generics.ListCreateAPIView):
    serializer_class = ProposalSerializer
    queryset = Proposal.objects.all()
    
