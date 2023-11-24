from django.shortcuts import render, redirect, get_object_or_404

from .forms import BusinessCustomForm
from .models import (BusinessInfo, BusinessAddressInfo,
                     BusinessInvestmentStage, BusinessInvestorType)


def business_list(request):
    try:
        businesses = BusinessInfo.objects.all()
    except Exception as e:
        error_message = f"Error: {e}"
        return render(request, 'index.html', {'error_message': error_message})
    return render(request, 'index.html', {'businesses': businesses})


def create_business(request):
    if request.method == 'POST':
        form = BusinessCustomForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            employee_size = form.cleaned_data['employee_size']
            owner_info = form.cleaned_data['owner_info']
            street = form.cleaned_data['street']
            city = form.cleaned_data['city']
            country = form.cleaned_data['country']
            investor_type = form.cleaned_data['investor_type']
            investor_stage = form.cleaned_data['investor_stage']

            business = BusinessInfo.objects.create(
                name=name,
                employee_size=employee_size,
                owner_info=owner_info
            )

            business_address = BusinessAddressInfo.objects.create(
                street=street,
                city=city,
                country=country,
                business=business
            )

            business_investor = BusinessInvestorType.objects.create(business_investor_type=investor_type,
                                                                    business=business)

            business_investment = [BusinessInvestmentStage(business=business, business_investment_stage=stage)
                                   for stage in investor_stage]

            BusinessInvestmentStage.objects.bulk_create(business_investment)
            return redirect('business_list')

    else:
        form = BusinessCustomForm()
    return render(request, 'create_business.html', {'form': form})


def edit_business(request, business_id):
    try:
        business = get_object_or_404(BusinessInfo, pk=business_id)
        business_address = get_object_or_404(BusinessAddressInfo, business=business)
        business_investor_type = get_object_or_404(BusinessInvestorType, business=business)
        business_investment_stages = BusinessInvestmentStage.objects.filter(business=business)

        if request.method == 'POST':
            form = BusinessCustomForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                employee_size = form.cleaned_data['employee_size']
                owner_info = form.cleaned_data['owner_info']
                street = form.cleaned_data['street']
                city = form.cleaned_data['city']
                country = form.cleaned_data['country']
                investor_type = form.cleaned_data['investor_type']
                investor_stage = form.cleaned_data['investor_stage']

                business.name = name
                business.employee_size = employee_size
                business.owner_info = owner_info
                business.save()

                business_address.street = street
                business_address.city = city
                business_address.country = country
                business_address.save()

                business_investor_type.investor_type = investor_type
                business_investor_type.save()

                new_investment_stages = [BusinessInvestmentStage(business=business, business_investment_stage=stage)
                                         for stage in investor_stage]

                new_stage_ids = set(stage.business_investment_stage_id for stage in new_investment_stages)

                existing_stage_ids = set(
                    old_stage.business_investment_stage.stage_id for old_stage in business_investment_stages)

                stages_to_delete = business_investment_stages.filter(
                    business_stage_id__in=existing_stage_ids - new_stage_ids)

                stages_to_delete.delete()

                new_stages_to_create = [stage for stage in new_investment_stages if
                                        stage.business_investment_stage_id not in existing_stage_ids]

                BusinessInvestmentStage.objects.bulk_create(new_stages_to_create)

                return redirect('business_list')
        else:
            initial_data = {
                'name': business.name,
                'employee_size': business.employee_size,
                'owner_info': business.owner_info,
                'street': business_address.street,
                'city': business_address.city,
                'country': business_address.country,
                'investor_type': business_investor_type.business_investor_type,
                'investor_stage': [stage.business_investment_stage for stage in business_investment_stages]
            }
            form = BusinessCustomForm(initial=initial_data)
        return render(request, 'edit_business.html', {'form': form, 'business': business})
    except Exception as e:
        error_message = f"Error: {e}"
        return render(request, 'index.html', {'error_message': error_message})


def get_business(request, business_id):
    try:
        business = get_object_or_404(BusinessInfo, pk=business_id)
        business_investor_type = get_object_or_404(BusinessInvestorType, business=business)
        business_investment_stages = BusinessInvestmentStage.objects.filter(business=business)
        business_dict = {
            'name': business.name,
            'employee_size': business.employee_size,
            'owner_info': business.owner_info,
            'street': business.business_address.street,
            'city': business.business_address.city,
            'country': business.business_address.country,
            'investor_type': business_investor_type.business_investor_type.investor_type,
            'investor_stage': [stages.business_investment_stage for stages in business_investment_stages]
        }
        return render(request, 'get_business.html', {'business': business_dict})

    except Exception as e:
        error_message = f"Error: {e}"
        return render(request, 'index.html', {'error_message': error_message})


def delete_business(request, business_id):
    try:
        business = get_object_or_404(BusinessInfo, pk=business_id)
        business.delete()
        return redirect('business_list')
    except Exception as e:
        error_message = f"Error: {e}"
        return render(request, 'index.html', {'error_message': error_message})

