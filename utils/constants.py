URL_WEATHER = 'https://api.weather.yandex.ru/v2/informers?'
URL_HISTORY_DAY = 'https://www.denvistorii.ru/'

# координаты посёлка Лыхма
LAT_LYHMA = '63.2190753'
LON_LYHMA = '66.9436997'

LANG_CODE = 'ru_RU'
TIME_ZONE = 'Asia/Yekaterinburg'
# TIME_ZONE = 'Europe/Moscow'

DAY_PARTS = {
    'morning': 'Утром',
    'day': 'Днём',
    'evening': 'Вечером',
    'night': 'Ночью',
}

MONTH_NAMES = {
    '1': 'январь',
    '2': 'февраль',
    '3': 'март',
    '4': 'апрель',
    '5': 'май',
    '6': 'июнь',
    '7': 'июль',
    '8': 'август',
    '9': 'сентябрь',
    '10': 'октябрь',
    '11': 'ноябрь',
    '12': 'декабрь',
}

CONDITIONS_WEATHER = {
    'clear': 'Ясно',
    'partly-cloudy': 'Местами облачно',
    'cloudy': 'Облачно',
    'overcast': 'Пасмурно',
    'drizzle': 'Морось',
    'light-rain': 'Небольшой дождь',
    'rain': 'Дождь',
    'moderate-rain': 'Умеренный дождь',
    'heavy-rain': 'Ливень',
    'continuous-heavy-rain': 'Затяжной ливень',
    'showers': 'Проливной дождь',
    'wet-snow': 'Снег с дождём',
    'light-snow': 'Небольшой снег',
    'snow': 'Снег',
    'snow-showers': 'Снегопад',
    'hail': 'Град',
    'thunderstorm': 'Гроза',
    'thunderstorm-with-rain': 'Дождь с грозой',
    'thunderstorm-with-hail': 'Град с грозой',
}

TANK_FULL_NAME = {
    'н': 'МБН',
    'д': 'МБД',
}

GSM_TANKS = {
    '1': {'length': 8604, 'radius': 2700},
    '2': {'length': 8483, 'radius': 2660},
    '3': {'length': 8483, 'radius': 2660},
    '4': {'length': 9660, 'radius': 2540},
    '5': {'length': 9660, 'radius': 2540},
    '6': {'length': 4287, 'radius': 2430},
}

HYDRO_AKK_VOL = 1252

LOAD_PATTERNS = [
    r'(?:гпа\d\d\w|\d\d\w)\s\d+/\d+\s\w+',  # 62Д 225/253 МХ2
    r'\dбпм\d\s\d+/\d+\s\w+',  # 2БПМ3 225/253 3БПМ2
    r'мх\d\s\d+/\d+\s\w+',  # МХ3 225/253 ГСМ3
    r'гсм\d\s\d+/\d+\s\w+',  # ГСМ3 225/253 АЦ
]

LEVEL_PATTERNS = [
    r'((?:гсм|мх|\dбпм)(?:\s\d-\d+){1,6})',
    r'\w+\s(?:д|н)-\d{1,3}\s(?:д|н)-\d{1,3}',
]

