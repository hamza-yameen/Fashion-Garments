from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import product
from django.http import Http404
from carts.models import Cart


class ProductListView(ListView):
    queryset = product.objects.all()
    template_name = "products/proview.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        return context


def Product_List_View(request):
    qs = product.objects.all()
    context = {
        'qset': qs
    }
    return render(request, "products/proview.html", context)


class DetailListView(DetailView):
    queryset = product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DetailListView, self).get_context_data(*args, **kwargs)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product Does'n Exist")
        return instance


def Detail_List_View(request, pk=None, *args, **kwargs):
    # instance = product.objects.get(pk=pk)
    # instance = get_object_or_404(product, pk = pk)
    """
    try:
        instance = product.objects.get(id=pk)
    except product.DoesNotExist:
        print("No Product Found")
        raise Http404("Product Does'n Exist")
        print("OK.....")
    """

    instance = product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product Does'n Exist")

    """
    qs = product.objects.filter(id=pk)
    if qs.exists() and qs.count() == 1:
        instance = qs.first()
    else:
        raise Http404("Product Does'n Exists..")
    """

    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)


class ProductFeatureListView(ListView):
    template_name = "products/proview.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return product.objects.all().features()


class ProductFeatureDetailView(DetailView):
    queryset = product.objects.featured()
    template_name = "products/feature-detail.html"

    # def get_queryset(self, *args, **kwargs):
    #    request = self.request
    #    return product.objects.featured()


class DetailSlugListView(DetailView):
    queryset = product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DetailSlugListView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(product, slug='slug', active=True)
        try:
            instance = product.objects.get(slug=slug, active=True)
        except product.DoesNotExist:
            raise Http404("Not Found....")
        except product.MultipleObjectsReturned:
            qs = product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhhh")
        return instance
