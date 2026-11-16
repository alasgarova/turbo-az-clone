from django.db import models


class Brand(models.Model):
  name = models.CharField(max_length=100, verbose_name='Marka')

  def __str__(self):
    return self.name


class CarModel(models.Model):
  brand = models.ForeignKey(
      Brand, on_delete=models.CASCADE, verbose_name='Marka'
  )
  name = models.CharField(max_length=100, verbose_name='Model')

  def __str__(self):
    return f'{self.brand.name} {self.name}'


class Listing(models.Model):
  FUEL_CHOICES = (
      ('benzin', 'Benzin'),
      ('dizel', 'Dizel'),
      ('hibrid', 'Hibrid'),
      ('elektrik', 'Elektrik'),
  )

  TRANSMISSION_CHOICES = (
      ('avtomat', 'Avtomat'),
      ('mexaniki', 'Mexaniki'),
  )

  brand = models.ForeignKey(
      Brand, on_delete=models.CASCADE, verbose_name='Marka'
  )
  car_model = models.ForeignKey(
      CarModel, on_delete=models.CASCADE, verbose_name='Model'
  )
  price = models.DecimalField(
      max_digits=10, decimal_places=2, verbose_name='Qiymət'
  )
  currency = models.CharField(
      max_length=5, default='AZN', verbose_name='Valyuta'
  )
  year = models.IntegerField(verbose_name='Buraxılış ili')
  mileage = models.IntegerField(verbose_name='Yürüş (km)')
  fuel_type = models.CharField(
      max_length=20, choices=FUEL_CHOICES, verbose_name='Yanacaq növü'
  )
  transmission = models.CharField(
      max_length=20,
      choices=TRANSMISSION_CHOICES,
      verbose_name='Sürətlər qutusu',
  )
  city = models.CharField(max_length=50, verbose_name='Şəhər')
  image = models.ImageField(
      upload_to='images/', blank=True, null=True, verbose_name='Şəkil'
  )
  description = models.TextField(verbose_name='Əlavə məlumat / Təsvir')
  created_at = models.DateTimeField(
      auto_now_add=True, verbose_name='Yaradılma tarixi'
  )

  def __str__(self):
    return (
        f'{self.brand.name} {self.car_model.name} - {self.price}'
        f' {self.currency}'
    )