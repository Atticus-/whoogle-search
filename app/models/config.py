
class Config:
    # Derived from here:
    # https://sites.google.com/site/tomihasa/google-language-codes#searchlanguage
    LANGUAGES = [
        {'name': 'English', 'value': 'lang_en'},
        {'name': 'Afrikaans', 'value': 'lang_af'},
        {'name': 'Arabic', 'value': 'lang_ar'},
        {'name': 'Armenian', 'value': 'lang_hy'},
        {'name': 'Belarusian', 'value': 'lang_be'},
        {'name': 'Bulgarian', 'value': 'lang_bg'},
        {'name': 'Catalan', 'value': 'lang_ca'},
        {'name': 'Chinese (Simplified)', 'value': 'lang_zh-CN'},
        {'name': 'Chinese (Traditional)', 'value': 'lang_zh-TW'},
        {'name': 'Croatian', 'value': 'lang_hr'},
        {'name': 'Czech', 'value': 'lang_cs'},
        {'name': 'Danish', 'value': 'lang_da'},
        {'name': 'Dutch', 'value': 'lang_nl'},
        {'name': 'Esperanto', 'value': 'lang_eo'},
        {'name': 'Estonian', 'value': 'lang_et'},
        {'name': 'Filipino', 'value': 'lang_tl'},
        {'name': 'Finnish', 'value': 'lang_fi'},
        {'name': 'French', 'value': 'lang_fr'},
        {'name': 'German', 'value': 'lang_de'},
        {'name': 'Greek', 'value': 'lang_el'},
        {'name': 'Hebrew', 'value': 'lang_iw'},
        {'name': 'Hindi', 'value': 'lang_hi'},
        {'name': 'Hungarian', 'value': 'lang_hu'},
        {'name': 'Icelandic', 'value': 'lang_is'},
        {'name': 'Indonesian',  'value': 'lang_id'},
        {'name': 'Italian',  'value': 'lang_it'},
        {'name': 'Japanese',  'value': 'lang_ja'},
        {'name': 'Korean',  'value': 'lang_ko'},
        {'name': 'Latvian',  'value': 'lang_lv'},
        {'name': 'Lithuanian',  'value': 'lang_lt'},
        {'name': 'Norwegian',  'value': 'lang_no'},
        {'name': 'Persian',  'value': 'lang_fa'},
        {'name': 'Polish', 'value': 'lang_pl'},
        {'name': 'Portuguese', 'value': 'lang_pt'},
        {'name': 'Romanian', 'value': 'lang_ro'},
        {'name': 'Russian', 'value': 'lang_ru'},
        {'name': 'Serbian', 'value': 'lang_sr'},
        {'name': 'Slovak', 'value': 'lang_sk'},
        {'name': 'Slovenian', 'value': 'lang_sl'},
        {'name': 'Spanish', 'value': 'lang_es'},
        {'name': 'Swahili', 'value': 'lang_sw'},
        {'name': 'Swedish', 'value': 'lang_sv'},
        {'name': 'Thai', 'value': 'lang_th'},
        {'name': 'Turkish', 'value': 'lang_tr'},
        {'name': 'Ukrainian', 'value': 'lang_uk'},
        {'name': 'Vietnamese', 'value': 'lang_vi'},
    ]

    def __init__(self, **kwargs):
        self.url = ''
        self.lang = 'lang_en'
        self.dark = False
        self.nojs = False
        self.near = ''

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __getitem__(self, name):
        return getattr(self, name)

    def __setitem__(self, name, value):
        return setattr(self, name, value)

    def __delitem__(self, name):
        return delattr(self, name)

    def __contains__(self, name):
        return hasattr(self, name)