# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ gobject-introspection-devel imake libXt-devel perl(BibTeX/Parser.pm) perl(BibTeX/Parser/Author.pm) perl(Date/Format.pm) perl(Date/Parse.pm) perl(Digest/SHA1.pm) perl(Encode.pm) perl(ExtUtils/MakeMaker.pm) perl(Fatal.pm) perl(File/Copy/Recursive.pm) perl(File/Which.pm) perl(HTML/FormatText.pm) perl(HTML/TreeBuilder.pm) perl(HTTP/Request/Common.pm) perl(IPC/System/Simple.pm) perl(JSON.pm) perl(LWP/Protocol/https.pm) perl(LWP/Simple.pm) perl(LWP/UserAgent.pm) perl(LaTeX/ToUnicode.pm) perl(Locale/Maketext/Simple.pm) perl(Math/Trig.pm) perl(Output.pm) perl(Pod/Man.pm) perl(Pod/Text.pm) perl(Pod/Usage.pm) perl(Spreadsheet/ParseExcel.pm) perl(Statistics/Descriptive.pm) perl(Statistics/Distributions.pm) perl(Term/ANSIColor.pm) perl(Term/ReadKey.pm) perl(Test.pm) perl(Tk.pm) perl(Tk/Dialog.pm)
BuildRequires: perl(Tk/NoteBook.pm) perl(URI/Escape.pm) perl(WWW/Mechanize.pm) perl(autodie.pm) perl-devel texinfo xorg-cf-files zlib-devel
# END SourceDeps(oneline)
# findreq artefacts
# let's drop the dep for now
%filter_from_requires /^gambit$/d
# noise
%filter_from_requires /^.bin.sh5$/d
%filter_from_requires /^.bin.bsh$/d
%filter_from_requires /^.bin.ksh$/d
%filter_from_requires /^perl(make-rules.pl)/d
%filter_from_requires /^perl(installer.ctan-mirrors.pl)/d
%filter_from_requires /^perl(installer.mirrors.pl)/d
%filter_from_requires /^perl(TeXLive.trans.pl)/d

BuildRequires: libpixman-devel
BuildRequires: chrpath
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

%global __requires_exclude ^perl\\((PDF::Reuse.*|Pedigree.*|TeXLive.*|Tk::path_tre|only|pdfTeX|script::MakeSPList)\\)|pear\\(animals.php\\)
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_docdir}

# need to bootstrap first
# - xindy need clisp in main
# - let asymptote be packaged separately, as the generated one is known
#   to not be fully functional
%define enable_asymptote	0
%define enable_xindy		0

# in its own package
%define enable_xdvik            1
%define enable_dvi2tty          1

# luajit supports only these architectures
%ifarch %ix86 x86_64 %arm aarch64 %mips
%define enable_luajittex	1
%define enable_mfluajit		1
%else
%define enable_luajittex	0
%define enable_mfluajit		0
%endif

%define with_system_poppler	1
%define with_system_dialog	1
%define with_system_icu		1
%define with_system_lcdf	0
%define with_system_psutils	1
%define with_system_t1lib	1
%define with_system_tex4ht	0
%define with_system_teckit	1

%define enable_shared		1

%define texmfbindir		%{_bindir}
%define texmfdir		%{_datadir}/texmf
%define texmfdistdir		%{_datadir}/texmf-dist
%define texmflocaldir		%{_datadir}/texmf-local
%define texmfextradir		%{_datadir}/texmf-extra
%define texmffontsdir		%{_datadir}/texmf-fonts
%define texmfprojectdir		%{_datadir}/texmf-project
%define texmfvardir		%{_localstatedir}/lib/texmf
%define texmfconfdir		%{_sysconfdir}/texmf
%define relYear	2019
%global tl_version %relYear
%global mga_tl_timestamp 20190410


#-----------------------------------------------------------------------
Name:		texlive
Version:	%relYear
Release:	alt1_2
Summary:	The TeX formatting system
Group:		Publishing
License:	http://www.tug.org/texlive/LICENSE.TL
URL:		http://tug.org/texlive/
Source0:	ftp://tug.org/historic/systems/texlive/%{relYear}/%{name}-%{mga_tl_timestamp}-source.tar.xz
Source1:	ftp://tug.org/historic/systems/texlive/%{relYear}/%{name}-%{mga_tl_timestamp}-source.tar.xz.sha512

%if %{enable_xdvik}
Requires:	ghostscript-module-X
%endif


