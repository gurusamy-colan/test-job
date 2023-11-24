from rest_framework import serializers
from organization.models import (BusinessInfo, BusinessAddressInfo, BusinessInvestorType, )


class BusinessInformation(serializers.ModelSerializer):
    class Meta:
        model = BusinessInfo
        fields = '__all__'
