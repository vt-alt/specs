%set_verify_info_method relaxed

%define DEFAULT_LISP    sbcl

%define BUILD_GCL	0
%define BUILD_CLISP 	1
%define BUILD_SBCL	1
%define BUILD_CMUCL	0

%define BUILD_LANG_ES		1
%define BUILD_LANG_ES_UTF	1
%define BUILD_LANG_PT		1
%define BUILD_LANG_PT_UTF	1
%define BUILD_LANG_PT_BR	1
%define BUILD_LANG_PT_BR_UTF	1

%define BUILD_GCL_ANSI  1

%define BUILD_EMACS     1
%define BUILD_XMAXIMA   1

%define BUILD_BOOK      0

%define CVS_BUILD	0

Name: maxima
Version: 5.43.2
%define maxima_version 5.43.2
Release: alt1
Summary: Maxima Computer Algebra System
License: GPL-2.0
Group: Sciences/Mathematics
Url: http://maxima.sourceforge.net
Packager: Ilya Mashkin <oddity@altlinux.ru>

ExclusiveArch: armh aarch64 %ix86 x86_64 ppc sparcv9                                                           

Source0: maxima-%version.tar.gz
Source6: maxima-modes.el
%if %BUILD_BOOK
Source7: breqn-0.94.tar.bz2
%endif

Patch1: maxima-alt-desktop-i18n.patch

## upstreamable patches
# https://bugzilla.redhat.com/show_bug.cgi?id=837142
# https://sourceforge.net/tracker/?func=detail&aid=3539587&group_id=4933&atid=104933
Patch50: maxima-5.37.1-clisp-noreadline.patch

# Build the fasl while building the executable to avoid double initialization
Patch51: maxima-5.30.0-build-fasl.patch

## Other maxima reference docs
Source10: http://starship.python.net/crew/mike/TixMaxima/macref.pdf
Source11: http://maxima.sourceforge.net/docs/maximabook/maximabook-19-Sept-2004.pdf

%description
Maxima is a full symbolic computation program.  It is full featured
doing symbolic manipulation of polynomials, matrices, rational
functions, integration, Todd-coxeter, graphing, bigfloats.  It has a
symbolic debugger source level debugger for maxima code.  Maxima is
based on the original Macsyma developed at MIT in the 1970's.  It is
quite reliable, and has good garbage collection, and no memory leaks.
It comes with hundreds of self tests.

%package common
Summary: Maxima Symbolic Computation Program. Common files
Group: Sciences/Mathematics
Provides: maxima = %version-%release

Requires: gnuplot >= 4.0.0 rlwrap maxima-bin = %version-%release
BuildRequires: sed perl texlive-collection-latexrecommended texinfo automake_1.7
AutoReq: yes, noshell
%description common
This package contains common files needed to run Maxima with
any lisp interpreter, documentation etc.


%if %BUILD_CLISP
%package bin-clisp
Summary: Maxima Symbolic Computation Program. Clisp binaries
Group: Sciences/Mathematics
Provides: maxima-bin = %version-%release
Requires: maxima-common = %version-%release 
BuildRequires: clisp
%description bin-clisp
Maxima binaries compiled with clisp.
%endif

%if %BUILD_GCL
%package bin-gcl
Summary: Maxima Symbolic Computation Program. GCL binaries
Group: Sciences/Mathematics
Provides: maxima-bin = %version-%release
Requires: maxima-common = %version-%release libreadline libncurses terminfo libgpm
BuildRequires: gcl >= 2.6.5
%description bin-gcl
Maxima binaries compiled with GCL (GNU Common Lisp).
%endif

%if %BUILD_CMUCL
%package bin-cmucl
Summary: Maxima Symbolic Computation Program. CMUCL binaries
Group: Sciences/Mathematics
Provides: maxima-bin = %version-%release
Requires: maxima-common = %version-%release
BuildRequires: cmucl
%description bin-cmucl
Maxima binaries compiled with CMUCL (CMU Common Lisp).
%endif

%if %BUILD_SBCL
%package bin-sbcl
Summary: Maxima Symbolic Computation Program. SBCL binaries
Group: Sciences/Mathematics
Provides: maxima-bin = %version-%release
Requires: maxima-common = %version-%release sbcl >= 1.4.12
BuildRequires: sbcl >= 1.4.12
BuildRequires: /proc
%description bin-sbcl
Maxima binaries compiled with SBCL (Steel Bank Common Lisp).
%endif

