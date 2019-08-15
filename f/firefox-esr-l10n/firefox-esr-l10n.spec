%define cid            langpack-ru@firefox.mozilla.org
%define cid_dir        %firefox_noarch_extensionsdir/%cid

%define cid_dict       ru@dictionaries.addons.mozilla.org
%define cid_dict_dir   %firefox_noarch_extensionsdir/%cid_dict

Name:		firefox-esr-l10n
Version:	68.0.1
Release:	alt1
Summary:	Language Pack for Firefox ESR

License:	MPL/GPL/LGPL
Group:		Networking/WWW
URL:		http://www.mozilla.org/products/firefox/
Packager:	Andey Cherepanov <cas@altlinux.org>

Source0:	%name-%version.tar
# Language package template
Source1:	firefox-l10n-template.in

BuildRequires(pre): rpm-build-firefox

# Spell dictionaries
BuildRequires: hunspell-af
BuildRequires: hunspell-ak
BuildRequires: hunspell-am
BuildRequires: hunspell-ar
BuildRequires: hunspell-as
BuildRequires: hunspell-ast
BuildRequires: hunspell-az
BuildRequires: hunspell-be
BuildRequires: hunspell-ber
BuildRequires: hunspell-bg
BuildRequires: hunspell-bn
BuildRequires: hunspell-br
BuildRequires: hunspell-ca
BuildRequires: hunspell-cop
BuildRequires: hunspell-csb
BuildRequires: hunspell-cv
BuildRequires: hunspell-cy
BuildRequires: hunspell-da
BuildRequires: hunspell-de
BuildRequires: hunspell-dsb
BuildRequires: hunspell-el
BuildRequires: hunspell-en
BuildRequires: hunspell-en_CA
BuildRequires: hunspell-eo
BuildRequires: hunspell-es
BuildRequires: hunspell-et
BuildRequires: hunspell-eu
BuildRequires: hunspell-fa
BuildRequires: hunspell-fj
BuildRequires: hunspell-fo
BuildRequires: hunspell-fr
BuildRequires: hunspell-fur
BuildRequires: hunspell-fy
BuildRequires: hunspell-ga
BuildRequires: hunspell-gd
BuildRequires: hunspell-gl
BuildRequires: hunspell-grc
BuildRequires: hunspell-gu
BuildRequires: hunspell-gv
BuildRequires: hunspell-haw
BuildRequires: hunspell-he
BuildRequires: hunspell-hi
BuildRequires: hunspell-hil
BuildRequires: hunspell-hr
BuildRequires: hunspell-hsb
BuildRequires: hunspell-ht
BuildRequires: hunspell-hu
BuildRequires: hunspell-hy
BuildRequires: hunspell-ia
BuildRequires: hunspell-id
BuildRequires: hunspell-is
BuildRequires: hunspell-it
BuildRequires: hunspell-kk
BuildRequires: hunspell-km
BuildRequires: hunspell-kn
BuildRequires: hunspell-ko
BuildRequires: hunspell-ku
BuildRequires: hunspell-ky
BuildRequires: hunspell-la
BuildRequires: hunspell-lb
BuildRequires: hunspell-ln
BuildRequires: hunspell-lt
BuildRequires: hunspell-mai
BuildRequires: hunspell-mg
BuildRequires: hunspell-mi
BuildRequires: hunspell-mk
BuildRequires: hunspell-ml
BuildRequires: hunspell-mn
BuildRequires: hunspell-mos
BuildRequires: hunspell-mr
BuildRequires: hunspell-ms
BuildRequires: hunspell-mt
BuildRequires: hunspell-nb
BuildRequires: hunspell-nds
BuildRequires: hunspell-ne
BuildRequires: hunspell-nl
BuildRequires: hunspell-nn
BuildRequires: hunspell-nr
BuildRequires: hunspell-nso
BuildRequires: hunspell-ny
BuildRequires: hunspell-oc
BuildRequires: hunspell-om
BuildRequires: hunspell-or
BuildRequires: hunspell-pa
BuildRequires: hunspell-pl
BuildRequires: hunspell-pt
BuildRequires: hunspell-qu
BuildRequires: hunspell-quh
BuildRequires: hunspell-ro
BuildRequires: hunspell-ru-lebedev
BuildRequires: hunspell-rw
BuildRequires: hunspell-sc
BuildRequires: hunspell-se
BuildRequires: hunspell-shs
BuildRequires: hunspell-si
BuildRequires: hunspell-sk
BuildRequires: hunspell-sl
BuildRequires: hunspell-smj
BuildRequires: hunspell-so
BuildRequires: hunspell-sq
BuildRequires: hunspell-sr
BuildRequires: hunspell-ss
BuildRequires: hunspell-st
BuildRequires: hunspell-sv
BuildRequires: hunspell-sw
BuildRequires: hunspell-ta
BuildRequires: hunspell-te
BuildRequires: hunspell-tet
BuildRequires: hunspell-th
BuildRequires: hunspell-ti
BuildRequires: hunspell-tk
BuildRequires: hunspell-tl
BuildRequires: hunspell-tn
BuildRequires: hunspell-tpi
BuildRequires: hunspell-ts
BuildRequires: hunspell-tt
BuildRequires: hunspell-uk
BuildRequires: hunspell-ur
BuildRequires: hunspell-uz
BuildRequires: hunspell-ve
BuildRequires: hunspell-vi
BuildRequires: hunspell-wa
BuildRequires: hunspell-xh
BuildRequires: hunspell-yi
BuildRequires: hunspell-zu

