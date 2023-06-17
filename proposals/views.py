from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Proposal
from rest_framework import generics
from .serializers import ProposalSerializer
from .tasks import send_proposal_result
from rest_framework import status
from django.forms.models import model_to_dict

# Create your views here.


@api_view(["POST"])
def create_proposal(request):
    proposal_value = request.data.get("value")
    proposal_name = request.data.get("full_name")
    proposal_cpf = request.data.get("cpf")
    proposal_address = request.data.get("address")
    # queryset = Proposal.objects.all()

    # proposals_list = []
    # for proposal in queryset:
    #     proposal_data = {
    #         "id": proposal.id,
    #         "full_name": proposal.full_name,
    #         "cpf": proposal.cpf,
    #         "address": proposal.address,
    #         "value": proposal.value,
    #         "proposal_result": proposal.proposal_result,
    #     }
    #     proposals_list.append(proposal_data)

    proposal = Proposal.objects.create(
        value=proposal_value,
        full_name=proposal_name,
        cpf=proposal_cpf,
        address=proposal_address,
    )
    send_proposal_result.delay(proposal.id)

    return Response(
        {"success": "Proposal created successfully."}, status=status.HTTP_201_CREATED
    )


@api_view(["GET"])
def get_proposal(request):
    queryset = Proposal.objects.all()

    proposals_list = []
    # for proposal in queryset:
    #     proposal_dict = model_to_dict(proposal)
    #     proposals_list.append(proposal_dict)

    for proposal in queryset:
        proposal_data = {
            "id": proposal.id,
            "full_name": proposal.full_name,
            "cpf": proposal.cpf,
            "address": proposal.address,
            "value": proposal.value,
            "proposal_result": proposal.proposal_result,
        }
        proposals_list.append(proposal_data)
    return Response(proposals_list)

    # return Response({proposals_list}, status=status.HTTP_200_OK)


# queryset = Proposal.objects.all()
# serializer_class = ProposalSerializer
