from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.dispatch import receiver

class Product(models.Model):
	product_code = models.CharField(max_length=100,blank=True,null=True)
	slug = models.SlugField(blank=True,null=True)
	borrohed = models.BooleanField(default=False)
	featured = models.BooleanField(default=False)
	sold = models.BooleanField(default=False)
	title = models.CharField(max_length=40)
	description = models.TextField(max_length=1000,blank=True,null=True)
	price = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
	points_price = models.IntegerField(max_length=40,default=0,blank=True,null=True)
	category = models.ManyToManyField('Category',blank=True,null=True)
	brand = models.ManyToManyField('Brand',null=True,blank=True)
	gender = models.CharField(max_length=40,choices=(('Male','Male'),('Female','Female'),('Unisex','Unisex'),),blank=True,null=True)
	discount = models.CharField(max_length=40,choices=(('15%','15%'),('20%','20%'),('25%','25%'),(None,None)),blank=True,null=True)
	status = models.CharField(max_length=40,choices=(('New','New'),('Regular','Regular')),blank=True,null=True)
	size = models.ForeignKey('SizeCollection',blank=True,null=True)
	created = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)

	def __unicode__(self):
		return "%s %s %s" %(self.title,':',str(self.id))
	def brand_relation(self):
		brands = []
		try:
			for brand in self.brand.values():
				brands.append(str(brand['name']))
			return brands[0]
		except:
			return "No Brand"
	

# -----------------------------------------------------------------------------------
# post_save generate product code and slug
# -----------------------------------------------------------------------------------

def generate_product_code_receiver(sender,instance,created,*args,**kwargs):
	if created:
		generated_code = "%s %s" %('BORRPRO-',instance.id)
		try:
			obj_exists = Product.objects.get(product_code=generated_code)
			instance.save()
		except Product.DoesNotExist:
			instance.product_code = generated_code
			instance.save()
		except:
			pass
		
def generate_slug_receiver(sender,instance,created,*args,**kwargs):
	if created:
		new_slug = "%s %s" %(instance.title,instance.id)
		slug_title = slugify(new_slug)
		try:
			obj_exists = Product.objects.get(slug=slug_title)
			slugify(new_slug)
			instance.save()
		except Product.DoesNotExist:
			instance.slug = slug_title
			instance.save()
		except Product.MultipleObjectsReturned:
			slugify(new_slug)
			instance.save()
		except:
			pass


post_save.connect(generate_product_code_receiver,sender=Product)
post_save.connect(generate_slug_receiver,sender=Product)


# -----------------------------------------------------------------------------------

class Image(models.Model):
	default = models.BooleanField(default=False,blank=False,null=False)
	image = models.ImageField(upload_to='product_images')
	zoom_image = models.BooleanField(default=False)
	product = models.ForeignKey(Product,blank=True,null=True)
	
	def __unicode__(self):
		return str(self.image)

 			
class Category(models.Model):
	title = models.CharField(max_length=40)
	gender = models.CharField(max_length=40,choices=(('Male','Male'),('Female','Female'),('Unisex','Unisex')),blank=True,null=True)

	def __unicode__(self):
		return self.gender + ":" + self.title


class Collection(models.Model):
	name = models.CharField(max_length=40)
	category = models.ManyToManyField(Category)
	
	def __unicode__(self):
		return self.name
	
	def collection_contents(self):
		categories = []
		for category in self.category.values():
			categories.append(str(category['title']))
		return categories




class Brand(models.Model):
	name = models.CharField(max_length=40)
	def __unicode__(self):
		return self.name

class SizeCollection(models.Model):
	name = models.CharField(max_length=40)
	size = models.ManyToManyField('Size')
	def __unicode__(self):
		return self.name
	def contents(self):
		contents = []
		for content in self.size.values():
			contents.append(str(content['name']))
		return contents

	def contents_to_string(self):
		categories = ''
		for content in self.size.values():
			categories += str(content['name']) + '/'
		return categories

class Size(models.Model):
	name = models.CharField(max_length=40)
	def __unicode__(self):
		return self.name

