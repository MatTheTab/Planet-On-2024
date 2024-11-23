from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.apps import apps

import os
import pandas as pd

from search.utils import extract_cpv_codes, extract_description, get_matching_rows

def search_home(request):
    return render(request, 'search/home.html')

def search_similar_projects(request):
    table_html = None
    app_config = apps.get_app_config('search')

    if request.method == 'POST' and 'pdf_file' in request.FILES:
        pdf_file = request.FILES['pdf_file']

        # Read the PDF content directly from the uploaded file
        try:
            cpv_codes = extract_cpv_codes(pdf_file.name)
            description = extract_description(pdf_file.name)

            # TODO? load somewhere else?
            # df = pd.read_csv("../data_processed/app_data.csv")
            df = app_config.dataframe
            model = app_config.model
            
            sorted_df = get_matching_rows(cpv_codes, df, description, model)
            sorted_df = sorted_df[["noticeNumber", "orderObject"]]
            sorted_df.rename(columns={"orderObject": "Description", "noticeNumber": "Order number"}, inplace=True)
            
            # Convert DataFrame to HTML table
            table_html = sorted_df.to_html(
                classes="table table-striped table-bordered", 
                index=False, 
                table_id="resultsTable"
            )
        except Exception as e:
            table_html = f"<p class='text-danger'>Error processing file: {e}</p>"

    return render(request, 'search/home.html', {'table_html': table_html})