RECOMMEND_TEMP = {
    '1': {'1': '10.0', '2': '10.0', '3': '10.0', '4': '10.0', '5': '10.0', '6': '10.0', '7': '10.0', '8': '10.0', '9': '10.0', '10': '10.0',},
    '2': {'1': '10.0', '2': '10.0', '3': '10.0', '4': '10.0', '5': '10.0', '6': '10.0', '7': '10.0', '8': '10.0', '9': '10.0', '10': '10.0',},
    '3': {'1': '10.0', '2': '10.0', '3': '10.0', '4': '10.0', '5': '10.0', '6': '10.0', '7': '10.1', '8': '10.2', '9': '10.3', '10': '10.4',},
    '4': {'1': '10.6', '2': '10.7', '3': '10.8', '4': '10.9', '5': '11.0', '6': '11.0', '7': '11.3', '8': '11.7', '9': '12.0', '10': '12.3',},
    '5': {'1': '12.7', '2': '13.0', '3': '13.3', '4': '13.7', '5': '14.0', '6': '14.0', '7': '14.8', '8': '15.6', '9': '16.3', '10': '17.1',},
    '6': {'1': '17.9', '2': '18.7', '3': '19.4', '4': '20.2', '5': '21.0', '6': '21.0', '7': '21.3', '8': '21.7', '9': '22.0', '10': '22.3',},
    '7': {'1': '22.7', '2': '23.0', '3': '23.3', '4': '23.7', '5': '24.0', '6': '24.0', '7': '23.9', '8': '23.8', '9': '23.7', '10': '23.6',},
    '8': {'1': '23.4', '2': '23.3', '3': '23.2', '4': '23.1', '5': '23.0', '6': '23.0', '7': '22.4', '8': '21.9', '9': '21.3', '10': '20.8',},
    '9': {'1': '20.2', '2': '19.7', '3': '19.1', '4': '18.6', '5': '18.0', '6': '18.0', '7': '17.7', '8': '17.3', '9': '17.0', '10': '16.7',},
    '10': {'1': '16.3', '2': '16.0', '3': '15.7', '4': '15.3', '5': '15.0', '6': '15.0', '7': '14.7', '8': '14.3', '9': '14.0', '10': '13.7',},
    '11': {'1': '13.3', '2': '13.0', '3': '12.7', '4': '12.3', '5': '12.0', '6': '12.0', '7': '11.8', '8': '11.6', '9': '11.3', '10': '11.1',},
    '12': {'1': '10.9', '2': '10.7', '3': '10.4', '4': '10.2', '5': '10.0', '6': '10.0', '7': '10.0', '8': '10.0', '9': '10.0', '10': '10.0',},
}

