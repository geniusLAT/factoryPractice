#['Chrome Mobile', 'Yandex Browser', 'Chrome', 'Chrome Mobile WebView', 'Edge', 'Opera', 'MiuiBrowser', 'Samsung Internet', 'Chrome Mobile iOS', 
# 'Mobile Safari', 'YandexSearch', 'Opera Mobile', 'Google', 'Firefox', 'Chromium', 'Mobile Safari UI/WKWebView', 'Edge Mobile', 'Safari', 'Firefox Mobile', 
# 'Facebook', 'Mail.ru Chromium Browser', 'Iron', 'Instagram', 'Mint Browser', 'Opera Mini', 'Bytespider', 'HeadlessChrome', 'Amazon Silk', 'Seznam prohlížeč', 
# 'IE', 'UC Browser', 'Maxthon', 'Pinterest', 'YandexModule2', 'Phantom', 'Flipboard', 'IE Mobile', 'Puffin', 'Electron', 'Android', 'Bot', 'QQ Browser', 'Firefox iOS', 
# 'Opera Coast', 'Pale Moon', 'Dragon', 'Sogou Explorer', 'Other', 'Apple Mail', 'Whale', 'Flipboard-Briefing', 'QQ Browser Mobile', 'Waterfox', 'SeaMonkey', 
# 'DuckDuckGo Mobile', 'WebKit Nightly', 'Vivaldi', 'Crosswalk', 'Basilisk', 'HbbTV']


def get_browser_release_year(browser_name, version=None):
    if browser_name == 'Chrome':
        return get_Chrome_release_year(version)
    if browser_name == 'Yandex Browser':
        return get_Yandex_Browser_release_year(version)
    if browser_name == 'Chrome Mobile':
        return get_Chrome_Mobile_release_year(version)
    if browser_name == 'Chrome Mobile WebView':
        return get_Chrome_Mobile_WebView_release_year(version)
    if browser_name == 'Edge':
        return get_Edge_release_year(version)
    if browser_name == 'Opera':
        return get_Opera_release_year(version)
    if browser_name == 'Firefox':
        return get_Firefox_release_year(version)
    if browser_name == 'Safari':
        return get_Safari_release_year(version)

def get_Yandex_Browser_release_year(version=None):
    #18.11.1
    dot_separated = version.split('.')
    print(dot_separated[0])
    first_digit = int(dot_separated[0])

    if first_digit > 21:
        return "2022"
    if first_digit > 20:
        return "2021"
    if first_digit > 19:
        return "2020"
    if first_digit > 18:
        return "2018"
    if first_digit > 17:
        return "2017"
    if first_digit > 15:
        return "2016"
    if first_digit > 15:
        return "2016"
    if first_digit > 14:
        return "2015"
    if first_digit > 13:
        return "2014"
    if first_digit > 1:
        return "2013"
    
    return "2012"

def get_Chrome_release_year(version=None):
    # 118.0.5993
    dot_separated = version.split('.')
    print(dot_separated[0])
    first_digit = int(dot_separated[0])

    if first_digit >119:
        return "2024"
    if first_digit >101:
        return "2023"
    if first_digit >92:
        return "2022"
    if first_digit >87:
        return "2021"
    if first_digit >76:
        return "2020"
    if first_digit >69:
        return "2019"
    if first_digit >62:
        return "2018"
    if first_digit >53:
        return "2017"
    if first_digit >45:
        return "2016"
    if first_digit >33:
        return "2015"
    if first_digit >27:
        return "2014"
    if first_digit >18:
        return "2013"
    if first_digit >9:
        return "2012"
    if first_digit >4:
        return "2011"
    if first_digit >2:
        return "2010"
    if first_digit >1:
        return "2009"
    return "2008"

