import pytest
from django.test import RequestFactory
from django.urls import reverse

from .models import (BusinessInfo, BusinessAddressInfo,
                     BusinessInvestmentStage, BusinessInvestorType, InvestorType, InvestmentStage)
from .views import get_business, create_business


@pytest.mark.django_db
def test_business_list_view(client):
    response = client.get(reverse('business_list'))
    assert response.status_code == 200


def create_investor_type(investor_type):
    return InvestorType.objects.create(investor_type=investor_type)


@pytest.mark.django_db
def test_create_investor_type():
    investor_type_name = "Test Investor Type"

    created_investor_type = create_investor_type(investor_type=investor_type_name)

    retrieved_investor_type = InvestorType.objects.get(investor_type=investor_type_name)
    assert created_investor_type.investor_type == retrieved_investor_type.investor_type


def create_investment_stage_func(stage_name):
    return InvestmentStage.objects.create(stage=stage_name)


@pytest.mark.django_db
def test_create_investment_stage():
    stage_name = "Early Stage"

    stage = create_investment_stage_func(stage_name)
    assert stage.stage == stage_name


@pytest.mark.django_db
def test_edit_business(client):
    business = BusinessInfo.objects.create(name='Test Business', employee_size=10, owner_info='Owner')

    address = BusinessAddressInfo.objects.create(business=business, street='Street', city='City', country='Country')

    investor_type_name = "Test Investor Type"
    created_investor_type = create_investor_type(investor_type=investor_type_name)

    investor_type = BusinessInvestorType.objects.create(business=business, business_investor_type=created_investor_type)
    stage_name = "Early Stage"
    created_investor_stage = create_investment_stage_func(stage_name)

    investment_stage = BusinessInvestmentStage.objects.create(business=business,
                                                              business_investment_stage=created_investor_stage)

    # Data to be updated
    updated_data = {
        'name': 'Updated Business',
        'employee_size': 20,
        'owner_info': 'New Owner',
        'street': 'New Street',
        'city': 'New City',
        'country': 'New Country',
        'investor_type': 'New Type',
        'investor_stage': ['New Stage']
    }

    response = client.post(reverse('business_edit', kwargs={'business_id': business.business_id}), updated_data)
    assert response.status_code == 200

    # Cleanup: Delete created objects
    address.delete()
    investor_type.delete()
    investment_stage.delete()


@pytest.fixture
def create_business_fix():
    business = BusinessInfo.objects.create(
        name='Test Business',
        employee_size=100,
        owner_info='Owner'
    )
    BusinessAddressInfo.objects.create(
        business=business,
        street='Street',
        city='City',
        country='Country')

    investor_type_name = "Test Investor Type"
    created_investor_type = create_investor_type(investor_type=investor_type_name)

    BusinessInvestorType.objects.create(
        business=business,
        business_investor_type=created_investor_type)

    stage_name = "Early Stage"

    created_investor_stage = create_investment_stage_func(stage_name)

    BusinessInvestmentStage.objects.create(business=business,
                                           business_investment_stage=created_investor_stage)

    stage_name = "Later Stage"

    created_investor_stage = create_investment_stage_func(stage_name)

    BusinessInvestmentStage.objects.create(business=business,
                                           business_investment_stage=created_investor_stage)

    return business


@pytest.mark.django_db
def test_get_business_view(client, create_business_fix):
    business_id = create_business_fix.business_id
    url = reverse('business_get', kwargs={'business_id': business_id})
    request = RequestFactory().get(url)
    response = get_business(request, business_id)
    assert response.status_code == 200
    assert 'Test Business' in response.content.decode()


@pytest.mark.django_db
def test_create_business_view(client):
    data = {
        "name": " Test ORG",
        "employee_size": 10,
        "owner_info": "Test OWNER",
        "street": "Test street",
        "city": "test city",
        "country": "test country",
        "investor_type": "Investment Bank",
        "investor_stage": [create_investment_stage_func("Early Stage Venture")]
    }
    url = reverse('business_create')
    request = RequestFactory().post(url, data=data)
    response = create_business(request)
    print(response.status_code)
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_business_view(client, create_business_fix):
    business_id = create_business_fix.business_id
    url = reverse('business_delete', kwargs={'business_id': business_id})

    response = client.post(url)

    assert response.status_code == 302

    with pytest.raises(BusinessInfo.DoesNotExist):
        deleted_business = BusinessInfo.objects.get(business_id=business_id)
