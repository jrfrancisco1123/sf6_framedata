commons = {
    'forward dash': ['', '', '19 total frames', ['', ''], '0', ''],
    'backward dash': ['', '', '25 total frames', ['', ''], '0', ''],
    'drive impact': ['26', '26-27', '35', ['D', '-3'], '800', 'High'],
    'drive reversal (blocking)': ['20', '20-35', '26', ['D', '-6'], '500', 'High'],
    'drive reversal (recovering)': ['18', '18-33', '26', ['D', '-6'], '500', 'High'],
    'drive parry': ['1', '1-12', '33', ['', ''], '0', ''],
    'perfect parry (strike)': ['1', '', '1', ['', ''], '0', ''],
    'perfect parry (projectile)': ['1', '', '10', ['', ''], '0', ''],
    'parry drive rush': ['', '', '45 total frames', ['', ''], '0', ''],
    'cancel drive rush': ['', '', '46 total frames', ['', ''], '0', '']
}

normals = {
        'lp': ['4', '4-6', '7', ['5', '-3'], '300', 'High'],
        'mp': ['5', '5-8', '10', ['6', '1'], '600', 'High'],
        'hp': ['13', '13-15', '20', ['2', '-3'], '800', 'High'],
        'lk': ['5', '5-7', '10', ['2', '-2'], '300', 'High'],
        'mk': ['7', '7-10', '16', ['4', '-2'], '500', 'High'],
        'hk': ['14', '14-16', '18', ['4', '0'], '900', 'High'],
        'clp': ['4', '4-6', '7', ['4', '-2'], '300', 'High'],
        'cmp': ['6', '6-9', '13', ['4', '-2'], '600', 'High'],
        'chp': ['11', '11-23', '18', ['1', '-3'], '900', 'High'],
        'clk': ['4', '4-5', '10', ['0', '-2'], '200', 'Low'],
        'cmk': ['7', '7-9', '19', ['-2', '-6'], '500', 'Low'],
        'chk': ['9', '9-14', '19', ['D', '-7'], '900', 'Low'],
        'jlp': ['4', '4-13', '3 frames after landing', ['', ''], '300', 'Mid'],
        'jmp': ['7', '7-21', '3 frames after landing', ['', ''], '600', 'Mid'],
        'jhp': ['9', '9-14', '3 frames after landing', ['', ''], '800', 'Mid'],
        'jlk': ['4', '4-11', '3 frames after landing', ['', ''], '300', 'Mid'],
        'jmk': ['6', '6-10', '3 frames after landing', ['', ''], '500', 'Mid'],
        'jhk': ['8', '8-14', '3 frames after landing', ['', ''], '800', 'Mid'],
        'jhk (neutral jump)': ['8', '8-12', '3 frames after landing', ['', ''], '800', 'Mid']
    }

uniques = {
    'swift thrust': ['7', '7-9', '15', ['2', '-3'], '600', 'High'],
    'hakkei': ['8', '8-13', '14', ['5', '-1'], '800', 'High'],
    'water lotus fist': ['21', '21-24', '14', ['1', '-2'], '800', 'Mid'],
    'yokusen kick': ['16', '16-17', '23', ['-1', '-4'], '800', 'High'],
    'falling crane': ['37', '37-38', '1+12 frames after landing', ['7', '3'], '800', 'Mid'], 
    'yoso kick (1)': ['3', '3-13', '3 frames after landing', ['', ''], '300', 'High'],
    'yoso kick (2)': ['6', '6-16', '3 frames after landing', ['', ''], '300', 'High'],
    'yoso kick (3)': ['6', '6-16', '3 frames after landing', ['', ''], '500', 'High'],
    'soaring eagle punches': ['6', '6-9', '3 frames after landing', ['', ''], '500', 'Mid'],
    'serenity stream': ['', '', '89 total frames', ['', ''], '0', ''],
    'orchid palm': ['5', '5-9', '17', ['-3', '-4'], '500', 'High'],
    'snake strike': ['7', '7-17', '20', ['D', '-15'], '750', 'Low'],
    'lotus fist': ['23', '23-32', '19', ['2', '-3'], '900', 'Mid-High'],
    'forward strike': ['8', '8-12', '13', ['-1', '-5'], '500', 'Low'],
    'senpu kick': ['10', '10-14', '23', ['-4', '-10'], '800', 'Low'],
    'tenku kick': ['8', '8-12', '24', ['D', '-9'], '700', 'High']
}

