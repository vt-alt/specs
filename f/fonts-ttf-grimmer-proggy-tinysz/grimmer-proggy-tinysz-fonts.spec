Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname grimmer-proggy-tinysz-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname grimmer-proggy-tinysz
%global fontconf 66-%{fontname}.conf

Name: fonts-ttf-grimmer-proggy-tinysz
Version: 1.0
Release: alt3_17
License: MIT
URL: http://upperbounds.net/
Source0: http://upperbounds.net/download/ProggyTinySZ.ttf.zip
Source1: 66-grimmer-proggy-tinysz.conf
Source2: %{fontname}.metainfo.xml

BuildArch: noarch
Summary: Proggy Tiny with slashed zero programming font
BuildRequires: fontpackages-devel
BuildRequires: libappstream-glib
Source44: import.info

%description
The proggy fonts are a set of fixed-width screen fonts that are designed for
code listings. Proggy Tiny Slashed Zero is identical to Proggy Tiny but has a
slashed zero instead of a dot.

%prep
%setup -q -c -n %{oldname}-%{version}

%build
sed -i 's/\r//' Licence.txt

%install
mkdir -p %{buildroot}/%{_fontdir}

install -m 0644 ProggyTinySZ.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

appstream-util validate-relax --nonet \
               %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
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
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%{_fontbasedir}/*/%{_fontstem}/*.ttf
%doc Licence.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_17
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_11
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_7
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_6
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_5
- rebuild with new rpm-build-fonts

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5
- initial release by fcimport

