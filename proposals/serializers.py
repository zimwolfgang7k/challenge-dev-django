from rest_framework import serializers
from .models import Proposal

class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = '__all__'

    def create(self, validated_data: dict) -> Proposal:
        return Proposal.objects.create(**validated_data)
