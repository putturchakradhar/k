from django.shortcuts import render
from .forms import UrlForm
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def open_url_view(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            
            # Open the URL using Selenium
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.get(url)
            driver.quit()
            
            return render(request, 'success.html', {'url': url})
    else:
        form = UrlForm()

    return render(request, 'open_url.html', {'form': form})
