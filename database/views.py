from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from .models import Mol


def listing(request):
	mol_list = Mol.objects.all().order_by('id')
	paginator = Paginator(mol_list, 100) # Show 100 moleculars per page

	page = request.GET.get('page')
	try:
		mols = paginator.page(page)
	except PageNotAnInteger:
    # If page is not an integer, deliver first page.
		mols = paginator.page(1)
	except EmptyPage:
     # If page is out of range (e.g. 9999), deliver last page of results.
		mols = paginator.page(paginator.num_pages)

	return render(request, 'database/mol_list.html', {'mols': mols})
