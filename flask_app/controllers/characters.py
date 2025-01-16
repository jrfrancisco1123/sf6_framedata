from flask_app import app
from flask import render_template

from flask_app.frame_data import aki, akuma, bison, blanka, cammy, chunli, deejay, dhalsim, ed, guile, honda, jamie, jp, juri, ken, kimberly, lily, luke, manon, marisa, rashid, ryu, terry, zangief

@app.route('/sf6_framedata/character/aki')
def view_aki():
    return render_template('characters/aki.html', commons=aki.commons, normals=aki.normals, uniques=aki.uniques, specials=aki.specials, super_arts=aki.super_arts, throws=aki.throws)

@app.route('/sf6_framedata/character/akuma')
def view_akuma():
    return render_template('characters/akuma.html', commons=akuma.commons, normals=akuma.normals, uniques=akuma.uniques, specials=akuma.specials, super_arts=akuma.super_arts, throws=akuma.throws)

@app.route('/sf6_framedata/character/bison')
def view_bison():
    return render_template('characters/bison.html', commons=bison.commons, normals=bison.normals, uniques=bison.uniques, specials=bison.specials, super_arts=bison.super_arts, throws=bison.throws)

@app.route('/sf6_framedata/character/blanka')
def view_blanka():
    return render_template('characters/blanka.html', commons=blanka.commons, normals=blanka.normals, uniques=blanka.uniques, specials=blanka.specials, super_arts=blanka.super_arts, throws=blanka.throws)

@app.route('/sf6_framedata/character/cammy')
def view_cammy():
    return render_template('characters/cammy.html', normals=cammy.normals, uniques=cammy.uniques, specials=cammy.specials, super_arts=cammy.super_arts, throws=cammy.throws, commons=cammy.commons)

@app.route('/sf6_framedata/character/chunli')
def view_chunli():
    return render_template('characters/chunli.html', normals=chunli.normals, uniques=chunli.uniques, specials=chunli.specials, super_arts=chunli.super_arts, throws=chunli.throws, commons=chunli.commons)

@app.route('/sf6_framedata/character/deejay')
def view_deejay():
    return render_template('characters/deejay.html', commons=deejay.commons, normals=deejay.normals, uniques=deejay.uniques, specials=deejay.specials, super_arts=deejay.super_arts, throws=deejay.throws)

@app.route('/sf6_framedata/character/dhalsim')
def view_dhalsim():
    return render_template('characters/dhalsim.html', commons=dhalsim.commons, normals=dhalsim.normals, uniques=dhalsim.uniques, specials=dhalsim.specials, super_arts=dhalsim.super_arts, throws=dhalsim.throws)

@app.route('/sf6_framedata/character/ed')
def view_ed():
    return render_template('characters/ed.html', commons=ed.commons, normals=ed.normals, uniques=ed.uniques, specials=ed.specials, super_arts=ed.super_arts, throws=ed.throws)

@app.route('/sf6_framedata/character/guile')
def view_guile():
    return render_template('characters/guile.html', commons=guile.commons, normals=guile.normals, uniques=guile.uniques, specials=guile.specials, super_arts=guile.super_arts, throws=guile.throws)

@app.route('/sf6_framedata/character/honda')
def view_honda():
    return render_template('characters/honda.html', commons=honda.commons, normals=honda.normals, uniques=honda.uniques, specials=honda.specials, super_arts=honda.super_arts, throws=honda.throws)

@app.route('/sf6_framedata/character/jamie')
def view_jamie():
    return render_template('characters/jamie.html', commons=jamie.commons, normals=jamie.normals, uniques=jamie.uniques, specials=jamie.specials, super_arts=jamie.super_arts, throws=jamie.throws)

@app.route('/sf6_framedata/character/jp')
def view_jp():
    return render_template('characters/jp.html', normals=jp.normals, uniques=jp.uniques, specials=jp.specials, super_arts=jp.super_arts, throws=jp.throws, commons=jp.commons)

@app.route('/sf6_framedata/character/juri')
def view_juri():
    return render_template('characters/juri.html', normals=juri.normals, uniques=juri.uniques, specials=juri.specials, super_arts=juri.super_arts, throws=juri.throws, commons=juri.commons)

@app.route('/sf6_framedata/character/ken')
def view_ken():
    return render_template('characters/ken.html', normals=ken.normals, uniques=ken.uniques, specials=ken.specials, super_arts=ken.super_arts, throws=ken.throws, commons=ken.commons)

@app.route('/sf6_framedata/character/kimberly')
def view_kimberly():
    return render_template('characters/kimberly.html', normals=kimberly.normals, uniques=kimberly.uniques, specials=kimberly.specials, super_arts=kimberly.super_arts, throws=kimberly.throws, commons=kimberly.commons)

@app.route('/sf6_framedata/character/lily')
def view_lily():
    return render_template('characters/lily.html', normals=lily.normals, uniques=lily.uniques, specials=lily.specials, super_arts=lily.super_arts, throws=lily.throws, commons=lily.commons)

@app.route('/sf6_framedata/character/luke')
def view_luke():
    return render_template('characters/luke.html', commons=luke.commons, normals=luke.normals, uniques=luke.uniques, specials=luke.specials, super_arts=luke.super_arts, throws=luke.throws)

@app.route('/sf6_framedata/character/mai')
def view_mai():
    return render_template('characters/mai.html')

@app.route('/sf6_framedata/character/manon')
def view_manon():
    return render_template('characters/manon.html', normals = manon.normals, uniques=manon.uniques ,specials=manon.specials, super_arts=manon.super_arts, throws=manon.throws, commons=manon.commons)

@app.route('/sf6_framedata/character/marisa')
def view_marisa():
    return render_template('characters/marisa.html', normals=marisa.normals, uniques=marisa.uniques, specials=marisa.specials, super_arts=marisa.super_arts, throws=marisa.throws, commons=marisa.commons)

@app.route('/sf6_framedata/character/rashid')
def view_rashid():
    return render_template('characters/rashid.html', commons=rashid.commons, normals=rashid.normals, uniques=rashid.uniques, specials=rashid.specials, super_arts=rashid.super_arts, throws=rashid.throws)

@app.route('/sf6_framedata/character/ryu')
def view_ryu():
    return render_template('characters/ryu.html', normals=ryu.normals, uniques=ryu.uniques, specials=ryu.specials, super_arts=ryu.super_arts, throws=ryu.throws, commons=ryu.commons)

@app.route('/sf6_framedata/character/terry')
def view_terry():
    return render_template('characters/terry.html', commons=terry.commons, normals=terry.normals, uniques=terry.uniques, specials=terry.specials, super_arts=terry.super_arts, throws=terry.throws)

@app.route('/sf6_framedata/character/zangief')
def view_zangief():
    return render_template('characters/zangief.html', normals=zangief.normals, uniques=zangief.uniques, specials=zangief.specials, super_arts=zangief.super_arts, throws=zangief.throws, commons=zangief.commons)