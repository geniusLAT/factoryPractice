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


if __name__ == "__main__":
    print(get_browser_release_year("Chrome","118.0.5993"))