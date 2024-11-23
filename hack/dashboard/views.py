from django.shortcuts import render

def dashboard_home(request):
    # Mock dane
    mock_data = {
        'charts': [
            {'id': 1, 'title': 'Wykres Sprzedaży', 'value': [30, 50, 80, 120]},
            {'id': 2, 'title': 'Analiza Użytkowników', 'value': [200, 300, 400, 500]},
        ],
        'cards': [
            {'title': 'Liczba Użytkowników', 'value': 1500, 'icon': 'fa-user'},
            {'title': 'Obroty (w tys.)', 'value': 250, 'icon': 'fa-chart-line'},
        ]
    }
    return render(request, 'dashboard/home.html', {'mock_data': mock_data})