%description
Language Pack for Firefox ESR.

# Spell check dictionaries
%define dictionaries af_NA af_ZA ak_GH am_ET ar_AE ar_BH ar_DJ ar_DZ ar_EG ar_ER ar_IL ar_IN ar_IQ ar_JO ar_KM ar_KW ar_LB ar_LY ar_MA ar_MR ar_OM ar_PS ar_QA ar_SA ar_SD ar_SO ar_SY ar_TD ar_TN ar_YE as_IN ast_ES az_AZ be_BY ber_MA bg_BG br_FR bs_BA ca_AD ca_ES ca_FR ca_IT cop_EG csb_PL cv_RU cy_GB da_DK de_BE de_CH de_DE de_LI de_LU dsb_DE el_CY el_GR en_AU en_BS en_BZ en_CA en_GB en_GH en_IE en_IN en_JM en_NA en_NZ en_PH en_TT en_US en_ZA en_ZW eo es_AR es_BO es_CL es_CO es_CR es_CU es_DO es_EC es_ES es_GT es_HN es_MX es_NI es_PA es_PE es_PR es_PY es_SV es_US es_UY es_VE et_EE eu_ES fa_IR fil_PH fj fo_FO fr_BE fr_CA fr_CH fr_FR fr_LU fr_MC fur_IT fy_DE fy_NL ga_IE gd_GB gl_ES grc gu_IN gv_GB haw he_IL hi_IN hil_PH hr_HR hsb_DE ht_HT hu_HU hy_AM ia id_ID is_IS it_CH it_IT kk_KZ km_KH kn_IN ko_KR ku_SY ku_TR ky_KG la lb_LU ln_CD lt_LT mai_IN mg mi_NZ mk_MK ml_IN mn_MN mos_BF mr_IN ms_BN ms_MY mt_MT nb_NO nds_DE nds_NL ne_IN ne_NP nl_AW nl_BE nl_NL nn_NO nr_ZA nso_ZA ny_MW oc_FR om_ET om_KE or_IN pa_IN pl_PL plt pt_BR qu_EC quh_BO ro_RO ru_RU-lebedev rw_RW sc_IT se_FI se_NO se_SE sh_ME sh_RS sh_YU shs_CA si_LK sk_SK sl_SI smj_NO smj_SE so_DJ so_ET so_KE so_SO sq_AL sr_ME sr_RS sr_YU ss_ZA st_ZA sv_FI sv_SE sw_KE sw_TZ ta_IN te_IN tet_ID tet_TL th_TH ti_ER ti_ET tk tl_PH tn_BW tn_ZA tpi_PG ts_ZA tt_RU uk_UA ur_IN ur_PK uz_UZ ve_ZA vi_VN wa_BE xh_ZA yi_US zu

# Supported l10n language lists
%define langlist af an ar ast az be bg bn br bs ca cs cy da de el en_CA en_GB en_US eo es_AR es_CL es_ES es_MX et eu fa ff fi fr fy_NL ga_IE gd gl gu_IN he hi_IN hr hsb hu hy_AM ia id is it ja kk km kn ko lij lt lv mk mr ms my nb_NO nl nn_NO oc pa_IN pl pt_BR pt_PT ro ru si sk sl sq sr sv_SE ta te th tr uk ur uz vi xh zh_CN zh_TW cak ka kab

