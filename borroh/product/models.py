from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify

class Product(models.Model):
	product_code = models.CharField(max_length=100,blank=True,null=True)
	title = models.CharField(max_length=40)
	description = models.TextField(max_length=1000)
	price = models.CharField(max_length=40)
	# category = models.ManyToManyField('Category',blank=True,null=True)
	slug = models.SlugField(blank=True,null=True)
	image_set = models.ManyToManyField('Image',blank=True,null=True)
	discount = models.CharField(max_length=40,choices=(('15%','15%'),('20%','20%'),('25%','25%')),blank=True,null=True)
	points_price = models.CharField(max_length=40,blank=True,null=True)
	borrohed = models.BooleanField(default=False)
	sold = models.BooleanField(default=False)
	status = models.CharField(max_length=40,choices=(('New','New'),('Featured','Featured'),('Regular','Regular')),blank=True,null=True)
	variants = models.ManyToManyField('Variant',blank=True,null=True)
	brand = models.CharField(max_length=40, blank=True,null=True)

	created = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)

	def __unicode__(self):
		return self.title


# -----------------------------------------------------------------------------------
# post_save generate product code and slug
# -----------------------------------------------------------------------------------

# def generate_product_code_receiver(sender,instance,created,*args,**kwargs):
# 	generated_code = "%s %s %s" %('BUR',instance.title.replace(' ','')[5],instance.id)
# 	instance.product_code = generated_code
# 	instance.save()

# def generate_slug_receiver(sender,instance,created,*args,**kwargs):
# 	if created:
# 		slug_title = slugify(instance.title)
# 		new_slug = "%s %s" %(instance.title,instance.id)
# 		try:
# 			obj_exists = Product.objects.get(slug=slug_title)
# 			slugify(new_slug)
# 			instance.save()
# 		except Product.DoesNotExist:
# 			instance.title = slug_title
# 			instance.save()
# 		except Product.MultipleObjectsReturned:
# 			slugify(new_slug)
# 			instance.save()
# 		except:
# 			pass

# post_save.connect(generate_product_code_receiver,sender=Product)
# post_save.connect(generate_slug_receiver,sender=Product)


# -----------------------------------------------------------------------------------


class Image(models.Model):
	image = models.ImageField(upload_to='product_images')
	def __unicode__(self):
		return str(self.image)

class Variant(models.Model):
	title = models.CharField(max_length=40)
	options = models.ManyToManyField('VariantSelection')
	def __unicode__(self):
		return self.title	

class VariantSelection(models.Model):
	name = models.CharField(max_length=40)
	def __unicode__(self):
		return self.name

class Category(models.Model):
	title = models.CharField(max_length=40)

	def __unicode__(self):
		return self.title
