import requests
from bs4 import BeautifulSoup

suicide_websites_list = [
    'https://pobedish.ru/main/suicide_methods/suitsid_bez_rozovyh_ochkov.htm',
    'https://pobedish.ru/main/suicide_methods?id=22'
    'http://www.suicide-forum.com/',
    'https://pobedish.ru/main/help/plohie_mysli_lezut_v_golovu_vse_bolshe_zagonyayus.htm',
    'https://pobedish.ru/main/help',
    'http://nosuicid.ru/',
    'https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%BE%D1%81%D0%BE%D0%B1%D1%8B_%D1%81%D0%B0%D0%BC%D0%BE%D1%83%D0%B1%D0%B8%D0%B9%D1%81%D1%82%D0%B2%D0%B0',
    'https://smisl-zhizni.com/kak-umeret-bez-boli/',
    'https://ru.qaz.wiki/wiki/Suicide_methods',
    'http://www.palata6.net/forum/index.php?s=e61dd56fdafba7613df14ec890a27b43&showtopic=22338',
    'https://pobedish.ru/main/ikillmyself',
    'https://pobedish.ru/main/ikillmyself/kak_ya_sobiralas_pokonchit_s_soboy_buduchi_beremennoy.htm',
    'https://pobedish.ru/main/ikillmyself?id=203',
    'https://pobedish.ru/main/ikillmyself?id=164',
    'https://pobedish.ru/main/help/ya_hochu_prosto_izbavitsya_ot_problem..._no_ya_viju_tolko_odin_vyhod....htm',
    'https://pobedish.ru/main/ikillmyself/shag_do_beskonechnosti.htm',
    'https://pobedish.ru/main/rodnie/papa_povesilsya.htm',
    'https://pobedish.ru/main/help/ya_prosto_ne_viju_smysla_vo_vsem_etom...zachem_ya_voobshe_etom_mire.htm',
    'https://pobedish.ru/main/help?action=&keyword=&where=&page=15',
    'https://pobedish.ru/main/help/vse_ot_menya_v_etoj_zhizni_otvernulis.htm',
    'https://pobedish.ru/main/help/zhizn_-_ne_zhizn._chasto_zadumyvayus_o_samoubijstve.htm',
    'https://pobedish.ru/main/help/ya_poteryala_smysl_zhizni_i_mechtayu_o_smerti.htm',
    'https://pobedish.ru/main/help/postoyanno_dumayu_o_suicide_vozmojno_eto_edinstvennyy_sposob_prekratit_moi_stradaniya..htm',
    'https://pobedish.ru/main/help/moya_jizn_-_polnoe_nichto_i_ya_nenaviju_sebya..htm',
    'https://pobedish.ru/main/help/iz-za_vseh_muk_kotorye_so_mnoy_byli_v_techenii_mnogih_let_ya_hochu_pokonchit_s_soboy_i_polojit_konec_pozoru_i_usherbnosti..htm', 
]

normal_websites_list = [
    'http://nosuicid.ru/',
    'https://ru.wikipedia.org/wiki/%D0%A1%D0%BC%D0%B5%D1%80%D1%82%D1%8C_%D1%87%D0%B8%D0%BD%D0%BE%D0%B2%D0%BD%D0%B8%D0%BA%D0%B0',
    'https://www.yandex.ru/search/',
    'https://dicktanty.ru/diktant-1750/',
    'https://plusiminusi.ru/plyusy-i-minusy-zhizni-v-gorax/',
    'https://ru.wikipedia.org/wiki/%D0%A8%D0%BF%D0%B0%D0%B6%D0%BD%D0%B8%D0%BA_%D1%82%D0%BE%D0%BD%D0%BA%D0%B8%D0%B9',
    'https://allatravesti.com/s_chego_nachinaetsya_zhizn_cheloveka',
    'https://vsdelke.ru/biznes/biznes-chto-eto.html',
    'https://mogu-pisat.ru/txt/?ELEMENT_ID=7081168',
    'https://mogu-pisat.ru/txt/?ELEMENT_ID=2529526',
    'https://texterra.ru/',
    'https://direct.yandex.ru/',
    'https://yandex.ru/company/',
    'https://www.who.int/ru',
    'https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B8%D1%88%D0%B8%D0%BD,_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80_%D0%9D%D0%B8%D0%BA%D0%B8%D1%84%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D1%87',
    'https://ru.wikipedia.org/wiki/%D0%AD%D1%87%D0%B5%D0%B1%D0%B5%D1%80%D1%80%D0%B8%D0%B0,_%D0%A5%D0%BE%D1%81%D0%B5%D0%B1%D0%B0',
    'https://ru.wikipedia.org/wiki/%D0%93%D0%B0%D0%BB%D1%81%D1%82%D1%83%D0%BA_%D0%B8%D0%B7_%D0%BF%D0%B5%D0%BD%D1%8C%D0%BA%D0%B8',
    'https://ru.texthandler.com/',
    'https://dicktanty.ru/diktant-1742/',
    'https://dicktanty.ru/diktant-1744/',
    'https://dictants.com/5-klass/5-klass-2-chetvert/',
    'https://dictants.com/1-klass/diktanty-1-klass-3-chetvert/',
    'https://dictants.com/2-klass/diktanty-2-klass-2-chetvert/',
    'https://ru.wikipedia.org/wiki/%D0%A1%D0%BC%D0%B5%D1%80%D1%82%D1%8C_%D1%87%D0%B8%D0%BD%D0%BE%D0%B2%D0%BD%D0%B8%D0%BA%D0%B0',
    'https://pitportal.ru/samples_docs/gigiena_pitaniya/6418.html',
    'https://ru.wikipedia.org/wiki/%D0%90%D1%80%D0%B0%D1%80%D0%B0%D1%82',
]

def get_suicide_contents_soup():
    l = []
    for url in suicide_websites_list:
        result = requests.get(url)
        result.encoding='utf-8'
        l.append(BeautifulSoup(result.text, "html.parser"))
    return l

def get_normal_websites_soup():
    l = []
    for url in normal_websites_list:
        result = requests.get(url)
        result.encoding='utf-8'
        l.append(BeautifulSoup(result.text, "html.parser"))
    return l