EXCEL_COORDINATES = {
    # кортеж (
    #   0-название листа,
    #   1-МБ прошлый месяц,
    #   2-МС прошлый месяц,
    #   3-МБ текущий месяц,
    #   4-МС текущий месяц,
    #   5-расход на работу,
    #   6-закачано-сколько,
    #   7-закачано-откуда
    #   8-скачано-сколько
    #   9-скачано-откуда)
    'ГПА_52_Д': ('Цех5,6', 'C8', 'D8', 'O8', 'P8', 'G8', 'E8', 'F8', 'M8', 'N8'),
    'ГПА_52_Н': ('Цех5,6', 'C9', 'D9', 'O9', 'P9', 'G9', 'E9', 'F9', 'M9', 'N9'),
    'ГПА_53_Д': ('Цех5,6', 'C10', 'D10', 'O10', 'P10', 'G10', 'E10', 'F10', 'M10', 'N10'),
    'ГПА_53_Н': ('Цех5,6', 'C11', 'D11', 'O11', 'P11', 'G11', 'E11', 'F11', 'M11', 'N11'),
    'ГПА_54_Д': ('Цех5,6', 'C12', 'D12', 'O12', 'P12', 'G12', 'E12', 'F12', 'M12', 'N12'),
    'ГПА_54_Н': ('Цех5,6', 'C13', 'D13', 'O13', 'P13', 'G13', 'E13', 'F13', 'M13', 'N13'),
    'ГПА_55_Д': ('Цех5,6', 'C14', 'D14', 'O14', 'P14', 'G14', 'E14', 'F14', 'M14', 'N14'),
    'ГПА_55_Н': ('Цех5,6', 'C15', 'D15', 'O15', 'P15', 'G15', 'E15', 'F15', 'M15', 'N15'),
    'ГПА_61_Д': ('Цех5,6', 'C16', 'D16', 'O16', 'P16', 'G16', 'E16', 'F16', 'M16', 'N16'),
    'ГПА_61_Н': ('Цех5,6', 'C17', 'D17', 'O17', 'P17', 'G17', 'E17', 'F17', 'M17', 'N17'),
    'ГПА_62_Д': ('Цех5,6', 'C18', 'D18', 'O18', 'P18', 'G18', 'E18', 'F18', 'M18', 'N18'),
    'ГПА_62_Н': ('Цех5,6', 'C19', 'D19', 'O19', 'P19', 'G19', 'E19', 'F19', 'M19', 'N19'),
    'ГПА_63_Д': ('Цех5,6', 'C20', 'D20', 'O20', 'P20', 'G20', 'E20', 'F20', 'M20', 'N20'),
    'ГПА_63_Н': ('Цех5,6', 'C21', 'D21', 'O21', 'P21', 'G21', 'E21', 'F21', 'M21', 'N21'),
    'ГПА_64_Д': ('Цех5,6', 'C22', 'D22', 'O22', 'P22', 'G22', 'E22', 'F22', 'M22', 'N22'),
    'ГПА_64_Н': ('Цех5,6', 'C23', 'D23', 'O23', 'P23', 'G23', 'E23', 'F23', 'M23', 'N23'),
    'ГПА_65_Д': ('Цех5,6', 'C24', 'D24', 'O24', 'P24', 'G24', 'E24', 'F24', 'M24', 'N24'),
    'ГПА_65_Н': ('Цех5,6', 'C25', 'D25', 'O25', 'P25', 'G25', 'E25', 'F25', 'M25', 'N25'),
    'МХ_5_1': ('Склад2 КЦ-5,6', 'D32', '', 'O32', '', '', 'K32', 'L32'),
    'МХ_5_2': ('Склад2 КЦ-5,6', 'D33', '', 'O33', '', '', 'K33', 'L33'),
    'МХ_5_3': ('Склад2 КЦ-5,6', 'D34', '', 'O34', '', '', 'K34', 'L34'),
    'МХ_5_4': ('Склад2 КЦ-5,6', 'D35', '', 'O35', '', '', 'K35', 'L35'),
    'ГСМ_5_1': ('Склад2 КЦ-5,6', 'D8', '', 'S8', '', '', 'M8', 'N8'),
    'ГСМ_5_2': ('Склад2 КЦ-5,6', 'D9', '', 'S9', '', '', 'M9', 'N9'),
    'ГСМ_5_3': ('Склад2 КЦ-5,6', 'D10', '', 'S10', '', '', 'M10', 'N10'),
    'ГСМ_5_4': ('Склад2 КЦ-5,6', 'D11', '', 'S11', '', '', 'M11', 'N11'),
    'ГСМ_5_5': ('Склад2 КЦ-5,6', 'D12', '', 'S12', '', '', 'M12', 'N12'),
    'ГСМ_5_6': ('Склад2 КЦ-5,6', 'D13', '', 'S13', '', '', 'M13', 'N13'),
    'БПМ_2_1': ('Склад2 КЦ-5,6', 'D19', '', 'S19', '', '', 'G19', 'H19'),
    'БПМ_2_2': ('Склад2 КЦ-5,6', 'D20', '', 'S20', '', '', 'G20', 'H20'),
    'БПМ_3_1': ('Склад2 КЦ-5,6', 'D21', '', 'S21', '', '', 'G21', 'H21'),
    'БПМ_3_2': ('Склад2 КЦ-5,6', 'D22', '', 'S22', '', '', 'G22', 'H22'),
    'АЦ_5_1': ('Склад2 КЦ-5,6', 'A45', '', 'B45', '', '', '', ''),
    'КОЛОДЕЦ_5_0': ('Склад2 КЦ-5,6', 'A46', '', 'B46', '', '', '', ''),
}


GPA_PARAMS =  {
    'fsn': 'ФСН',
    'fun': 'ФУН',
    'mbd': 'МБД',
    'fsd': 'ФСД',
    'mbn': 'МБН',
    'rso': 'Рсо',
    'dst': 'Рст',
    'dvh': 'Рвх',
}


GPA_NUMS = ['52', '53', '54', '55', '61', '62', '63', '64', '65']


HEADERS = [
    'Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Origin: https://web.gid.ru',
    'DNT: 1',
    'Sec-Fetch-Dest: empty',
    'Sec-Fetch-Mode: cors',
    'Sec-Fetch-Site: same-site',
    'Connection: keep-alive',
    'TE: trailers',
]

USER_AGENTS = [
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991'
    'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7',
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
]

AUTHORS = [
    'Александр Пушкин',
    'Владимир Маяковский',
    'Сергей Есенин',
    'Корней Чуковский',
    'Афанасий Фет',
    'Михаил Лермонтов',
    'Иосиф Бродский',
    'Борис Пастернак',
    'Николай Некрасов',
    'Булат Окуджава',
    'Роберт Рождественский',
    'Шекспир',
    'Александр Блок',
    'Владимир Высоцкий',
    'Омар Хайям',
    'Константин Симонов',
]
