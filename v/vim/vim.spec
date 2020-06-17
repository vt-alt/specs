# vim: set ft=spec: -*- rpm-spec -*-
# vim600: set fdm=marker:

# {{{ Perl/Python/Ruby/Tcl/MzScheme support
%def_enable perlinterp
%def_disable pythoninterp
%def_enable python3interp
%def_enable rubyinterp
%def_enable tclinterp
%def_disable mzschemeinterp
%def_enable luainterp
# }}}
# {{{ enable/disable logic
%def_enable gpm

%def_enable selinux

%def_enable minimal

%def_enable devel

%def_disable gui_athena
%def_enable gui_gnome2
%def_enable gui_gtk2
%def_disable gui_motif
%def_enable gui_neXtaw

%global gui %nil
%if_enabled gui_athena
%global gui %gui athena
%endif
%if_enabled gui_gnome2
%global gui %gui gnome2
%endif
%if_enabled gui_gtk2
%global gui %gui gtk2
%endif
%if_enabled gui_motif
%global gui %gui motif
%endif
%if_enabled gui_neXtaw
%global gui %gui neXtaw
%endif

%if "%gui" != "%nil"
%force_enable gui_any
%endif
# }}}

# vimspell interface version
%define vimspell_version	50.1

Name: vim
%define branch 8.2
Version: %branch.0011
Release: alt1
Epoch: 4

Summary: VIsual editor iMproved
License: Charityware
Group: Editors
Url: http://www.vim.org
Packager: Gleb Fotengauer-Malinovskiy <glebfm@altlinux.org>

