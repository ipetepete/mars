search_1 = '''\
{"meta": {"api_version": "0.1.7",
          "comment": "WARNING: RESULTS missing values: surve_id, depth. (Where do they come from???)",
          "debug": 1,
          "offset": 0,
          "page_limit": 100,
          "page_result_count": 1,
          "timestamp": "2018-01-07T09:52:25.434",
          "to_here_count": 1,
          "total_count": 1},
 "resultset": [{"dec": ["-0.7410988888888889", "-0.7410988888888889"],
                "exposure": ["10.0", "10.0"],
                "filename": "/data/small-json-scrape/c4d_170815_054546_ori.fits.json",
                "filesize": 233191,
                "filter": ["g DECam SDSS c0001 4720.0 1520.0"],
                "id": 108331,
                "image_type": null,
                "instrument": "decam",
                "md5sum": "48c33967420e9e7ee04690ebb2836c94",
                "obs_date": ["2017-08-15", "2017-08-16"],
                "observation_mode": null,
                "observation_type": ["object"],
                "original_filename": "/data/small-json-scrape/c4d_170815_054546_ori.fits.json",
                "pi": "Vivas",
                "product": "image",
                "prop_id": "2017B-0951",
                "ra": ["323.36257499999994", "323.36257499999994"],
                "release_date": "2017-09-14",
                "seeing": null,
                "telescope": "ct4m"}]}'''

tipairs_0 = [["soar", "goodman"], ["soar", "goodman spectrograph"], ["soar", "osiris"], ["soar", "soi"], ["soar", "spartan"], ["soar", "spartan ir camera"], ["soar", "sami"], ["ct4m", "decam"], ["ct4m", "cosmos"], ["ct4m", "ispi"], ["ct4m", "mosaic"], ["ct4m", "newfirm"], ["ct4m", "arcoiris"], ["ct15m", "chiron"], ["ct15m", "echelle"], ["ct15m", "arcon"], ["ct13m", "andicam"], ["ct1m", "y4kcam"], ["ct09m", "ccd_imager"], ["ctlab", "cosmos"], ["kp4m", "mosaic"], ["kp4m", "mosaic3"], ["kp4m", "newfirm"], ["kp4m", "kosmos"], ["kp4m", "cosmos"], ["kp4m", "ice"], ["kp4m", "wildfire"], ["kp4m", "flamingos"], ["kp35m", "whirc"], ["wiyn", "whirc"], ["wiyn", "bench"], ["kp35m", "minimo/ice"], ["kp35m", "(p)odi"], ["kp21m", "mop/ice"], ["kp21m", "wildfire"], ["kp21m", "falmingos"], ["kp21m", "gtcam"], ["kpcf", "mop/ice"], ["kp09m", "hdi"], ["kp09m", "mosaic"], ["kp09m", "ice"], ["bok23m", "90prime"], ["bok23m", "kosmos"]]


