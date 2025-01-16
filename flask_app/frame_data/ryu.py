commons = {
    'forward dash': ['', '', '19 total frames', ['', ''], '0', ''],
    'backward dash': ['', '', '23 total frames', ['', ''], '0', ''],
    'drive impact': ['26', '26-27', '35', ['D', '-3'], '800', 'High'],
    'drive reversal (blocking)': ['20', '20-22', '26', ['D', '-6'], '500', 'High'],
    'drive reversal (recovering)': ['18', '18-20', '26', ['D', '-6'], '500', 'High'],
    'drive parry': ['1', '1-12', '33', ['', ''], '0', ''],
    'perfect parry (strike)': ['1', '', '1', ['', ''], '0', ''],
    'perfect parry (projectile)': ['1', '', '10', ['', ''], '0', ''],
    'parry drive rush': ['', '', '45 total frames', ['', ''], '0', ''],
    'cancel drive rush': ['', '', '46 total frames', ['', ''], '0', '']
}

normals = {
        'lp': ['4', '4-6', '7', ['4', '-1'], '300', 'High'],
        'mp': ['6', '6-9', '11', ['7', '-1'], '600', 'High'],
        'hp': ['10', '10-14', '18', ['4', '-2'], '800', 'High'],
        'lk': ['5', '5-7', '11', ['2', '-4'], '300', 'High'],
        'mk': ['9', '9-11', '18', ['4', '-4'], '700', 'High'],
        'hk': ['12', '12-15', '20', ['9', '1'], '900', 'High'],
        'clp': ['4', '4-5', '9', ['4', '-1'], '300', 'High'],
        'cmp': ['6', '6-9', '13', ['5', '0'], '600', 'High'],
        'chp': ['9', '9-14', '22', ['1', '-7'], '800', 'High'],
        'clk': ['5', '5-6', '10', ['3', '-3'], '200', 'Low'],
        'cmk': ['8', '8-10', '19', ['1', '-6'], '500', 'Low'],
        'chk': ['9', '9-11', '23', ['D', '-12'], '900', 'Low'],
        'jlp': ['4', '4-13', '3 frames after landing', ['', ''], '300', 'Mid'],
        'jmp': ['8', '8-12', '3 frames after landing', ['', ''], '700', 'Mid-High'],
        'jhp': ['9', '9-14', '3 frames after landing', ['', ''], '800', 'Mid'],
        'jlk': ['6', '6-15', '3 frames after landing', ['', ''], '300', 'Mid'],
        'jmk': ['7', '7-12', '3 frames after landing', ['', ''], '500', 'Mid'],
        'jhk': ['12', '12-19', '3 frames after landing', ['', ''], '800', 'Mid']
    }

uniques = {
    'collarbone breaker': ['20', '20-23', '19', ['3', '-1'], '600', 'Mid-High'],
    'solar plexus strike': ['20', '20-24', '16', ['6', '3'], '800', 'High'],
    'short uppercut': ['7', '7-10', '26', ['1', '-13'], '800', 'High'],
    'axe kick': ['10', '10-23', '21', ['0', '-4'], '800', 'High'],
    'whirlwind kick': ['16', '16-19', '20', ['2', '-4'], '800', 'High'],
    'high double strike': ['9', '9-12', '20', ['D', '-8'], '1000', 'High'],
    'fuwa triple strike (2)': ['5', '5-7', '16', ['1', '-4'], '300', 'High'],
    'fuwa triple strike (3)': ['17', '17-20', '20', ['D', '-8'], '900', 'High'],
}

