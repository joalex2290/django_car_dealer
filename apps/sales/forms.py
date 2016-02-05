# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django import forms
from models import Cliente, Venta, VentaLinea
from apps.manager.models import Sucursal
from apps.inventory.models import Articulo

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente

class VentasForm(forms.ModelForm):
	class Meta:
		model = Venta

	id_venta = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'span1','readonly':'true'}))
	total = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control pull-right','style':'margin-top:6px; margin-right:6px;','value':'0','readonly':'true'}))
	comentario = forms.CharField(widget=forms.Textarea(attrs={'rows':'1'}))

class VentasLineaForm(forms.ModelForm):
	class Meta:
		model = VentaLinea

	articulo = forms.ModelChoiceField(widget=forms.Select,queryset=Articulo.objects.all().filter(is_active=True),initial=None)
	sucursal = forms.ModelChoiceField(widget=forms.Select,queryset=Sucursal.objects.all().filter(is_active=True),initial=None)
	total_linea = forms.IntegerField(widget=forms.NumberInput(attrs={'value':'0','readonly':'true'}))