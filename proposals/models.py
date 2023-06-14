from django.db import models

# Create your models here.


class ProposalChoices(models.TextChoices):
    APPROVED = "Approved"
    REJECTED = "Rejected"
    NOT_INFORMED = "Not Informed"


class Proposal(models.Model):
    full_name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    address = models.CharField(max_length=30)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    proposal_result = models.CharField(
        max_length=20,
        choices=ProposalChoices.choices,
        default=ProposalChoices.NOT_INFORMED,
    )
