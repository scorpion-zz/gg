from main.models import Brand, Manufacture


def get_context_data(request):
    brands = Brand.objects.all()
    manufactur = Manufacture.objects.all()
    context = {
        'brand': brands,
        'manufacturer': manufactur,
    }
    return context
