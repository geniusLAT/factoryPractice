def get_os_release_year(os_name, version=None):
    os_data = {
        "windows": {
            "xp": 2001,
            "vista": 2007,
            "7": 2009,
            "8": 2012,
            "8.1": 2013,
            "10": 2015,
            "11": 2021
        },
        "mac os": {None: 1984},
        "mac os x": {
            None: 2001,
            "10.11.6": 2015,
            "10.12.6": 2016,
            "10.13.6": 2018,
            "10.14.6": 2018,
            "10.15.7": 2019,
            "11.7.10": 2020,
            "12.7.6": 2021,
            "13.7": 2022,
            "14.7": 2023,
            "15.0.1": 2024
        },
        "ubuntu": {
            None: 2004,
            "11.04": 2011,
            "11.10": 2011,
            "12.04 LTS": 2012,
            "12.10": 2012,
            "13.04": 2013,
            "13.10": 2013,
            "14.04 LTS": 2014,
            "14.10": 2014,
            "15.04": 2015,
            "15.10": 2015,
            "16.04 LTS": 2016,
            "16.10": 2016,
            "17.04": 2017,
            "17.10": 2017,
            "18.04 LTS": 2018,
            "18.10": 2018,
            "19.04": 2019,
            "19.10": 2019,
            "20.04 LTS": 2020,
            "20.10": 2020,
            "21.04": 2021,
            "21.10": 2021,
            "22.04 LTS": 2022,
            "22.10": 2022
            },
        "fedora": {
            None: 2003,
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
            None: 1996,
            "6": 2011,
            "7": 2013,
            "8": 2015,
            "9": 2017,
            "10": 2019,
            "11": 2021
            },
        "android": {
            "3": 2011,
            "4": 2011,
            "4": 2012,
            "4": 2013,
            "5": 2014,
            "6": 2015,
            "7": 2016,
            "8": 2017,
            "9": 2018,
            "10": 2019,
            "11": 2020,
            "12": 2021,
            "13": 2022
        },
        "ios": {
            None: 2007,
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
            "15": 2021
        }
    }

    result = None
    os_name = os_name.lower()

    if os_name in os_data:
        if version in os_data[os_name]:
            result = os_data[os_name][version]
        elif version is None:
            result = os_data[os_name][None]
        else: result = None

    return result
