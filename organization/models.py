from django.db import models


class BusinessInfo(models.Model):
    business_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=50, null=True)
    employee_size = models.IntegerField(null=True)
    owner_info = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.business_id)

    class Meta:
        db_table = "business_info"
        verbose_name_plural = "Business Information"


class BusinessAddressInfo(models.Model):
    address_id = models.AutoField(primary_key=True, editable=False)
    street = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    business = models.OneToOneField(BusinessInfo, on_delete=models.CASCADE, related_name='business_address')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.address_id)

    class Meta:
        db_table = "business_address_info"
        verbose_name_plural = "Business Address Information"


class InvestorType(models.Model):
    investor_type_id = models.AutoField(primary_key=True, editable=False)
    investor_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.investor_type)

    class Meta:
        db_table = "investor_type"
        verbose_name_plural = "Investor Type"


class InvestmentStage(models.Model):
    stage_id = models.AutoField(primary_key=True, editable=False)
    stage = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.stage)

    class Meta:
        db_table = "investment_stage"
        verbose_name_plural = "Investment Stage"


class BusinessInvestorType(models.Model):
    business_investor_id = models.AutoField(primary_key=True, editable=False)
    business_investor_type = models.ForeignKey(InvestorType, on_delete=models.CASCADE,
                                               related_name='business_investor_type')
    business = models.ForeignKey(BusinessInfo, on_delete=models.CASCADE, related_name='business_investor')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.business_investor_id)

    class Meta:
        db_table = "business_investor_type"
        verbose_name_plural = "Business Investor Type"


class BusinessInvestmentStage(models.Model):
    business_stage_id = models.AutoField(primary_key=True, editable=False)
    business_investment_stage = models.ForeignKey(InvestmentStage, on_delete=models.CASCADE,
                                                  related_name='business_investment_stage')
    business = models.ForeignKey(BusinessInfo, on_delete=models.CASCADE, related_name='business_investment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.business_stage_id)

    class Meta:
        db_table = "business_investment_stage"
        verbose_name_plural = "Business Investment Stage"