def get_Chrome_Mobile_release_year(version=None):
    
    dot_separated = version.split('.')
    print(dot_separated[0])
    first_digit = int(dot_separated[0])

    if first_digit >= 32 and first_digit <= 39:
        return "2017"
    if first_digit >= 40 and first_digit <= 47:
        return "2017"
    if first_digit >= 48 and first_digit <= 55:
        return "2017"
    if first_digit >= 56 and first_digit <= 70:
        return "2017"
    if first_digit >= 64 and first_digit <= 71:
        return "2018"
    if first_digit >= 70 and first_digit <= 81:
        return "2020"
    if first_digit >= 82 and first_digit <= 95:
        return "2021"
    if first_digit >= 96 and first_digit <= 106:
        return "2022"
    if first_digit >= 107 and first_digit <= 119:
        return "2023"
    if first_digit >= 120 and first_digit <= 130:
        return "2024"
    return "2013"

def get_Chrome_Mobile_WebView_release_year(version=None):
    
    dot_separated = version.split('.')
    print(dot_separated[0])
    first_digit = int(dot_separated[0])

    if first_digit >= 40 and first_digit <= 76:
        return "2015"
    if first_digit >= 77 and first_digit <= 79:
        return "2019"
    if first_digit >= 80 and first_digit <= 89:
        return "2020"
    if first_digit >= 90:
        return "2021"
    return "2013"

def get_Edge_release_year(version=None):
    
    dot_separated = version.split('.')
    print(dot_separated[0])
    first_digit = int(dot_separated[0])

    if first_digit >= 38 and first_digit <= 39:
        return "2016"
    if first_digit >= 40 and first_digit <= 41:
        return "2017"
    if first_digit >= 42 and first_digit <= 43:
        return "2018"
    if first_digit >= 44:
        return "2019"
    return "2015"

def get_Opera_release_year(version=None):
    
    dot_separated = version.split('.')
    print(dot_separated[0])
    first_digit = int(dot_separated[0])

    if first_digit > 12:
        return "2013"
    if first_digit > 11:
        return "2012"
    if first_digit > 10:
        return "2011"
    if first_digit > 3:
        return "2000"
    return "1997"

def get_Safari_release_year(version=None):
    
    dot_separated = version.split('.')
    print(dot_separated[0])
    first_digit = int(dot_separated[0])

    if first_digit == 2:
        return "2005"
    if first_digit == 3:
        return "2007"
    if first_digit == 4:
        return "2009"
    if first_digit == 5:
        return "2010"
    if first_digit == 6:
        return "2012"
    if first_digit == 7:
        return "2013"
    if first_digit == 8:
        return "2014"
    if first_digit == 9:
        return "2015"
    if first_digit == 10:
        return "2016"
    if first_digit == 11:
        return "2017"
    if first_digit == 12:
        return "2018"
    if first_digit == 13:
        return "2019"
    if first_digit == 14:
        return "2020"
    if first_digit == 15:
        return "2021"
    if first_digit == 16:
        return "2022"
    if first_digit == 17:
        return "2023"
    if first_digit == 18:
        return "2024"
    return "2003"

def get_Firefox_release_year(version=None):
    
    dot_separated = version.split('.')
    print(dot_separated[0])
    first_digit = int(dot_separated[0])

    if first_digit >= 5 and first_digit <= 9:
        return "2011"
    if first_digit >= 10 and first_digit <= 23:
        return "2012"
    if first_digit >= 24 and first_digit <= 30:
        return "2013"
    if first_digit >= 31 and first_digit <= 37:
        return "2014"
    if first_digit >= 38 and first_digit <= 44:
        return "2015"
    if first_digit >= 45 and first_digit <= 51:
        return "2016"
    if first_digit >= 52 and first_digit <= 59:
        return "2017"
    if first_digit >= 60 and first_digit <= 67:
        return "2018"
    if first_digit >= 68 and first_digit <= 77:
        return "2019"
    if first_digit >= 78 and first_digit <= 90:
        return "2020"
    if first_digit >= 91 and first_digit <= 101:
        return "2021"
    if first_digit >= 102 and first_digit <= 114:
        return "2022"
    if first_digit >= 115 and first_digit <= 127:
        return "2023"
    if first_digit >= 128:
        return "2024"
    return "2010"

if __name__ == "__main__":
    print(get_browser_release_year("Chrome","118.0.5993"))