# Disabled l10n languages, for any reason
# - no locales-XX package (or virtual provides):
# ach ak dsb rm son uu ne_NP

# Disabled hunspell dicts, for any reason
%define disabled_dict_langlist an bn cs en_GB en_US en_ZA es_AR es_CL es_ES es_MX ff fi fy_NL ga_IE gu_IN hi_IN hy_AM ja lij lv nb_NO nn_NO pa_IN pt_BR pt_PT sv_SE tr zh_CN zh_TW cak ka kab my ne_NP

# Language descriptions
%define language_af af
%define langname_af Afrikaans
%define language_ak ak
%define langname_ak Akan
%define language_an an
%define langname_an Aragonese
%define language_ar ar
%define langname_ar Arabic
%define language_as as
%define langname_as Assamese
%define language_ast ast
%define langname_ast Asturian
%define language_az az
%define langname_az Azeri
%define language_be be
%define langname_be Belarusian
%define language_bg bg
%define langname_bg Bulgarian
%define language_bn bn
%define langname_bn Bengali
%define language_br br
%define langname_br Breton
%define language_bs bs
%define langname_bs Bosnian
%define language_ca ca
%define langname_ca Catalan
%define language_cak cak
%define langname_cak Kaqchikel
%define language_cs cs
%define langname_cs Czech
%define language_csb csb
%define langname_csb Kashubian
%define language_cy cy
%define langname_cy Welsh
%define language_da da
%define langname_da Dansk
%define language_de de
%define langname_de German
%define language_el el
%define langname_el Greek
%define language_en_CA en-CA
%define langname_en_CA English (Caribbean)
%define language_en_GB en-GB
%define langname_en_GB British English
%define language_en_US en-US
%define langname_en_US English (United States)
%define language_en_ZA en-ZA
%define langname_en_ZA English (South Africa)
%define language_eo eo
%define langname_eo Esperanto
%define language_es_AR es-AR
%define langname_es_AR Spanish (Argentina)
%define language_es_CL es-CL
%define langname_es_CL Spanish (Chile)
%define language_es_ES es-ES
%define langname_es_ES Spanish
%define language_es_MX es-MX
%define langname_es_MX Spanish (Mexico)
%define language_et et
%define langname_et Estonian
%define language_eu eu
%define langname_eu Basque
%define language_fa fa
%define langname_fa Farsi
%define language_ff ff
%define langname_ff Fulah
%define language_fi fi
%define langname_fi Finnish
%define language_fr fr
%define langname_fr French
%define language_fy_NL fy-NL
%define langname_fy_NL Frisian
%define language_ga_IE ga-IE
%define langname_ga_IE Irish
%define language_gd gd
%define langname_gd Scottish Gaelic
%define language_gl gl
%define langname_gl Galician
%define language_gu_IN gu-IN
%define langname_gu_IN Gujarati
%define language_he he
%define langname_he Hebrew
%define language_hi_IN hi-IN
%define langname_hi_IN Hindi
%define language_hr hr
%define langname_hr Croatian
%define language_hsb hsb
%define langname_hsb Upper Sorbian
%define language_hu hu
%define langname_hu Hungarian
%define language_hy_AM hy-AM
%define langname_hy_AM Armenian
%define language_ia ia
%define langname_ia Interlingua
%define language_id id
%define langname_id Indonesian
%define language_is is
%define langname_is Icelandic
%define language_it it
%define langname_it Italian
%define language_ja ja
%define langname_ja Japanese
%define language_ka ka
%define langname_ka Georgian
%define language_kab kab
%define langname_kab Taqbaylit
%define language_kk kk
%define langname_kk Kazakh
%define language_ko ko
%define langname_ko Korean
%define language_km km
%define langname_km Khmer
%define language_kn kn
%define langname_kn Kannada
%define language_ku ku
%define langname_ku Kurdish
%define language_lg lg
%define langname_lg Ganda
%define language_lij lij
%define langname_lij Ligurian
%define language_lt lt
%define langname_lt Lithuanian
%define language_lv lv
%define langname_lv Latvian
%define language_mai mai
%define langname_mai Maithili
%define language_mk mk
%define langname_mk Macedonian
%define language_ml ml
%define langname_ml Malayalam
%define language_mr mr
%define langname_mr Marathi
%define language_ms ms
%define langname_ms Malay
%define language_my my
%define langname_my Burmese
%define language_nb_NO nb-NO
%define langname_nb_NO Norwegian Bokmaal
%define language_nn_NO nn-NO
%define langname_nn_NO Norwegian Nynorsk
%define language_nl nl
%define langname_nl Dutch
%define language_nso nso
%define langname_nso Northern Sotho
%define language_oc oc
%define langname_oc Occitan
%define language_or or
%define langname_or Oriya
%define language_pa_IN pa-IN
%define langname_pa_IN Punjabi (gurmukhi)
%define language_pl pl
%define langname_pl Polish
%define language_pt_BR pt-BR
%define langname_pt_BR Brazilian portuguese
%define language_pt_PT pt-PT
%define langname_pt_PT Portuguese
%define language_rm rm
%define langname_rm Rumantsch
%define language_ro ro
%define langname_ro Romanian
%define language_ru ru
%define langname_ru Russian
%define language_si si
%define langname_si Sinhala
%define language_sk sk
%define langname_sk Slovak
%define language_sl sl
%define langname_sl Slovenian
%define language_son son
%define langname_son Soŋay
%define language_sq sq
%define langname_sq Shqipe
%define language_sr sr
%define langname_sr Serbian
%define language_sv_SE sv-SE
%define langname_sv_SE Swedish
%define language_ta ta
%define langname_ta Tamil
%define language_ta_LK ta-LK
%define langname_ta_LK Tamil (Sri Lanka)
%define language_te te
%define langname_te Telugu
%define language_th th
%define langname_th Thai
%define language_tr tr
%define langname_tr Turkish
%define language_uk uk
%define langname_uk Ukrainian
%define language_uk_UA uk-UA
%define langname_uk_UA Ukrainian
%define language_ur ur
%define langname_ur Urdu
%define language_uz uz
%define langname_uz Uzbek
%define language_vi vi
%define langname_vi Vietnamese
%define language_xh xh
%define langname_xh Xhosa
%define language_zh_CN zh-CN
%define langname_zh_CN Simplified Chinese
%define language_zh_TW zh-TW
%define langname_zh_TW Traditional Chinese
%define language_zu zu
%define langname_zu Zulu

