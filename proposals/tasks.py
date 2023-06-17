from celery import Celery
from .models import Proposal
from django.forms.models import model_to_dict
from .serializers import ProposalSerializer

app = Celery("tasks", broker="pyamqp://guest@localhost//")


@app.task
def send_proposal_result(proposal_id):
    # queryset = Proposal.objects.all()
    # proposals_list = []
    # for proposal in queryset:
    #     proposal_dict = model_to_dict(proposal)
    #     proposals_list.append(proposal_dict)

    if proposal_id % 2 == 0:
        proposal = Proposal.objects.get(id=proposal_id)
        proposal.proposal_result = "Approved"
    else:
        proposal = Proposal.objects.get(id=proposal_id)
        proposal.proposal_result = "Rejected"

    proposal.save()
