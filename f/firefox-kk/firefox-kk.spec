%define cid            langpack-kk@firefox.mozilla.org
%define cid_dir        %firefox_noarch_extensionsdir/%cid

%define cid_dict       kk@dictionaries.addons.mozilla.org
%define cid_dict_dir   %firefox_noarch_extensionsdir/%cid_dict

Name:		firefox-kk
Version:	68.0
Release:	alt1
Summary:	Kazakh (KZ) Language Pack for Firefox

License:	MPL/GPL/LGPL
Group:		Networking/WWW
URL:		http://www.mozilla-russia.org/products/firefox/
Packager:	Alexey Gladkov <legion@altlinux.ru>
BuildArch:	noarch

Source0:	kk-%version.xpi

Requires:	firefox >= %version
Requires:	hunspell-kk

BuildRequires(pre):	rpm-build-firefox
BuildRequires:		unzip

%description
The Mozilla Firefox Kazakh translation.

%prep
%setup -c -n %name-%version/%cid

%install
cd ..

mkdir -p -- \
	%buildroot/%cid_dir \
	%buildroot/%cid_dict_dir/dictionaries

# Install translation
cp -r -- %cid/* %buildroot/%cid_dir

# Install dictionary
cat > %buildroot/%cid_dict_dir/install.rdf <<-EOF
	<?xml version="1.0"?>
	<RDF xmlns="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	     xmlns:em="http://www.mozilla.org/2004/em-rdf#">
	  <Description about="urn:mozilla:install-manifest"
	               em:id="%cid_dict"
	               em:name="Kazakh (KZ) Dictionary"
	               em:version="%version"
	               em:type="64"
	               em:unpack="true"
	               em:creator="Mozilla Russia">
	    <em:targetApplication>
	      <Description>
	        <em:id>{ec8030f7-c20a-464f-9b0e-13a3a9e97384}</em:id>
	        <em:minVersion>%version</em:minVersion>
	        <em:maxVersion>%version.*</em:maxVersion>
	      </Description>
	    </em:targetApplication>
	  </Description>
	</RDF>
EOF
ln -s %_datadir/myspell/kk_KZ.aff %buildroot/%cid_dict_dir/dictionaries/kk.aff
ln -s %_datadir/myspell/kk_KZ.dic %buildroot/%cid_dict_dir/dictionaries/kk.dic


%files
%cid_dir
%cid_dict_dir

%changelog
* Mon Jul 15 2019 Alexey Gladkov <legion@altlinux.ru> 68.0-alt1
- New version (68.0).

* Fri May 31 2019 Alexey Gladkov <legion@altlinux.ru> 67.0-alt1
- New version (67.0).

* Sun Mar 31 2019 Alexey Gladkov <legion@altlinux.ru> 66.0.1-alt1
- New version (66.0.1).

* Fri Feb 01 2019 Alexey Gladkov <legion@altlinux.ru> 65.0-alt1
- New version (65.0).

* Fri Dec 21 2018 Alexey Gladkov <legion@altlinux.ru> 64.0-alt1
- New version (64.0).

* Tue Nov 13 2018 Alexey Gladkov <legion@altlinux.ru> 63.0.1-alt1
- New version (63.0.1).

* Fri Oct 05 2018 Alexey Gladkov <legion@altlinux.ru> 62.0.3-alt1
- New version (62.0.3).

* Wed Jul 04 2018 Alexey Gladkov <legion@altlinux.ru> 61.0-alt1
- New version (61.0).

* Wed May 23 2018 Alexey Gladkov <legion@altlinux.ru> 60.0.1-alt1
- New version (60.0.1).

* Tue Mar 27 2018 Alexey Gladkov <legion@altlinux.ru> 59.0.2-alt1
- New version (59.0.2).

* Mon Feb 12 2018 Alexey Gladkov <legion@altlinux.ru> 58.0.2-alt1
- New version (58.0.2).

* Mon Dec 04 2017 Alexey Gladkov <legion@altlinux.ru> 57.0.1-alt1
- New version (57.0.1).

* Fri Oct 13 2017 Alexey Gladkov <legion@altlinux.ru> 56.0-alt1
- New version (56.0).

* Mon Aug 14 2017 Alexey Gladkov <legion@altlinux.ru> 55.0.1-alt1
- New version (55.0.1).

* Thu Jul 13 2017 Alexey Gladkov <legion@altlinux.ru> 54.0.1-alt1
- New version (54.0.1).

* Mon May 08 2017 Alexey Gladkov <legion@altlinux.ru> 53.0.2-alt1
- New version (53.0.2).

* Mon Mar 20 2017 Alexey Gladkov <legion@altlinux.ru> 52.0-alt1
- New version (52.0).

* Tue Jan 31 2017 Alexey Gladkov <legion@altlinux.ru> 51.0.1-alt1
- New version (51.0.1).

* Thu Nov 17 2016 Alexey Gladkov <legion@altlinux.ru> 50.0-alt1
- New version (50.0).

* Thu Sep 29 2016 Alexey Gladkov <legion@altlinux.ru> 49.0.1-alt1
- New version (49.0.1).

* Wed Aug 10 2016 Alexey Gladkov <legion@altlinux.ru> 48.0-alt1
- New version (48.0).

* Tue Jun 21 2016 Alexey Gladkov <legion@altlinux.ru> 47.0-alt1
- New version (47.0).

* Sun May 01 2016 Alexey Gladkov <legion@altlinux.ru> 46.0-alt1
- New version (46.0).

* Tue Mar 22 2016 Alexey Gladkov <legion@altlinux.ru> 45.0.1-alt1
- New version (45.0.1).

* Thu Jan 28 2016 Alexey Gladkov <legion@altlinux.ru> 44.0-alt1
- New version (44.0).

* Thu Dec 24 2015 Alexey Gladkov <legion@altlinux.ru> 43.0.1-alt1
- New version (43.0.1).

* Tue Nov 10 2015 Alexey Gladkov <legion@altlinux.ru> 42.0-alt1
- New version (42.0).

* Tue Sep 29 2015 Alexey Gladkov <legion@altlinux.ru> 41.0-alt1
- New version (41.0).

* Mon Aug 17 2015 Alexey Gladkov <legion@altlinux.ru> 40.0.2-alt1
- New version (40.0.2).

* Mon Aug 10 2015 Alexey Gladkov <legion@altlinux.ru> 39.0.3-alt1
- New version (39.0.3).

* Mon May 25 2015 Alexey Gladkov <legion@altlinux.ru> 38.0.1-alt1
- New version (38.0.1).

* Thu Apr 09 2015 Alexey Gladkov <legion@altlinux.ru> 37.0.1-alt1
- New version (37.0.1).

* Mon Mar 09 2015 Alexey Gladkov <legion@altlinux.ru> 36.0.1-alt1
- New version (36.0.1).

* Tue Jan 27 2015 Alexey Gladkov <legion@altlinux.ru> 35.0-alt1
- New version (35.0).

* Tue Dec 09 2014 Alexey Gladkov <legion@altlinux.ru> 34.0-alt1
- New version (34.0).

* Fri Oct 24 2014 Alexey Gladkov <legion@altlinux.ru> 33.0-alt1
- New version (33.0).

* Wed Oct 01 2014 Alexey Gladkov <legion@altlinux.ru> 32.0-alt1
- New version (32.0).

* Wed Jul 30 2014 Alexey Gladkov <legion@altlinux.ru> 31.0-alt1
- New version (31.0).

* Sun May 11 2014 Alexey Gladkov <legion@altlinux.ru> 29.0.1-alt1
- New version (29.0.1).

* Thu Mar 27 2014 Alexey Gladkov <legion@altlinux.ru> 28.0-alt1
- New version (28.0).

* Fri Feb 14 2014 Alexey Gladkov <legion@altlinux.ru> 27.0-alt1
- New version (27.0).

* Sat Dec 28 2013 Alexey Gladkov <legion@altlinux.ru> 26.0-alt1
- New version (26.0).

* Wed Nov 06 2013 Alexey Gladkov <legion@altlinux.ru> 25.0-alt1
- New version (25.0).

* Fri Oct 25 2013 Alexey Gladkov <legion@altlinux.ru> 24.0-alt1
- New version (24.0).

* Wed Aug 14 2013 Alexey Gladkov <legion@altlinux.ru> 23.0-alt1
- New version (23.0).

* Mon Jul 01 2013 Alexey Gladkov <legion@altlinux.ru> 22.0-alt1
- New version (22.0).

* Tue Jun 18 2013 Alexey Gladkov <legion@altlinux.ru> 21.0-alt2
- Add dictionary extension (ALT#29063).

* Wed Jun 05 2013 Alexey Gladkov <legion@altlinux.ru> 21.0-alt1
- New version (21.0)

* Mon Apr 15 2013 Alexey Gladkov <legion@altlinux.ru> 20.0-alt1
- New version (20.0)

* Mon Mar 11 2013 Alexey Gladkov <legion@altlinux.ru> 19.0.2-alt1
- New version (19.0.2)
- First build for ALT Linux.
