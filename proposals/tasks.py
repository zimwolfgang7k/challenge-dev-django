from celery import Celery
from .models import Proposal
from django.forms.models import model_to_dict

app = Celery("tasks", broker="pyamqp://guest@localhost//")


@app.task
def send_proposal_result():
    queryset = Proposal.objects.all()
    # queryset = Proposal.objects.filter(id=1)
    proposals_list = []
    for proposal in queryset:
        proposal_dict = model_to_dict(proposal)
        proposals_list.append(proposal_dict)

    for i in proposals_list:
        if i["id"] % 2 == 0:
            i["proposal_result"] = "Approved"
            for objeto in queryset:
                objeto.save()
            # Proposal.objects.update()
        else:
            i["proposal_result"] = "Rejected"
            for objeto in queryset:
                objeto.save()
            # Proposal.objects.update()

    return proposals_list
