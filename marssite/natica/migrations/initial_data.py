# Generated by Django 2.0.1 on 2018-01-28 19:34

from django.db import migrations

def forwards_func(apps, schema_editor):
    db_alias = schema_editor.connection.alias

    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Site = apps.get_model("natica", "Site")
    Site.objects.using(db_alias).bulk_create([
        Site(name="cp"),
        Site(name="ct"),
        Site(name="kp"),
    ])
    Telescope = apps.get_model("natica", "Telescope")
    Telescope.objects.using(db_alias).bulk_create([
        Telescope(name="bok23m"),
        Telescope(name="ct09m"),
        Telescope(name="ct13m"),
        Telescope(name="ct15m"),
        Telescope(name="ct1m"),
        Telescope(name="ct4m"),
        Telescope(name="ctlab"),
        Telescope(name="kp09m"),
        Telescope(name="kp21m"),
        Telescope(name="kp35m"),
        Telescope(name="kp4m"),
        Telescope(name="kpcf"),
        Telescope(name="soar"),
        Telescope(name="wiyn"),
    ])
    Instrument = apps.get_model("natica", "Instrument")
    Instrument.objects.using(db_alias).bulk_create([
        Instrument(name="90prime"),
        Instrument(name="andicam"),
        Instrument(name="arcoiris"),
        Instrument(name="arcon"),
        Instrument(name="bench"),
        Instrument(name="ccd_imager"),
        Instrument(name="chiron"),
        Instrument(name="cosmos"),
        Instrument(name="decam"),
        Instrument(name="echelle"),
        Instrument(name="falmingos"),
        Instrument(name="flamingos"),
        Instrument(name="goodman"),
        Instrument(name="goodman spectrograph"),
        Instrument(name="gtcam"),
        Instrument(name="hdi"),
        Instrument(name="ice"),
        Instrument(name="ispi"),
        Instrument(name="kosmos"),
        Instrument(name="minimo/ice"),
        Instrument(name="mop/ice"),
        Instrument(name="mosaic"),
        Instrument(name="mosaic3"),
        Instrument(name="newfirm"),
        Instrument(name="osiris"),
        Instrument(name="(p)odi"),
        Instrument(name="sami"),
        Instrument(name="soi"),
        Instrument(name="spartan"),
        Instrument(name="spartan ir camera"),
        Instrument(name="whirc"),
        Instrument(name="wildfire"),
        Instrument(name="y4kcam"),
    ])  
    TacInstrumentAlias = apps.get_model("natica", "TacInstrumentAlias")
    TacInstrumentAlias.objects.create(tac="ARCoIRIS", hdr_id="arcoiris")
    TacInstrumentAlias.objects.create(tac="CFIM+T2K", hdr_id="ccd_imager")
    TacInstrumentAlias.objects.create(tac="COSMOS", hdr_id="cosmos")
    TacInstrumentAlias.objects.create(tac="DECam", hdr_id="decam")
    TacInstrumentAlias.objects.create(tac="Goodman", hdr_id="goodman")
    TacInstrumentAlias.objects.create(tac="HDI", hdr_id="hdi")
    TacInstrumentAlias.objects.create(tac="KOSMOS", hdr_id="kosmos")
    TacInstrumentAlias.objects.create(tac="MOSA3", hdr_id="mosaic3")
    TacInstrumentAlias.objects.create(tac="NEWFIRM", hdr_id="newfirm")
    TacInstrumentAlias.objects.create(tac="OSIRIS", hdr_id="osiris")
    TacInstrumentAlias.objects.create(tac="SAMI", hdr_id="sami")
    TacInstrumentAlias.objects.create(tac="SOI", hdr_id="soi")
    TacInstrumentAlias.objects.create(tac="Spartan", hdr_id="spartan")
    TacInstrumentAlias.objects.create(tac="WHIRC", hdr_id="whirc")

    FilePrefix = apps.get_model("natica", "FilePrefix")
    FilePrefix.objects.create(site_id="cp", telescope_id="soar", instrument_id="goodman", prefix="psg")
    FilePrefix.objects.create(site_id="cp", telescope_id="soar", instrument_id="goodman spectrograph", prefix="psg")
    FilePrefix.objects.create(site_id="cp", telescope_id="soar", instrument_id="osiris", prefix="pso")
    FilePrefix.objects.create(site_id="cp", telescope_id="soar", instrument_id="soi", prefix="psi")
    FilePrefix.objects.create(site_id="cp", telescope_id="soar", instrument_id="spartan", prefix="pss")
    FilePrefix.objects.create(site_id="cp", telescope_id="soar", instrument_id="spartan ir camera", prefix="pss")
    FilePrefix.objects.create(site_id="cp", telescope_id="soar", instrument_id="sami", prefix="psa")
    FilePrefix.objects.create(site_id="ct", telescope_id="ct4m", instrument_id="decam", prefix="c4d")
    FilePrefix.objects.create(site_id="ct", telescope_id="ct4m", instrument_id="cosmos", prefix="c4c")
    FilePrefix.objects.create(site_id="ct", telescope_id="ct4m", instrument_id="ispi", prefix="c4i")
    FilePrefix.objects.create(site_id="ct", telescope_id="ct4m", instrument_id="mosaic", prefix="c4m")
    FilePrefix.objects.create(site_id="ct", telescope_id="ct4m", instrument_id="newfirm", prefix="c4n")
    FilePrefix.objects.create(site_id="ct", telescope_id="ct4m", instrument_id="arcoiris", prefix="c4ai")
    FilePrefix.objects.create(site_id="ct", telescope_id="ct15m", instrument_id="chiron", prefix="c15e")
    FilePrefix.objects.create(site_id="ct", telescope_id="ct15m", instrument_id="echelle", prefix="c15e")
    FilePrefix.objects.create(site_id="ct", telescope_id="ct15m", instrument_id="arcon", prefix="c15s")
    FilePrefix.objects.create(site_id="ct", telescope_id="ct13m", instrument_id="andicam", prefix="c13a")
    FilePrefix.objects.create(site_id="ct", telescope_id="ct1m", instrument_id="y4kcam", prefix="c1i")
    FilePrefix.objects.create(site_id="ct", telescope_id="ct09m", instrument_id="ccd_imager", prefix="c09i")
    FilePrefix.objects.create(site_id="ct", telescope_id="ctlab", instrument_id="cosmos", prefix="clc")
    FilePrefix.objects.create(site_id="kp", telescope_id="kp4m", instrument_id="mosaic", prefix="k4m")
    FilePrefix.objects.create(site_id="kp", telescope_id="kp4m", instrument_id="mosaic3", prefix="k4m")
    FilePrefix.objects.create(site_id="kp", telescope_id="kp4m", instrument_id="newfirm", prefix="k4n")
    FilePrefix.objects.create(site_id="kp", telescope_id="kp4m", instrument_id="kosmos", prefix="k4k")
    FilePrefix.objects.create(site_id="kp", telescope_id="kp4m", instrument_id="cosmos", prefix="k4k")
    FilePrefix.objects.create(site_id="kp", telescope_id="kp4m", instrument_id="ice", prefix="k4i")
    FilePrefix.objects.create(site_id="kp", telescope_id="kp4m", instrument_id="wildfire", prefix="k4w")
    FilePrefix.objects.create(site_id="kp", telescope_id="kp4m", instrument_id="flamingos", prefix="k4f")
    FilePrefix.objects.create(site_id="kp", telescope_id="kp35m", instrument_id="whirc", prefix="kww")
    FilePrefix.objects.create(site_id="kp", telescope_id="wiyn", instrument_id="whirc", prefix="kww")
    FilePrefix.objects.create(site_id="kp", telescope_id="wiyn", instrument_id="bench", prefix="kwb")
    FilePrefix.objects.create(site_id="kp", telescope_id="kp35m", instrument_id="minimo/ice", prefix="kwi")
    FilePrefix.objects.create(site_id="kp", telescope_id="kp35m", instrument_id="(p)odi", prefix="kwo")
    FilePrefix.objects.create(site_id="kp", telescope_id="kp21m", instrument_id="mop/ice", prefix="k21i")
    FilePrefix.objects.create(site_id="kp", telescope_id="kp21m", instrument_id="wildfire", prefix="k21w")
    FilePrefix.objects.create(site_id="kp", telescope_id="kp21m", instrument_id="falmingos", prefix="k21f")
    FilePrefix.objects.create(site_id="kp", telescope_id="kp21m", instrument_id="gtcam", prefix="k21g")
    FilePrefix.objects.create(site_id="kp", telescope_id="kpcf", instrument_id="mop/ice", prefix="kcfs")
    FilePrefix.objects.create(site_id="kp", telescope_id="kp09m", instrument_id="hdi", prefix="k09h")
    FilePrefix.objects.create(site_id="kp", telescope_id="kp09m", instrument_id="mosaic", prefix="k09m")
    FilePrefix.objects.create(site_id="kp", telescope_id="kp09m", instrument_id="ice", prefix="k09i")
    FilePrefix.objects.create(site_id="kp", telescope_id="bok23m", instrument_id="90prime", prefix="ksb")
    FilePrefix.objects.create(site_id="ct", telescope_id="bok23m", instrument_id= "kosmos", prefix="ksb")

    Obstype = apps.get_model("natica", "Obstype")
    Obstype.objects.using(db_alias).bulk_create([
        Obstype(name="zero", code="z"),
        Obstype(name="object", code="o"),
        Obstype(name="photometric standard", code="p"),
        Obstype(name="bias", code="z"),
        Obstype(name="dome or projector flat", code="f"),
        Obstype(name="dome flat", code="f"),
        Obstype(name="dflat", code="f"),
        Obstype(name="flat", code="f"),
        Obstype(name="projector", code="f"),
        Obstype(name="sky", code="s"),
        Obstype(name="skyflat", code="s"),
        Obstype(name="dark", code="d"),
        Obstype(name="calibration", code="c"),
        Obstype(name="calibration or comparison", code="c"),
        Obstype(name="comp", code="c"),
        Obstype(name="comparison", code="c"),
        Obstype(name="illumination calibration", code="i"),
        Obstype(name="focus", code="g"),
        Obstype(name="fringe", code="h"),
        Obstype(name="pupil", code="r"),
        Obstype(name="nota", code="u"),
        ])
    Proctype = apps.get_model("natica", "Proctype")
    Proctype.objects.using(db_alias).bulk_create([
        Proctype(name="raw", code="r"),
        Proctype(name="instcal", code="o"),
        Proctype(name="mastercal", code="c"),
        Proctype(name="projected", code="p"),
        Proctype(name="stacked", code="s"),
        Proctype(name="skysub", code="k"),
        Proctype(name="nota", code="u"),
        ])
    Prodtype = apps.get_model("natica", "Prodtype")
    Prodtype.objects.using(db_alias).bulk_create([
        Prodtype(name="image", code="i"),
        Prodtype(name="image 2nd version 1", code="j"),
        Prodtype(name="dqmask", code="d"),
        Prodtype(name="expmap", code="e"),
        Prodtype(name="graphics (size)", code="g"),
        Prodtype(name="weight", code="w"),
        Prodtype(name="nota", code="u"),
        Prodtype(name="wtmap", code="-"), # Found in pipeline, not used for filename
        Prodtype(name="resampled", code="-"), # Found in pipeline, not used for filename
        ])

def reverse_func(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Site = apps.get_model("natica", "Site")
    Site.objects.using(db_alias).all.delete()

    Telescope = apps.get_model("natica", "Telescope")
    Telescope.objects.using(db_alias).all.delete()

    Instrument = apps.get_model("natica", "Instrument")
    Instrument.objects.using(db_alias).all.delete()

    TacInstrumentAlias = apps.get_model("natica", "TacInstrumentAlias")
    TacInstrumentAlias.objects.using(db_alias).all.delete()

    FilePrefix = apps.get_model("natica", "FilePrefix")
    FilePrefix.objects.using(db_alias).all.delete()

    Obstype = apps.get_model("natica", "Obstype")
    Obstype.objects.using(db_alias).all.delete()

    Proctype = apps.get_model("natica", "Proctype")
    Proctype.objects.using(db_alias).all.delete()

    Prodtype = apps.get_model("natica", "Prodtype")
    Prodtype.objects.using(db_alias).all.delete()

    
class Migration(migrations.Migration):

    dependencies = [
        ('natica', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]