%add_findreq_skiplist %_datadir/vim/*

# Avoid rm -rf $DOCDIR...
%define _customdocdir %_defaultdocdir/%name-common-%version

# {{{ RPM macros
%define vim_runtime_dir %_datadir/vim/vimfiles
# }}}

Source: %name-%version-%release.tar

# {{{ BuildRequires
# Automatically added by buildreq on Mon Apr 28 2003 and filtered by raorn
# Common requires
BuildPreReq: alternatives >= 0.2.0-alt0.7
BuildPreReq: iconv
BuildPreReq: libacl-devel
BuildPreReq: libattr-devel
%if_enabled gpm
BuildPreReq: libgpm-devel
%endif
%if_enabled selinux
BuildPreReq: libselinux-devel
%endif
BuildPreReq: libtinfo-devel
BuildPreReq: unzip
# man commandline check
BuildPreReq: man
# ctags commandline check
BuildPreReq: ctags
# Common X11
%if_enabled gui_any
BuildPreReq: libICE-devel libSM-devel libX11-devel libXdmcp-devel libXpm-devel libXt-devel xorg-proto-devel
%endif
# Athena
%if_enabled gui_athena
BuildPreReq: libXaw-devel libXext-devel libXmu-devel
%endif
# GNOME2
%if_enabled gui_gnome2
BuildPreReq: ORBit2-devel glib2-devel gnome-vfs2-devel libGConf2-devel libart_lgpl-devel libatk-devel libbonobo2-devel libbonoboui-devel libcairo-devel libgnome-devel libgnomecanvas-devel libgnomeui-devel libgtk+2-devel libpango-devel libpopt-devel libxml2-devel pkg-config zlib-devel
%endif
# gtk+2
%if_enabled gui_gtk2
BuildPreReq: glib2-devel libatk-devel libcairo-devel libgtk+2-devel libpango-devel pkg-config
%endif
# motif
%if_enabled gui_motif
BuildPreReq: libXau-devel libXext-devel libXmu-devel libXp-devel openmotif-devel
%endif
# neXtaw
%if_enabled gui_neXtaw
BuildPreReq: libXext-devel libXmu-devel libneXtaw-devel
%endif
# Perl
%if_enabled perlinterp
BuildPreReq: perl-devel
%endif
# Python
%if_enabled pythoninterp
BuildPreReq: python-devel
BuildConflicts: python-dev < 2.3.4-alt1
BuildConflicts: python-devel-static
%endif
# Python
%if_enabled python3interp
BuildPreReq: python3-devel
BuildConflicts: python3-devel-static
%endif
# Ruby
%if_enabled rubyinterp
BuildPreReq: libruby-devel >= 1.8.4-alt1
BuildPreReq: ruby >= 1.8
%endif
# Tcl
%if_enabled tclinterp
BuildPreReq: tcl-devel >= 8.4.0-alt1
%endif
# MzScheme
%if_enabled mzschemeinterp
BuildPreReq: plt2
%endif
%if_enabled luainterp
BuildPreReq: liblua5-devel
%endif
# }}}

# /proc: for "<(command)" bash syntax
# /dev/pts and expect: for some tests which require terminal
# python-module-json: for testdir/test_channel.py
%{?!_without_check:%{?!_disable_check:BuildPreReq: /dev/pts /proc python-module-json expect}}

# {{{ Description
%description
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features: multiple
windows, multi-level undo, block highlighting and more.  The vim-common
package contains files which every VIM binary will need in order to run.
# }}}

# {{{ vim-common
%package common
Summary: The common files needed by any version of the VIM editor
Group: Editors
BuildArch: noarch
PreReq: coreutils
PreReq: %name
PreReq: %_bindir/vim
Requires: mktemp >= 1:1.3.1
Requires: xxd = %epoch:%version-%release
Provides: vimspell-interface = %vimspell_version
Provides: %_datadir/vim/vimfiles/after/compiler
Provides: %_datadir/vim/vimfiles/after/ftplugin
Provides: %_datadir/vim/vimfiles/after/indent
Provides: %_datadir/vim/vimfiles/after/plugin
Provides: %_datadir/vim/vimfiles/after/syntax
Provides: %_datadir/vim/vimfiles/after
Provides: %_datadir/vim/vimfiles/autoload
Provides: %_datadir/vim/vimfiles/colors
Provides: %_datadir/vim/vimfiles/compiler
Provides: %_datadir/vim/vimfiles/doc
Provides: %_datadir/vim/vimfiles/ftdetect
Provides: %_datadir/vim/vimfiles/ftplugin
Provides: %_datadir/vim/vimfiles/indent
Provides: %_datadir/vim/vimfiles/keymap
Provides: %_datadir/vim/vimfiles/lang
Provides: %_datadir/vim/vimfiles/plugin
Provides: %_datadir/vim/vimfiles/print
Provides: %_datadir/vim/vimfiles/syntax
Provides: %_datadir/vim/vimfiles
Provides: %_datadir/vim/spell
Provides: %_datadir/vim
# Bundled plugins:
Provides: vim-plugin-getscript = 33.vim
Obsoletes: vim-plugin-getscript < 33.vim
Provides: vim-plugin-netrw = 143.vim
Obsoletes: vim-plugin-netrw < 143.vim
Provides: vim-plugin-tar-ftplugin = 27.vim
Obsoletes: vim-plugin-tar-ftplugin < 27.vim
Provides: vim-plugin-vimball = 34.vim
Obsoletes: vim-plugin-vimball < 34.vim
Provides: vim-plugin-zip-ftplugin = 24.vim
Obsoletes: vim-plugin-zip-ftplugin < 24.vim
Provides: vim-plugin-vimruby = 20070302.vim
Obsoletes: vim-plugin-vimruby < 20070302.vim

%description common
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features: multiple
windows, multi-level undo, block highlighting and more.  The vim-common
package contains files which every VIM binary will need in order to run.

If you are installing any version of the VIM editor, you'll also need to
the vim-common package installed.
# }}}
# {{{ vimtutor
%package -n vimtutor
Summary: VIM tutor
Group: Editors
BuildArch: noarch
PreReq: %name-common = %epoch:%version-%release
Requires: %_bindir/vim

%description -n vimtutor
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features: multiple
windows, multi-level undo, block highlighting and more.  The vim-common
package contains files which every VIM binary will need in order to run.

This package contains VIM tutor.
# }}}
# {{{ vim-spell
%package spell-source
Summary: vimspell dictionary sources
Group: Development/Other
BuildArch: noarch
Requires: rpm-build-vim = %epoch:%version-%release

%description spell-source
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features: multiple
windows, multi-level undo, block highlighting and more.  The vim-common
package contains files which every VIM binary will need in order to run.

This package contains vimspell sources for building additional
dictionaries.
# }}}
# {{{ vim-minimal
%package minimal
Summary: A minimal version of the VIM editor
Group: Editors
PreReq: coreutils
Provides: vi = %epoch:%version-%release
Provides: /bin/vi

%description minimal
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features: multiple
windows, multi-level undo, block highlighting and more.  The vim-minimal
package includes a minimal version of VIM, which is installed into
/bin/vi for use when only the root partition is present.

Just install it because you'll need it.
# }}}
# {{{ vim-enhanced
%package enhanced
Summary: A terminal-based, full-featured version of the VIM editor
Group: Editors
PreReq: coreutils
PreReq: alternatives >= 0.2.0-alt0.7
Requires: %name-common = %epoch:%version-%release
Provides: %name = %epoch:%version-%release
Provides: %_bindir/vim
Obsoletes: vim-color

%description enhanced
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features: multiple
windows, multi-level undo, block highlighting and more.  The
vim-enhanced package contains a version of VIM with extra, recently
introduced features like Python and Perl interpreters.

Install the vim-enhanced package if you'd like to use a full-featured
VIM, but you don't want to use GUI version of VIM.
You'll also need to install the vim-common package.
# }}}
# {{{ vim-console
%package console
Summary: A terminal-based, full-featured version of the VIM editor
Group: Editors
PreReq: coreutils
PreReq: alternatives >= 0.2.0-alt0.7
Requires: %name-common = %epoch:%version-%release
Provides: %name = %epoch:%version-%release
Provides: %_bindir/vim
Obsoletes: vim-color

%description console
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features: multiple
windows, multi-level undo, block highlighting and more.  The vim-console
package contains a version of VIM with extra, recently introduced
features like Python and Perl interpreters.

Install the vim-console package if you'd like to use a full-featured
VIM, but you don't use X11 or don't want to use GUI version of VIM nor
want to use perl/python/ruby/tcl interface.  You'll also need to install
the vim-common package.
# }}}
# {{{ vim-X11
%package X11
Summary: A full version of VIM editor, including GUI for the X Window System
Group: Editors
BuildArch: noarch
PreReq: coreutils
PreReq: alternatives >= 0.2.0-alt0.7
PreReq: %name-X11-gui
Requires: menu >= 2.1.25-alt4
Requires: %name-common = %epoch:%version-%release
Provides: %name = %epoch:%version-%release
Provides: %_bindir/vim
Obsoletes: vim-color

%description X11
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features: multiple
windows, multi-level undo, block highlighting and more.

VIM-X11 is a full version of the VIM editor, including the GUI. You can
run it either in terminal or within the X Window System. This package
supersedes vim-ehnanced package.

Install the vim-X11 package if you'd like to use a full-featured VIM
with both terminal and X11 interface.  You'll also need to install the
vim-common package.
# }}}
# {{{ vim-X11-athena
%package X11-athena
Summary: A full version of VIM editor, including Xaw GUI for the X Window System
Group: Editors
PreReq: coreutils
PreReq: alternatives >= 0.2.0-alt0.7
Requires: %name-X11 = %epoch:%version-%release
Provides: %name-X11-gui = %epoch:%version-%release
Provides: %_bindir/vim-X11
Obsoletes: vim-color

%description X11-athena
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features: multiple
windows, multi-level undo, block highlighting and more.

VIM-X11 is a full version of the VIM editor, including the GUI. You can
run it either in terminal or within the X Window System. This package
supersedes vim-ehnanced package.

Install the vim-X11 package if you'd like to use a full-featured VIM
with both terminal and X11 Xaw interface.  You'll also need to install
the vim-X11 package.
# }}}
# {{{ vim-X11-gnome2
%package X11-gnome2
Summary: A full version of VIM editor, including GNOME GUI for the X Window System
Group: Editors
PreReq: coreutils
PreReq: alternatives >= 0.2.0-alt0.7
Requires: %name-X11 = %epoch:%version-%release
Provides: %name-X11-gui = %epoch:%version-%release
Provides: %_bindir/vim-X11
Obsoletes: vim-color

%description X11-gnome2
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features: multiple
windows, multi-level undo, block highlighting and more.

VIM-X11 is a full version of the VIM editor, including the GUI. You can
run it either in terminal or within the X Window System. This package
supersedes vim-ehnanced package.

Install the vim-X11 package if you'd like to use a full-featured VIM
with both terminal and X11 GNOME interface.  You'll also need to install
the vim-X11 package.
# }}}
# {{{ vim-X11-gtk2
%package X11-gtk2
Summary: A full version of VIM editor, including gtk+2 GUI for the X Window System
Group: Editors
PreReq: coreutils
PreReq: alternatives >= 0.2.0-alt0.7
Requires: libgtk+2 >= 2.0
Requires: %name-X11 = %epoch:%version-%release
Provides: %name-X11-gui = %epoch:%version-%release
Provides: %_bindir/vim-X11
Obsoletes: vim-color

%description X11-gtk2
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features: multiple
windows, multi-level undo, block highlighting and more.

VIM-X11 is a full version of the VIM editor, including the GUI. You can
run it either in terminal or within the X Window System. This package
supersedes vim-ehnanced package.

Install the vim-X11 package if you'd like to use a full-featured VIM
with both terminal and X11 gtk+2 interface.  You'll also need to install
the vim-X11 package.
# }}}
# {{{ vim-X11-motif
%package X11-motif
Summary: A full version of VIM editor, including Motif GUI for the X Window System
Group: Editors
PreReq: coreutils
PreReq: alternatives >= 0.2.0-alt0.7
Requires: %name-X11 = %epoch:%version-%release
Provides: %name-X11-gui = %epoch:%version-%release
Provides: %_bindir/vim-X11
Obsoletes: vim-color

%description X11-motif
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features: multiple
windows, multi-level undo, block highlighting and more.

VIM-X11 is a full version of the VIM editor, including the GUI. You can
run it either in terminal or within the X Window System. This package
supersedes vim-ehnanced package.

Install the vim-X11 package if you'd like to use a full-featured VIM
with both terminal and X11 Motif interface.  You'll also need to install
the vim-X11 package.
# }}}
# {{{ vim-X11-neXtaw
%package X11-neXtaw
Summary: A full version of VIM editor, including neXtaw GUI for the X Window System
Group: Editors
PreReq: coreutils
PreReq: alternatives >= 0.2.0-alt0.7
Requires: %name-X11 = %epoch:%version-%release
Provides: %name-X11-gui = %epoch:%version-%release
Provides: %_bindir/vim-X11
Obsoletes: vim-color

%description X11-neXtaw
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features: multiple
windows, multi-level undo, block highlighting and more.

VIM-X11 is a full version of the VIM editor, including the GUI. You can
run it either in terminal or within the X Window System. This package
supersedes vim-ehnanced package.

Install the vim-X11 package if you'd like to use a full-featured VIM
with both terminal and X11 neXtaw interface.  You'll also need to
install the vim-X11 package.
# }}}
# {{{ vim-devel
%package -n rpm-build-vim
Summary: RPM macros needed to build additional VIM plugin packages
Group: Development/Other
BuildArch: noarch
#Conflicts: %name-common < %epoch:%version-%release
#Conflicts: %name-common > %epoch:%version-%release
Provides: %name-devel = %epoch:%version-%release
Obsoletes: %name-devel < 4:7.2

%description -n rpm-build-vim
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features: multiple
windows, multi-level undo, block highlighting and more.  The vim-common
package contains files which every VIM binary will need in order to run.

This package contains RPM macros needed to build additional VIM plugin
packages.
# }}}
# {{{ xxd
%package -n xxd
Summary: Make a hexdump or do the reverse
Group: File tools
Conflicts: %name-common < %epoch:%version-%release
Conflicts: %name-common > %epoch:%version-%release

%description -n xxd
xxd creates a hex dump of a given file or standard input. It can
also convert a hex dump back to its original binary form. Like
uuencode(1) and uudecode(1) it allows the transmission of binary
data in a `mail-safe' ASCII representation, but has the
advantage of decoding to standard output. Moreover, it can be
used to perform binary file patching.
# }}}

# {{{ prep section
%prep
%setup -n %name-%version-%release
touch src/auto/*

# Compressed documentation
#__subst 's|^.*#[[:blank:]]*define[[:blank:]]\+DFLT_HELPFILE[[:blank:]]\+.*$|#define DFLT_HELPFILE "$VIMRUNTIME/doc/help.txt.gz"|' src/feature.h

VIMSPELLVERSION=`grep '^[[:blank:]]*#define[[:blank:]]\+VIMSPELLVERSION[[:blank:]]\+[[:digit:]]\+[[:blank:]]*$' src/spellfile.c | sed -e 's/^[[:blank:]]*#define[[:blank:]]\+VIMSPELLVERSION[[:blank:]]\+\([[:digit:]]\+\)[[:blank:]]*$/\1/'`
VIMSUGVERSION=`grep '^[[:blank:]]*#define[[:blank:]]\+VIMSUGVERSION[[:blank:]]\+[[:digit:]]\+[[:blank:]]*$' src/spell.c | sed -e 's/^[[:blank:]]*#define[[:blank:]]\+VIMSUGVERSION[[:blank:]]\+\([[:digit:]]\+\)[[:blank:]]*$/\1/'`
if [ "$VIMSPELLVERSION.$VIMSUGVERSION" != "%vimspell_version" ]; then
  echo "FATAL: %%vimspell_version (%vimspell_version) does not match source ($VIMSPELLVERSION.$VIMSUGVERSION)"
  exit 1
fi
# }}}
# {{{ build section
%build
# autoreconf
%make -C src autoconf
PLTHOME=%_libdir/plt2; export PLTHOME
# {{{ Build CFLAGS
# Load (g)vimrc file(s) from %_sysconfdir
%add_optflags -DSYS_VIMRC_FILE=\\\"%_sysconfdir/vim/vimrc\\\"
%add_optflags -DSYS_GVIMRC_FILE=\\\"%_sysconfdir/vim/gvimrc\\\"
# Largefile support
%add_optflags -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE64_SOURCE=1
# }}}
# {{{ minimal
%if_enabled minimal
make -C src shadow
cd src/shadow
%configure \
	--exec-prefix=/ \
	--with-features=tiny \
	--with-x=no \
	--enable-gui=no \
	--disable-gpm \
	--enable-multibyte \
	--disable-rpath \
	%{subst_enable selinux} \
	--with-tlib=tinfo \
	--with-compiledby="%packager" \
	#

%make_build
cd -
ls src/shadow/vim
mv src/shadow src/build-minimal
%endif
# }}}

common_opts="--with-features=huge \
	--disable-rpath \
	--enable-cscope \
	%{subst_enable gpm} \
	--enable-multibyte \
	%{subst_enable selinux} \
	--with-global-runtime=%vim_runtime_dir \
	--with-tlib=tinfo"

interp_opts="%{subst_enable perlinterp} \
	%{subst_enable pythoninterp} \
	%{subst_enable python3interp} \
	%{subst_enable rubyinterp} \
	%{subst_enable tclinterp} \
	%{subst_enable mzschemeinterp} \
	%{subst_enable luainterp}"

# {{{ full without GUI and interpreters
make -C src shadow
cd src/shadow
%configure \
	$common_opts \
	--with-features=big \
	--disable-perlinterp \
	--disable-pythoninterp \
	--disable-python3interp \
	--disable-rubyinterp \
	--disable-tclinterp \
	--disable-mzschemeinterp \
	--with-x=no \
	--disable-xsmp \
	--enable-gui=no \
	--with-compiledby="%packager" \
	#
%make_build
cd -
ls src/shadow/vim
mv src/shadow src/build-console
# }}}

# {{{ full version with GUI
%if_enabled gui_any
for gui in %{gui}; do
make -C src shadow
cd src/shadow
%configure \
	$common_opts \
	$interp_opts \
	--with-x=yes \
	--enable-gui="$gui" \
	--enable-multibyte \
	--enable-xim \
	--enable-fontset \
	--enable-xsmp \
	--with-compiledby="%packager" \
	#
%make_build
cd -
ls src/shadow/vim
mv src/shadow src/build-$gui
done
%endif
# }}}
# {{{ full without GUI
make -C src shadow
cd src/shadow
%configure \
	$common_opts \
	$interp_opts \
	--with-x \
	--enable-gui=no \
	--disable-xsmp \
	--with-compiledby="%packager" \
	#
%make_build
cd -
ls src/shadow/vim
mv src/shadow src/build-enhanced
# }}}
# }}}
# {{{ install section
%install
mkdir -p %buildroot{%_altdir,%_sysconfdir/vim,/bin,%_bindir,%_man1dir,%_datadir/vim/{ftdetect,langmap,langrc},%_customdocdir,%_usrsrc/vimspell,%_rpmmacrosdir}
# {{{2 make install
for gui in %{gui}; do
	%makeinstall_std -C src/build-"$gui"
	break
done
%makeinstall_std -C src/build-enhanced

mv %buildroot%_bindir/vim %buildroot%_bindir/vim-enhanced

%if_enabled minimal
# Install the minimal version into the /bin
install -p -m755 "src/build-minimal/vim" %buildroot/bin/vi
%endif

for ui in console %{gui}; do
	install -p -m755 "src/build-$ui/vim" "%buildroot%_bindir/vim-$ui"
done
%if_enabled gui_any
for ui in %{gui}; do
	ln -s "vim-$ui" "%buildroot%_bindir/gvim-$ui"
done
%endif
# 2}}}
# {{{2 Set up links for minimal and gui versions
%if_enabled minimal
for i in ex rvi rview ; do
	ln -s -f vi "%buildroot/bin/$i"
done
%endif

%if_enabled gui_any
for i in evim eview gview gvim gvimdiff rgview rgvim ; do
	ln -s -f vim-X11 "%buildroot%_bindir/$i"
done
%endif

# 2}}}
# {{{2 Install documentation
ln -s -f ../../vim/doc %buildroot%_customdocdir/doc
# 2}}}

install -p -m644 vimrc.system %buildroot%_sysconfdir/vim/vimrc
install -p -m644 gvimrc.system %buildroot%_sysconfdir/vim/gvimrc
install -p -m644 vimrc_hebrew %buildroot%_datadir/vim
# ALT-specific filetype
install -p -m644 runtime/ftdetect/* %buildroot%_datadir/vim/ftdetect/

pushd %buildroot%_datadir/vim/tools
    # i need to make a choice :(.
    subst 's|#!/usr/bin/nawk|#!/usr/bin/gawk|' mve.awk
    subst 's,#!/bin/csh.*.*,#!/bin/sh,' vim132
    chmod a-x vimspell* ref*
popd

# {{{2 post-install cleanup
find %buildroot%_datadir/vim \( -name '*.info' -o -name 'README.txt' \) -print0 |
	xargs -r0 rm -f --

for i in autoload colors compiler ftplugin indent keymap lang macros plugin spell syntax tools tutor; do
    cp -f runtime/$i/README.txt README_$i.txt
done
#__cp -f official-patches/README README_patches.txt
# 2}}}

# {{{2 Create RPM macros and runtime dirs in buildroot
mkdir -p %buildroot%vim_runtime_dir
%if_enabled devel
cat <<EOF >%buildroot%_rpmmacrosdir/vim
# Global runtime
%%vim_dir	%_datadir/vim

# Spell files are in vim_dir
%%vim_spell_dir	%%vim_dir/spell
%%vim_spell_source_dir	%_usrsrc/vimspell
%%mkvimspell(L:a)	%%{!-L:%%{!-a:%%{error:mkvimspell: neither language nor -a is specified} }}%%{-L:env LANG="%%{-L*}"} %_bindir/vim-console -E -X -N -n -i NONE -u NONE -U NONE -c 'mkspell! %%{-a:-ascii} %%*' -c q
# VIMSPELLVERSION.VIMSUGVERSION
%%vimspell_version	%vimspell_version

%%vim_runtime_dir	%%vim_dir/vimfiles
# Additional dirs in global runtime
EOF
%endif
for d in after autoload colors compiler doc ftdetect ftplugin indent keymap lang plugin print syntax ; do
    mkdir -p %buildroot%vim_runtime_dir/$d
%if_enabled devel
    cat <<EOF >>%buildroot%_rpmmacrosdir/vim
%%vim_${d}_dir	%%vim_runtime_dir/$d
EOF
%endif
done
%if_enabled devel
cat <<EOF >>%buildroot%_rpmmacrosdir/vim

# "after" dirs in global runtime
EOF
%endif
for d in compiler ftplugin indent plugin syntax ; do
    mkdir -p %buildroot%vim_runtime_dir/after/$d
%if_enabled devel
    cat <<EOF >>%buildroot%_rpmmacrosdir/vim
%%vim_after_${d}_dir	%%vim_after_dir/$d
EOF
%endif
done
%if_enabled devel
cat <<EOF >>%buildroot%_rpmmacrosdir/vim

%%vim_script_url() http://www.vim.org/scripts/script.php?script_id=%%1%%nil

# post-install commands (obsoleted by filetrigger)
%%update_vimhelp	%%{warning %%%%update_vimhelp is obsolete}
%%clean_vimhelp		%%{warning %%%%clean_vimhelp is obsolete}
EOF
%endif
# 2}}}
# {{{2 update-vimhelp script
cat <<EOF >%buildroot%_bindir/update-vimhelp
#! /bin/sh

VIM=%_bindir/vim
DOCDIR=

[ -x "\$VIM" ] || exit 1
[ -z "\$RPM_INSTALL_NAME" ] || exit 0

if [ -n "\$1" ]; then
  if [ -d "\$1" -a -w "\$1" ]; then
    DOCDIR="\$1"
  fi
else
  if [ -d %vim_runtime_dir/doc -a -w %vim_runtime_dir/doc ]; then
    DOCDIR="%vim_runtime_dir/doc"
  elif [ -d "\$HOME/.vim/doc" -a -w "\$HOME/.vim/doc" ]; then
    DOCDIR="\$HOME/.vim/doc"
  fi
fi

[ -n "\$DOCDIR" ] || exit 1

echo ":helptags \$DOCDIR" | \$VIM -E -s -X -N -n -i NONE -u NONE -U NONE ||:
EOF

chmod 755 %buildroot%_bindir/update-vimhelp
# 2}}}
# {{{2 Filetrigger
cat <<EOF >%buildroot%_rpmlibdir/vim.filetrigger
#!/bin/sh -e

grep -qs '^%vim_runtime_dir/doc/' && update-vimhelp ||:
EOF

chmod 755 %buildroot%_rpmlibdir/vim.filetrigger
# 2}}}
# {{{2 files.req
cat <<EOF >%buildroot%_rpmlibdir/vim-files.req.list
%_datadir/vim/vimfiles/after/compiler	vim-common
%_datadir/vim/vimfiles/after/ftplugin	vim-common
%_datadir/vim/vimfiles/after/indent	vim-common
%_datadir/vim/vimfiles/after/plugin	vim-common
%_datadir/vim/vimfiles/after/syntax	vim-common
%_datadir/vim/vimfiles/after	vim-common
%_datadir/vim/vimfiles/autoload	vim-common
%_datadir/vim/vimfiles/colors	vim-common
%_datadir/vim/vimfiles/compiler	vim-common
%_datadir/vim/vimfiles/doc	vim-common
%_datadir/vim/vimfiles/ftdetect	vim-common
%_datadir/vim/vimfiles/ftplugin	vim-common
%_datadir/vim/vimfiles/indent	vim-common
%_datadir/vim/vimfiles/keymap	vim-common
%_datadir/vim/vimfiles/lang	vim-common
%_datadir/vim/vimfiles/plugin	vim-common
%_datadir/vim/vimfiles/print	vim-common
%_datadir/vim/vimfiles/syntax	vim-common
%_datadir/vim/vimfiles	vim-common
%_datadir/vim/spell	vim-common
%_datadir/vim	vim-common
EOF
# 2}}}
# {{{2 spell-source
cp -a runtime/spell/[a-z][a-z] %buildroot%_usrsrc/vimspell
cp -a runtime/spell/[a-z][a-z].vim %buildroot%_usrsrc/vimspell
cp -a runtime/spell/*.aap %buildroot%_usrsrc/vimspell
# 2}}}
# {{{2 Install icons
%if_enabled gui_any
install -p -m644 -D runtime/vim16x16.png %buildroot%_miconsdir/gvim.png
install -p -m644 -D runtime/vim32x32.png %buildroot%_niconsdir/gvim.png
install -p -m644 -D runtime/vim48x48.png %buildroot%_liconsdir/gvim.png
%endif
# 2}}}
# {{{2 Install menu
%if_enabled gui_any
install -p -m644 -D gvim.desktop %buildroot%_desktopdir/gvim.desktop
%endif
# 2}}}
# {{{2 Install alternatives files
install -p -m644 alternatives/vim-enhanced %buildroot%_altdir/vim-enhanced
install -p -m644 alternatives/vim-console %buildroot%_altdir/vim-console
%if_enabled gui_any
install -p -m644 alternatives/vim-X11 %buildroot%_altdir/vim-X11

 %if_enabled gui_athena
install -p -m644 alternatives/vim-X11-athena %buildroot%_altdir/vim-X11-athena
 %endif
 %if_enabled gui_gnome2
install -p -m644 alternatives/vim-X11-gnome2 %buildroot%_altdir/vim-X11-gnome2
 %endif
 %if_enabled gui_gtk2
install -p -m644 alternatives/vim-X11-gtk2 %buildroot%_altdir/vim-X11-gtk2
 %endif
 %if_enabled gui_motif
install -p -m644 alternatives/vim-X11-motif %buildroot%_altdir/vim-X11-motif
 %endif
 %if_enabled gui_neXtaw
install -p -m644 alternatives/vim-X11-neXtaw %buildroot%_altdir/vim-X11-neXtaw
 %endif
%endif
# 2}}}
# {{{2 Language-specific parts
%find_lang --with-man --output vim.lang vim ex rview rvim view vimdiff
%find_lang --with-man --output xxd.lang xxd
%find_lang --with-man --output vimtutor.lang --custom-file-script 's:\(%_datadir/vim/tutor/tutor\)\(\.\([a-z][a-z]\)\(\..*\)\?\)$:%%lang(\3) \1\2:; s:^\([^%%].*\)::; s:%%lang(en) ::;' vimtutor
%find_lang --with-man --output vim-X11.lang evim eview gvim gview gvimdiff rgvim rgview
install -p -m644 runtime/langrc/* %buildroot%_datadir/vim/langrc
install -p -m644 runtime/langmap/*.vim %buildroot%_datadir/vim/langmap

# 2}}}
# }}}

%check
# This testsuite requires terminal for some tests
# At least, expect is not worse way to do this.
# May be, there is better.
cat > check.exp <<@@@
set dir [lindex \$argv 0]

spawn /bin/sh
send "make -C \$dir test\r"
send "echo \\\$?\r"
expect '0'
@@@

for ui in minimal console enhanced console %{gui}; do
	if expect -f check.exp src/build-"$ui"; then
		echo "testsuite for $ui variant PASSED" >> check-log
	else
		echo "testsuite for $ui variant FAILED" >> check-log
	fi
done

cat check-log
if grep -q 'FAILED$' check-log; then
	exit 1
fi

# {{{ triggers
%if_enabled minimal
%triggerpostun minimal -- vim-minimal < 6.0.118
[ $2 -gt 0 ] || exit 0
[ -e %_bindir/vi -a -h %_bindir/vi ] && rm -f %_bindir/vi ||:
%endif
# }}}
# {{{ pre/post install scripts
%pre common
if [ -L "%_datadir/vim/doc" ]; then
  d=$(realpath "%_datadir/vim/doc")
  rm -f -- "%_datadir/vim/doc"
  mv -f -- "$d" "%_datadir/vim/doc"
fi
# }}}

# {{{ vim-common files
%files common -f vim.lang
# Note to self: NEVER try to use %%doc in subpackages
%doc README*.txt runtime/gvimrc_example.vim
%doc runtime/termcap runtime/vimrc_example.vim vimrc_hebrew
%doc README.ALT-ru_RU.UTF-8

%dir %_sysconfdir/vim
%config(noreplace) %_sysconfdir/vim/vimrc
%config(noreplace) %_sysconfdir/vim/gvimrc
# {{{2 $VIMRUNTIME
%dir %_datadir/vim
%_datadir/vim/autoload
%_datadir/vim/colors
%_datadir/vim/compiler
%dir %_datadir/vim/doc
%doc %_datadir/vim/doc/*.txt
%doc %_datadir/vim/doc/tags
%_datadir/vim/ftdetect
%_datadir/vim/ftplugin
%_datadir/vim/indent
%_datadir/vim/keymap
%_datadir/vim/lang
%_datadir/vim/langmap
%_datadir/vim/langrc
%_datadir/vim/macros
%_datadir/vim/pack
%_datadir/vim/plugin
%_datadir/vim/print
%_datadir/vim/rgb.txt
%dir %_datadir/vim/spell
%_datadir/vim/spell/cleanadd.vim
%_datadir/vim/spell/fixdup.vim
%_datadir/vim/syntax
%_datadir/vim/tools
%_datadir/vim/vimfiles
%_datadir/vim/*.vim
%_datadir/vim/vimrc_hebrew
# 2}}}
%_bindir/ex
%_bindir/view
%_bindir/rvim
%_bindir/rview
%_bindir/vimdiff
%_bindir/update-vimhelp
%_man1dir/*
%_rpmlibdir/vim.filetrigger
# }}}
# {{{ vimtutor
%files -n vimtutor -f vimtutor.lang
%if_enabled gui_any
%_bindir/gvimtutor
%endif
%_bindir/vimtutor
%dir %_datadir/vim/tutor
%_datadir/vim/tutor/tutor
%_datadir/vim/tutor/tutor.utf-8
%_datadir/vim/tutor/tutor.vim
%_datadir/vim/tutor/README*
# }}}
# {{{ vim-spell files
%files spell-source
%dir %_usrsrc/vimspell
%_usrsrc/vimspell/[a-z][a-z]
%_usrsrc/vimspell/[a-z][a-z].vim
%_usrsrc/vimspell/*.aap
# }}}
# {{{ vim-devel files
%if_enabled devel
%files -n rpm-build-vim
%_rpmmacrosdir/vim
%_rpmlibdir/vim-files.req.list
%endif
# }}}
# {{{ vim-minimal files
%if_enabled minimal
%files minimal
/bin/*
%endif
# }}}
# {{{ vim-console files
%files console
%_altdir/vim-console
%_bindir/vim-console
# }}}
# {{{ vim-enhanced files
%files enhanced
%_altdir/vim-enhanced
%_bindir/vim-enhanced
# }}}
# {{{ vim-X11 files
%if_enabled gui_any
%files X11 -f vim-X11.lang
%_altdir/vim-X11
%_bindir/evim
%_bindir/eview
%_bindir/gvim
%_bindir/gview
%_bindir/gvimdiff
%_bindir/rgvim
%_bindir/rgview
%_niconsdir/gvim.png
%_miconsdir/gvim.png
%_liconsdir/gvim.png
%_desktopdir/gvim.desktop
%endif
# }}}
# {{{ vim-X11-athena files
%if_enabled gui_athena
%files X11-athena
%_altdir/vim-X11-athena
%_bindir/vim-athena
%_bindir/gvim-athena
%endif
# }}}
# {{{ vim-X11-gnome2 files
%if_enabled gui_gnome2
%files X11-gnome2
%_altdir/vim-X11-gnome2
%_bindir/vim-gnome2
%_bindir/gvim-gnome2
%endif
# }}}
# {{{ vim-X11-gtk2 files
%if_enabled gui_gtk2
%files X11-gtk2
%_altdir/vim-X11-gtk2
%_bindir/vim-gtk2
%_bindir/gvim-gtk2
%endif
# }}}
# {{{ vim-X11-motif files
%if_enabled gui_motif
%files X11-motif
%_altdir/vim-X11-motif
%_bindir/vim-motif
%_bindir/gvim-motif
%endif
# }}}
# {{{ vim-X11-neXtaw files
%if_enabled gui_neXtaw
%files X11-neXtaw
%_altdir/vim-X11-neXtaw
%_bindir/vim-neXtaw
%_bindir/gvim-neXtaw
%endif
# }}}
# {{{ xxd
%files -n xxd -f xxd.lang
%_bindir/xxd
# }}}

# {{{ changelog
%changelog
* Mon Dec 16 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 4:8.2.0011-alt1
- Updated to 8.2.0011.
- Enabled python3 support (ALT#37460).
- Disabled python2 support.

* Mon Oct 07 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 4:8.1.2120-alt1
- Updated to 8.1.2120.

* Tue Sep 17 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 4:8.1.2047-alt1
- Updated to 8.1.2047.

* Tue Jun 11 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 4:8.1.1517-alt1
- Updated to 8.1.1517 (fixes: CVE-2019-12735) (ALT#36882).

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 4:8.1.26-alt1.1
- rebuild with new perl 5.28.1

* Mon May 28 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 4:8.1.26-alt1
- Updated to 8.1.0026.
- %name-minimal: enabled support of multibyte encodings (ALT#33359).

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 4:8.0.711-alt1.1.2
- Rebuild with Ruby 2.5.0

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 4:8.0.711-alt1.1.1
- rebuild with new perl 5.26.1

* Wed Sep 06 2017 Andrey Cherepanov <cas@altlinux.org> 4:8.0.711-alt1.1
- Rebuild with Ruby 2.4.1

* Fri Jul 14 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 4:8.0.711-alt1
- Updated to v8.0.0711.

* Wed Mar 22 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 4:8.0.381-alt1.qa1
- NMU: rebuild against Tcl/Tk 8.6

* Mon Feb 27 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 4:8.0.381-alt1
- Updated to v8.0.0381.

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 4:8.0.170-alt1.1
- rebuild with new perl 5.24.1

* Wed Jan 11 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 4:8.0.170-alt1
- Updated to v8.0.0170.
- Do not reset bg variable in default colorscheme.

* Fri Dec 02 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 4:8.0.118-alt1
- Updated to v8.0.0118.
- vi, ex: Disabled reading of vimrc files (ALT#32833).
- Packaged missing manpages.

* Mon Nov 28 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 4:8.0.104-alt1
- Updated to v8.0.0104.
- Disabled default.vim.
- Fixed spec.vim issues.

* Tue Nov 22 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 4:8.0.95-alt1
- Updated to v8.0.0095.

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 4:7.3.353-alt4.2
- rebuild with Ruby 2.3.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 4:7.3.353-alt4.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 4:7.3.353-alt4.1
- rebuild with new perl 5.20.1

* Thu Mar 20 2014 Led <led@altlinux.ru> 4:7.3.353-alt4
- Rebuilt with ruby-2.0.0-alt1
- add upstream fixes for build with Ruby 2.0

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 4:7.3.353-alt3
- built for perl 5.18

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 4:7.3.353-alt2
- rebuilt for perl-5.16

* Thu Nov 24 2011 Dmitry V. Levin <ldv@altlinux.org> 4:7.3.353-alt1
- Updated to 7.3.353.

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4:7.3.333-alt1.1.1
- Rebuild with Python-2.7

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 4:7.3.333-alt1.1
- rebuilt for perl-5.14

* Wed Oct 05 2011 Dmitry V. Levin <ldv@altlinux.org> 4:7.3.333-alt1
- Updated to 7.3.333.

* Fri Jul 08 2011 Dmitry V. Levin <ldv@altlinux.org> 4:7.3.244-alt1
- Updated to 7.3.244.

* Wed May 25 2011 Dmitry V. Levin <ldv@altlinux.org> 4:7.3.206-alt1
- Updated to 7.3.206.

* Sun Apr 24 2011 Dmitry V. Levin <ldv@altlinux.org> 4:7.3.162-alt1
- Updated to 7.3.162.

* Sun Apr 03 2011 Dmitry V. Levin <ldv@altlinux.org> 4:7.3.154-alt1
- Updated to 7.3.154.
- syntax/spec.vim: Added %%dev macro support (by raorn@).

* Thu Mar 03 2011 Dmitry V. Levin <ldv@altlinux.org> 4:7.3.137-alt1
- Updated to 7.3.137 (closes: #25013).

* Wed Feb 02 2011 Dmitry V. Levin <ldv@altlinux.org> 4:7.3.112-alt1
- Updated to 7.3.112.

* Tue Dec 21 2010 Alexey I. Froloff <raorn@altlinux.org> 4:7.3.087-alt1
- Official patches (087)

* Tue Nov 09 2010 Alexey I. Froloff <raorn@altlinux.org> 4:7.3.050-alt1
- Official patches (050)

* Wed Sep 29 2010 Alexey I. Froloff <raorn@altlinux.org> 4:7.3.011-alt1
- Official patches (011)

* Tue Sep 14 2010 Alexey I. Froloff <raorn@altlinux.org> 4:7.3.003-alt2
- Reverted brain-damaged clipboard timestamp patch

* Mon Aug 23 2010 Alexey I. Froloff <raorn@altlinux.org> 4:7.3.003-alt1
- 7.3 patchlevel 003
  + dropped GTK 1.2 support
  + added Lua interpreter
- Enabled SELinux

* Mon Jun 07 2010 Alexey I. Froloff <raorn@altlinux.org> 4:7.2.442-alt2
- Fix langmaps for 4.2.426

* Sun Jun 06 2010 Alexey I. Froloff <raorn@altlinux.org> 4:7.2.442-alt1
- Official patches (442)

* Sat Apr 10 2010 Alexey I. Froloff <raorn@altlinux.org> 4:7.2.411-alt1
- Official patches (411)

* Sat Feb 27 2010 Alexey I. Froloff <raorn@altlinux.org> 4:7.2.377-alt1
- Official patches (377)

* Sat Jan 30 2010 Alexey I. Froloff <raorn@altlinux.org> 4:7.2.351-alt1
- Official patches (351)
- syntax/spec.vim: %%__python_version -> %%_python_version
- vimrc: turn on incremental search by default

* Tue Dec 29 2009 Alexey I. Froloff <raorn@altlinux.org> 4:7.2.323-alt1
- Official patches (323)
- Completely disabled some official patches (7.2.044, 7.2.251 and
  7.2.316)

* Mon Dec 14 2009 Alexey I. Froloff <raorn@altlinux.org> 4:7.2.315-alt1
- Official patches (315)

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4:7.2.284-alt1.1
- Rebuilt with python 2.6

* Tue Nov 10 2009 Alexey I. Froloff <raorn@altlinux.org> 4:7.2.284-alt1
- Official patches (284)
- syntax/spec.vim: hightlight %%post_service/%%preun_service and
  %%pre_control/%%post_control as directives

* Wed Sep 23 2009 Alexey I. Froloff <raorn@altlinux.org> 4:7.2.262-alt1
- Official patches (262)
- syntax/spec.vim: %%undefine is directive, %%nil is global macro
  (reported by thresh@)

* Wed Sep 09 2009 Alexey I. Froloff <raorn@altlinux.org> 4:7.2.245-alt1
- Official patches (245)
- Packaged README_patches.txt from ftp://ftp.vim.org/pub/vim/patches/7.2/README
- syntax/spec.vim: add %%check section

* Fri Jul 17 2009 Alexey I. Froloff <raorn@altlinux.org> 4:7.2.234-alt1
- Official patches (234)
  + cannot debug problems with being in a wrong directory
  + it is not possible to ignore file names without a suffix
- syntax/spec.vim:
  + fixed -abc option syntax for %%setup and %%patch
  + do not highlight certain macros that starts with double underscore
    as Error

* Sun Jul 12 2009 Alexey I. Froloff <raorn@altlinux.org> 4:7.2.228-alt1
- Official patches (228)
 + (after 7.2.215) BufEnter "cd" autocommand causes problems
 + X cut_buffer0 text may be used in the wrong encoding
 + ":mksession" doesn't work properly with 'acd' set
 + a script run with ":silent" cannot give any messages
 + when using ":normal" a saved character may be executed
 + when using ":cd" in a script there is no way to track this
 + cscope is limited to 8 connections
- syntax/spec.vim:
 + highlight "autoreconf" macro as specDirective
 + higlight Tab and trailing whitespaces as Error in %%description and
   %%changelog sections
 + highlight characters after column g:spec_textarea_width (defaults to 72)
   as Error in %%description and %%changelog sections

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 4:7.2.218-alt1
- Official patches (218)
 + if no ctags program found, "make tags" executes first C file
 + crash with specific use of function calls
 + possible hang for deleting auto-indent
 + the register executed by @@ isn't stored in viminfo
 + leaking memory for the command Vim was started with
 + cannot copy/paste HTML to/from Firefox via the clipboard
 + BufWipeout autocmd that edits another buffer causes problems
 + using current window to work on hidden buffer has side effects
 + "set novice" gives an error message, it should be ignored
 + warning for file changed outside of vim even after :checktime
 + memory leak when expanding a series of file names
- syntax/spec.vim: rewritten from scratch
- syntax/perl.vim: support for s||| and s,,, (closes: #19708)

* Sun May 03 2009 Alexey I. Froloff <raorn@altlinux.org> 4:7.2.166-alt1
- Official patches (166)
 + ":hist a" doesn't work like ":hist all" as the docs suggest
 + "silent echo x" inside ":redir" leaves cursor halfway the line
 + (after 7.2.132) can still do ":cd" in SwapExists autocmd
 + no completion for :scscope and :lcscope commands
 + folds messed up in other tab page
 + the quickfix window may get the wrong filetype
 + the command line window may get folding
 + when 'showbreak' is set wrong Visual block size reported
 + FuncUndefined autocmd event argument is expanded like filename
 + no completion for ":sign" command

* Mon Apr 13 2009 Alexey I. Froloff <raorn@altlinux.org> 4:7.2.148-alt2
- Fix filetrigger interpreter

* Sun Apr 05 2009 Sir Raorn <raorn@altlinux.ru> 4:7.2.148-alt1
- Official patches (148)
 + using wrong cursor highlighting after clearing 'keymap'
 + accessing freed memory when changing dir in SwapExists autocmd
 + ":diffoff!" changes settings in windows not in diff mode
 + memory leak when redefining user command with complete arg
 + (after 7.2.132) ":cd" still possible in SwapExists autocmd
 + wrong left shift of blockwise selection in tab when 've' set
 + crash when 'virtualedit' is "all"
 + diff highlighting missing if Visual area starts at cursor pos
 + fixing bold spill redraws too many characters
 + no command line completion for ":cscope" command
 + colorscheme is reloaded when 't_Co' is set to the same value
 + v:warningmsg isn't used for all warnings
 + cursor in wrong position after Tab for small version
 + highlighting a character after the line doesn't always work
- Set 'is_posix' for syntax/sh.vim (closes: #19296)
- xxd utility moved to separate package
- vim-common package made noarch

* Wed Mar 04 2009 Sir Raorn <raorn@altlinux.ru> 4:7.2.130-alt1
- Official patches (130)
 + 'langmap' does not work for multi-byte characters
 + selection unclear for Visual block mode with 'cursorcolumn'
 + cursor invisible in first col in Visual mode if 'number' set
 + crash when using submatch() in substitute()
 + location list incorrectly labelled "Quickfix List"
 + <PageUp> at the more prompt only does half a page
 + status line is redrawn too often
 + location list is copied and then deleted when opening window
 + can't stop output of "!grep a *.c" in gvim with CTRL-C
 + invalid mem access if VimResized autocmd changes screen size
 + ":map" output continues after typing 'q' at more prompt
 + ":tselect" output continues after typing 'q' at more prompt
 + leaking memory when reading XPM bitmap for a sign
 + get another more prompt after typing 'q'
 + (after 7.2.055) ":lcd" causes invalid session file
 + opening command window from input() uses the search history
 + Vim may haing until CTRL-C is typed when using CTRL-Z
- Dropped multibyte langmap patch (implemented in upstream)

* Wed Feb 18 2009 Sir Raorn <raorn@altlinux.ru> 4:7.2.108-alt1
- Official patches (108)
 + using "r" and then CTRL-C Visual highlighting is not removed
 + after ":number" "Press Enter" msg may be on the wrong screen
 + "!xterm&" doesn't work when 'shell' is "bash"
 + unnecessary redraw when changing GUI options in terminal
 + missing first three bytes on sourced FIFO
 + tab page line isn't always updated, e.g. when 'bomb' is set
 + after ":saveas foo" the tab label isn't updated right away
 + modeline setting for 'foldmethod' overrules diff options
 + endless loop for "]s" in HTML when there are no misspellings
 + After a GUI dialog ":echo" messages are deleted

* Sun Feb 01 2009 Sir Raorn <raorn@altlinux.ru> 4:7.2.093-alt1
- Official patches (093)
 + problems with deleting folds
 + "killed" netbeans events are not handled correctly
 + accessing wrong memory with completion and composing char
 + if 'ff' is "mac" then "ga" on a ^J shows 0x0d instead of 0x0a
 + ":tag" doesn't return to the right tag entry in the tag stack
 + Python: vim.eval() is wrong for recursive structures
 + ":set <M-b>=<Esc>b" does not work when 'encoding' is utf-8
 + using ":diffget 1" in buffer 1 corrupts the text
 + adding URL to 'path' doesn't work to edit a file
 + user command containing 0x80 does not work properly
 + ":cs help" output is not aligned for some languages
 + some error messages are not translated
 + (extra) dialogs can't always handle multi-byte text
- Fix python search path on x86_64 (closes: #18377)

* Tue Jan 06 2009 Sir Raorn <raorn@altlinux.ru> 4:7.2.077-alt1
- Official patches (077)
 + (after 7.2.076) rename() fails if names differ only in case
 + problems with deleting folds

* Thu Dec 25 2008 Sir Raorn <raorn@altlinux.ru> 4:7.2.075-alt1
- Official patches (075)
 + the Python interface has an empty entry in sys.path
 + wrong check for filling buffer with encoding
 + using -nb while it is not supported makes other side hang
 + v:count and v:prevcount are not set correctly
 + can't avoid 'wig' and 'suffixes' for glob() and globpath()
 + synIDattr() doesn't support "sp" for special color
 + crash when using WorkShop command ":ws foo"
 + diff is not always displayed properly
 + spell checking doesn't work well for compound words
 + creating funcref requires loading the autoload script first
 + "[Scratch]" is not translated
 + repeating "~" on a Visual block doesn't always update screen
 + GTK GUI: cursor disappears doing ":vsp" when maximized
 + not easy to check if 'encoding' is a multi-byte encoding
 + can't load sesison extra file when it contains special chars
 + error when Emacs tags file line is too long
 + crash when a function returns a:000
 + ":set <xHome>" has the same output as ":set <Home>"
- Don't update help index when $RPM_INSTALL_NAME is set
- Macros moved to %%_rpmmacrosdir
- Eliminated %%__macro abuse

* Sat Dec 13 2008 Kirill A. Shutemov <kas@altlinux.org> 4:7.2.042-alt1.1
- NMU:
  + Compile vim-enhanced with X11 support (closes: #18055)
  + Drop unneeded triggers and post/preun

* Sun Nov 16 2008 Sir Raorn <raorn@altlinux.ru> 4:7.2.042-alt1
- Official patches (042)
 + can use cscope commands in the sandbox, might not be safe
 + no completion for ":doautoall" like for ":doautocmd"
 + file names from viminfo are not available to the user
 + using "ucs-2le" for two-byte BOM, but text might be "utf-16le"
 + memory leak in spell info when deleting a buffer
 + ":e ++ff=dos foo" gets "unix" 'ff' when CR before NL missing
 + diff messed up when editing a diff buffer in another tab page
 + restoring view in autocmd sometimes doesn't work completely
- Removed obsolete update_menus calls
- Packaged filetrigger for updating help indicies
- %%update_vimhelp/%%clean_vimhelp macros made obsolete
- Pacgaged files.req.list with common subdirs

* Sat Nov 01 2008 Sir Raorn <raorn@altlinux.ru> 4:7.2.026-alt1
- Official patches (026)
 + (after 7.2.010) 'K' uses the rest of the line (closes: #17660)

* Fri Oct 03 2008 Sir Raorn <raorn@altlinux.ru> 4:7.2.025-alt1
- Official patches (025)
 + wrong window count when using :bunload in a BufHidden autocmd
 + "K" in Visual mode does not properly escape all characters
 + error when inserting a float value from expression register
 + hang when waiting for X selection, consuming lots of CPU time
 + synstack() doesn't work in an emptly line
 + X11: strlen() used wrongly, pasting very big selection fails
 + completion and exists() don't work for ":noautocmd"
 + getting full file name when executing autocmds may be slow
 + 'cursorcolumn' wrong in a closed fold when display is shifted
 + 'history' can be made negative, causes out-of-memory error
 + a CursorHold event that invokes system() is retriggered

* Wed Aug 27 2008 Sir Raorn <raorn@altlinux.ru> 4:7.2.006-alt1
- Official patches (006)
 + leaking memory when displaying menus
 + typo in translated message, message not translated
 + Cscope help message is not translated
 + HTML files are not recognized by contents
- Removed non-non-latin symbols from langmaps (closes: #16907)

* Wed Aug 13 2008 Sir Raorn <raorn@altlinux.ru> 4:7.2-alt2
- Added missing Serial to rpm-build-vim Privides/Obsoletes

* Tue Aug 12 2008 Sir Raorn <raorn@altlinux.ru> 4:7.2-alt1
- [7.2]
- vim-devel renamed to rpm-build-vim
- Applied langmapmb patch by Konstantin Korikov ('langmap' support
  in UTF-8 locales)
- Added Ukrainian langmaps (led@)
- Added "/media" to list of removable locations in 'viminfo'

* Thu Jul 10 2008 Sir Raorn <raorn@altlinux.ru> 4:7.1.330-alt1
- Official patches (330)
 + when 'cscopetag' is set ":tag" gives an error message
 + illegal memory access when pasting illegal utf-8 on cmd line
 + can't get start of Visual area in an <expr> mapping
 + editing a command line that doesn't fit reverses char order
 + ":smagic!from!to!" doesn't work, it sees the "!" as a flag
 + right halve of double-wide char under popup menu not redrawn
 + reading uninitialized memory when using Del in replace mode

* Wed Jun 18 2008 Sir Raorn <raorn@altlinux.ru> 4:7.1.315-alt1
- Fixed handling of special characters in file names which could
  lead to arbitrary VimL code execution
- Official patches (315)
 + leaking memory when executing a shell command
 + vimtutor only works with vim, not gvim
 + wrong parenmatch highlighting after search/replace dialog
 + filetype detection fails for file name with special characters
 + value of asmsyntax argument isn't checked for valid characters
 + "File/Save" menu in Insert mode doesn't update tab page label
 + shortpath_for_invalid_fname() is too complex and wrong
 + can't edit compressed file with special characters in the name
 + some Unicode symbol chars are handled like word chars
 + when in readonly mode ":options" produces an error
 + incomplete utf-8 byte sequence at end of the file not detected
 + status and tile not updated when using netbeans setModified
 + 'pastetoggle' is written to the session file without escaping
 + crash with specific search pattern using look-behind match
- Updated plugins:
 + vimball (27)
 + netrw (125)
 + tar (17a)
 + getscript (31a)
- Documented -p option in russian man (closes: #11987)

* Mon Apr 14 2008 Sir Raorn <raorn@altlinux.ru> 4:7.1.293-alt1
- Official patches (293)
 + (after 7.1.103) "w" at end of buffer moves cursor too far
 + crash when reversing a list after using it
 + reading unwritten bytes when spell checking with large indent
 + when using a pattern with "\@<=" the submatches can be wrong
 + spell checking considers super/subscript chars as word chars
- Call %%clean_menus in %%postun, not %%preun

* Mon Mar 31 2008 Sir Raorn <raorn@altlinux.ru> 4:7.1.285-alt1
- Official patches (285)
 + always shows "+" at end of screen line with 'cursurline'
 + matchparen plugin has an arbitrary line number limit
 + ":?foo?" matches in current line since patch 7.1.025
 + in tiny version ":!touch %%" causes curbuf to be wrong
 + buffer name [Location List] not used for buffer in other tab
 + "gw" uses 'formatexpr', even though the docs say it doesn't
 + default for 'paragraphs' misses some items
 + when using cscope temporary files are left behind
 + (after 7.1.279) Vim hangs when cscope doesn't exit

* Fri Mar 07 2008 Sir Raorn <raorn@altlinux.ru> 4:7.1.267-alt1
- Official patches (267)
 + (after 7.1.240) "U" doesn't work on all text in Visual mode
 + GUI may have part of the command line cut off
 + pressing CTRL-\ three times causes Vim to quit
 + Netbeans: backspacing in Insert mode may skip a character
 + can't set the '" mark; can't know if setpos() was successful
 + after "U" the cursor can be past end of line
 + error for ":setglobal fenc=anything" when 'modifiable' is off
 + ":sort" doesn't work in a one line file
 + Vim doesn't support utf-32
 + findfile() also returns directories
 + crash when doing "d/\n/e" and 'virtualedit' is "all"
 + cursor in wrong place with 'rl', "utf-8" and illegal byte
 + cursor position wrong after ^@ wrapping halfway if using utf-8
 + for a 2 byte BOM UCS-2 is used, which doesn't work for UTF-16
 + can't get the process ID of Vim
 + filetype with dot doesn't work for indent plugins
 + crash when C-indenting
 + hang when completing file name and space in 'isfname'
 + version string returned by terminal may be used as typed input
 + when changing folds cursor may be positioned in a wrong place

* Thu Jan 31 2008 Sir Raorn <raorn@altlinux.ru> 4:7.1.242-alt1
- Official patches (242)
 + can't get the operator in an ":omap"
 + netbeans: "remove" cannot delete one line
 + GTK GUI: when using the netrw plugin ":gui" causes a hang
 + listing mapping for 0xdb fails when 'encoding' is utf-8
 + matchparen plugin may take so long it looks like Vim hangs
 + aborting ":tabedit" from the ATTENTION dialog leaves tab open
 + ":1s/g\n\zs1//" deletes characters from the first line
 + it's difficult to figure out the nesting of syntax items
 + variants of --remote-tab are not mentioned for "vim --help"
 + syntax region without "keepend" could be truncated
 + (after 7.1.215) synstack() doesn't work for one char region
 + cursor may end up on trail byte after ")"
 + when inserting a "(" the following highlighting may be wrong
 + (after 7.1.217) wildcards of ":helptags" are not expanded
 + glob() doesn't handle "'" when 'shell' is "sh" or "bash"
 + "vim -F -o one two" sets 'rightleft' in one window only
 + command line completion fails for a file name with a '&' char
 + hang in syntax HL when moving over a ")"
 + with 'foldmethod' "indent" fold can't be closed after "3>>"
 + a fold is closed when backspacing in Insert mode
 + memory leak when executing SourceCmd autocommands
 + when shifting lines the change is acted upon multiple times
 + crash with Insert mode completion for a user defined command
 + display problems when diff'ing three files
 + pattern matching is slow when using a lot of simple patterns
 + hang when using complicated pattern and 'hlsearch' or ":match"
 + searchpair() may fail when using 'c' or 'r' flag
 + "gUe" may stop before the end of the word
 + focus change events not always ignored
 + "cib" doesn't work properly on "(x)"
- vimtutor manpage moved to vimtutor package (closes: #13915)
- %%lang'ified non-english tutors

* Sat Jan 05 2008 Sir Raorn <raorn@altlinux.ru> 4:7.1.203-alt1
- Official patches (203)
 + "%%" doesn't work on "/* comment *//* comment */"
 + regexp patterns are not sufficiently tested
 + with tab pages and an argument list session file may be wrong
 + Internal error for ":echo matchstr('a', 'a\%%[\&]')"
 + crash when deleting backwards over a line break in Insert mode
 + "gR" and then BS doesn't work properly with multi-byte chars
 + "expand('<afile>')" returns a bogus value after ":cd dir"
 + cursor after end-of-line: "iA sentence.<Esc>)"
 + CTRL-C doesn't stop duplicating text for "s" in Visual block
 + some of the Vim 5.x digraphs could be supported
 + Unix: ":echo glob('~/{}')" results in "/home/user//"
 + '0 mark doesn't work for "~/foo ~ foo"
 + hang when using ":s/\n//gn"
 + can't do command line completion for a file name extension
 + when reading stdin 'fenc' and 'ff' are not set
 + incomplete utf-8 byte sequence is not checked for validity
 + if 'virtualedit' is "onemore" then ":normal 99|" is not right

