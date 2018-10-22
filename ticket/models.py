from django.db import models
from django.urls import reverse


# Create your models here.



def  generate_filename(instance, filename):
	 filename = instance.name + '.jpg'
	 return "{0}/{1}".format(instance, filename)


def  generate_filename1(instance, filename):
	 filename = instance.slug +'.'+ filename.split('.')[1]
	 return "{0}/{1}".format(instance, filename)







class Scont(models.Model):
	name = models.CharField('название', max_length=50)
	adress1 = models.CharField('adress', max_length=50)
	contact1 = models.TextField('tel', max_length=200)
	maile1 = models.CharField('почта', max_length=50)

	


	def __str__(self):
		return self.name

class IndexPrimary(models.Model):
	name = models.CharField('название', max_length=50)
	texts = models.TextField('текст')
	doptext1 = models.TextField('доп. текст 1', max_length=100, blank=True)
	doptext2 = models.TextField('доп. текст 2', max_length=100, blank=True)
	doptext3 = models.TextField('доп. текст 3', max_length=100, blank=True)
	doptext4 = models.TextField('доп. текст 4', max_length=100, blank=True)



	def __str__(self):
		return self.name


class About(models.Model):

	name = models.CharField('название', max_length=50)
	texts = models.TextField('текст')
	texts1 = models.TextField('текст1', blank=True)
	texts2 = models.TextField('текст2', blank=True)
	image = models.ImageField(upload_to=generate_filename, blank=True)



	def __str__(self):
		return self.name


class PriceUslugi(models.Model):
	
	name = models.CharField('название', max_length=50)
	slug = models.SlugField('slug', unique=True)
	service = models.TextField('услуга')
	value = models.DecimalField('стоимость', max_digits=10, decimal_places=2)
	summ = models.DecimalField( 'сумма', max_digits=10, decimal_places=2, blank=True, null=True)

	def __str__(self):
		return '{}''_''{}''_''{}'.format(self.id , self.name, self.service)





class CatSchetchic(models.Model):

	title = models.CharField('Заголовок', max_length=50)
	slug = models.SlugField('slug', unique=True)

	class Meta:
		verbose_name='кат Счетчик'
		verbose_name_plural= 'кат Счетчики'

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('catalogclassview', kwargs={'slug' : self.slug})



class VodTepSchetchic(models.Model):

	title = models.CharField('Заголовок', max_length=50)
	slug = models.SlugField('slug', unique=True)
	category = models.ForeignKey(CatSchetchic, verbose_name='Категория',
         on_delete=models.CASCADE, null=True)


	class Meta:
		verbose_name ='под Счетчик'
		verbose_name_plural = 'под Счетчики'
		ordering = ['category']

	def __str__(self):
		return '{}'.format(self.title )

	def get_absolute_url(self):
		return reverse('catalogvidview', kwargs={'slug' : self.slug})

	

class Du(models.Model):

	title = models.CharField('Заголовок', max_length=50)
	slug = models.SlugField('slug', unique=True)
	category = models.ForeignKey(CatSchetchic, verbose_name='Категория',
                                  on_delete=models.CASCADE, null=True)
	vodcategory = models.ManyToManyField(VodTepSchetchic, blank=True, verbose_name='Счетчик')

	class Meta:
		verbose_name='Ду'
		verbose_name_plural= 'Ду'

	def __str__(self):
		return '{}'.format(self.title )

	def get_absolute_url(self):
		return reverse('du', kwargs={'slug' : self.slug})



class Schetchic(models.Model):

	title = models.CharField('название', max_length=50)
	slug = models.SlugField('slug', unique=True)
	text = models.TextField('описание', blank=True)
	specifications = models.TextField('характиристики', blank=True)

	category = models.ForeignKey(CatSchetchic, verbose_name='Категория',
         on_delete=models.CASCADE, null=True)
	vodcategory = models.ForeignKey(VodTepSchetchic, verbose_name='вод теп Счетчик',
         on_delete=models.CASCADE, null=True)
	shdu = models.ForeignKey(Du, verbose_name='ду',
         on_delete=models.CASCADE, blank=True, null=True)

	image = models.ImageField(upload_to=generate_filename1, blank=True)
	price = models.DecimalField('Цена', max_digits=10, decimal_places=2, blank=True, null=True)

	class Meta:
		verbose_name='Счетчик'
		verbose_name_plural= 'Счетчики'
		ordering = ['title']

	def __str__(self):
		return '{}''_''{}''_''{}''_''{}'.format(self.title,
		             self.category, self.vodcategory, self.shdu )

	def get_absolute_url(self):
		return reverse('selectprice', kwargs={'slug' : self.slug})


class Tag(models.Model):
	""" обратная связь"""
	name = models.CharField('Ваше имя', max_length=50)
	telephon = models.PositiveIntegerField('Телефон')
	email_t = models.EmailField('Ваш @email', blank=True)
	comment = models.TextField('Коментарии')
	datetime_t = models.DateTimeField('Дата, время', auto_now_add=True)

	def __str__(self):
		return '{}''-''{}'.format(self.name, self.datetime_t)

	def get_absolute_url(self):
		return reverse('tag_create_url')



















	