%if %BUILD_EMACS
%package -n emacs-maxima
Summary: Emacs Maxima modes
Group: Editors
Requires:  emacs emacs-mode-auctex 
BuildRequires: emacs-common
#Requires: maxima-common = %version-%release
Obsoletes: maxima-emacs
BuildArch: noarch

%description -n emacs-maxima
Set of Maxima emacs modes.
%endif

%if %BUILD_XMAXIMA
%package -n xmaxima
Summary: Maxima graphical frontend
Group: Sciences/Mathematics
Requires: maxima-common = %version-%release tk tcl
Provides: %name-xmaxima = %EVR
Obsoletes: %name-xmaxima < %EVR
%description -n xmaxima
Maxima graphical frontend written in Tcl/Tk.
%endif

%if %BUILD_LANG_ES
%package lang-es
Summary: Maxima Spanish language pack
Group: Sciences/Mathematics
#Requires: maxima-common = %version-%release
BuildArch: noarch

%description lang-es
Maxima Spanish language pack.
%endif

%if %BUILD_LANG_ES_UTF
%package lang-es-utf8
Summary: Maxima Spanish language pack (UTF-8)
Group: Sciences/Mathematics
#Requires: maxima-common = %version-%release
BuildArch: noarch

%description lang-es-utf8
Maxima Spanish language pack (UTF-8).
%endif

%if %BUILD_LANG_PT
%package lang-pt
Summary: Maxima Portuguese language pack
Group: Sciences/Mathematics
#Requires: maxima-common = %version-%release
BuildArch: noarch

%description lang-pt
Maxima Portuguese language pack.
%endif

%if %BUILD_LANG_PT_UTF
%package lang-pt-utf8
Summary: Maxima Portuguese language pack (UTF-8)
Group: Sciences/Mathematics
#Requires: maxima-common = %version-%release
BuildArch: noarch

%description lang-pt-utf8
Maxima Portuguese language pack (UTF-8).
%endif

%if %BUILD_LANG_PT_BR
%package lang-pt_BR
Summary: Maxima Brazilian Portuguese language pack
Group: Sciences/Mathematics
#Requires: maxima-common = %version-%release
BuildArch: noarch

%description lang-pt_BR
Maxima Brazilian Portuguese language pack.
%endif

%if %BUILD_LANG_PT_BR_UTF
%package lang-pt_BR-utf8
Summary: Maxima Brazilian Portuguese language pack (UTF-8)
Group: Sciences/Mathematics
#Requires: maxima-common = %version-%release
BuildArch: noarch

%description lang-pt_BR-utf8
Maxima Brazilian Portuguese language pack (UTF-8).
%endif

%if %BUILD_BOOK
%package book
Summary: Maxima book
Group: Sciences/Mathematics
BuildRequires: ghostscript
BuildArch: noarch
%description book
Maxima book
%endif

%if %CVS_BUILD
%define maxima_dir    %_builddir/maxima
%else
%define maxima_dir    %_builddir/maxima-%maxima_version
%endif

%prep
%if %CVS_BUILD
%setup -q -b0 -nmaxima
%else
%setup -q -b0 -nmaxima-%maxima_version
%endif

%if %BUILD_BOOK
tar jxf %SOURCE7 -C doc/maximabook
%endif

%patch1 -p2
%patch50 -p1 -b .clisp-noreadline
%patch51 -p1 -b .build-fasl

# Set new path to maxima-index.lisp
subst 's|maxima::\*maxima-infodir\* |"%_datadir/maxima/%maxima_version/doc" |' src/cl-info.lisp

# Extra docs
install -p -m644 %{SOURCE10} .
install -D -p -m644 %{SOURCE11} doc/maximabook/maxima.pdf

sed -i -e 's|@ARCH@|%{_target_cpu}|' src/maxima.in

sed -i -e 's:/usr/local/info:/usr/share/info:' \
  interfaces/emacs/emaxima/maxima.el
sed -i -e \
  's/(defcustom\s+maxima-info-index-file\s+)(\S+)/$1\"maxima.info-16\"/' \
  interfaces/emacs/emaxima/maxima.el