* Sun Dec 23 2007 Sir Raorn <raorn@altlinux.ru> 4:7.1.175-alt1
- Official patches (175)
 + :" in Ex mode at end of file results in an error message
 + getting/losing focus may cause hit-enter prompt to be redrawn
 + crash when using a modifier before "while" or "for"
 + warning for the unknown option 'bufsecret'
 + crash related to getting X window ID
 + memory leak when using "gp" in Visual mode
 + xxd crashes when using "xxd -b -c 110"
 + if 'buftype' is "acwrite" Vim still does overwrite check
 + accessing freed memory when using "\%%^" pattern
 + <BS> doesn't work with some combination of option settings
- Fixed linking with libtcl on 64-bit architectures (sbolshakov@)

* Sun Nov 11 2007 Sir Raorn <raorn@altlinux.ru> 4:7.1.155-alt1
- Official patches (155)
 + GTK: can't use negative offset with -geom argument
 + ":redir @A>" doesn't work
 + uninitialized memory read when diffing three files
 + after ":diffup" cursor can be in the wrong position
 + stay in Insert completion mode depending on the char typed
 + (after 7.1.127) freeing memory twice completing user name
 + completion menu messed up when using the scroll bar
 + Visual mode "p" doesn't work when 'clipboard' has "unnamed"
 + lalloc(0) error for line completion with 'ic' and 'inf' set
 + display problem when 'hls' and 'cursorcolumn' are set
 + crash when 'undolevels' is 0 and repeating "udd"

