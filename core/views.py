from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


class IndexView(TemplateView):
    template_name = 'index.html'

class DadosJSONView(BaseLineChartView):
    def get_labels(self):
        labels = [
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro"
        ]
        return labels

    def get_providers(self):
        datasets = [
            "Programação para leigos",
            "Algoritimo e lógica",
            "Programação em C",
            "Programação em java",
            "Programação em python",
            "Bamco de dados"
        ]
        return datasets

    def get_data(self):
        dados = []
        for l in range(6):
            for c in range(12):
                dado = [
                    randint(1, 200),
                    randint(1, 200),
                    randint(1, 200),
                    randint(1, 200),
                    randint(1, 200),
                    randint(1, 200),
                    randint(1, 200),
                    randint(1, 200),
                    randint(1, 200),
                    randint(1, 200),
                    randint(1, 200),
                    randint(1, 200)

                ]
            dados.append(dado)
        return dados