specials = {
    'light hadoken': ['16', '', '47 total frames', ['1', '-5'], '600', 'High-Projectile'],
    'medium hadoken': ['14', '', '47 total frames', ['-1', '-7'], '600', 'High-Projectile'],
    'heavy hadoken': ['12', '', '47 total frames', ['-3', '-9'], '600', 'High-Projectile'],
    'hadoken (denjin charge)': ['12', '', '42 total frames', ['D', '-3'], '800', 'High-Projectile'],
    'od hadoken': ['12', '', '40 total frames', ['D', '-1'], '800', 'High-Projectile'],
    'od hadoken (denjin charge)': ['12', '', '38 total frames', ['D', '2'], '1000', 'High-Projectile'],
    'light shoryuken': ['5', '5-14', '21+12 frames after landing', ['D', '-23'], '1100', 'High'],
    'medium shoryuken': ['6', '6-15', '30+12 frames after landing', ['D', '-32'], '1200', 'High'],
    'heavy shoryuken': ['7', '7-16', '34+15 frames after landing', ['D', '-39'], '1400', 'High'],
    'od shoryuken': ['6', '6-15', '37+15 frames after landing', ['D', '-40'], '1600', 'High'],
    'light tatsumaki senpu-kyaku': ['12', '12-14', '14+18 frames after landing', ['D', '-15'], '900', 'High'],
    'medium tatsumaki senpu-kyaku': ['14', '14-30', '11+20 frames after landing', ['D', '-13'], '1000', 'High'],
    'heavy tatsumaki senpu-kyaku': ['16', '16-47', '14+17 frames after landing', ['D', '-13'], '1200', 'High'],
    'od tatsumaki senpu-kyaku': ['13', '13-37', '10+13 frames after landing', ['D', '-14'], '1000', 'High'],
    'aerial tatsumaki senpu-kyaku': ['11', '11-27', '16 frames after landing', ['D', ''], '900', 'High'],
    'od aerial tatsumaki senpu-kyaku': ['11', '11-28', '16 frames after landing', ['D', ''], '1500', 'High'],
    'light high blade kick': ['14', '14-19', '22', ['D', '-11'], '1100', 'High'],
    'medium high blade kick': ['18', '18-26', '19', ['D', '-8'], '1200', 'High'],
    'heavy high blade kick': ['27', '27-35', '15', ['D', '-3'], '1300', 'High'],
    'od high blade kick': ['17', '17-21', '33', ['D', '-18'], '800', 'High'],
    'light hashogeki': ['12', '12-17', '18', ['2', '-3'], '700', 'High'],
    'medium hashogeki': ['19', '19-24', '17', ['2', '-6'], '800', 'High'],
    'heavy hashogeki': ['30', '30-35', '19', ['D', '2'], '800', 'High'],
    'hashogeki (denjin charged)': ['20', '20-25', '19', ['D', '3'], '800', 'High'],
    'od hashogeki': ['18', '18-22', '20', ['3', '3'], '1100', 'High'],
    'od hashogeki (denjin charged)': ['18', '18-23', '19', ['D', '4'], '800', 'High'],
    'denjin charge': ['', '', '52 total frames', ['', ''], '0']
    }

super_arts = {
    'shinku hadoken': ['7', '', '86 total frames', ['D', '-24'], '2000', 'High-Projectile'],
    'shinku hadoken (denjin charged)': ['7', '', '86 total frames', ['D', '-24'], '2400', 'High-Projectile'],
    'shin hashogeki (lvl1)': ['12', '12-17', '39', ['D', '-20'], '2800', 'High'],
    'shin hashogeki (lvl2)': ['20', '20-25', '39', ['D', '-20'], '2900', 'High'],
    'shin hashogeki (lvl3)': ['70', '70-75', '39', ['D', '-20'], '3000', 'High'],
    'shin hashogeki (denjin charged) (lvl1)': ['12', '12-17', '39', ['D', '-20'], '3200', 'High'],
    'shin hashogeki (denjin charged) (lvl2)': ['20', '20-25', '39', ['D', '-20'], '3300', 'High'],
    'shin hashogeki (denjin charged) (lvl3)': ['70', '70-75', '39', ['D', '-20'], '3400', 'High'],
    'shin shoryuken': ['5', '5-16', '71', ['D', '-52'], '4000', 'High'],
    'shin shoryuken (under 25% vit)': ['5', '5-16', '71', ['D', '-52'], '4500', 'High']
}

throws = {
    'shoulder throw': ['5', '5-7', '23', ['D', ''], '1200', 'Throw'],
    'somersault throw': ['5', '5-7', '23', ['D', ''], '1200', 'Throw']
}