prefix = '[{"site": "cp", "instrument": "goodman", "telescope": "soar", "prefix": "psg"}, {"site": "cp", "instrument": "goodman spectrograph", "telescope": "soar", "prefix": "psg"}, {"site": "cp", "instrument": "osiris", "telescope": "soar", "prefix": "pso"}, {"site": "cp", "instrument": "soi", "telescope": "soar", "prefix": "psi"}, {"site": "cp", "instrument": "spartan", "telescope": "soar", "prefix": "pss"}, {"site": "cp", "instrument": "spartan ir camera", "telescope": "soar", "prefix": "pss"}, {"site": "cp", "instrument": "sami", "telescope": "soar", "prefix": "psa"}, {"site": "ct", "instrument": "decam", "telescope": "ct4m", "prefix": "c4d"}, {"site": "ct", "instrument": "cosmos", "telescope": "ct4m", "prefix": "c4c"}, {"site": "ct", "instrument": "ispi", "telescope": "ct4m", "prefix": "c4i"}, {"site": "ct", "instrument": "mosaic", "telescope": "ct4m", "prefix": "c4m"}, {"site": "ct", "instrument": "newfirm", "telescope": "ct4m", "prefix": "c4n"}, {"site": "ct", "instrument": "arcoiris", "telescope": "ct4m", "prefix": "c4ai"}, {"site": "ct", "instrument": "chiron", "telescope": "ct15m", "prefix": "c15e"}, {"site": "ct", "instrument": "echelle", "telescope": "ct15m", "prefix": "c15e"}, {"site": "ct", "instrument": "arcon", "telescope": "ct15m", "prefix": "c15s"}, {"site": "ct", "instrument": "andicam", "telescope": "ct13m", "prefix": "c13a"}, {"site": "ct", "instrument": "y4kcam", "telescope": "ct1m", "prefix": "c1i"}, {"site": "ct", "instrument": "ccd_imager", "telescope": "ct09m", "prefix": "c09i"}, {"site": "ct", "instrument": "cosmos", "telescope": "ctlab", "prefix": "clc"}, {"site": "kp", "instrument": "mosaic", "telescope": "kp4m", "prefix": "k4m"}, {"site": "kp", "instrument": "mosaic3", "telescope": "kp4m", "prefix": "k4m"}, {"site": "kp", "instrument": "newfirm", "telescope": "kp4m", "prefix": "k4n"}, {"site": "kp", "instrument": "kosmos", "telescope": "kp4m", "prefix": "k4k"}, {"site": "kp", "instrument": "cosmos", "telescope": "kp4m", "prefix": "k4k"}, {"site": "kp", "instrument": "ice", "telescope": "kp4m", "prefix": "k4i"}, {"site": "kp", "instrument": "wildfire", "telescope": "kp4m", "prefix": "k4w"}, {"site": "kp", "instrument": "flamingos", "telescope": "kp4m", "prefix": "k4f"}, {"site": "kp", "instrument": "whirc", "telescope": "kp35m", "prefix": "kww"}, {"site": "kp", "instrument": "whirc", "telescope": "wiyn", "prefix": "kww"}, {"site": "kp", "instrument": "bench", "telescope": "wiyn", "prefix": "kwb"}, {"site": "kp", "instrument": "minimo/ice", "telescope": "kp35m", "prefix": "kwi"}, {"site": "kp", "instrument": "(p)odi", "telescope": "kp35m", "prefix": "kwo"}, {"site": "kp", "instrument": "mop/ice", "telescope": "kp21m", "prefix": "k21i"}, {"site": "kp", "instrument": "wildfire", "telescope": "kp21m", "prefix": "k21w"}, {"site": "kp", "instrument": "falmingos", "telescope": "kp21m", "prefix": "k21f"}, {"site": "kp", "instrument": "gtcam", "telescope": "kp21m", "prefix": "k21g"}, {"site": "kp", "instrument": "mop/ice", "telescope": "kpcf", "prefix": "kcfs"}, {"site": "kp", "instrument": "hdi", "telescope": "kp09m", "prefix": "k09h"}, {"site": "kp", "instrument": "mosaic", "telescope": "kp09m", "prefix": "k09m"}, {"site": "kp", "instrument": "ice", "telescope": "kp09m", "prefix": "k09i"}, {"site": "kp", "instrument": "90prime", "telescope": "bok23m", "prefix": "ksb"}, {"site": "ct", "instrument": "kosmos", "telescope": "bok23m", "prefix": "ksb"}]'

obstype = '[{"name": "zero", "code": "z"}, {"name": "object", "code": "o"}, {"name": "photometric standard", "code": "p"}, {"name": "bias", "code": "z"}, {"name": "dome or projector flat", "code": "f"}, {"name": "dome flat", "code": "f"}, {"name": "dflat", "code": "f"}, {"name": "flat", "code": "f"}, {"name": "projector", "code": "f"}, {"name": "sky", "code": "s"}, {"name": "skyflat", "code": "s"}, {"name": "dark", "code": "d"}, {"name": "calibration", "code": "c"}, {"name": "calibration or comparison", "code": "c"}, {"name": "comp", "code": "c"}, {"name": "comparison", "code": "c"}, {"name": "illumination calibration", "code": "i"}, {"name": "focus", "code": "g"}, {"name": "fringe", "code": "h"}, {"name": "pupil", "code": "r"}, {"name": "nota", "code": "u"}]'

proctype = '[{"name": "raw", "code": "r"}, {"name": "instcal", "code": "o"}, {"name": "mastercal", "code": "c"}, {"name": "projected", "code": "p"}, {"name": "stacked", "code": "s"}, {"name": "skysub", "code": "k"}, {"name": "nota", "code": "u"}]'

