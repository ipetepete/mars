!function(e,n){"object"==typeof exports&&"undefined"!=typeof module?module.exports=n():"function"==typeof define&&define.amd?define(n):(e.__vee_validate_locale__sl=e.__vee_validate_locale__sl||{},e.__vee_validate_locale__sl.js=n())}(this,function(){"use strict";var e={name:"sl",messages:{_default:function(e){return"Vrednost polja "+e+" ni veljavna."},after:function(e,n){return"Polje "+e+" mora biti za "+n[0]+"."},alpha_dash:function(e){return"Polje "+e+" lahko vsebuje le alfanumerične znake kot tudi vezaje in podčrtaje."},alpha_num:function(e){return"Polje "+e+" lahko vsebuje le alfanumerične znake."},alpha_spaces:function(e){return"Polje "+e+" lahko vsebuje le črkovne znake in presledke."},alpha:function(e){return"Polje "+e+" lahko vsebuje le črkovne znake."},before:function(e,n){return"Polje "+e+" mora biti pred "+n[0]+"."},between:function(e,n){return"Polje "+e+" mora biti med "+n[0]+" in "+n[1]+"."},confirmed:function(e){return"Polje "+e+" se ne ujema."},credit_card:function(e){return"Polje "+e+" ni veljavno."},date_between:function(e,n){return"Datum v polju "+e+" mora biti med "+n[0]+" in "+n[1]+"."},date_format:function(e,n){return"Datum v polju "+e+" mora biti sledečega formata: "+n[0]+"."},decimal:function(e,n){void 0===n&&(n=["*"]);var t=n[0];return"Polje "+e+" mora biti numerično in lahko vsebuje "+("*"===t?"":t)+" decimalnih mest."},digits:function(e,n){return"Vrednost polja "+e+" mora biti numerična in vsebovati natančno "+n[0]+" številk."},dimensions:function(e,n){return"Slika "+e+" mora biti široka "+n[0]+" slikovnih točk in visoka "+n[1]+" slikovnih točk."},email:function(e){return"Vrednost polja "+e+" mora biti ustrezen e-naslov."},ext:function(e){return"Datoteka polja "+e+" mora biti ustrezna."},image:function(e){return"Datoteka polja "+e+" mora biti slika."},in:function(e){return"Polje "+e+" mora biti ustrezne vrednosti."},ip:function(e){return"Vrednost polja "+e+" mora biti ustrezen IP naslov."},max:function(e,n){return"Dolžina polja "+e+" ne sme biti večja od "+n[0]+" znakov."},max_value:function(e,n){return"Vrednost polja "+e+" mora biti "+n[0]+" ali manj."},mimes:function(e){return"Datoteka polja "+e+" mora biti ustreznega tipa."},min:function(e,n){return"Dolžina polja "+e+" mora biti vsaj "+n[0]+" znakov."},min_value:function(e,n){return"Vrednost polja "+e+" mora biti "+n[0]+" ali več."},not_in:function(e){return"Polje "+e+" mora biti ustrezne vrednosti."},numeric:function(e){return"Polje "+e+" lahko vsebuje le numerične znake."},regex:function(e){return"Vrednost polja "+e+" ni v ustreznem formatu."},required:function(e){return"Polje "+e+" je obvezno."},size:function(e,n){return"Velikost datoteke "+e+" mora biti manjša kot "+n[0]+" KB."},url:function(e){return"Vrednost polja "+e+" ni veljavni URL naslov."}},attributes:{}};return"undefined"!=typeof VeeValidate&&VeeValidate&&(VeeValidate.Validator,!0)&&VeeValidate.Validator.addLocale(e),e});