* Mon Oct 15 2007 Sir Raorn <raorn@altlinux.ru> 4:7.1.140-alt1
- Official patches (140)
 + Perl: Msg() doesn't stop when "q" is typed at the more prompt
 + fold truncated when ending Insert mode with CTRL-C
 + v:count can't be used in an expression mapping
- Enable largefile support in -minimal and -console (don't depend
  on Perl and TCL interps)

* Mon Oct 08 2007 Sir Raorn <raorn@altlinux.ru> 4:7.1.137-alt1
- Official patches (137)
 + ":mksession" always adds ":setlocal autoread"
 + getpos("'>") may return < 0 for a Linewise selection
 + memory leak when using Ruby syntax highlighting

* Tue Oct 02 2007 Sir Raorn <raorn@altlinux.ru> 4:7.1.130-alt1
- Official patches (130)
 + (extra) ":vimgrep */*" doesn't work if autocmd changes dir
 + memory leak when doing completing
 + crash with some combination of undo and redo

* Sun Sep 30 2007 Sir Raorn <raorn@altlinux.ru> 4:7.1.125-alt1
- Official patches (125)
 + can't check wether Vim was compiled with Gnome
 + crash after setting 'cmdheight' to huge value
 + ":cd %%:h" fails when editing file in current directory
 + the TermResponse autocommand event is not always triggered
