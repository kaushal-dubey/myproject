from django.db import models


class State(models.Model):
    state_id=models.IntegerField(primary_key=True)
    state_name=models.CharField(max_length=50)


class City(models.Model):
    city_id=models.IntegerField(primary_key=True)
    state_name=models.ForeignKey(State,on_delete=models.CASCADE)
    city_name=models.CharField(max_length=50)


class Citizen(models.Model):
    citizen_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50,primary_key=True)
    contact=models.IntegerField()
    password=models.CharField(max_length=50)
    address=models.CharField(max_length=500)
    state_name=models.ForeignKey(State,on_delete=models.CASCADE)
    city_name=models.ForeignKey(City,on_delete=models.CASCADE)


class Officer(models.Model):
    officer_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50,primary_key=True)
    contact=models.IntegerField()
    password=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    state_name=models.ForeignKey(State,on_delete=models.CASCADE)
    city_name=models.ForeignKey(City,on_delete=models.CASCADE)


class Ngo(models.Model):
    ngo_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, primary_key=True)
    contact = models.IntegerField()
    password = models.CharField(max_length=50)
    social_cause=models.CharField(max_length=1000)
    state_name = models.ForeignKey(State, on_delete=models.CASCADE)
    city_name = models.ForeignKey(City, on_delete=models.CASCADE)





