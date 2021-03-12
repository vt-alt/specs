Name: asymptote
Version: 2.68
Release: alt1

Summary: Descriptive vector graphics language

Group: Sciences/Other
License: GPL
Url: http://asymptote.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/vectorgraphics/asymptote/archive/%version.tar.gz
Source: %name-%version.tar

Patch: asymptote-1.91-alt-DSO.patch
Patch1: asymptote-1.91-alt-glibc-2.16.patch
Patch2: asymptote-2.28-alt-gsl1.16.patch

BuildRequires: flex gcc-c++ libfftw3-devel libgsl-devel libreadline-devel libtirpc-devel zlib-devel
BuildRequires: libglm-devel
BuildRequires: libfreeglut-devel
BuildRequires: libcurl-devel

BuildRequires: libgc-devel >= 7.4.2

BuildRequires(pre): rpm-build-tex rpm-build-python3
BuildRequires: /proc
BuildRequires: texlive-collection-latexrecommended ghostscript-utils
BuildRequires: python3-module-PyQt5
BuildRequires: python3-module-mpl_toolkits python3-module-yieldfrom
# explicitly added texinfo for info files
BuildRequires: texinfo
BuildRequires: texi2dvi

%add_python3_path %_datadir/%name/GUI/
%add_python3_lib_path %_datadir/%name/GUI/
%add_python3_req_skip configs

%description
Asymptote is a powerful descriptive vector graphics language for technical
drawings, inspired by MetaPost but with an improved C++-like syntax.
Asymptote provides for figures the same high-quality level of typesetting
that LaTeX does for scientific text.

%package doc
Summary: Documentation and examples for %name
Group: Documentation
BuildArch: noarch

%description doc
Documentation and examples for %name.

%prep
%setup
%__subst "s|/lib |/%_lib |" configure.ac
%__subst "s|-lgc |-lgc -lgccpp |" configure.ac
#patch0 -p2
#patch1 -p2
#patch2 -p2
# some incompatibilities?
sed -i "s|@printindex cp||g" doc/%name.texi

# sure we do not using internal libgc
rm -fv *.tar.gz

%build
%autoreconf
%configure --with-docdir=%_docdir/%name-doc-%version \
	--with-latex=%_texmfmain/tex/latex \
	--with-context=%_texmfmain/tex/context/third \
	--enable-gc=system \
	--enable-gsl
%make_build

%install
%makeinstall_std
# TODO: conflicts with  texlive-collection-basic-2018-alt1_5.noarch
mv %buildroot%_man1dir/asy.1 %buildroot%_man1dir/asy-asymptote.1

%files
%doc BUGS LICENSE README TODO
%_bindir/asy
%_bindir/xasy
%_datadir/%name/
%_texmfmain/tex/latex/%name/
%_texmfmain/tex/context/third/%name/
%_man1dir/*.1*

%files doc
%_docdir/%name-doc-%version/
%_infodir/*.info*
%_infodir/%name/*.info*

%changelog
* Sat Feb 06 2021 Anton Midyukov <antohami@altlinux.org> 2.68-alt1
- new version 2.68 (with rpmrb script)
- update buildrequires

* Tue May 14 2019 Vitaly Lipatov <lav@altlinux.ru> 2.49-alt1
- new version 2.49 (with rpmrb script)

* Fri Dec 14 2018 Vitaly Lipatov <lav@altlinux.ru> 2.47-alt1
- new version 2.47 (with rpmrb script)

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 2.46-alt1
- new version 2.46 (with rpmrb script)
- build with gsl support

* Wed Oct 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.44-alt2
- NMU: rebuilt with libGLUT.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 2.44-alt1.qa1
- NMU: applied repocop patch

* Mon May 21 2018 Vitaly Lipatov <lav@altlinux.ru> 2.44-alt1
- new version 2.44 (with rpmrb script)

* Mon Mar 05 2018 Igor Vlasenko <viy@altlinux.ru> 2.41-alt1.1
- build with texlive 2017

* Sat Apr 08 2017 Vitaly Lipatov <lav@altlinux.ru> 2.41-alt1
- new version 2.41 (with rpmrb script)

* Wed Mar 15 2017 Vitaly Lipatov <lav@altlinux.ru> 2.40-alt1
- new version (2.40) with rpmgs script

* Sat Jan 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.39-alt1
- new version 2.39 (with rpmrb script)

* Tue Jul 26 2016 Vitaly Lipatov <lav@altlinux.ru> 2.38-alt1
- new version 2.38 (with rpmrb script)

* Thu Feb 25 2016 Vitaly Lipatov <lav@altlinux.ru> 2.36-alt2
- build with system libgc

* Wed Feb 24 2016 Vitaly Lipatov <lav@altlinux.ru> 2.36-alt1
- new version 2.36 (with rpmrb script)
- build without libgsl support

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 2.35-alt1.1
- NMU: added BR: texinfo

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 2.35-alt1
- new version 2.35 (with rpmrb script)

* Tue Sep 02 2014 Vitaly Lipatov <lav@altlinux.ru> 2.32-alt1
- new version 2.32 (with rpmrb script)

* Sat Jul 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.28-alt1.1
- Rebuilt with new gsl

* Tue Jun 03 2014 Vitaly Lipatov <lav@altlinux.ru> 2.28-alt1
- new version 2.28 (with rpmrb script)

* Tue Aug 27 2013 Vitaly Lipatov <lav@altlinux.ru> 2.24-alt1
- new version 2.24 (with rpmrb script)

* Sat Aug 03 2013 Vitaly Lipatov <lav@altlinux.ru> 2.23-alt1
- new version 2.23 (with rpmrb script)

* Wed Nov 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.91-alt1.3
- Fixed build with glibc 2.16

* Thu Jun 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.91-alt1.2
- Fixed build

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.91-alt1.1
- Rebuild with Python-2.7

* Fri Feb 19 2010 Vitaly Lipatov <lav@altlinux.ru> 1.91-alt1
- new version 1.91 (with rpmrb script)

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.43-alt1.1
- Rebuilt with python 2.6

* Mon Jul 21 2008 Vitaly Lipatov <lav@altlinux.ru> 1.43-alt1
- new version 1.43 (with rpmrb script)

* Thu Jan 17 2008 Vitaly Lipatov <lav@altlinux.ru> 1.40-alt1
- initial build for ALT Linux Sisyphus
