from django.shortcuts import render, get_object_or_404, redirect
from ticket.models import Scont, IndexPrimary, About, PriceUslugi
from ticket.models import CatSchetchic, VodTepSchetchic, Schetchic, Du, Tag
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from .forms import TagForm
from django.core.paginator import Paginator


# Create your views here.

def catalog_paginator( paginator, page_number ):
	""" paginator продукции"""

	# paginator = Paginator(products,4)		
	# page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)

	is_paginator = page.has_other_pages()

	if page.has_previous():
		prev_url = '?page={}'.format(page.previous_page_number())
	else:
		prev_url = ''

	if page.has_next():
		next_url = '?page={}'.format(page.next_page_number())
	else:
		next_url = ''
	return (page, prev_url, next_url)






# def cont_list(request):
# 	"""Вывод всех новостей"""
# 	new = Scont.objects.get()
# 	textz = IndexPrimary.objects.get()
	
	
# 	return render(request,'ticket/index.html', context={'name' : new.name, 'adress' : new.adress1,
# 	              'tel' : new.contact1, 'email'  : new.maile1, 'zag' : textz.name, 'texts' : textz.texts,
# 	              'dop1' : textz.doptext1, 'dop2' : textz.doptext2, 'dop3' : textz.doptext3,
# 	              'dop4' : textz.doptext4 })

class IndexHtml(View):
	
	def get(self, request):

		form = TagForm()
		return render(request, 'ticket/index.html', context={'form': form})

	def post(self, request):
		bound_form = TagForm(request.POST)

		if bound_form.is_valid():
			new_tag = bound_form.save()
			return redirect('obrsvaz1.html')

		return render(request, '/', context={'form' : bound_form })






class ShcontView(TemplateView):

	def get(self, request):

	    sh = Scont.objects.get()
	    

	    aboutmod = About.objects.get()
 
	    

	    return render(request, 'about.html', context={'name' : sh.name,
	                         'adress' : sh.adress1, 'tel' : sh.contact1,
	                         'email'  : sh.maile1, 'namea' : aboutmod.name
	                         , 'texts' : aboutmod.texts , 'image' : aboutmod.image 
	                          }  )




class ServiceView(TemplateView):

	def get(self, request):

	    uslugi = PriceUslugi.objects.all()


	    return render(request, 'uslugi.html', context={'uslugi' : uslugi})


class CatalogView(TemplateView):

	def get(self, request):

		vodoshet = CatSchetchic.objects.all()
		products = Schetchic.objects.all()
			
		paginator = Paginator(products,15)		
		page_number = request.GET.get('page', 1)
		page, prev_url, next_url = catalog_paginator(paginator, page_number)

		context={
		        'vodoshet'    : vodoshet,
		         'page_object': page,
		         'next_url'   : next_url,
		         'prev_url'   : prev_url,

		         }

		return render(request, 'catalog.html', context)

class CatalogClassView(View):

	def get(self, request, slug):

		product = CatSchetchic.objects.get(slug__iexact=slug)
		new = product.vodtepschetchic_set.all()
		products = product.schetchic_set.all()
		paginator = Paginator(products,15)		
		page_number = request.GET.get('page', 1)
		page, prev_url, next_url = catalog_paginator(paginator, page_number)

		context={
		        'new' : new,
		        'products' : products,
		        'product': product,

		        'page_object': page,
		        'next_url'   : next_url,
		        'prev_url'   : prev_url
		        }
		
		return render(request, 'catalog1.html', context)


class CatalogVidView(View):

	def get(self, request, slug):

		
		product = VodTepSchetchic.objects.get(slug=slug )
		ls = CatSchetchic.objects.get(title__iexact=product.category) # путь категорий
		new = product.du_set.all().filter(vodcategory=product.id)
		products = product.schetchic_set.all()
		
		paginator = Paginator(products,15)		
		page_number = request.GET.get('page', 1)
		page, prev_url, next_url = catalog_paginator(paginator, page_number)
		context={
		        'new' : new,
		        'ls' : ls,
		        'products' : products,
		        'product' : product,
		        'slug' : slug,
		        'page_object': page,
		        'next_url'   : next_url,
		        'prev_url'   : prev_url,
		        }


		return render(request, 'catalog2.html', context)

class CatalogDuView(View):

	def get(self, request, slug):

		categ = request.GET.get('cat')
		product = Du.objects.get(slug__iexact=slug)
		idcat = VodTepSchetchic.objects.get(slug=categ )
		ls = CatSchetchic.objects.get(title__iexact=product.category)# путь категорий
		ls1 = VodTepSchetchic.objects.get(id__iexact=idcat.id)       # путь категорий
		ls3 = product                                                # путь категорий


		new = product.schetchic_set.all().filter(vodcategory=idcat.id)
		products = product.schetchic_set.all().filter(vodcategory=idcat.id)

		paginator = Paginator(products,15)		
		page_number = request.GET.get('page', 1)
		page, prev_url, next_url = catalog_paginator(paginator, page_number)

		context={
		         'new' : new,
		         'products' : products,
		         'categ' : categ,
		         'idcat' : idcat.id,
		         'ls': ls,
		         'ls1': ls1,
		         'ls3': ls3,


		         'page_object': page,
		        'next_url'   : next_url,
		        'prev_url'   : prev_url,
		         }

		return render(request, 'catalog3.html', context)

class SelectPrice(View):

	def get(self, request, slug):

		product = Schetchic.objects.get(slug__iexact=slug)
		new = product

		ls = CatSchetchic.objects.get(title__iexact=product.category)
		ls1 = VodTepSchetchic.objects.get(title__iexact=product.vodcategory) 
		try:
			ls2 = Du.objects.get(title__iexact=product.shdu)
		except:
			ls2 = ''


		context={
				'new' : new,
				 'ls': ls,
		         'ls1': ls1,
		         'ls2': ls2,

				 'slug' : slug}
		return render(request, 'selectprice.html', context)


class TagCreate(View):

	def get(self, request):
		form = TagForm()
		return render(request, 'obrsvaz.html', context={'form': form})

	def post(self, request):
		bound_form = TagForm(request.POST)

		if bound_form.is_valid():
			new_tag = bound_form.save()
			return redirect('obrsvaz1.html')

		return render(request, 'catalog.html', context={'form' : bound_form })

def tag_form_redirect(request):

	n = 'отправлено'
	return render(request, 'obrsvaz1.html', {'n' : n })





















