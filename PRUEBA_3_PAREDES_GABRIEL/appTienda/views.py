from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria
from .forms import PedidoForm
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
from .models import Pedido
from django.shortcuts import render






def catalogo(request):
#se muestra el catalogo por filtros y por id_categoria (filtro es el filtro)
    categorias = Categoria.objects.all()  
    filtro = request.GET.get("filtro", "").strip()
    id_categoria = request.GET.get("categoria", "").strip()
    productos = Producto.objects.all()

    if filtro:
        productos = productos.filter(nombre__icontains=filtro)
    if id_categoria:
        productos = productos.filter(categoria_id=id_categoria)

    return render(request, "catalogo.html", {
        "productos": productos,
        "categorias": categorias,
        "filtro": filtro,
        "id_categoria": id_categoria,})



def detalle_producto(request, id):
#se muestra la info de un producto
    producto = get_object_or_404(Producto, id=id)
    return render(request, "detalle_producto.html", {
        "producto": producto})




def solicitud_pedido(request):
#se crea un pedido de un produvto elegido
    producto_id = request.GET.get("producto")
#esta es la "proteccion" por si no hay producto no falle
    if not producto_id:
        return redirect("catalogo")
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":
        form = PedidoForm(request.POST, request.FILES)
        if form.is_valid():
            pedido = form.save(commit=False)

            # Asignamos el producto para el pedido
            pedido.producto_referencia = producto
            # Aqui sabemos de donde viene el pedido
            pedido.plataforma_origen = "SITIO_WEB"
            pedido.save()
            # vemos al detalle de seguimiento
            return redirect("detalle_seguimiento", token=pedido.token_seguimiento)
    else:
        form = PedidoForm()
    return render(request, "solicitud.html", {
        "form": form,
        "producto": producto})




def detalle_seguimiento(request, token):
#aqui se muestra el seguimiento usando el token
    from .models import Pedido
    pedido = get_object_or_404(Pedido, token_seguimiento=token)
    return render(request, 'seguimiento.html', {'pedido': pedido})



@staff_member_required
def reporte_pedidos(request):
    # Agrupar pedidos por estado
    pedidos_por_estado = (
        Pedido.objects
        .values("estado_pedido")
        .annotate(total=Count("id"))
        .order_by("estado_pedido")
    )
    return render(request, "reporte.html", {
        "pedidos_por_estado": pedidos_por_estado
    })