# remove CVS crud
find -name CVS -type d | xargs --no-run-if-empty rm -rv
cp -pv /usr/share/gnu-config/* .


%build
export SBCL_HOME=%_libdir/sbcl/
%if %CVS_BUILD
#%set_automake_version 1.7
./bootstrap
%endif

touch ./src/*.mk ./src/Makefile.in

%if %BUILD_GCL_ANSI
export GCL_ANSI="yes"
%else
export GCL_ANSI=""
%endif

./configure  --with-default-lisp=%DEFAULT_LISP \
%if %BUILD_CLISP
  --enable-clisp  \
%endif
%if %BUILD_GCL
  --enable-gcl    \
%endif
%if %BUILD_CMUCL
  --enable-cmucl  \
%endif
%if %BUILD_SBCL
  --enable-sbcl-exec   \
%endif
%if %BUILD_LANG_ES
  --enable-lang-es	\
%endif
%if %BUILD_LANG_ES_UTF
  --enable-lang-es-utf8	\
%endif
%if %BUILD_LANG_PT
  --enable-lang-pt	\
%endif
%if %BUILD_LANG_PT_UTF
  --enable-lang-pt-utf8	\
%endif
%if %BUILD_LANG_PT_BR
  --enable-lang-pt_BR		\
%endif
%if %BUILD_LANG_PT_BR_UTF
  --enable-lang-pt_BR-utf8	\
%endif
  --prefix=%prefix           \
  --infodir=%_infodir        \
  --mandir=%_mandir          \
  --libdir=%_libdir          \
  --datadir=%_datadir        \
  --libexecdir=%_libexecdir

make

pushd doc
  %if %BUILD_BOOK
  pushd maximabook
    make pdf-final
  popd
  %endif
  # comment 25112010 3str:
  #pushd intromax
  #    pdflatex intromax.ltx
  # popd
popd  

%install
#export RPM_FINDREQ_METHOD=none
#%define _findreq_default_method none
# info files must be uncompressed
%define _compress_method no

%define maxima_libdir 	  %buildroot%_libdir/maxima
%define maxima_bindir     %buildroot%_bindir
%if %BUILD_EMACS
%define emacs_maxima_dir  %_datadir/emacs/site-lisp/maxima
%endif

# extra dirs and files not handled by standard make install

#  emacs modes
%if %BUILD_EMACS
install -d %buildroot%emacs_maxima_dir
install -d %buildroot%_sysconfdir/emacs/site-start.d
install -d %buildroot%_datadir/texmf/tex/latex/emaxima
%endif

#  documentation
install -d %buildroot%_docdir/maxima-%version
install -d %buildroot%_docdir/maxima-%version/implementation
%if %BUILD_BOOK
install -d %buildroot%_docdir/maxima-%version/maximabook
%endif
%if %BUILD_EMACS
install -d %buildroot%_docdir/maxima-%version/emaxima
%endif

# emacs modes
%if %BUILD_EMACS
install -D -m644 %SOURCE6 %buildroot%_sysconfdir/emacs/site-start.d/maxima.el
echo "(setq load-path (cons \"%emacs_maxima_dir\" load-path))" >> \
  %buildroot%_sysconfdir/emacs/site-start.d/maxima.el
%endif

# documentation
%define maxima_docdir %buildroot%_docdir/maxima-%version
%if %BUILD_BOOK
install -D -m644 %maxima_dir/doc/maximabook/maxima.pdf %maxima_docdir/maxima.pdf
%endif
install -D -m644 %maxima_dir/doc/intromax/intromax.html %maxima_docdir/intromax.html
install -D -m644 %maxima_dir/doc/implementation/*.txt %maxima_docdir/implementation
%if %BUILD_EMACS
install -D -m644 %maxima_dir/doc/emaxima/EMaximaIntro.ps %maxima_docdir/emaxima/EMaximaIntro.ps
%endif

cd %maxima_dir
%makeinstall

%if %BUILD_EMACS
# Move emacs .el and .lisp scripts to subdirectory
mv %buildroot%_datadir/emacs/site-lisp/*.{el,lisp} %buildroot%emacs_maxima_dir
mkdir -p %buildroot%_datadir/texmf/tex/latex/emaxima
mv %buildroot%_datadir/emacs/site-lisp/*.sty %buildroot%_datadir/texmf/tex/latex/emaxima
%endif

# Move all maxima-index.lisp from /usr/share/info to maxima directory
%define doc_dir %_datadir/maxima/%maxima_version/doc
pushd %buildroot%_infodir
find . -name maxima-index.lisp | while read f;do
	d="$(dirname $f)"
	d="${d//\.\/}"
	mkdir -p %buildroot%doc_dir/$d 2>/dev/null ||:
	mv "$f" %buildroot%doc_dir/$d
	if [ "$d" == "." ]; then
		for i in `ls maxima.info*`; do
			ln -s ../../../info/$i %buildroot%doc_dir/$i
		done
	else
		for i in `ls $d/maxima.info*`; do
			ln -s ../../../../info/$i %buildroot%doc_dir/$i
		done
	fi
done
popd

# Remove disallowed ELF files in /usr/share
rm -f %buildroot%_datadir/maxima/%maxima_version/share/test_encodings/escape-double-quote

%files common
%doc doc/maximabook/maxima.pdf
%_bindir/maxima
%_bindir/rmaxima
%_infodir/*
%if %BUILD_LANG_ES
%exclude %_infodir/es
%exclude %doc_dir/es
%endif
%if %BUILD_LANG_ES_UTF
%exclude %_infodir/es.utf8
%exclude %doc_dir/es.utf8
%endif
%if %BUILD_LANG_PT
%exclude %_infodir/pt
%exclude %doc_dir/pt
%endif
%if %BUILD_LANG_PT_UTF
%exclude %_infodir/pt.utf8
%exclude %doc_dir/pt.utf8
%endif
%if %BUILD_LANG_PT_BR
%exclude %_infodir/pt_BR
%exclude %doc_dir/pt_BR
%endif
%if %BUILD_LANG_PT_BR_UTF
%exclude %_infodir/pt_BR.utf8
%exclude %doc_dir/pt_BR.utf8
%endif
%_mandir/man1/maxima.1*
%dir %_libexecdir/maxima
%dir %_libexecdir/maxima/%maxima_version
%_libexecdir/maxima/%maxima_version/mgnuplot
%dir %_datadir/maxima
%dir %_datadir/maxima/%maxima_version
%_datadir/maxima/%maxima_version/demo
%_datadir/maxima/%maxima_version/doc
%_datadir/maxima/%maxima_version/share
%_datadir/maxima/%maxima_version/src
%_datadir/maxima/%maxima_version/tests
%_datadir/bash-completion/completions/*maxima
%_datadir/pixmaps/*maxima*
%if %BUILD_LANG_ES
%exclude %_datadir/maxima/%maxima_version/doc/html/es
%endif
%if %BUILD_LANG_ES_UTF
%exclude %_datadir/maxima/%maxima_version/doc/html/es.utf8
%endif
%if %BUILD_LANG_PT
%exclude %_datadir/maxima/%maxima_version/doc/html/pt
%endif
%if %BUILD_LANG_PT_UTF
%exclude %_datadir/maxima/%maxima_version/doc/html/pt.utf8
%endif
%if %BUILD_LANG_PT_BR
%exclude %_datadir/maxima/%maxima_version/doc/html/pt_BR
%endif
%if %BUILD_LANG_PT_BR_UTF
%exclude %_datadir/maxima/%maxima_version/doc/html/pt_BR.utf8
%endif
%doc AUTHORS
%doc README
%doc README.external
%doc README.lisps
%doc %_docdir/maxima-%version/intromax.html
%doc %_docdir/maxima-%version/implementation

%if %BUILD_CLISP
%files bin-clisp
%dir %_libdir/maxima
%dir %_libdir/maxima/%maxima_version
%_libdir/maxima/%maxima_version/binary-clisp
%endif

%if %BUILD_GCL
%files bin-gcl
%dir %_libdir/maxima
%dir %_libdir/maxima/%maxima_version
%_libdir/maxima/%maxima_version/binary-gcl
%endif

%if %BUILD_CMUCL
%files bin-cmucl
%dir %_libdir/maxima
%dir %_libdir/maxima/%maxima_version
%_libdir/maxima/%maxima_version/binary-cmucl
%endif

%if %BUILD_SBCL
%files bin-sbcl
%dir %_libdir/maxima
%dir %_libdir/maxima/%maxima_version
%_libdir/maxima/%maxima_version/binary-sbcl
%endif

%if %BUILD_EMACS
%files -n emacs-maxima
%emacs_maxima_dir
%_sysconfdir/emacs/site-start.d/*.el
%_datadir/texmf/tex/latex/emaxima
%dir %_docdir/maxima-%version
%doc %_docdir/maxima-%version/emaxima
%endif

%if %BUILD_XMAXIMA
%files -n xmaxima
%_bindir/xmaxima
%_desktopdir/*.desktop
%dir %_datadir/maxima
%dir %_datadir/maxima/%maxima_version
%_datadir/maxima/%maxima_version/xmaxima
%_datadir/mime/packages/*.xml
%_datadir/metainfo/*.appdata.xml
%endif

%if %BUILD_BOOK
%files book
%dir %_docdir/maxima-%version
%doc %_docdir/maxima-%version/maxima.pdf
%endif

%if %BUILD_LANG_ES
%files lang-es
%_datadir/maxima/%maxima_version/doc/html/es
%_infodir/es
%doc_dir/es
%endif

%if %BUILD_LANG_ES_UTF
%files lang-es-utf8
%_datadir/maxima/%maxima_version/doc/html/es.utf8
%_infodir/es.utf8
%doc_dir/es.utf8
%endif

%if %BUILD_LANG_PT
%files lang-pt
%_datadir/maxima/%maxima_version/doc/html/pt
%_infodir/pt
%doc_dir/pt
%endif

%if %BUILD_LANG_PT_UTF
%files lang-pt-utf8
%_datadir/maxima/%maxima_version/doc/html/pt.utf8
%_infodir/pt.utf8
%doc_dir/pt.utf8
%endif

%if %BUILD_LANG_PT_BR
%files lang-pt_BR
%_datadir/maxima/%maxima_version/doc/html/pt_BR
%_infodir/pt_BR
%doc_dir/pt_BR
%endif

%if %BUILD_LANG_PT_BR_UTF
%files lang-pt_BR-utf8
%_datadir/maxima/%maxima_version/doc/html/pt_BR.utf8
%_infodir/pt_BR.utf8
%doc_dir/pt_BR.utf8
%endif

%changelog
* Wed Apr 29 2020 Andrey Cherepanov <cas@altlinux.org> 5.43.2-alt1
- 5.43.2 (ALT #34445).
- Fix bogus changelog entries.
- Fix License tag according to SPDX.
- Rename maxima-xmaxima to xmaxima and package its metainfo.
- Move all maxima-index.lisp from info dir (ALT #21842).

* Wed Feb 13 2019 Andrey Cherepanov <cas@altlinux.org> 5.42.1-alt2.1
- Build with default cmucl lisp.

* Thu Dec 06 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.42.1-alt2
- rebuilt with recent libffcall
- enabled build on aarch64

* Sat Nov 24 2018 Ilya Mashkin <oddity@altlinux.ru> 5.42.1-alt1
- 5.42.1

* Thu Oct 04 2018 Ilya Mashkin <oddity@altlinux.ru> 5.42.0-alt1
- 5.42.0

* Thu Sep 20 2018 Ilya Mashkin <oddity@altlinux.ru> 5.41.0-alt3
- rebuild with sbcl 1.4.10 (Closes: #33271)
- Try build with --enable-sbcl-exec instead of --enable-sbcl

* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 5.41.0-alt2.1
- NMU: build with texlive 2017
- packaged mime xml

* Wed Dec 20 2017 Ilya Mashkin <oddity@altlinux.ru> 5.41.0-alt2
- rebuild with sbcl 1.4.2

* Wed Oct 04 2017 Ilya Mashkin <oddity@altlinux.ru> 5.41.0-alt1
- 5.41.0

* Sun Jun 18 2017 Ilya Mashkin <oddity@altlinux.ru> 5.40.0-alt1
- 5.40.0

* Sun Dec 18 2016 Ilya Mashkin <oddity@altlinux.ru> 5.39.0-alt1
- 5.39.0

* Thu May 26 2016 Ilya Mashkin <oddity@altlinux.ru> 5.38.1-alt1
- 5.38.1

* Sun Nov 29 2015 Ilya Mashkin <oddity@altlinux.ru> 5.37.3-alt1
- 5.37.3

* Mon Sep 07 2015 Ilya Mashkin <oddity@altlinux.ru> 5.37.1-alt1
- 5.37.1

* Thu May 14 2015 Ilya Mashkin <oddity@altlinux.ru> 5.36.1-alt1
- 5.36.1

* Tue Dec 16 2014 Ilya Mashkin <oddity@altlinux.ru> 5.35.1-alt1
- 5.35.1

* Fri Sep 19 2014 Ilya Mashkin <oddity@altlinux.ru> 5.34.1-alt1
- 5.34.1

* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 5.34.0-alt1
- 5.34.0

* Fri Apr 11 2014 Ilya Mashkin <oddity@altlinux.ru> 5.33.0-alt1
- 5.33.0

* Sat Jan 04 2014 Ilya Mashkin <oddity@altlinux.ru> 5.32.1-alt1
- 5.32.1

* Sun Dec 29 2013 Ilya Mashkin <oddity@altlinux.ru> 5.32.0-alt1
- 5.32.0

* Wed Oct 30 2013 Ilya Mashkin <oddity@altlinux.ru> 5.31.3-alt1
- 5.31.3

* Tue Sep 24 2013 Ilya Mashkin <oddity@altlinux.ru> 5.31.1-alt1
- 5.31.1

* Wed Sep 04 2013 Ilya Mashkin <oddity@altlinux.ru> 5.31.0-alt1
- 5.31.0

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 5.30.0-alt1.qa1
- NMU: rebuilt with libsigsegv.so.2.

* Sun Apr 07 2013 Ilya Mashkin <oddity@altlinux.ru> 5.30.0-alt1
- 5.30.0

* Wed Mar 06 2013 Ilya Mashkin <oddity@altlinux.ru> 5.29.1-alt2
- build with sbcl 1.1.5

* Sun Dec 16 2012 Ilya Mashkin <oddity@altlinux.ru> 5.29.1-alt1
- 5.29.1

* Mon Sep 03 2012 Ilya Mashkin <oddity@altlinux.ru> 5.28.0-alt1
- 5.28.0

* Mon Aug 27 2012 Ilya Mashkin <oddity@altlinux.ru> 5.27.0-alt2
- build with sbcl 1.0.58

* Fri Apr 27 2012 Ilya Mashkin <oddity@altlinux.ru> 5.27.0-alt1
- 5.27.0

* Fri Jan 06 2012 Ilya Mashkin <oddity@altlinux.ru> 5.26.0-alt1
- 5.26.0

* Wed Sep 14 2011 Ilya Mashkin <oddity@altlinux.ru> 5.25.1-alt1
- 5.25.1

* Mon Aug 15 2011 Ilya Mashkin <oddity@altlinux.ru> 5.25.0-alt1
- 5.25.0

* Mon Jun 13 2011 Ilya Mashkin <oddity@altlinux.ru> 5.24.0-alt1
- 5.24.0

* Sat Mar 26 2011 Ilya Mashkin <oddity@altlinux.ru> 5.23.2-alt2
- rebuild with sbcl 1.0.46

* Sat Feb 19 2011 Ilya Mashkin <oddity@altlinux.ru> 5.23.2-alt1
- 5.23.2

* Tue Dec 21 2010 Ilya Mashkin <oddity@altlinux.ru> 5.22.1-alt0.M51.1
- Build for 5.1

* Mon Dec 20 2010 Ilya Mashkin <oddity@altlinux.ru> 5.22.1-alt1
- version up
- set lang packages to noarch

* Wed Dec 08 2010 Ilya Mashkin <oddity@altlinux.ru> 5.22.1-alt0.2
- rebuild with current sbcl

* Thu Nov 25 2010 Ilya Mashkin <oddity@altlinux.ru> 5.22.1-alt0.1
- 5.22.1

* Mon Dec 14 2009 Ilya Mashkin <oddity@altlinux.ru> 5.20.1-alt0.1
- 5.20.1

* Fri Oct 30 2009 Ilya Mashkin <oddity@altlinux.ru> 5.19.2-alt0.2
- rebuild with sbcl 1.0.32
- remove old TeX calls in %%post

* Sun Sep 06 2009 Ilya Mashkin <oddity@altlinux.ru> 5.19.2-alt0.1
- 5.19.2
- fix desktop file
- fix icons locations

* Thu Jul 23 2009 Ilya Mashkin <oddity@altlinux.ru> 5.18.1-alt0.3
- rebuild with sbcl 1.0.29

* Fri Jun 19 2009 Ilya Mashkin <oddity@altlinux.ru> 5.18.1-alt0.2
- fix build in new environment

* Mon Apr 20 2009 Ilya Mashkin <oddity@altlinux.ru> 5.18.1-alt0.1
- 5.18.1

* Tue Mar 17 2009 Ilya Mashkin <oddity@altlinux.ru> 5.17.1-alt0.3
- rebuild with sbcl 1.0.25

* Sat Jan 10 2009 Ilya Mashkin <oddity@altlinux.ru> 5.17.1-alt0.2
- rebuild with sbcl 1.0.24

* Tue Jan 06 2009 Ilya Mashkin <oddity@altlinux.ru> 5.17.1-alt0.1
- 5.17.1
- build with sbcl 1.0.23 instead of gcl
- apply repocop patch
- package maxima-bin-gcl temporary disabled

* Tue Sep 09 2008 Ilya Mashkin <oddity@altlinux.ru> 5.16.3-alt0.1
- 5.16.3

* Thu Jan 03 2008 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.14.0-alt2
- AutoReq fixed for maxima-common.

* Tue Jan 01 2008 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.14.0-alt1
- Maxima 5.14.0.

* Mon Nov 05 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.13.0-alt2
- Rebuilt with new new clisp version.

* Sun Sep 23 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.13.0-alt1
- Maxima 5.13.0.
- Removed Russian summary and description.

* Sun May 06 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.12.0-alt1
- Maxima 5.12.0.

* Thu Jan 11 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.11.0-alt2
- Rebuilt with sbcl 1.0.1.

* Fri Dec 22 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.11.0-alt1
- Maxima 5.11.0.

* Tue Oct 24 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.10.0-alt3
- Fixed problem with gcl compiler temp dir.

* Thu Oct 12 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.10.0-alt2
- Rebuilt with new lisp versions.

* Thu Sep 21 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.10.0-alt1
- Maxima 5.10.0.

* Sun Sep 03 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.3.99rc3-alt0.01
- Maxima 5.9.3.99rc3.

* Fri Sep 01 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.3.99rc2-alt0.03
- Maxima 5.9.3.99rc2.

* Wed Aug 02 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.3.99rc1-alt0.01
- Maxima 5.9.3.99rc1.

* Sat Jul 08 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.3.1cvs-alt0.1cvs20060708
- Spanish and Portuguese languge packs.

* Mon Mar 20 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.3-alt1
- Maxima 5.9.3.

* Sun Mar 05 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.2.99rc2-alt0.01
- Maxima 5.9.2.99rc2.

* Sat Mar 04 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.2.99rc1-alt0.01
- Maxima 5.9.2.99rc1.

* Thu Jan 19 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.2-alt7
- Rebuilt without CMUCL.

* Mon Jan 16 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.2-alt6
- Rebuilt with SBCL 0.9.8.

* Sat Nov 12 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.2-alt5
- Fix clisp banner.

* Fri Oct 28 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.2-alt4
- Build for x86_64 - gcl and clisp.

* Fri Oct 28 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.2-alt3
- Fix for weird SBCL automake problem.

* Tue Oct 18 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.2-alt2
- Rebuilt with SBCL 0.9.5.

* Wed Oct 12 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.2-alt1
- Maxima 5.9.2 - only GCL and CLISP. 

* Sat Feb 26 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.1-alt5
- Rebuild with new GCL and Clisp.

* Sat Dec 25 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.1-alt4
- More fixes for directories.

* Wed Dec 15 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.1-alt3
- Rebuilt without SBCL due to incompatibility with SBCL 0.8.17.

* Mon Dec 06 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.1-alt2
- Add %_libdir/maxima %_datadir/maxima to the package.

* Sat Sep 25 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.1-alt1
- Maxima 5.9.1 release.

* Fri Sep 17 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0.9rc1-alt1
- Maxima 5.9.0.9 RC 1

* Mon Jul 26 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0.9beta2-alt1
- Maxima 5.9.0.9 beta 2

* Wed Jul 21 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0.1-alt0.14
- Rebuilt with new versions of GCL, CLISP and SBCL.

* Thu May 27 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0.1-alt0.13
- Maxima CVS 09.05.2004.
- maxima-book - Maxima book draft.

* Mon Apr 05 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0.1-alt0.12
- Disable sbcl in maxima server mode due to absence of sb-vsd-sockets 
  in sbcl 0.8.8.

* Sat Mar 27 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0.1-alt0.11
- Maxima CVS 27.03.2004 (5.9.1 prerelease).
- Require sbcl 0.8.8

* Wed Mar 03 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0.1-alt0.10
- hack around automake 1.8 incompatibility.

* Sat Nov 29 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0.1-alt0.09
- Resolve readline problem for Maxima GCL when buit under hasher.
- Maxima CVS 28.11.2003.
- Static builds for Clisp and CMUCL.
- Now we need ANSI GCL.

* Sat Sep 27 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0.1-alt0.08
- Maxima CVS 07.09.2003.
- rebuild with sbcl 0.8.3 and gcl 2.6.1 (traditional+ansi).

* Thu Aug 28 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0.1-alt0.07
- Maxima CVS 26.08.2003.
- fix files section for maxima-common.

* Tue Aug 05 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0.1-alt0.06
- /etc/emacs/site-start.d should not be in the emacs-maxima package.
- imaxima removed from maxima.el.

* Fri Aug 01 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0.1-alt0.05
- Maxima CVS 01.08.2003.

* Wed Jul 09 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0.1-alt0.04
- Maxima CVS 06.07.2003.
- maxima-emacs package renamed to emacs-maxima.
- imaxima removed.

* Sat Jun 07 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0.1-alt0.03
- rebuild with gcl 2.5.3.
- Maxima CVS 05.06.2003.

* Fri Mar 21 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0.1-alt0.02
- rebuild with gcl 2.5.2.

* Tue Mar 18 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0.1-alt0.01
- Maxima CVS 18.03.2003.
- SBCL support. 

* Mon Feb 10 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0-alt1
- Maxima 5.9.0.

* Thu Feb 06 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0-alt0.12
- Missing release documentation is installed.

* Wed Feb 05 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0-alt0.11
- Maxima RC4.  It's not expected to be different from final 5.9.0 
  on Linux and other UNIX. 

* Wed Oct 23 2002 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0-alt0.10
- Maxima RC1 CVS 23.10.2002.

* Thu Oct 17 2002 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0-alt0.09
- Maxima RC1 CVS 17.10.2002.
- Rebuild with clisp 2.29

* Sat Oct 12 2002 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0-alt0.08
- Maxima RC1 CVS 12.10.2002.

* Sun Sep 29 2002 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 5.9.0-alt0.07
- Maxima RC1 CVS 29.09.2002.

* Sun Jul 21 2002 Vadim V. Zhytnikov <vvzhy@mail.ru> 5.9.0-alt0.06
- Many Maxima bugfixes.
- Some spec rewrite. In particular subpackages maxima-<lisp> are
  renamed to maxima-bin-<lisp>.

* Mon May 20 2002 Vadim V. Zhytnikov <vvzhy@mail.ru> 5.9.0-alt0.05
- optional build for some packages.
- default lisp now can be selected.
- xmaxima is back.

* Fri Apr 26 2002 Vadim V. Zhytnikov <vvzhy@mail.ru> 5.9.0-alt0.04
- Search path is now in place.

* Sun Mar 24 2002 Vadim V. Zhytnikov <vvzhy@mail.ru> 5.9.0-alt0.03
- Now based on new SourceForge CVS module maxima.
  No migrate is required.

* Fri Mar 8 2002 Vadim V. Zhytnikov <vvzhy@mail.ru> 5.9-alt0.02
- Now new buid system is almost complete.
- Extra subpackages:
    maxima-xmaxima  - xmaxima frontend.
    maxima-emacs    - emacs modes for maxima.

* Thu Feb 21 2002 Vadim V. Zhytnikov <vvzhy@mail.ru> 5.9-alt0.01
- Maxima is split on three packages:
     maxima-common  -  common files
     maxima-clisp   -  clisp binaries
     maxima-gcl     -  gcl binaries
- New build system.

* Thu Jan 10 2002 Vadim V. Zhytnikov <vvzhy@mail.ru> 5.6-alt2
- GCL compilation problem fixed.
- spec rewrite.

* Fri Oct 26 2001 Vadim V. Zhytnikov <vvzhy@mail.ru> 5.6-alt1
- Initial ALT Linux release.