#-----------------------------------------------------------------------
%if %{with_system_dialog}
Requires:	dialog
%endif
Requires:	gambit
%if %{enable_asymptote}
Requires:	gv
Requires:	tkinter
%endif
%if %{with_system_lcdf}
Requires:	lcdf-typetoools
%else
%endif
%if %{with_system_psutils}
Requires:	psutils
%endif
%if %{with_system_teckit}
Requires:	libteckit-utils
%endif
%if %{with_system_tex4ht}
Requires:	tex4ht
%else
%endif
Requires:	texlive-collection-basic

# Fix upgrade for luatex (mga#12303)

#-----------------------------------------------------------------------
BuildRequires:	bison
%if %{enable_xindy}
BuildRequires:	clisp
BuildRequires:	libffcall-devel
%endif
%if %{enable_asymptote}
BuildRequires:	libfftw3-devel libfftw3-mpi-devel
BuildRequires:	flex
%endif
BuildRequires:	libfreetype-devel
BuildRequires:	pkgconfig(fontconfig)
BuildRequires: pkgconfig(gdlib)
%if %{enable_asymptote}
BuildRequires:	libgc-devel
BuildRequires:	libsigsegv-devel
BuildRequires:	ghostscript-utils
BuildRequires:	libgsl-devel
BuildRequires:	libGL-devel
%endif
BuildRequires:	pkgconfig(gdlib)
%if %{with_system_poppler}
BuildRequires: pkgconfig(poppler)
%endif
BuildRequires:	pkgconfig(xaw7)
%if !%{with_system_dialog}
BuildRequires:	ncurses-devel
%endif
BuildRequires:	pkgconfig(libpng)
%if %{with_system_t1lib}
BuildRequires:	t1lib-devel
%endif
%if %{with_system_teckit}
BuildRequires:	libteckit-devel
%endif
%if %{with_system_icu}
BuildRequires:	libicu-devel
%endif
%if %{enable_xindy}
BuildRequires:	texlive
%endif
%if %{enable_asymptote}
BuildRequires:	makeinfo
%endif
BuildRequires:	pkgconfig(zziplib)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	libpaper-devel
BuildRequires:	mercurial mercurial-hgext

#-----------------------------------------------------------------------
Patch1: texlive-20160523-mageia-format.patch
%if %{enable_asymptote}
Patch2: texlive-20160523-mageia-asymptote.patch
%endif
Patch4: texlive-20160523-texmf-mageia-kpfix.patch
Patch5: includePatch.patch
# Poppler patches
Patch101: 0001-try-to-adapt-to-poppler-0.58.patch
Patch102: pdftex-poppler0.76.patch
Source44: import.info
Provides: dvipng = %{tl_version}
Provides: lcdf-typetools = %{tl_version}
Provides: ps2eps = %{tl_version}
Provides: tex4ht = %{tl_version}
Obsoletes: dvipng <= 1.14-alt1.qa1.1
Obsoletes: lcdf-typetools <= 2.104-alt1
Obsoletes: ps2eps <= 1.68-alt1
Obsoletes: tex4ht <= 1.0.2009_06_11_1038-alt1
Conflicts: dvipng <= 1.14-alt1.qa1.1
Conflicts: lcdf-typetools <= 2.104-alt1
Conflicts: ps2eps <= 1.68-alt1
Conflicts: tetex-afm < 2.01
Conflicts: tetex-bibtex8 < 2.01
Conflicts: tetex-core < 2.01
Conflicts: tetex-dvilj < 2.01
Conflicts: tetex-dvips < 2.01
Conflicts: tetex-latex < 2.01
Conflicts: tetex-xdvi < 2.01
Conflicts: tex4ht <= 1.0.2009_06_11_1038-alt1
Conflicts: texlive-base-bin < 2009
Conflicts: texlive-extra-utils < 2009
Conflicts: texlive-font-utils < 2009
Conflicts: texlive-lang-indic < 2009
Conflicts: texlive-latex-base < 2009
Conflicts: texlive-metapost < 2009
Conflicts: texlive-omega < 2009
Conflicts: texlive-xetex < 2009
Patch33: texlive-2017-alt-texmf-first.patch
Patch34: texlive-2018-alt-gcc8.patch
Provides: texlive-collection-binextra = %{tl_version}
Patch35: texlive-2018-e2k-graphite2.patch
Patch36: texlive-2018-e2k-luatex.patch
Patch37: texlive-2018-e2k-variant.patch

