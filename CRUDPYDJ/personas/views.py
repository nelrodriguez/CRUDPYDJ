from django.shortcuts import render,redirect
from . models import Vehiculo,Categoria,Vendedor

# Create your views here.
def inicio(request):
    categorias=Categoria.objects.all()
    vendedores=Vendedor.objects.all()
    data={
        "categorias":categorias,
        "vendedores":vendedores,
    }
    return render(request,'persona/registro.html',data)

def registrar_vehiculo(request):
    if request.method=='POST':
        placa=request.POST.get('txtPlaca')
        modelo=request.POST.get('txtModelo')
        estado=request.POST.get('txtEstado')
        precio=request.POST.get('txtPrecio')
        color=request.POST.get('txtColor')
        id_categoria=request.POST.get('txtCategoria')
        vendedor=request.POST.get('txtVendedor')
        
        
        vehiculo=Vehiculo(
            placa=placa,
            modelo=modelo,
            estado=estado,
            precio=precio,
            color=color,
            categoria=Categoria.objects.get(id=id_categoria),
            vendedor=Vendedor.objects.get(id=vendedor),
            
        )
        
        vehiculo.save()
    return redirect('inicio')

def listar_personas(request):
    personas=Vendedor.objects.all()
    
    data={
        "personas":personas
    }
    return render(request,'persona/listavendedores.html',data)

def pre_editar_persona(request,id):
    persona=Vendedor.objects.get(id=id)
    
    data={
        "persona":persona,
    
    }
    return render(request,"persona/editar.html",data)
def actualizar_persona(request,id):
    if request.method=="POST":
        persona=Vendedor.objects.get(id=id)
        
        persona.documento=request.POST.get("txtDocumento")
        persona.nombre=request.POST.get("txtNombre")
        persona.apellido=request.POST.get("txtApellido")
        persona.direccion=request.POST.get("txtDireccion")
        persona.correo=request.POST.get("txtCorreo")
        persona.telefono=request.POST.get("txtTelefono")
       
        
        persona.save()
        return redirect("listar_personas")
def listar_vehiculos(request):
    vehiculos=Vehiculo.objects.all()
    
    data={
        "vehiculos":vehiculos
    }
    return render(request,'persona/lista.html',data)