specials = {
    'light kikoken': ['15', '15-104', '47 total frames', ['-3', '-7'], '600', 'High-Projectile'],
    'medium kikoken': ['12', '12-66', '45 total frames', ['-3', '-7'], '600', 'High-Projectile'],
    'heavy kikoken': ['11', '11-35', '43 total frames', ['-2', '-6'], '600', 'High-Projectile'],
    'od kikoken': ['11', '', '39 total frames', ['0', '5'], '800', 'High-Projectile'],
    'light hundred lightning kicks': ['8', '8-23', '20', ['3', '-8'], '800', 'High'],
    'medium hundred lightning kicks': ['14', '14-34', '22', ['3', '-8'], '900', 'High'],
    'heavy hundred lightning kicks': ['23', '23-47', '15', ['D', '-3'], '1000', 'High'],
    'od hundred lightning kicks': ['8', '8-33', '21', ['3', '-3'], '800', 'High'],
    'lightning kick barrage': ['11', '11-46', '25', ['D', '-13'], '700', 'High'],
    'light aerial hundred lightning kicks': ['8', '21', '15 frames after landing', ['', ''], '900', 'High'],
    'medium aerial hundred lightning kicks': ['10', '10-30', '15 frames after landing', ['', ''], '1000', 'High'],
    'heavy aerial hundred lightning kicks': ['12', '12-35', '15 frames after landing', ['', ''], '1100', 'High'],
    'od aerial hundred lightning kicks': ['6', '6-31', '15 frames after landing', ['', ''], '1600', 'High'],
    'light spinning bird kick': ['9', '9-26', '6+24 frames after landing', ['D', '-18'], '1000', 'High'],
    'medium spinning bird kick': ['16', '16-48', '8+21 frames after landing', ['D', '-17'], '1200', 'High'],
    'heavy spinning bird kick': ['20', '20-64', '8+22 frames after landing', ['D', '-18'], '1400', 'High'],
    'od spinning bird kick': ['16', '16-55', '8+15 frames after landing', ['D', '-12'], '800', 'High'],
    'light hazanshu': ['23', '23-24', '21', ['0', '-9'], '1000', 'Mid'],
    'medium hazanshu': ['27', '27-29', '16', ['2', '-3'], '1000', 'Mid'],
    'heavy hazanshu': ['32', '32-34', '18', ['6', '-1'], '1200', 'Mid'],
    'od hazanshu': ['26', '26-28', '16', ['D', '-5'], '1200', 'Mid'],
    'light tensho kicks': ['5', '5-18', '27+12 frames after landing', ['D', '-37'], '900', 'High'],
    'medium tensho kicks': ['7', '7-20', '31+12 frames after landing', ['D', '-41'], '1000', 'High'],
    'heavy tensho kicks': ['9', '9-43', '26+12 frames after landing', ['D', '-57'], '1200', 'High'],
    'od tensho kicks': ['6', '6-65', '14+27 frames after landing', ['D', '-40'], '1400', 'High']
    }

super_arts = {
    'kikosho': ['7', '7-76', '122 total frames', ['D', '-22'], '1700', 'High'],
    'aerial kikosho': ['7', '7-56', '16 frames after landing', ['D', ''], '2000', 'High'],
    'hoyoku-sen': ['11', '11-96', '48', ['D', '-35'], '2000', 'High'],
    'soten ranka': ['8', '8-42', '40', ['D', '-24'], '4000', 'High'],
    'soten ranka (under 25% vit)': ['8', '8-42', '40', ['D', '-24'], '4500', 'High']
}

throws = {
    'koshuto': ['5', '5-7', '23', ['D', ''], '1200', 'Throw'],
    'taiji fan': ['5', '5-7', '23', ['D', ''], '1200', 'Throw'],
    'ryuseiraku': ['5', '5-7', '3 frames after landing', ['D', ''], '1200', 'Throw']
}
