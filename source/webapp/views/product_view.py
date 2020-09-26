from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from webapp.forms import ProductForm
from webapp.models import Product


class IndexView(ListView):
    template_name = 'product/index.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 5
    paginate_orphans = 0

    def get_queryset(self):
        data = Product.objects.all()
        return data


class ProductView(DetailView):
    template_name = 'product/product_view.html'
    model = Product
    paginate_reviews_by = 2
    paginate_reviews_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews, page, is_paginated = self.paginate_reviews(self.object)
        context['reviews'] = reviews
        context['page_obj'] = page
        context['is_paginated'] = is_paginated
        return context

    def paginate_reviews(self, product):
        reviews = product.product_order.all()
        if reviews.count() > 0:
            paginator = Paginator(reviews, self.paginate_reviews_by, orphans=self.paginate_reviews_orphans)
            page_number = self.request.GET.get('page', 1)
            page = paginator.get_page(page_number)
            is_paginated = paginator.num_pages > 1  # page.has_other_pages()
            return page.object_list, page, is_paginated
        else:
            return reviews, None, False


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_create.html'
    permission_required = 'webapp.add_product'

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(PermissionRequiredMixin,UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_update.html'
    permission_required = 'webapp.change_product'


    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'product/product_delete.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_product'


