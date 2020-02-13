from django.shortcuts import render, redirect
from carts.models import Cart
from product.models import product
from Order.models import order
from accounts.form import LoginForm, GuestForm
from billing.models import Billing
from accounts.models import GuestModel


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    context = {
        'cart': cart_obj
    }
    return render(request, "cart/cartview.html", context)


def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            pro_obj = product.objects.get(id=product_id)
        except product.DoesNotExist:
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if pro_obj in cart_obj.product.all():
            cart_obj.product.remove(pro_obj)
        else:
            cart_obj.product.add(pro_obj)
        request.session['product_counter'] = cart_obj.product.count()
    # return redirect(product_obj.get_absolute_url())
    return redirect("cart:home")


def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)

    if cart_created or cart_obj.product.count() == 0:
        return redirect("cart:home")

    login_form = LoginForm()
    guest_form = GuestForm()

    guest_email_id = request.session.get("guest_email_id")

    user = request.user
    billing_profile = None

    if user.is_authenticated:
        billing_profile, billing_profile_created = Billing.objects.get_or_create(user=user, email=user.email)
    elif guest_email_id is not None:
        guest_email_id_obj = GuestModel.objects.get(id=guest_email_id)
        billing_profile, billing_guest_profile_created = Billing.objects.get_or_create(email=guest_email_id_obj.email)
    else:
        pass

    order_obj = None
    if billing_profile is not None: 
        order_qs = order.objects.filter(billing_profile=billing_profile, cart=cart_obj, active=True)
        print(order_qs.count())
        if order_qs.count() == 1:
            order_obj = order_qs.first()
        else:
            old_order_qs = order.objects.exclude(billing_profile=billing_profile).filter(cart=cart_obj, active=True)
            print(old_order_qs)
            if old_order_qs.exists():
                old_order_qs.update(active=False)
            order_obj = order.objects.create(billing_profile=billing_profile, cart=cart_obj)
            print(order_obj)

    context = {
        'object': order_obj,
        'billing': billing_profile,
        'login_form': login_form,
        'guest_form': guest_form,
    }
    return render(request, "cart/checkout.html", context)