#-----------------------------------------------------------------------
%description
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system. It includes
all the major TeX-related programs, macro packages, and fonts that are
free software, including support for many languages around the world.

%files
%{texmfbindir}/*
%dir %{texmfvardir}
%dir %{texmfconfdir}/web2c
%ghost %config(noreplace) %{texmfconfdir}/web2c/updmap.cfg


#-----------------------------------------------------------------------
%if %{enable_shared}
########################################################################
%define        kpathsea_major          6
%define        kpathsea                libkpathsea%{kpathsea_major}
%exclude %{texmfbindir}/teckit_compile

%package	-n %{kpathsea}
Summary:	Path searching library for TeX-related files
Group:		System/Libraries

%description	-n %{kpathsea}
Kpathsea implements generic path searching, configuration,
and TeX-specific file searching.

%files		-n %{kpathsea}
%{_libdir}/libkpathsea.so.%{kpathsea_major}
%{_libdir}/libkpathsea.so.%{kpathsea_major}.*

#-----------------------------------------------------------------------
%define	kpathsea_devel		libkpathsea-devel

%package	-n %{kpathsea_devel}
Summary:	Kpathsea development files
Group:		Development/C
Provides:	kpathsea-devel = %{version}-%{release}

%description	-n %{kpathsea_devel}
Kpathsea implements generic path searching, configuration,
and TeX-specific file searching.
This package includes the kpathsea development files.

%files		-n %{kpathsea_devel}
%{_includedir}/kpathsea
%{_libdir}/libkpathsea.so
%{_libdir}/pkgconfig/kpathsea.pc

#-----------------------------------------------------------------------
%define	kpathsea_static_devel	libkpathsea-devel-static

%package	-n %{kpathsea_static_devel}
Summary:	Kpathsea development files
Group:		Development/C
Provides:	kpathsea-devel-static = %{version}-%{release}

%description	-n %{kpathsea_static_devel}
Kpathsea implements generic path searching, configuration,
and TeX-specific file searching.
This package includes the static kpathsea library.

%files		-n %{kpathsea_static_devel}
%{_libdir}/libkpathsea.a

#-----------------------------------------------------------------------
%define        texlua_major           5
%define        texluajit_major        2
%define        texlua                 libtexlua%{texlua_major}

%package	-n %{texlua}
Summary:	Library for TeXlua
Group:		System/Libraries

%description	-n %{texlua}
TeXlua library

%files		-n %{texlua}
%{_libdir}/libtexlua53.so.%{texlua_major}
%{_libdir}/libtexlua53.so.%{texlua_major}.*
%if %{enable_luajittex}
%{_libdir}/libtexluajit.so.%{texluajit_major}
%{_libdir}/libtexluajit.so.%{texluajit_major}.*
%endif


#-----------------------------------------------------------------------
%define	texlua_devel		libtexlua-devel

%package	-n %{texlua_devel}
Summary:	Library for TeXlua
Group:		Development/C
Provides:	texlua-devel = %{version}-%{release}

%description	-n %{texlua_devel}
TeXlua library
This package includes the TeXlua development files.

%files		-n %{texlua_devel}
%{_includedir}/texlua53
%{_libdir}/libtexlua53.so
%{_libdir}/pkgconfig/texlua53.pc
%if %{enable_luajittex}
%{_includedir}/texluajit
%{_libdir}/libtexluajit.so
%{_libdir}/pkgconfig/texluajit.pc
%endif

#-----------------------------------------------------------------------
%define	texlua_static_devel	libtexlua-devel-static

%package	-n %{texlua_static_devel}
Summary:	Library for TeXlua
Group:		Development/C
Provides:	texlua-devel-static = %{version}-%{release}

%description	-n %{texlua_static_devel}
TeXlua library
This package includes the static TeXlua library.

%files		-n %{texlua_static_devel}
%{_libdir}/libtexlua53.a
%if %{enable_luajittex}
%{_libdir}/libtexluajit.a
%endif

#-----------------------------------------------------------------------
%define        synctex_major           2
%define        synctex                 libsynctex%{synctex_major}

%package	-n %{synctex}
Summary:	Library for SyncTeX
Group:		System/Libraries

%description	-n %{synctex}
synctex library

%files		-n %{synctex}
%{_libdir}/libsynctex.so.%{synctex_major}
%{_libdir}/libsynctex.so.%{synctex_major}.*

#-----------------------------------------------------------------------
%define	synctex_devel		libsynctex-devel

%package	-n %{synctex_devel}
Summary:	Library for SyncTeX
Group:		Development/C
Provides:	synctex-devel = %{version}-%{release}

%description	-n %{synctex_devel}
synctex library
This package includes the synctex development files.

%files		-n %{synctex_devel}
%{_includedir}/synctex
%{_libdir}/libsynctex.so
%{_libdir}/pkgconfig/synctex.pc

#-----------------------------------------------------------------------
%define	synctex_static_devel	libsynctex-devel-static

%package	-n %{synctex_static_devel}
Summary:	Library for SyncTeX
Group:		Development/C
Provides:	synctex-devel-static = %{version}-%{release}

%description	-n %{synctex_static_devel}
synctex library
This package includes the static synctex library.

%files		-n %{synctex_static_devel}
%{_libdir}/libsynctex.a

#-----------------------------------------------------------------------
%define        ptexenc_major           1
%define        ptexenc                 libptexenc%{ptexenc_major}

%package	-n %{ptexenc}
Summary:	Library for Japanese pTeX
Group:		System/Libraries

%description	-n %{ptexenc}
ptexenc is a useful library for Japanese pTeX
(which stands for publishing TeX, and is an extension of
TeX by ASCII Co.) and its surrounding tools.

%files		-n %{ptexenc}
%{_libdir}/libptexenc.so.%{ptexenc_major}
%{_libdir}/libptexenc.so.%{ptexenc_major}.*

#-----------------------------------------------------------------------
%define	ptexenc_devel		libptexenc-devel

%package	-n %{ptexenc_devel}
Summary:	Library for Japanese pTeX
Group:		Development/C
Provides:	ptexenc-devel = %{version}-%{release}

%description	-n %{ptexenc_devel}
ptexenc is a useful library for Japanese pTeX
(which stands for publishing TeX, and is an extension of
TeX by ASCII Co.) and its surrounding tools.
This package includes the ptexenc development files.

%files		-n %{ptexenc_devel}
%{_includedir}/ptexenc
%{_libdir}/libptexenc.so
%{_libdir}/pkgconfig/ptexenc.pc

#-----------------------------------------------------------------------
%define	ptexenc_static_devel	libptexenc-devel-static

%package	-n %{ptexenc_static_devel}
Summary:	Library for Japanese pTeX
Group:		Development/C
Provides:	ptexenc-devel-static = %{version}-%{release}

%description	-n %{ptexenc_static_devel}
ptexenc is a useful library for Japanese pTeX
(which stands for publishing TeX, and is an extension of
TeX by ASCII Co.) and its surrounding tools.
This package includes the static ptexenc library.

%files		-n %{ptexenc_static_devel}
%{_libdir}/libptexenc.a

########################################################################
# enable_shared
%endif

#-----------------------------------------------------------------------
%prep
%setup -q -n %{name}-%{mga_tl_timestamp}-source
%patch1 -p1
%if %{enable_asymptote}
%patch2 -p1
%endif
%patch4 -p1
%patch5 -p1
%patch101 -p1
%patch102 -p1


# poppler
cp -pv texk/web2c/pdftexdir/pdftoepdf{-poppler0.76.0,}.cc
cp -pv texk/web2c/pdftexdir/pdftosrc{-poppler0.76.0,}.cc

# setup default builtin values, added to paths.h from texmf.cnf
perl -pi -e 's%%^(TEXMFMAIN\s+= ).*%%$1%{texmfdistdir}%%;'			  \
	 -e 's%%^(TEXMFDIST\s+= ).*%%$1%{texmfdistdir}%%;'			  \
	 -e 's%%^(TEXMFLOCAL\s+= ).*%%$1%{texmflocaldir}%%;'			  \
	 -e 's%%^(TEXMFSYSVAR\s+= ).*%%$1%{texmfvardir}%%;'		  \
	 -e 's%%^(TEXMFSYSCONFIG\s+= ).*%%$1%{texmfconfdir}%%;'		  \
	 -e 's%%^(TEXMFHOME\s+= ).*%%$1\$HOME/texmf%%;'			  \
	 -e 's%%^(TEXMFVAR\s+= ).*%%$1\$HOME/.texlive%{relYear}/texmf-var%%;'	  \
	 -e 's%%^(TEXMFCONFIG\s+= ).*%%$1\$HOME/.texlive%{relYear}/texmf-config%%;'\
	 -e 's%%^(OSFONTDIR\s+= ).*%%$1%{_datadir}/fonts%%;'		  \
	texk/kpathsea/texmf.cnf
%patch33 -p0
%patch34 -p1
%patch35 -p2
%patch36 -p2
#patch37 -p2

#-----------------------------------------------------------------------
%build
%add_optflags -fpermissive
export CXXFLAGS="%{optflags} -std=c++11"

[ -d Work ] || mkdir Work
pushd Work
ln -sf ../configure .

%configure							\
        LDFLAGS="-Wl,--no-as-needed -ldl"                       \
	--with-banner-add="/Mageia"				\
	--disable-native-texlive-build				\
	--enable-missing					\
	--disable-linked-scripts				\
	--with-system-libpaper					\
	--with-system-zlib					\
%if %{enable_luajittex}
	--enable-luajittex					\
%else
	--disable-luajittex					\
%endif
%if %{enable_mfluajit}
	--enable-mfluajit					\
%else
	--disable-mfluajit					\
%endif
%if %{enable_shared}
	--enable-shared						\
%else
	--disable-shared					\
%endif
%if %{enable_xindy}
	--enable-xindy-rules            			\
%else
	--disable-xindy						\
%endif
%if %{enable_xdvik}
        --enable-xdvik                                          \
%else
        --disable-xdvik                                         \
%endif
%if %{enable_dvi2tty}
        --enable-dvi2tty                                        \
%else
        --disable-dvi2tty                                       \
%endif
	--with-system-freetype					\
	--with-freetype-includes=%{_includedir}/freetype	\
	--with-system-freetype2					\
	--with-freetype2-includes=%{_includedir}/freetype2	\
%if %{with_system_dialog}
	--disable-dialog					\
%else
	--enable-dialog						\
%endif
%if %{with_system_psutils}
	--disable-psutils					\
%else
	--enable-psutils					\
%endif
	--with-system-gd					\
%if %{with_system_lcdf}
	--disable-lcdf-typetools				\
%endif
	--with-system-png					\
%if %{with_system_t1lib}
	--with-system-t1lib					\
	--disable-t1utils					\
%endif
%if %{with_system_teckit}
	--disable-teckit					\
	--with-teckit-includes=%{_includedir}/teckit		\
%endif
%if %{with_system_tex4ht}
	--disable-tex4htk					\
%endif
%if %{with_system_icu}
	--with-system-icu					\
%else
	--without-system-icu					\
%endif
%if %{with_system_poppler}
	--with-system-xpdf					\
	--with-system-poppler					\
%else
	--without-system-xpdf					\
%endif
	--with-system-zziplib					\
	--with-system-cairo					\
	--with-system-pixman
%make_build

popd

%if %{enable_asymptote}
pushd utils/asymptote
%configure							\
	--enable-gc=system					\
	--enable-texlive-build					\
	--datadir=%{texmfdir}
%make_build
popd
%endif

#-----------------------------------------------------------------------
%install
pushd Work
%makeinstall_std
popd

%if %{enable_asymptote}
pushd utils/asymptote
%makeinstall_std
popd
%endif

mkdir -p %{buildroot}%{_datadir}
for dir in texmf texmf-dist; do
    if [ -d %{buildroot}%{_prefix}/$dir ]; then
	rm -fr %{buildroot}%{_datadir}/$dir
	mv %{buildroot}%{_prefix}/$dir %{buildroot}%{_datadir}
    fi
done

mkdir -p %{buildroot}%{texmfvardir}
mkdir -p %{buildroot}%{texmfconfdir}

%if %{with_system_lcdf}
# stray directory left
rm -fr %{buildroot}%{_datadir}/lcdf-typetools-for-tex-live
%else
# openmpi has a program with the same name
if [ -f %{buildroot}%{texmfbindir}/otfinfo ]; then
    mv -f %{buildroot}%{texmfbindir}/otfinfo{,-texlive}
fi
%endif

pushd %{buildroot}%{texmfbindir}
	# missing symbolic links
	ln -sf aleph lamed
	ln -sf luatex dvilualatex
	ln -sf luatex lualatex
	ln -sf luatex dviluatex
	ln -sf pdftex amstex
	ln -sf pdftex cslatex
	ln -sf pdftex csplain
	ln -sf pdftex eplain
	ln -sf pdftex etex
	ln -sf pdftex latex
	ln -sf pdftex mex
	ln -sf pdftex mltex
	ln -sf pdftex mllatex
	ln -sf pdftex pdfcslatex
	ln -sf pdftex pdfcsplain
	ln -sf pdftex pdfetex
	ln -sf pdftex pdflatex
	ln -sf pdftex pdfmex
	ln -sf pdftex physe
	ln -sf pdftex phyzzx
	ln -sf pdftex utf8mex
	ln -sf pdftex texsis
	ln -sf ptex platex
	ln -sf mpost metafun
	ln -sf mpost mfplain
	ln -sf xetex xelatex

    # correct symlinks
    for file in *; do
	link=`readlink $file` || :
	if [ "x$link" != "x" ]; then
	    ln -sf `echo $link |					\
		sed	-e 's|\.\./.*texmf-dist/|%{texmfdistdir}/|'	\
			-e 's|\.\./.*texmf/|%{texmfdir}/|'`		\
		$file
	fi
    done
%if %{with_system_dialog}
	ln -sf %{_bindir}/dialog tcdialog
%endif
%if %{enable_asymptote}
	ln -sf %{texmfdir}/asymptote/GUI/xasy.py xasy
%endif
	# install scripts from texlive-texmf
	rm -f a2ping afm2afm arlatex authorindex autoinst bibexport		\
	bundledoc cachepic cmap2enc de-macro dviasm ebong e2pall	\
	epspdf epspdftk epstopdf fig4latex findhyph font2afm		\
	fragmaster ht htcontext htlatex htmex httex httexi htxelatex	\
	htxetex latex2man latexdiff latexdiff-vc latexmk latexrevise	\
	listings-ext.sh makeglossaries mathspic mk4ht mkgrkindex	\
	mkjobtexmf mkluatexfontdb mkt1font mptopdf ot2kpx pdf180	\
	pdf270 pdf90 pdfannotextractor pdfatfi pdfbook pdfcrop	\
	pdfflip pdfjam pdfjam-pocketmod pdfjam-slides3up		\
	pdfjam-slides6up pdfjoin pdfnup pdfpun pdfthumb perltex	\
	pfm2kpx pkfix  pkfix-helper ppower4 ps4pdf pst2pdf purifyeps	\
	repstopdf rpdfcrop rungs showglyphs simpdftex splitindex	\
	svn-multi texcount texdiff texdirflatten texdoc texdoctk	\
	texloganalyser thumbpdf tlmgr ulqda updmap vpe vpl2ovp	\
	vpl2vpl
popd

# use texmf data
rm -fr %{buildroot}%{texmfdir} %{buildroot}%{texmfdistdir}

# install manual pages and info files from texlive-texmf tarball
rm -fr %{buildroot}%{_mandir} %{buildroot}%{_infodir}

%if !%{enable_shared}
# do not generate dynamic libraries and do not install static ones
rm -fr %{buildroot}%{_libdir}
rm -fr %{buildroot}%{_includedir}
%endif

rm -f %{buildroot}%{_datadir}/applications/xdvi.desktop
for rpm404_ghost in %{texmfconfdir}/web2c/updmap.cfg
do
    mkdir -p %buildroot`dirname "$rpm404_ghost"`
    touch %buildroot"$rpm404_ghost"
done
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111 ! -name '*.la' `; do
	chrpath -d $i ||:
done


%post 
rm -f %{texmfdir}/ls-R %{texmfdistdir}/ls-R %{texmfconfdir}/ls-R


#-----------------------------------------------------------------------
%changelog
* Sat Jul 20 2019 Igor Vlasenko <viy@altlinux.ru> 2019-alt1_2
- new version

* Fri May 24 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2018-alt3_12
- Fixed build on architectures not supported by luajit.

* Tue Apr 09 2019 Igor Vlasenko <viy@altlinux.ru> 2018-alt2_12
- fixed build with poppler 75 (closes: #35567)

* Wed Feb 13 2019 Igor Vlasenko <viy@altlinux.ru> 2018-alt2_10
- fixed build

* Wed Dec 05 2018 Igor Vlasenko <viy@altlinux.ru> 2018-alt2_7
- built with new poppler (closes: #35711)

* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 2018-alt2_4
- rebuild with new icu

* Tue Oct 16 2018 Igor Vlasenko <viy@altlinux.ru> 2018-alt1_4
- new version; fixes CVE-2018-17407

* Sat Jun 16 2018 Igor Vlasenko <viy@altlinux.ru> 2017-alt2_4
- luatex bugfix thanks to lakostis@ (closes: #35024)

* Sun Mar 11 2018 Igor Vlasenko <viy@altlinux.ru> 2017-alt2_3
- final release

* Thu Mar 01 2018 Igor Vlasenko <viy@altlinux.ru> 2017-alt1_3
- new version

