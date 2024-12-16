def get_os_release_year(os_name, version=None):
    os_data = {
        "windows": {
            "NT": 1993,
            "2000": 2000,
            "XP": 2001,
            "Vista": 2007,
            "7": 2009,
            "8": 2012,
            "8.1": 2013,   
            "RT": 2012,
            "10": 2015,
            "11": 2021
        },
        "mac os": {None: 1984},
        "mac os x": {
            None: 2001,
            "": 2001,
            "10.6": 2009,
            "10.6.8": 2011,
            "10.8.5": 2012,
            "10.9.2": 2013,
            "10.9.5": 2013,
            "10.10": 2014,
            "10.10.0": 2014,
            "10.10.2": 2014,
            "10.10.3": 2014,
            "10.11": 2015,
            "10.11.1": 2015,
            "10.11.4": 2015,
            "10.11.6": 2015,
            "10.12.1": 2016,
            "10.12.2": 2016,
            "10.12.6": 2016,
            "10.13": 2018,
            "10.13.2": 2018,
            "10.13.4": 2018,
            "10.13.6": 2018,
            "10.14": 2018,
            "10.14.1": 2018,
            "10.14.2": 2018,
            "10.14.3": 2018,
            "10.14.4": 2018,
            "10.14.5": 2018,
            "10.14.6": 2018,
            "10.15": 2019,
            "10.15.0": 2019,
            "10.15.1": 2019,
            "10.15.2": 2019,
            "10.15.6": 2019,
            "10.15.7": 2019,
            "10.16.0": 2020,
            "10.16": 2020,
            "11.0.0": 2020,
            "11.3": 2021,
            "11.4": 2021,
            "11.13": 2017,
            "11.7.10": 2020,
            "12.1.0": 2021,
            "12.2.1": 2021,
            "12.7.6": 2021,
            "13.0.1": 2022,
            "13.7": 2022,
            "14.7": 2023,
            "15.0.1": 2024
        },
        "ubuntu": {
            None: 2004,
            "": 2004,
            "11": 2011,
            "12": 2012,
            "13": 2013,
            "14": 2014,
            "15": 2015,
            "16": 2016,
            "17": 2017,
            "18": 2018,
            "19": 2019,
            "20": 2020,
            "21": 2021,
            "22": 2022,
            },
        "fedora": {
            None: 2003,
            "": 2003,
            "15": 2011,
            "16": 2011,
            "17": 2012,
            "18": 2013,
            "19": 2013,
            "20": 2014,
            "21": 2014,
            "22": 2015,
            "23": 2015,
            "24": 2016,
            "25": 2016,
            "26": 2017,
            "27": 2017,
            "28": 2018,
            "29": 2018,
            "30": 2019,
            "31": 2019,
            "32": 2020,
            "33": 2020,
            "34": 2021,
            "35": 2021
            },
        "debian": {
            "": 1996,
            "6": 2011,
            "7": 2013,
            "8": 2015,
            "9": 2017,
            "10": 2019,
            "11": 2021
            },
        "android": {
            "3": 2011,
            "4": 2013,
            "5": 2014,
            "6": 2015,
            "7": 2016,
            "8": 2017,
            "9": 2018,
            "10": 2019,
            "11": 2020,
            "12": 2021,
            "13": 2022,
            "14": 2023,
            "15": 2024
        },
        "ios": {
            None: 2007,
            "": 2007,
            "5": 2011,
            "6": 2012,
            "7": 2013,
            "8": 2014,
            "9": 2015,
            "10": 2016,
            "11": 2017,
            "12": 2018,
            "13": 2019,
            "14": 2020,
            "15": 2021,
            "16": 2022,
            "17": 2023,
            "18": 2024
        },
        "tizen": {
            None: 2013,
            "": 2013,
            "2": 2013,
            "3": 2015,
            "5": 2018,
            "6": 2020,
            "7": 2023
        },
        "windows phone": {
            None: 2012,
            "": 2012,
            "8": 2012,
            "10": 2015
        }
    }

    result = None
    os_name = os_name.lower()

    if os_name != 'mac os x' and os_name !='windows' and version != None:
        dot_separated = version.split('.')
        first_digit = int(dot_separated[0])
    else:
        first_digit = version

    if os_name == 'chrome os':
        result = 2019
    elif os_name == 'chromecast':
        result = 2015
    elif os_name == 'chrome os':
        result = 2011
    elif os_name in os_data:
        if first_digit in os_data[os_name]:
            result = os_data[os_name][first_digit]
        elif first_digit is None:
            result = os_data[os_name][None]
        else: result = None

    return result