# Defaults (all languages enabled by default)
# dicts
%{expand:%(for lang in %{langlist}; do echo "%%global with_dict_$lang 1"; done)}
%{expand:%(for lang in %{disabled_dict_langlist}; do echo "%%global with_dict_$lang 0"; done)}

# Locales
%{expand:%(for lang in %{langlist}; do echo "%%global locale_$lang `echo $lang | cut -d _ -f 1` "; done)}

# Expand all languages packages.
%{expand:%(\
	for lang in %langlist; do\
		echo "%%{expand:%%(sed "s!__LANG__!$lang!g" %SOURCE1 2> /dev/null)}";\
	done\
	)
}

%prep
%setup -c

%install
# Convert rpm macros to bash variables
%{expand:%(for lang in %{langlist}; do echo "language_$lang=%%{language_$lang}"; done)}

mkdir -p %buildroot%firefox_noarch_extensionsdir \
         %buildroot%firefox_prefix/dictionaries

# Install all languages
for lang in %langlist; do
	language="language_$lang"
	language=${!language}
	cp ${language}.xpi %buildroot%firefox_noarch_extensionsdir/langpack-${language}@firefox.mozilla.org.xpi
done

# Link to spell dictionaries
for locale in %dictionaries; do
	l="${locale/_*}"
	echo ">> $l $locale"
	if [ ! -L "%buildroot%firefox_prefix/dictionaries/$l.dic" ]; then
		ln -s %_datadir/myspell/${locale}.dic %buildroot%firefox_prefix/dictionaries/$l.dic
		ln -s %_datadir/myspell/${locale}.aff %buildroot%firefox_prefix/dictionaries/$l.aff
	else
		ln -s %_datadir/myspell/${locale}.dic %buildroot%firefox_prefix/dictionaries/$locale.dic
		ln -s %_datadir/myspell/${locale}.aff %buildroot%firefox_prefix/dictionaries/$locale.aff
	fi

done