prodtype = '[{"name": "image", "code": "i"}, {"name": "image 2nd version 1", "code": "j"}, {"name": "dqmask", "code": "d"}, {"name": "expmap", "code": "e"}, {"name": "graphics (size)", "code": "g"}, {"name": "weight", "code": "w"}, {"name": "nota", "code": "u"}, {"name": "wtmap", "code": "-"}, {"name": "resampled", "code": "-"}]'

rawreq = '[{"name": "TELESCOP", "comment": ""}]'

filenamereq = '[{"name": "DATE-OBS", "comment": "triplespec doesn\'t have it; comes from other field"}, {"name": "DTSITE", "comment": "for BASENAME"}, {"name": "DTTELESC", "comment": "for BASENAME"}, {"name": "DTINSTRU", "comment": "for BASENAME"}, {"name": "OBSTYPE", "comment": "for BASENAME"}, {"name": "PROCTYPE", "comment": "for BASENAME"}, {"name": "PRODTYPE", "comment": "for BASENAME"}, {"name": "DTCALDAT", "comment": "for PATH (dome)"}, {"name": "DTPROPID", "comment": "for PATH (dome)"}]'

ingestreq = '[{"name": "SIMPLE", "comment": ""}, {"name": "OBSERVAT", "comment": "needed for std filename"}, {"name": "DTPROPID", "comment": "observing proposal ID"}, {"name": "DTCALDAT", "comment": "calendar date from observing schedule"}, {"name": "DTACQNAM", "comment": "file name supplied at telescope; User knows on THIS name."}, {"name": "DTNSANAM", "comment": "file name in archive (renamed from user supplied)"}, {"name": "DTTELESC", "comment": ""}, {"name": "DTSITE", "comment": ""}, {"name": "DTINSTRU", "comment": ""}]'

ingestrec = '[{"name": "INSTRUME", "comment": "moved from RAW_REQUIRED to statisfy: /scraped/mtn_raw/ct15m-echelle/chi150724.10"}, {"name": "DTCOPYRI", "comment": "coypright holder of data"}, {"name": "DTOBSERV", "comment": ""}, {"name": "DTPI", "comment": ""}, {"name": "DTPIAFFL", "comment": ""}, {"name": "DTTITLE", "comment": ""}, {"name": "OBSID", "comment": ""}, {"name": "DTACQNAM", "comment": ""}, {"name": "DTCALDAT", "comment": ""}, {"name": "DTINSTRU", "comment": ""}, {"name": "DTNSANAM", "comment": ""}, {"name": "DTPROPID", "comment": ""}, {"name": "DTSITE", "comment": ""}, {"name": "DTTELESC", "comment": ""}, {"name": "PROCTYPE", "comment": ""}, {"name": "PRODTYPE", "comment": ""}]'

supportreq = '[{"name": "IMAGETYP", "comment": ""}, {"name": "DATE-OBS", "comment": ""}, {"name": "TIME-OBS", "comment": ""}, {"name": "DATE", "comment": ""}, {"name": "PROPID", "comment": ""}]'

floatreq = '[{"name": "DATAMAX", "comment": ""}, {"name": "DATAMIN", "comment": ""}, {"name": "PSCAL", "comment": ""}, {"name": "PZERO", "comment": ""}, {"name": "TSCAL", "comment": ""}, {"name": "TZERO", "comment": ""}, {"name": "CRPIX", "comment": ""}, {"name": "CRVAL", "comment": ""}, {"name": "CDELT", "comment": ""}, {"name": "CROTA", "comment": ""}, {"name": "PC", "comment": ""}, {"name": "CD", "comment": ""}, {"name": "PV", "comment": ""}, {"name": "CRDER", "comment": ""}, {"name": "CSYER", "comment": ""}, {"name": "EPOCH", "comment": ""}, {"name": "EQUINOX", "comment": ""}, {"name": "MJD-OBS", "comment": ""}, {"name": "MJD-AVG", "comment": ""}, {"name": "LONPOLE", "comment": ""}, {"name": "LATPOLE", "comment": ""}, {"name": "OBSGEO-Z", "comment": ""}, {"name": "OBSGEO-Y", "comment": ""}, {"name": "OBSGEO-X", "comment": ""}, {"name": "RESTFRQ", "comment": ""}, {"name": "RESTWAV", "comment": ""}, {"name": "VELANGL", "comment": ""}, {"name": "VELOSYS", "comment": ""}, {"name": "ZSOURCE", "comment": ""}]'
