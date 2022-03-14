import webbrowser as wb


def open_url(url):
    try:
        wb.get(using='google-chrome').open_new_tab(str(url))
    except:
        pass
    try:
        wb.get(using='chrome').open_new_tab(str(url))
    except:
        pass
    try:
        wb.get(using='opera').open_new_tab(str(url))
    except:
        pass
    try:
        wb.open_new_tab(str(url))
    except:
        pass
