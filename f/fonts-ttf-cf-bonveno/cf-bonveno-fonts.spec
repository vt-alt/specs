# BEGIN SourceDeps(oneline):
BuildRequires: python unzip
# END SourceDeps(oneline)
%define oldname cf-bonveno-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global	fontname	cf-bonveno
%global fontconf	60-%{fontname}.conf


Name:		fonts-ttf-cf-bonveno
Version:	1.1
Release:	alt3_21
Summary:	A fun font by Barry Schwartz

Group:		System/Fonts/True type
License:	GPLv2+
URL:		http://home.comcast.net/~crudfactory/cf3/bonveno.xhtml
Source0:	http://home.comcast.net/~crudfactory/cf3/fonts/BonvenoCF-1.1.zip
Source1:	%{oldname}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml

BuildArch: 	noarch
BuildRequires:	fontforge libfontforge, fontpackages-devel
Source44: import.info


%description
A set of fun fonts from the crud factory.

%prep
%setup -n %{oldname}-%{version} -q -c


for txt in COPYING README ; do
	sed 's/\r//' $txt > $txt.new
	touch -r $txt $txt.new
	mv $txt.new $txt
done

%build
fontforge -lang=ff -script "-" BonvenoCF*.sfd <<EOF
i = 1 
while ( i < \$argc )
	Open (\$argv[i], 1)
	Generate (\$fontname + ".ttf")
	PrintSetup (5) 
	PrintFont (0, 0, "", \$fontname + "-sample.pdf")
	Close()
	i++ 
endloop
EOF

%install
rm -fr %{buildroot}

install -dm 755 %{buildroot}%{_fontdir}
install -pm 644 *.ttf  %{buildroot}%{_fontdir}

install -m 755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
	%{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
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
%{_datadir}/appdata/%{fontname}.metainfo.xml


%doc  COPYING* README*

%dir %{_fontbasedir}/*/%{_fontstem}/

%changelog
* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_21
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_19
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_17
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_16
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_15
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_14
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_13
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_12
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_11
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_11
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_10
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_10
- initial release by fcimport

