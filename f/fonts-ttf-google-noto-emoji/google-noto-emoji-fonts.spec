Group: System/Fonts/True type
%define oldname google-noto-emoji-fonts
%define fedora 32
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commit0 aac7ccaa4d1dea4543453b96f7d6fc47066a57ff
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global fontname google-noto-emoji

%if (0%{?fedora} > 25)
%global buildfont 0
%else
%global buildfont 0
%endif


Name:           fonts-ttf-google-noto-emoji
Version:        20200916
Release:        alt1_1
Summary:        Google a.'Noto Emojia.' Black-and-White emoji font

# In noto-emoji-fonts source
## noto-emoji code is in ASL 2.0 license
## Emoji fonts are under OFL license
### third_party color-emoji code is in BSD license
### third_party region-flags code is in Public Domain license
# In nototools source
## nototools code is in ASL 2.0 license
### third_party ucd code is in Unicode license
License:        OFL and ASL 2.0
URL:            https://github.com/googlei18n/noto-emoji
Source0:        https://github.com/googlei18n/noto-emoji/archive/%{commit0}.tar.gz#/noto-emoji-%{shortcommit0}.tar.gz
Source2:        %{fontname}.metainfo.xml
Source3:        %{fontname}-color.metainfo.xml

Patch0:         noto-emoji-build-all-flags.patch
Patch1:         noto-emoji-use-gm.patch
Patch2:         noto-emoji-use-system-pngquant.patch

BuildArch:      noarch
BuildRequires:  gcc
BuildRequires:  fontpackages-devel
%if %buildfont
BuildRequires:  fonttools
BuildRequires:  python3-module-fonttools
BuildRequires:  nototools
BuildRequires:  python3-module-nototools
BuildRequires:  python3-devel
BuildRequires:  libGraphicsMagick
BuildRequires:  pngquant
BuildRequires:  libzopfli zopfli
BuildRequires:  libcairo-devel
%endif


Obsoletes:      google-noto-color-emoji-fonts < 20150617
Provides:       google-noto-color-emoji-fonts = 20150617
Source44: import.info

%description
This package provides the Google a.'Noto Emojia.' Black-and-White emoji font.

%package -n fonts-ttf-google-noto-emoji-color
Group: System/Fonts/True type
Summary:        Google a.'Noto Color Emojia.' colored emoji font
Obsoletes:      google-noto-color-emoji-fonts < 20150617
Provides:       google-noto-color-emoji-fonts = 20150617

%description -n fonts-ttf-google-noto-emoji-color
This package provides the Google a.'Noto Color Emojia.' colored emoji font.

%prep
%setup -n noto-emoji-%{commit0}
%patch0 -p1 -b .noto-emoji-build-all-flags
%patch1 -p1 -b .noto-emoji-use-gm.patch
%patch2 -p1 -b .noto-emoji-use-system-pngquant

rm -rf third_party/pngquant

%build
%if %buildfont
# Work around UTF-8
export LANG=C.UTF-8

%make_build OPT_CFLAGS="$RPM_OPT_FLAGS" BYPASS_SEQUENCE_CHECK='True'
%endif

%install
install -m 0755 -d %{buildroot}%{_fontdir}

%if %buildfont
# Built by us from the supplied pngs:
install -m 0644 -p NotoColorEmoji.ttf %{buildroot}%{_fontdir}
%else
# Pre-built, and included with the source:
install -m 0644 -p fonts/NotoColorEmoji.ttf %{buildroot}%{_fontdir}
%endif

# Pre-built, and included with the source:
install -m 0644 -p fonts/NotoEmoji-Regular.ttf %{buildroot}%{_fontdir}

mkdir -p %{buildroot}%{_datadir}/appdata
install -m 0644 -p %{SOURCE2} %{buildroot}%{_datadir}/appdata
install -m 0644 -p %{SOURCE3} %{buildroot}%{_datadir}/appdata
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc pcf pcf.gz bdf afm pfa pfb; do
    case "$fontpatt" in 
	pcf*|bdf*) type=bitmap;;
	tt*|TT*) type=ttf;;
	otf|OTF) type=otf;;
	afm*|pf*) type=type1;;
    esac
    find $RPM_BUILD_ROOT/usr/share/fonts -type f -name '*.'$fontpatt | while read i; do
	j=`echo "$i" | sed -e s,/usr/share/fonts/,/usr/share/fonts/$type/,`;
	install -Dm644 "$i" "$j";
	rm -f "$i";
	olddir=`dirname "$i"`;
	mv -f "$olddir"/{encodings.dir,fonts.{dir,scale,alias}} `dirname "$j"`/ 2>/dev/null ||:
	rmdir -p "$olddir" 2>/dev/null ||:
    done
done
# kill invalid catalogue links
if [ -d $RPM_BUILD_ROOT/etc/X11/fontpath.d ]; then
    find -L $RPM_BUILD_ROOT/etc/X11/fontpath.d -type l -print -delete ||:
    # relink catalogue
    find $RPM_BUILD_ROOT/usr/share/fonts -name fonts.dir | while read i; do
	pri=10;
	j=`echo $i | sed -e s,$RPM_BUILD_ROOT/usr/share/fonts/,,`; type=${j%%%%/*}; 
	pre_stem=${j##$type/}; stem=`dirname $pre_stem|sed -e s,/,-,g`;
	case "$type" in 
	    bitmap) pri=10;;
	    ttf|ttf) pri=50;;
	    type1) pri=40;;
	esac
	ln -s /usr/share/fonts/$j $RPM_BUILD_ROOT/etc/X11/fontpath.d/"$stem:pri=$pri"
    done ||:
fi

%files
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/NotoEmoji-Regular.ttf
%doc --no-dereference LICENSE
%doc AUTHORS CONTRIBUTING.md CONTRIBUTORS README.md
%{_datadir}/appdata/google-noto-emoji.metainfo.xml

%files -n fonts-ttf-google-noto-emoji-color
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/NotoColorEmoji.ttf
%doc --no-dereference LICENSE
%doc AUTHORS CONTRIBUTING.md CONTRIBUTORS README.md
%{_datadir}/appdata/google-noto-emoji-color.metainfo.xml


%changelog
* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 20200916-alt1_1
- update to new release by fcimport

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 20200723-alt1_2
- update to new release by fcimport

* Wed Feb 26 2020 Igor Vlasenko <viy@altlinux.ru> 20191019-alt1_2
- update to new release by fcimport

* Wed Sep 18 2019 Igor Vlasenko <viy@altlinux.ru> 20190829-alt1_1
- update to new release by fcimport

* Wed Aug 07 2019 Igor Vlasenko <viy@altlinux.ru> 20190709-alt1_2
- update to new release by fcimport

* Thu Jun 20 2019 Igor Vlasenko <viy@altlinux.ru> 20180814-alt1_2
- new version

