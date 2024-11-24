from django.shortcuts import render
from django.conf import settings

import os

def dashboard_home(request):
    # Paths for the plot images (assuming they are saved under /media directory)
    plot_1_url = os.path.join(settings.STATIC_URL, 'bin_heat.png')
    plot_2_url = os.path.join(settings.STATIC_URL, 'corr_cat.png')
    plot_3_url = os.path.join(settings.STATIC_URL, 'corr_price.png')
    violin_plot_1_url = os.path.join(settings.STATIC_URL, 'violin_plot_1.png')

    # Render the dashboard template with the plot URLs
    return render(request, 'dashboard/home.html', {
        'plot_1_url': plot_1_url,
        'plot_2_url': plot_2_url,
        'plot_3_url': plot_3_url,
        'violin_plot_1_url': violin_plot_1_url,
    })