- Filter out non-UNIX and compile-time entries from changelog

* Sat Sep 22 2007 Sir Raorn <raorn@altlinux.ru> 4:7.1.116-alt1
- Official patches (116)
 + autocmmand for focus events may cause problems
 + reading past end of a string when resizing Vim
 + "setlocal stl=%%!expr" doesn't work
 + ":call s:var()" doesn't work if "s:var" is a Funcref
 + ":mkvimrc" doesn't work properly when 'paste' or 'keymap' set
 + Ruby: The Buffer.line= method does not work
 + Perl interface doesn't compile with new version of Perl
 + "dw" past end of last line deletes a character
 + (after 7.1.095) when 'lazyredraw' set redraw may be postponed
 + internal error when using "0 ? {'a': 1} : {}"
 + ":messages" doesn't quit listing on ":"
 + Visual block mode "s" that auto-indents fails in other lines
 + GTK GUI: click on arrow left of tab
 + after ":vimgrep /pat/j *" folds can be wrong
 + using input() with a wrong argument may crash Vim
 + map() on an empty list causes memory to be freed twice
 + memory leak in getmatches()
 + can't display characters above 0x10000

* Tue Sep 04 2007 Sir Raorn <raorn@altlinux.ru> 4:7.1.094-alt1
- Official patches (094)
 + (extra) window position wrong when using ":winpos"
 + when listing variables text of command is not cleared
 + read past end of screen line when checking for double width
 + using wrong buffer to check if syntax HL is present
- Recognize ash and dash scripts as shell-script

* Wed Aug 22 2007 Sir Raorn <raorn@altlinux.ru> 4:7.1.087-alt1
- Official patches (087)
 + GTK GUI: confirm() dialog has a default button when not wanted
 + (after 7.1.062) crash when 'preserveindent' is set
 + crash when using string() on a recursively nested List
 + ":let v:statusmsg" reads memory already freed
 + a couple more strcpy() with overlapping arguments
 + dropping file name on gvim containing CSI byte doesn't work
 + "@" character in 'isfname' doesn't pick up umlauts for latin1
 + completion doesn't work after ":!cat <foo"
 + matchparen plugin doesn't update after window split
 + (after 7.1.081) completion doesn't work with wildcards
 + netbeans doesn't get fileOpened events when using -nb twice
 + after ":split fold.c" folds in one window disappear
 + crash when using specific Python syntax highlighting
 + cscope: reading past command end; writing past buffer end

* Sun Aug 12 2007 Sir Raorn <raorn@altlinux.ru> 4:7.1.068-alt1
- Official patches (068)
 + using strcpy() with arguments that overlap
 + scrolling back at more prompt doesn't work properly
 + CursorHold causes problems for Normal and Visual mode commands
 + completion menu doesn't work properly when 'righleft' is set
 + in Ex mode "g/^/vi" and pressing CTRL-C: Vim hangs and beeps
 + splitting quickfix window messes up window layout
 + with latin1 'ignorecase' doesn't work for umlauts
 + (after 7.0.038) C comment indent can be wrong
 + when 'bomb' is changed the file should be considered modified
 + 'infercase' doesn't work for thesaurus completion
 + 'equalalways' equalizes windows too often

* Mon Aug 06 2007 Sir Raorn <raorn@altlinux.ru> 4:7.1.054-alt1
- Official patches (054)
 + accessing uninitialized memory when finding spell suggestions
 + when creating a new match not all fields are initialized
 + reading uninitialized memory when updating command line
 + accessing uninitialized memory when displaying the fold column

