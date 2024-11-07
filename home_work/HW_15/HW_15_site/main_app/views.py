from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.utils import timezone


def home(request):
    return render(request, 'home.html',{'message_home':'Welcome to main page'})

def about(request):
    return render(request, 'about.html', {'message_about':
                     'Ми займаємось дистриб`юцією хімічних компонентів вже понад десять років.'
                     'Основні напрямки нашої діяльності це'
                     'функціональні добавки для виробництва фарб, оздоблювальних матеріалів та сухих '
                     'будівельних сумішей. Також у нашому портфоліо є продукти для застосування в упаковці '
                     '(друк на картоні, виробництво скотчу та ламінування) та в нетканих матеріалах '
                     '(полотна, геотекстиль, синтепон).'})

class ContactView(TemplateView):
    template_name = 'contact.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email'] = 'maksym@serpa.com'
        context['phone'] = '+380123456789'
        context['address'] = 'вул. Шевченка, 1, Київ, Україна'
        context['updated_at'] = timezone.now()
        print( context['updated_at'])
        return context


class ServiceView(View):
    # @staticmethod
    def get(self, request):
        services = [
            'Дисперсії',
            'Ефіри целюлози',
            'Полімерні порошки',
            'Модифікатори реології',
            'Піногасники',
            'Диспергатори',
            'Акрилові загусники',
            'Опалесцентні полімери',
            'Допоміжні добавки',
            'Пігментні пасти',
            'Серпа',

        ]
        return render(request, 'services.html', {'services': services})