%changelog
* Fri Jul 19 2019 Andrey Cherepanov <cas@altlinux.org> 68.0.1-alt1
- New version.
- Deleted: as, bn-BD, bn-IN, en-ZA, mai, ml, or.
- Added: bn, en-CA.

* Tue Feb 05 2019 Anton Midyukov <antohami@altlinux.org> 60.5.0-alt2
- Not exslusive arch

* Fri Feb 01 2019 Andrey Cherepanov <cas@altlinux.org> 60.5.0-alt1
- New version.

* Tue Dec 11 2018 Andrey Cherepanov <cas@altlinux.org> 60.4.0-alt1
- New version.

* Mon Sep 10 2018 Andrey Cherepanov <cas@altlinux.org> 60.2.0-alt1
- New version.

* Fri Jun 08 2018 Andrey Cherepanov <cas@altlinux.org> 60.0.2-alt1
- New version.

* Tue Jun 05 2018 Andrey Cherepanov <cas@altlinux.org> 60.0.1-alt1
- New version.
- Added languages: Belarusian, Interlingua, Burmese, Occitan and Urdu.

* Wed May 09 2018 Andrey Cherepanov <cas@altlinux.org> 52.8.0-alt1
- New version.

* Wed May 02 2018 Andrey Cherepanov <cas@altlinux.org> 52.7.4-alt1
- New version.

* Mon Mar 26 2018 Andrey Cherepanov <cas@altlinux.org> 52.7.3-alt1
- New version.

* Thu Mar 15 2018 Andrey Cherepanov <cas@altlinux.org> 52.7.1-alt1
- New version.

* Sat Mar 10 2018 Andrey Cherepanov <cas@altlinux.org> 52.7.0-alt1
- New version.

* Mon Jan 22 2018 Andrey Cherepanov <cas@altlinux.org> 52.6.0-alt1
- New version.

* Wed Jan 10 2018 Andrey Cherepanov <cas@altlinux.org> 52.5.3-alt1
- New version.

* Sun Dec 10 2017 Andrey Cherepanov <cas@altlinux.org> 52.5.2-alt1
- New version.

* Thu Nov 16 2017 Andrey Cherepanov <cas@altlinux.org> 52.5.0-alt1
- New version.

* Fri Sep 29 2017 Andrey Cherepanov <cas@altlinux.org> 52.4.0-alt1
- New version

* Wed Aug 09 2017 Andrey Cherepanov <cas@altlinux.org> 52.3.0-alt1
- New version

* Tue Jul 11 2017 Andrey Cherepanov <cas@altlinux.org> 52.2.1-alt1
- New version

* Wed Jun 21 2017 Andrey Cherepanov <cas@altlinux.org> 52.2.0-alt1
- New version

* Mon May 08 2017 Andrey Cherepanov <cas@altlinux.org> 52.1.1-alt1
- New version
- Add new language packs: Georgian, Kaqchikel and Taqbaylit
- Remove language pack for Belarusian

* Thu Apr 20 2017 Andrey Cherepanov <cas@altlinux.org> 45.9.0-alt1
- New version

* Mon Mar 06 2017 Andrey Cherepanov <cas@altlinux.org> 45.8.0-alt1
- New version

* Wed Jan 25 2017 Andrey Cherepanov <cas@altlinux.org> 45.7.0-alt1
- New version

* Fri Dec 16 2016 Andrey Cherepanov <cas@altlinux.org> 45.6.0-alt1
- New version

* Thu Nov 17 2016 Andrey Cherepanov <cas@altlinux.org> 45.5.0-alt1
- New version

* Tue Sep 20 2016 Andrey Cherepanov <cas@altlinux.org> 45.4.0-alt1
- New version

* Sat Aug 13 2016 Andrey Cherepanov <cas@altlinux.org> 45.3.0-alt2
- Require firefox-esr to prevent work with ordinary firefox

* Tue Aug 02 2016 Andrey Cherepanov <cas@altlinux.org> 45.3.0-alt1
- New version

* Sun Jun 12 2016 Andrey Cherepanov <cas@altlinux.org> 45.2.0-alt1
- New version

* Thu May 05 2016 Andrey Cherepanov <cas@altlinux.org> 45.1.1-alt1
- New version
- Use hunspell dictionaries for spell check

* Mon Apr 18 2016 Andrey Cherepanov <cas@altlinux.org> 45.0.2-alt1
- Initial build in Sisyphus