* Sat Aug 04 2007 Sir Raorn <raorn@altlinux.ru> 4:7.1.050-alt1
- Official patches (050)
 + buffer marked modified after ":bdel" and ":next"
 + after ":s/./&/#" all listed lines have a line number
 + add "none" to completion of ":echohl" and ":match"
 + using strcpy() for an overlapping string
 + 'preseveindent' doesn't always work when 'et' is set
 + weird help-tags tag in docs file may make cause a crash
 + ":match" only supports three matches
 + in Ex mode using CTRL-D twice may cause a crash
 + in Insert mode 0 CTRL-T deletes all indent
 + double screen redraw in some situations
 + ":s/.*/&/" deletes composing characters
 + wrong argument for vim_regcomp()
 + paren highlighting is not updated after scrolling
 + can't compile with GTK2 when using hangul input feature
 + possible crash in C++ indenting

* Mon Jul 23 2007 Sir Raorn <raorn@altlinux.ru> 4:7.1.032-alt1
- Official patches (032)
 + when setting 'keymap' twice b:keymap_name variable isn't set
 + "dw" in a line with one character deletes the line
 + using a pointer that may have become invalid
 + search('pat', 'bc) doesn't find word under cursor at BOL
 + "[p" doesn't work in Visual mode
 + ":sort" does nothing special with empty search pattern
 + (after 7.1.019) can't compile when all interfaces are used
 + vimtutor shell script checks for "vim6" but not for "vim7"
 + virtcol([123, '$']) doesn't work
 + possible crash when doing completion on the command line

* Thu Jul 05 2007 Sir Raorn <raorn@altlinux.ru> 4:7.1.020-alt1
- Official patches (020)
 + ":syn include" only loads the first file
 + crash in C-indenting
 + MzScheme interface doesn't build on Mac; init problem
 + (after 7.1.012) error message when using ":cwindow"
 + ":confirm w" does not give a prompt when file is read-only
 + "p" at end of line doesn't work right when 've' is set
 + ":python" doesn't mention the command is not implemented
 + reading uninitialized memory when using a dialog

* Tue Jun 26 2007 Sir Raorn <raorn@altlinux.ru> 4:7.1.012-alt1
- Official patches (012)
 + crash when editing a directory
 + "cit" used on <foo></foo> deletes <foo>
 + when reading from stdin 'modified' can't be reset in autocmd
 + getfsize() returns an invalid number for very big files
 + diff mode: tab to spaces change not highlighted correctly
 + Gnome: tab pages are not included in the saved session
 + buffer overflow when $VIMRUNTIME is very long
 + ":let &tw = 'asdf'" does not give an error message

* Wed May 16 2007 Sir Raorn <raorn@altlinux.ru> 4:7.1.002-alt1
- Official patches (002)
 + can't build with Gnome GUI
 + Oracle Pro*C/C++ files are not detected

* Sun May 13 2007 Sir Raorn <raorn@altlinux.ru> 4:7.1-alt1
- [7.1]

* Thu May 10 2007 Sir Raorn <raorn@altlinux.ru> 4:7.1.000.a.001-alt1
- [7.1a.001]

* Tue Apr 17 2007 Sir Raorn <raorn@altlinux.ru> 4:7.0.224-alt2
- Removed Conflicts to vim-common in vim-mininal due to apt dry-run breakage

* Tue Apr 17 2007 Sir Raorn <raorn@altlinux.ru> 4:7.0.224-alt1
- Official patches (224), see README_patches.txt for more info
- Runtime files updated from ftp://ftp.vim.org/pub/vim/runtime/ (20070416)

* Sat Mar 17 2007 Sir Raorn <raorn@altlinux.ru> 4:7.0.218-alt1
- Official patches (218), see README_patches.txt for more info
- Runtime files updated from ftp://ftp.vim.org/pub/vim/runtime/ (20070317)
- Fixed crash in dictionary function, patch from OpenSUSE (closes: #10911)

* Thu Feb 22 2007 Sir Raorn <raorn@altlinux.ru> 4:7.0.201-alt1
- Official patches (201), see README_patches.txt for more info
- Runtime files updated from ftp://ftp.vim.org/pub/vim/runtime/ (20070220)
- Allow quoted arguments in lilo.conf for root=, image=, etc...
- Exclude-patterns for 'bsk' and 'wig' options, prefix pattern
  with '!' and get false match

* Tue Jan 23 2007 Sir Raorn <raorn@altlinux.ru> 4:7.0.188-alt1
- Official patches (188), see README_patches.txt for more info
- Runtime files updated from ftp://ftp.vim.org/pub/vim/runtime/ (20070118)
- Prevent "make install" from running strip

* Sat Jan 13 2007 Sir Raorn <raorn@altlinux.ru> 4:7.0.182-alt1
- Official patches (182), see README_patches.txt for more info
- Runtime files updated from ftp://ftp.vim.org/pub/vim/runtime/ (20070108)

* Tue Dec 12 2006 Sir Raorn <raorn@altlinux.ru> 4:7.0.178-alt1
- Official patches (178), see README_patches.txt for more info
- Runtime files updated from ftp://ftp.vim.org/pub/vim/runtime/ (20061128)

* Mon Nov 13 2006 Sir Raorn <raorn@altlinux.ru> 4:7.0.162-alt1
- Official patches (162), see README_patches.txt for more info
- Runtime files updated from ftp://ftp.vim.org/pub/vim/runtime/ (20061112)

* Sat Oct 21 2006 Sir Raorn <raorn@altlinux.ru> 4:7.0.146-alt1
- Official patches (146), see README_patches.txt for more info
- Runtime files updated from ftp://ftp.vim.org/pub/vim/runtime/ (20061018)
- Patch for 'eightbitmeta' option.  If unset, assume that Alt+Key
  sends "<Esc>Key" sequence.  Unset it by default.

* Tue Oct 10 2006 Sir Raorn <raorn@altlinux.ru> 4:7.0.122-alt1
- Official patches (122), see README_patches.txt for more info
- Runtime files updated from ftp://ftp.vim.org/pub/vim/runtime/ (20061009)

* Mon Oct 09 2006 Sir Raorn <raorn@altlinux.ru> 4:7.0.121-alt1
- Official patches (121), see README_patches.txt for more info
- Runtime files updated from ftp://ftp.vim.org/pub/vim/runtime/ (20060927)

* Sat Sep 16 2006 Sir Raorn <raorn@altlinux.ru> 4:7.0.109-alt1
- Official patches (109), see README_patches.txt for more info
- Updated vim-devel build-dep recomendation for use with gear(1)

* Mon Sep 11 2006 Sir Raorn <raorn@altlinux.ru> 4:7.0.099-alt1
- Official patches (099), see README_patches.txt for more info
- Runtime files updated from ftp://ftp.vim.org/pub/vim/runtime/ (20060910)
- Build -console with "big" features instead of "huge"
- Disabled GUIs:
 + athena
 + gtk1
 + motif

* Sat Sep 02 2006 Sir Raorn <raorn@altlinux.ru> 4:7.0.081-alt1
- Official patches (081), see README_patches.txt for more info
- ALT-specific filetypes moved to ftdetect/00-altlinux.vim (also
  call ftdetect/*.vim before falling back to "conf" filetype):
 + mutt tempfile
 + postfix aliases
 + bind configuration and zones
 + apache/apache2 configuration
 + tcb's shadow
- Removed patches:
 + alt-mutt-tempfile-filetype, alt-named-filetype - moved to
   ftdetect/00-altlinux.vim
 + alt-perl56 - obsolete
 + alt-tmpdir - obsolete
 + man-path - obsolete
 + langfont, vim_gvimrc, vim_vimrc - already in /etc/vim/*rc
- Runtime files updated from ftp://ftp.vim.org/pub/vim/runtime/ (20060824)
- Updated Provides/Obsoletes for bundled plugins
- Do not edit feature.h, add -D... to CFLAGS
- Removed obsolete tcl/python/gcc h4x0r substs
- Versioned tcl and python builddeps

* Sun Aug 13 2006 Sir Raorn <raorn@altlinux.ru> 4:7.0.051-alt1
- Official patches (051)
 + "%%!" at start of 'statusline' didn't work
 + Perl: changing a line in a non-current buffer may not work
 + (extra) Win32: MSVC 2005 compiler warnings for OLE version
 + the matchparen plugin didn't handle parens in single quotes
 + the exit status of the configure script can be wrong
 + the gzip plugin can't handle file names that have a paren
 + some Tcl scripts are not recognized
 + can't properly close a buffer through the NetBeans interface
 + (after 7.0.44) compile and/or run problem with Perl interface

* Wed Jul 26 2006 Sir Raorn <raorn@altlinux.ru> 4:7.0.042-alt1
- Official patches (042)
 + mouse selection with "z=" and inputlist() gets wrong entry
 + cursor([1, 2]) failed, required third item in the list
 + crash or hang when pasting a block in Insert mode

* Sat Jul 22 2006 Sir Raorn <raorn@altlinux.ru> 4:7.0.039-alt1
- Official patches (039)
 + can't compile with small features and syntax HL
 + crash when resizing Vim window when a line doesn't fit
 + complete() can be used from expr. mapping after inserting text
 + third argument for inputdialog() doesn't work in the console
- Runtime files updated from ftp://ftp.vim.org/pub/vim/runtime/ (20060716)

* Thu Jun 29 2006 Sir Raorn <raorn@altlinux.ru> 4:7.0.035-alt1
- Official patches (035)
 + VMS: plugins are not loaded on startup
 + crash for "VjA789" and repeating
 + GUI: crash when using 'mousefocus'
 + crash when using "\\[" and "\\]" in 'errorformat
 + Ruby: buffer.append() could append to the wrong buffer
 + crash after Insert mode completion without matches
 + it is possible to set arbitrary v: variables
 + crash when deleting an item from a:000
 + Unix: when using libcall() and old error may be shown
 + (extra) Win32: hang on exit when compiled with SNiFF+
 + (extra) OS/2: compilation problem
 + cursor position may be wrong when using getchar()
 + the ":compiler" command can't be used in a FileChangedRO event
 + after deleting a buffer its Select mode mappings remain
 + (extra, after 7.0.027) missing semicolon
 + pasting after autoindent removes the indent
 + repeating completion was wrong after typing text or using BS
 + repeating Insert mode completion doesn't work properly
- Runtime files updated from ftp://ftp.vim.org/pub/vim/runtime/ (20060627)
- Removed vi.1 and rvi.1 manpages (conflicts with tr00 vee klonez)
- Added gvim-UI -> vim-UI links for all versions with GUI

* Sun May 14 2006 Sir Raorn <raorn@altlinux.ru> 4:7.0.017-alt1
- Official patches (017)
 + Insert mode completion: CTRL-L jumped back to original text
 + Motif: doesn't compile with Motif 1.2 and earlier
 + Athena: type casts for lvalues
 + recognize encodings "mac-roman", "dec-mcs" and "hp-roman8"
 + Motif: doesn't link with Motif 1.2 and earlier

* Fri May 12 2006 Sir Raorn <raorn@altlinux.ru> 4:7.0.012-alt1
- Official patches (012)
 + can't compile with eval feature without folding feature
 + matchparen plugin changed cursor column in Insert mode
- gcc 4.1 fixes

* Wed May 10 2006 Sir Raorn <raorn@altlinux.ru> 4:7.0.010-alt1
- Official patches (010)
 + C omni complete has problem with %% and # in tags file path
 + GUI: click in tab pages label may warp mouse pointer
 + Compiler warning for debug_saved used before set
 + (extra) Win32: uninstall didn't delete spell and autoload dirs
 + Mac: "make shadow" didn't link infplist.xml
 + AIX: compiling failed for message.c
 + Can't call a function that uses both <SID> and {expr}
 + ml_get errors when 'spell' is set
 + spellfile plugin required typing login name and password

* Tue May 09 2006 Sir Raorn <raorn@altlinux.ru> 4:7.0.001-alt1
- Official patches (001)
 + 'spellsuggest' could not be added to

* Sun May 07 2006 Sir Raorn <raorn@altlinux.ru> 4:7.0-alt1
- [7.0]

* Mon May 01 2006 Sir Raorn <raorn@altlinux.ru> 4:7.0-alt0.1.g
- [7.0g]
- Set 'named' filetype for /var/lib/bind/etc/* (closes: #9496)

* Tue Apr 25 2006 Sir Raorn <raorn@altlinux.ru> 4:7.0-alt0.1.f
- [7.0f]

* Mon Apr 17 2006 Sir Raorn <raorn@altlinux.ru> 4:7.0-alt0.1.e
- [7.0e]

* Wed Apr 12 2006 Sir Raorn <raorn@altlinux.ru> 4:7.0-alt0.1.d
- [7.0d]

* Wed Mar 29 2006 Sir Raorn <raorn@altlinux.ru> 4:7.0-alt0.1.c01.cvs20060327
- CVS snapshot 20060327 (7.0c01)
- GNOME2 GUI support
- New alternatives weights:
 + vim:
  - X11:      50
  - enhanced: 40
  - console:  35
 + vim-X11:
  - gtk2:   50
  - gtk:    40
  - motif:  30
  - neXtaw: 25
  - athena: 20
  - gnome2: 10
- Added desktop file to vim-X11 package
- Removed menu-file from -X11 (menu >= 2.1.25-alt4 can use desktop files)
- Moved vimtutor to separate package
- New package -spell-source - Vim patches for creating dictionaries
- vim-common now provides vimspell-interface with internal vimspell version
- Changed Requires to Conflicts in vim-devel to vim-common
- Updated rpm macros:
 + Added %%vim_spell_dir
 + Added %%vim_spell_source_dir
 + Added %%mkvispell
 + Added %%vimspell_version
 + Removed %%vim_bitmaps_dir
- README.ALT updated:
 + /colors recomended type changed to "colorscheme"
 + Added note about buldrequres to vim-console/enhanced
 + Documented new macros and vim-spell-?? packaging
- Fix %%_*iconsdir mess
- Sanitized filelist in %%_datadir/vim
- Added more icons to vim-X11 package
- Buildreqs updated for Xorg7

* Mon Feb 20 2006 Sir Raorn <raorn@altlinux.ru> 4:6.4.007-alt1
- Official patches (007)
 + truncating message may write before buffer
 + ":argedit", "argdel" and ":argadd" used count argument
 + Unix: crash when expanding backticks
- Buildreqs updated for Xorg7

* Fri Dec 02 2005 Sir Raorn <raorn@altlinux.ru> 4:6.4.004-alt1
- Official patches (004)
 + (extra) Win32: can't compile the global IME code
 + Unix: may change owner of wrong file in rare cases
 + (after 6.4.002) build problem on non-Unix system
 + "go" doesn't work correctly when 'virtualedit' is set

* Tue Oct 18 2005 Sir Raorn <raorn@altlinux.ru> 4:6.4-alt1
- [6.4] (bugfix release)

* Sat Jul 30 2005 Sir Raorn <raorn@altlinux.ru> 4:6.3.086-alt1
- Official patches (086)
 + syntax highlighting wrong after unloading another buffer
 + crash when using Cscope interface with very long result
 + (extra) VMS: character after ESC not handled correctly
 + (extra, after 6.3.077) VMS: performance issue
 + crash after executing a command in the command-line window
 + (extra) Win32: edit fails when 'enc' is utf-8 and Chinese cp
 + glob() may execute shell command unexpectedly
 + (after 6.3.081) more generic solution to avoid shell commands
 + VMS: add function keys to vt320 termcap entry
 + (extra) Cygwin: update src makefile and add src/po makefile
 + crash in syntax highlighting
 + (extra) Russian translation has a few mistakes

* Wed May 25 2005 Sir Raorn <raorn@altlinux.ru> 4:6.3.074-alt1
- Official patches (074)
 + when converting text with illegal characters Vim may crash
 + crash when 'number' set and with a vertical split
 + CTRL-X message sticks after error for completion
 + crash for substitute message when using UTF-8 and Chinese
 + Win32 GUI: display errors when scrolling up/down
 + with 'insertmode' CTRL-V after Select mode doesn't work

* Mon Apr 04 2005 Sir Raorn <raorn@altlinux.ru> 4:6.3.068-alt1.1
- Fixed vim-console post-sripts

* Wed Mar 30 2005 Sir Raorn <raorn@altlinux.ru> 4:6.3.068-alt1
- Official patches (068)
- Fixed vim-console alternatives

* Wed Mar 23 2005 Sir Raorn <raorn@altlinux.ru> 4:6.3.067-alt1
- Official patches (067)
- New package -console - full version without interpreters (closes: #6270)

* Mon Mar 14 2005 Sir Raorn <raorn@altlinux.ru> 4:6.3.064-alt1.1
- Really removed summary/description translations

* Sun Mar 13 2005 Sir Raorn <raorn@altlinux.ru> 4:6.3.064-alt1
- Official patches (064)
- Rebuilt with python 2.4
- Removed summary and description translations (use specspo :-)

* Sat Jan 15 2005 Sir Raorn <raorn@altlinux.ru> 4:6.3.057-alt1
- Official patches (057)

* Thu Dec 09 2004 Sir Raorn <raorn@altlinux.ru> 4:6.3.045-alt1
- Official patches (045)

* Tue Dec 07 2004 Sir Raorn <raorn@altlinux.ru> 4:6.3.042-alt1
- Official patches (042)

* Thu Nov 18 2004 Sir Raorn <raorn@altlinux.ru> 4:6.3.031-alt1.1
- Removed libelf from build requires

* Wed Nov 17 2004 Sir Raorn <raorn@altlinux.ru> 4:6.3.031-alt1
- Official patches (031)
- Added FAQ in vimhelp format (closes: #5515)

* Tue Oct 05 2004 Sir Raorn <raorn@altlinux.ru> 4:6.3.028-alt2
- Enabled python, dynamic link

* Sun Sep 19 2004 Sir Raorn <raorn@altlinux.ru> 4:6.3.028-alt1
- Official patches (028)
- Do not put online docs in %%_docdir (closes: #5226)
- Keep "tags" file as-is

* Mon Sep 06 2004 Sir Raorn <raorn@altlinux.ru> 4:6.3.025-alt1
- Official patches (025)
- Updated spec syntax from conectiva (closes: #5015) with some changes:
  + Added ALT-specific macros
  + Escaped macros are not hilited
  + Escaped environment variables are not hilited
  + Recognize multiline strings
- Default font for gtk+2 version set to "Fixed 10" (closes: #5063)

* Mon Aug 30 2004 Sir Raorn <raorn@altlinux.ru> 4:6.3.019-alt1
- Official patches (019)
- Converted alternatives to new format
- Updates requires

* Tue Aug 03 2004 Sir Raorn <raorn@altlinux.ru> 4:6.3.015-alt1
- Official patches (015)
- Always update help tags - do not test help files presence

* Mon Jul 12 2004 Sir Raorn <raorn@altlinux.ru> 4:6.3.013-alt1
- Official patches (013)

* Thu Jun 24 2004 Sir Raorn <raorn@altlinux.ru> 4:6.3.007-alt1
- [6.3]
- Official patches (007)
- MzVim (0.560)
- Removed patches (merged upstream):
  + alt-spec-filetype-fixes.patch
  + alt-cp1251-tutor.patch
  + ruvim
- Fixed requires (mktemp >= 1:1.3.1 should be in vim-common)
- Changed global runtime dir from %%_sysconfdir/vim to
  %%_datadir/vim/vimfiles (this does not affect $VIMRUNTIME)
- Enabled +xterm_save
- Removed std_c syntax (now in vim-plugin-std_c-syntax)
- Removed vim-ruby plugin (now in vim-plugin-vimruby)
- Added README.ALT

* Mon Jun 07 2004 Sir Raorn <raorn@altlinux.ru> 4:6.2.532-alt1.1
- Fix gvim's menu entry (re-closes #3979)
- Disabled pythoninterp (*evil grin*)

* Thu May 06 2004 Sir Raorn <raorn@altlinux.ru> 4:6.2.532-alt1
- Official patches (532)
- MzVim (0.540)
- Always apply MzVim patch (scheme ftplugin and syntax updates)

* Tue Apr 27 2004 Sir Raorn <raorn@altlinux.ru> 4:6.2.506-alt1
- Official patches (506)
- MzVim temporary disabled due to glibc 2.3 migration
- Patch16 removed (fixed in upstream)

* Thu Apr 22 2004 Sir Raorn <raorn@altlinux.ru> 4:6.2.490-alt1
- Official patches (490)
- MzVim (0.530)
- eview, evim, gview, gvim, gvimdiff, rgview and rgvim are now
  symlinks to vim-X11, /usr/X11R6/bin/* removed (closes #3979)

* Fri Apr 09 2004 Sir Raorn <raorn@altlinux.ru> 4:6.2.461-alt1
- Official patches (461)
- MzVim (0.520)

* Sun Apr 04 2004 Sir Raorn <raorn@altlinux.ru> 4:6.2.442-alt1
- Official patches (442)
- Enabled perlinterp (due to official patch 233)

* Thu Mar 11 2004 Sir Raorn <raorn@altlinux.ru> 4:6.2.339-alt1
- Official patches (339)
- MzVim disabled (out of sync with upstream)

* Fri Mar 05 2004 Sir Raorn <raorn@altlinux.ru> 4:6.2.318-alt1
- Official patches (318)
- MzVim 0.201

* Wed Mar 03 2004 Sir Raorn <raorn@altlinux.ru> 4:6.2.311-alt1
- Official patches (311)
- MzVim 0.200 (disabled for now)

* Mon Feb 09 2004 Sir Raorn <raorn@altlinux.ru> 4:6.2.246-alt1
- Official patches (246)
- Fixed spec filetype plugin
- Added MzScheme support (Daedalus build only)

* Fri Nov 21 2003 Sir Raorn <raorn@altlinux.ru> 4:6.2.154-alt2
- Added russian translations (thanx to drF_ckoff)

* Mon Nov 17 2003 Sir Raorn <raorn@altlinux.ru> 4:6.2.154-alt1
- Official patches (154)

* Mon Nov 10 2003 Sir Raorn <raorn@altlinux.ru> 4:6.2.144-alt2
- Rebuild with openmotif (vim-X11-motif)

* Sun Nov 02 2003 Sir Raorn <raorn@altlinux.ru> 4:6.2.144-alt1
- Official patches (144)
- Fixed macros highlight in spec syntax
- %%update_vimhelp/%%clean_vimhelp reviewed:
  update-vimhelp is started:
  + after new package installation (not upgrade)
  + after old package removal (upgrade or remove)
- Updated patches:
  + alt-perl56 (due to official patch 139)

* Tue Oct 28 2003 Sir Raorn <raorn@altlinux.ru> 4:6.2.135-alt2
- vim-ruby's doc already in syntax.txt

* Mon Oct 27 2003 Sir Raorn <raorn@altlinux.ru> 4:6.2.135-alt1
- Official patches (135)
- Updated ruby compiler/ftplugin/indent/syntax (tarball from
  http://vim-ruby.rubyforge.org was repacked by raorn - DOS-like
  EOLs and +x attrs on scripts)
- Updated spec syntax
- enable/disable'd gpm support

* Mon Oct 13 2003 Sir Raorn <raorn@altlinux.ru> 4:6.2.117-alt1
- Official patches (117)
- Bring back <S-Insert> mappings to system gvimrc (recloses #2283)
  mswin.vim users should unmap it in their .gvimrc
- Removed patches:
  + alt-cp1251-support (merged upstream)
- enable/disable logic for gui variants (still always build minimal and enhanced)
- Treat %%global as %%define in spec syntax

* Tue Sep 30 2003 Sir Raorn <raorn@altlinux.ru> 4:6.2.106-alt1
- Official patches (106)
- Fixed typo in cp1251-tutor patch
- Recognize cp1251 encoding (closes #3077)
- Mappings to <S-Insert> removed from system gvimrc due to
  conflict with mswin.vim (closes #2283)

* Sun Sep 28 2003 Sir Raorn <raorn@altlinux.ru> 4:6.2.098-alt1
- Official patches (098)
- More updates to spec syntax
- Fix tutor in CP1251 locale (closes #0001810)

* Sat Sep 06 2003 Sir Raorn <raorn@altlinux.ru> 4:6.2.072-alt1
- Official patches (072)
- Fixed triggers
- Updates spec syntax

* Tue Aug 05 2003 Alexander Bokovoy <ab@altlinux.ru> 4:6.2.021-alt2
- Rebuild against Ruby 1.8.0

* Mon Jul 09 2003 Sir Raorn <raorn@altlinux.ru> 4:6.2.021-alt1
- Official patches (021)
- Removed patches (merged upstream):
  + alt-WANT_X11
- More README's to %%doc
- Cleanup $VIMRUNTIME (removed unneeded README's and Amiga icons)
- Removed all plugins (except std_c, script #234)
- Added update-vimhelp script to update help tags.
  Works both, for user updates ~/.vim/doc, for superuser
  updates $VIMRUNTIME/doc
- Reversed dependencies for common -> {enhanced,X11 -> X11-gui}
  to be sure that %%_bindir/vim exists in common's postinstall
  script (needed for update_vimhelp)
- devel subpackage
- Set guifont to "Andale Mono 11" for gtk+2 version (voins)
- Detect right filetype for mutt >= 1.4i temporary files

* Sun Jun 08 2003 Sir Raorn <raorn@altlinux.ru> 4:6.2.014-alt2
- Added some fold markers to specfile ;-)
- XSMP enabled (once again!)
- Do not blindly copy runtime/doc to docdir, but use make
  install'ed files
- Added some useful plugins from http://vim.sf.net:
  + Align (script #294)
  + bufexplorer (script #42)
  + cvcommand (script #90)
  + genutils.vim (script #197)
  + matchit (script #39)
  + multvals.vim (script #171)
  + SearchComplete (script #147)
  + selectbuf (script #107)
  + showmarks (script #152)
  + std_c (script #234) (add "let c_use_stdc=1" in your .vimrc to enable)
  + taglist (script #273)
  + winmanager (script #95)

* Fri Jun 06 2003 Sir Raorn <raorn@altlinux.ru> 4:6.2.014-alt1
- Official patches (014)
- XSMP temporary disabled

* Wed Jun 04 2003 Sir Raorn <raorn@altlinux.ru> 4:6.2.011-alt1
- [6.2]
- Official patches (011)
- Updated rpmspec syntax
- Enabled XSMP (autodetection was b0rken in upstream)

* Tue May 27 2003 Sir Raorn <raorn@altlinux.ru> 4:6.2-alt0.4.f
- [6.2f]

* Mon May 19 2003 Sir Raorn <raorn@altlinux.ru> 4:6.2-alt0.3.e
- [6.2e]
- Force cscope (it is enabled in unix+feat_big, but who knows?)

* Thu May 08 2003 Sir Raorn <raorn@altlinux.ru> 4:6.2-alt0.2.c
- [6.2c]

* Mon Apr 28 2003 Sir Raorn <raorn@altlinux.ru> 4:6.2-alt0.1.b
- [6.2b]
- BuildRequires update
- GTK+2 target
- Disabled perlinterp (threaded perl disabled in upstream)
- vim-minimal provides /bin/vi

* Sat Apr 26 2003 Sir Raorn <raorn@altlinux.ru> 4:6.1.474-alt18.1
- Fix uk translation

* Fri Apr 25 2003 Sir Raorn <raorn@altlinux.ru> 4:6.1.474-alt18
- Official-patches (474)
- Removed version from vim-X11-gui Requires (looks like it confuses apt)
- Reenabled libacl in vim-minimal (suggested by ab)
- Changed "set modelines=0" to "set nomodeline" in system vimrc
  Removed "set modelines=0" from system gvimrc (already disabled in vimrc)
- Fixed (and applied ;-) Patch13

* Thu Apr 10 2003 Stanislav Ievlev <inger@altlinux.ru> 4:6.1.280-alt17.1
- new alternatives config format

* Fri Mar 14 2003 Stanislav Ievlev <inger@altlinux.ru> 4:6.1.280-alt17
- PreReq fixes

* Wed Mar 12 2003 Stanislav Ievlev <inger@altlinux.ru> 4:6.1.280-alt16
- moved to new alternatives scheme
- warning to maintainer: added missing PreReq on update-alternatives

* Wed Jan 08 2003 Dmitry V. Levin <ldv@altlinux.org> 4:6.1.280-alt15
- Disabled modelines again.
- Reenabled perlinterp.
- Fixed interpackage dependencies again.
- Avoid autodependencies for files in /usr/share/vim/.

* Wed Jan 08 2003 Sir Raorn <raorn@altlinux.ru> 4:6.1.280-alt14
- Official patches (280)
- modeline's are back due to official patch 265

* Sat Dec 21 2002 Sir Raorn <raorn@altlinux.ru> 4:6.1.263-alt13
- Official patches (263)
- Fix vim-X11's obsoletes
- Remove libacl from vim-minimal's requires (closes #0001586)
- All interp's are now configurable via rpmbuild --enable/--disable
- Fixed provides for alternatives
- Buildrequires updated (honor --enable/--disable args to rpmbuld)

* Wed Nov 27 2002 Stanislav Ievlev <inger@altlinux.ru> 4:6.1.178-alt12
- temporary removed perlinterp (ldv request)
- disable modelines
- remove deps on csh
- fix tmpdir creation
- remove deps on ispell

* Thu Oct 31 2002 Dmitry V. Levin <ldv@altlinux.org> 3:6.1.178-alt11
- Rebuilt with perl-5.8.

* Sat Oct  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 3:6.1.178-alt10
- rebuilt with tcl 8.4

* Tue Sep 17 2002 Sir Raorn <raorn@altlinux.ru> 3:6.1.178-alt9
- Official patches (178)
- Fixed build with new rpm (thanx to inger)
- System-wide configs are back again ("light" version, thanx to SA)
  Now located in /etc/vim/*vimrc and made %%config(noreplace)
- All %%__perl's replaced with %%__subst's
- Added (experimental) ru_RU.UTF-8 langrc

* Mon Sep 09 2002 Sir Raorn <raorn@altlinux.ru> 3:6.1.174-alt8
- Official patches (174)
- Fixed %%preun X11 script
  Fixed %%triggerpostun X11 script (closes #0001073)
- neXtaw GUI support
- Build all vesions of GUI (gtk+, motif, athena, neXtaw)
- Built with tcl and ruby (closes #0000395)
- Removed default g?vimrc from $VIMRUNTIME
  (they're still available as g?vimrc_example.vim)
- Fixed .m-files sysntax autodetection (closes #0000702)
- Spec cleanup

* Tue Jul 02 2002 Dmitry V. Levin <ldv@altlinux.org> 3:6.1.82-alt7
- Fixed %%triggerpostun scripts again.

* Mon Jul 01 2002 Dmitry V. Levin <ldv@altlinux.org> 3:6.1.82-alt6
- Linked with libtinfo.
- Updated buildrequires and interpackage dependencies.
- Fixed %%post/%%preun/%%postun/%%triggerpostun scripts.

* Mon Jun  3 2002 SA <sa@altlinux.ru> 6.1.82-alt5/3
- pathces
- removed triggerpostun
- removed vim from files section (will be a link, produced by alternatives)

* Mon Mar 25 2002 SA <sa@altlinux.ru> 6.1.0-alt5/3
- new release
- removed clipboard patch (use $ vim -X instead)
- evim included in distribution (practically useless thing...)

* Mon Mar 11 2002 SA <sa@altlinux.ru> 6.1b
- new pre-release 6.1b

* Wed Feb 27 2002 SA <sa@altlinux.ru> 6.1a.008
- new pre-release

* Thu Jan  3 2002 SA <sa@altlinux.ru> 6.0.101-alt3
- triggerpostun

* Sun Dec 23 2001 SA <sa@altlinux.ru> 6.0.101-alt2
- patchlevel 101
- incorporated many ideas by Alexey Morozov <morozov@novosoft.ru>
  (the most important are treating official patches as 'source' and
  use of 'alternatives')
- gui font loading is now based on $LANG (new directory
  runtime/langrc is introduced for this).
- changed numbering of package
- removed vi from /usr/bin, since we have it in /bin anyway

* Fri Nov 30 2001 SA <sa@altlinux.ru> 6.0-alt1.93
- patchlevel 93

* Sun Oct 28 2001 SA <sa@altlinux.ru> 6.0-alt1.26
- patchlevel 26

* Wed Sep 19 2001 SA <sa@altlinux.ru> 6.0-alt0.8.aw
- 6.0aw

* Tue Sep 04 2001 Dmitry V. Levin <ldv@altlinux.ru> 6.0-alt0.8.au
- 6.0au

* Tue Aug 21 2001 Dmitry V. Levin <ldv@altlinux.ru> 6.0-alt0.7.as
- 6.0as

* Thu Aug 16 2001 Dmitry V. Levin <ldv@altlinux.ru> 6.0-alt0.6.ar
- 6.0ar

* Mon Aug 06 2001 Dmitry V. Levin <ldv@altlinux.ru> 6.0-alt0.6.aq
- 6.0aq
- Rebuilt with new perl.

* Tue Jul  3 2001 SA <sa@altlinux.ru> 6.0-alt0.5.am
- 6.0am
- removed unnecessary patches

* Tue Jun 16 2001 SA <sa@altlinux.ru> 6.0-alt0.4.ah
- Fixed slow startup of /usr/bin/vim from X11 package when
  run from remote xterm or if $DISPLAY is broken:
  1. FEAT_XCLIPBOARD (used in terminal vim) is switched off
  (in feature.h)
  2. 'title' and 'icon' features are switched off in vimrc and
  switched on back in gvimrc.
- spec.vim fixed again

* Sat Jun 09 2001 Dmitry V. Levin <ldv@altlinux.ru> 6.0-alt0.3.ah
- Fixed errors in %%post/%%preun introduced in alt0.1.ah.
- Specfile cleanup again (policy enforcement).

* Sat Jun 9 2001 SA <sermar@mail.ru> 6.0-alt0.2ah
- fixed langmap call in vimrc
- removed link to /usr/bin/view
- spec-syntax changed to highlight ALT macros

* Tue May 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 6.0-alt0.1.ah
- 6.0ah
- Changed release scheme; set serial to enable upgrading.
- Minor specfile cleanup (hope nothing have been broken).
- Regenerated spec-mode-update patch (requires checking).
- Recompressed sources and pacthes.

* Wed May 9 2001 SA <sermar@mail.ru>
- 6.0ae
- removed obsolete patches and patches that changed run-time options by
  changing source (system-wide vimrc is a better place)
- changed installation procedure: now it uses VIM Makefile 'install' target
- 'X11' (==gvim) if installed will be symlinked to {vi,vim, etc...}, so user
  will not need 'vim-enhanced' to use terminal-based VIM. 'enhanced' and 'X11'
  are made 'conflicting'

* Sat Dec 23 2000 AEN <aen@logic.ru>
- adopted for RE
- 6.0q
- perl include path fixed

* Wed Dec 13 2000 DindinX <odin@mandrakesoft.com> 6.0-0.07mdk
- 6.0p

* Tue Dec  5 2000 DindinX <odin@mandrakesoft.com> 6.0-0.06mdk
- 6.0o

* Mon Nov 27 2000 DindinX <odin@mandrakesoft.com> 6.0-0.05mdk
- really set CFLAGS to RPM_OPT_FLAGS (should make Dadou happier)
  (thanks to Guillaume)

* Mon Nov 27 2000 DindinX <odin@mandrakesoft.com> 6.0-0.04mdk
- fix ./configure call (--enable-max-feature is now --with-features=huge)
- include some fix in spec.vim from Geoffrey Lee

* Sat Nov 25 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 6.0-0.03mdk
- 6.0n.

* Wed Nov 08 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 6.0-0.02mdk
- Upgrade spec.vim and mandrakizifications.

* Tue Nov  7 2000 DindinX <odin@mandrakesoft.com> 6.0-0.01mdk
- 6.0
- remove ctags from this package

* Tue Sep 19 2000 DindinX <odin@mandrakesoft.com> 5.7-7mdk
- Added a patch to fix the paths in the man pages
  (Thx to Jerome Dumonteil for reporting this)

* Thu Aug 31 2000 DindinX <odin@mandrakesoft.com> 5.7-6mdk
- Rebuild on ke
- Macrozifications
- BM

* Tue Jun 27 2000 DindinX <odin@mandrakesoft.com> 5.7-5mdk
- really fix the help files
- now vi is very spartiate (VI-like) and vim has syntax highlighting

* Mon Jun 26 2000 DindinX <odin@mandrakesoft.com> 5.7-4mdk
- make vim-minimal very, very minimal

* Mon Jun 26 2000 DindinX <odin@mandrakesoft.com> 5.7-3mdk
- fix a typo which prevent the help files to be found
- remove syntax highlighting by default
- remove all trace of indenting

* Mon Jun 26 2000 DindinX <odin@mandrakesoft.com> 5.7-2mdk
- Corrected the ctags version: 3.5.1

* Mon Jun 26 2000 DindinX <odin@mandrakesoft.com> 5.7-1mdk
- 5.7
- use a more standard vimrc file

* Thu May 25 2000 DindinX <odin@mandrakesoft.com> 5.6-19mdk
- Upgrade to 5.6.072
- remove autoindentation :(

* Tue May  2 2000 DindinX <odin@mandrakesoft.com> 5.6-18mdk
- wrap option now defaults to FALSE

* Fri Apr 28 2000 DindinX <odin@mandrakesoft.com> 5.6-17mdk
- remove menu icon path

* Tue Apr 18 2000 Pixel <pixel@mandrakesoft.com> 5.6-16mdk
- fix for perl 5.6
- fix for ctags (i modified patch vim-typo)
- rebuild on true compile box (*with* spec-helper)
- remove abusive provides ctags (not needed)

* Tue Apr 18 2000 DindinX <odin@mandrakesoft.com> 5.6-15mdk
- Fix the online documentation

* Tue Apr 18 2000 DindinX <odin@mandrakesoft.com> 5.6-14mdk
- Make a separate rpm for ctags

* Mon Apr 17 2000 DindinX <odin@mandrakesoft.com> 5.6-13mdk
- fix the name of the menu entry
- remove etags
- move ctags from /bin to /usr/bin
- Added the ctags man page

* Tue Mar 28 2000 DindinX <odin@mandrakesoft.com> 5.6-12mdk
- Do the Right Thing for the menus with the help of
  Guillaume Cottenceau

* Tue Mar 28 2000 DindinX <odin@mandrakesoft.com> 5.6-11mdk
- Fix the menu group once again (sic)
  Thanks to Guillaume Cottenceau

* Mon Mar 27 2000 DindinX <odin@mandrakesoft.com> 5.6-10mdk
- Added icons

* Mon Mar 27 2000 DindinX <odin@mandrakesoft.com> 5.6-9mdk
- fix menu

* Fri Mar 24 2000 DindinX <odin@mandrakesoft.com> 5.6-8mdk
- remove the RPM_ROOT_BUILD references in %%post
  (thanks to Thierry Vignaud for pointing this)
- some changes to the default vimrc

* Wed Mar 22 2000 Pixel <pixel@mandrakesoft.com> 5.6-7mdk
- add provides vim for X11 enhanced and minimal
- changed license from freeware to OpenSource

* Mon Mar 20 2000 DindinX <odin@mandrakesoft.com> 5.6-6mdk
- Specs fixes
- removed absolute links
- Added menu entry
- Remove the hlsearch by default (cause it might be puzzling)

* Thu Feb 10 2000 DindinX <odin@mandrakesoft.com> 5.6-5mdk
- Finally include ctags in vim-common :-/

* Thu Feb 10 2000 DindinX <odin@mandrakesoft.com> 5.6-4mdk
- fix a typo in the call to the ./configure script so more features
  are now enabled.

* Sun Feb  6 2000 DindinX <odin@mandrakesoft.com> 5.6-3mdk
- Added support for Chinese/Japanese/Corean support for gvim
  (Thanks to Pablo)
- added a link for the default vimrc.

* Mon Jan 31 2000 DindinX <odin@mandrakesoft.com> 5.6-2mdk
- Added the doc/ subdirectory in /usr/doc/vim-common-5.6/doc
- Correctly install vimrc_hebrew

* Sun Jan 16 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 5.6-1mdk
- 5.6.
- Enable right to left mode.
- Add vimrc_hebrew from Tzafrir Cohen <tzafrir@technion.ac.il>

* Tue Oct 26 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Build release.

* Tue Sep 21 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- 5.5.

* Mon Aug  2 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Reinserting old patch.

* Thu Jul 29 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- First spec file for Mandrake distribution.

# }}}
# end of file
