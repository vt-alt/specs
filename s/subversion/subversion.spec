# hey Emacs, its -*- mode: rpm-spec; coding: cyrillic-cp1251; -*-
# Subversion
# Notes:
# * Do not build subversion on the system where an older version is
#   installed. Subversion links against system-installed libraries in
#   that case which may lead to failed tests or other failures during
#   validation stage. Prefer to build subversion in hasher.
# * Update alt-bdb patch when libdb version changes. Otherwise you may
#   have failures in tests for FS_TYPE=bdb.
%set_verify_elf_method unresolved=relaxed
%def_without doc
%def_disable static

%def_enable sqlite_external
%def_with server
%def_with dav
%ifarch %arm
%def_without javahl
%else
%def_with javahl
%endif
%def_with swig_py
%def_with swig_pl
%def_with kwallet
%def_with gnome_keyring
# Temporarily disbled due to fail on x86_64
%def_without swig_rb
# Note: this spec does not have support for building with swig_java
%def_without swig_java

# Global switch to enable/diable all tests
%def_disable check
# Use these switches to selectively turn on/off some of tests
# These make sence only if tests enabled
%def_with fsfs_check
%def_with bdb_check
%def_with pl_check
%def_without rb_check
%def_with javahl_check

%define check_lops 5

%define svn_ver_pre %nil
%define svn_rel alt1

# for %%libdb_soname_req macros
%define apr_name libapr1
%define apr_ver 1.4.6-alt0.M60P.1
%define apu_name libaprutil1
%define apu_ver 1.5.1-alt0.M60P.1

# solo's macros for full libdb version to point it in requires
# set %%libdb_soname_req (for Requires: <libname>-libdb = %%libdb_soname_req)
%define libdb_soname_req 4%(rpm -q --whatprovides libdb4-devel | sed -r 's/^libdb4(\\.[^-]+)-devel-.+$/\\1/')

%define svn_user subversion
%define svn_group subversion
%define svn_repo_dir %_localstatedir/subversion
%define svn_service svnserve

%define module_name dav_svn
%define modname dav_svn_module

Name:     subversion
Version:  1.14.1
Release:  alt1

Summary:  A version control system
Group:    Development/Other
License:  Apache-2.0
Url:      http://subversion.apache.org/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source:  %name-%version%svn_ver_pre.tar.bz2
Source1: %name.el
Source2: %name-config-1.4.0.tar
Source3: svnserve.init
Source4: svnserve.sysconfig
Source5: %module_name.conf
Source6: svnwrapper

Source9: %module_name.load
Source10: %module_name.start

Source11: sqlite3-amalgamation-3.6.11.c

Patch4: %name-1.5.4-alt-perl-DESTROY.patch
Patch5: %name-1.9.2-alt-custom-libtool.patch
Patch6: %name-1.9.2-alt-kwallet-build.patch

# http://bugs.gentoo.org/show_bug.cgi?id=219959
Patch16: %name-1.6.0-gentoo-java-headers.patch

# http://svn.haxx.se/dev/archive-2008-07/0494.shtml
Patch17: %name-1.6.6-deb-ssh-no-controlmaster.patch

# Patches from Fedora
Patch20: subversion-1.13.0-rpath.patch
Patch21: subversion-1.13.0-pie.patch
Patch22: subversion-1.8.0-rubybind.patch
Patch23: subversion-1.8.5-swigplWall.patch

Requires: lib%name = %version-%release

# Automatically added by buildreq on Mon Nov 03 2008
BuildRequires: libcom_err-devel zlib-devel libexpat-devel

# unconditionally need by configure
BuildRequires: libapr1-devel >= %apr_ver
BuildRequires: libaprutil1-devel >= %apu_ver

# it is not nesessary for simple build, but dav require this
BuildRequires: libneon-devel libkeyutils-devel

BuildRequires: libserf-devel
BuildRequires: libsasl2-devel
BuildRequires: libsecret-devel
BuildRequires: liblz4-devel
BuildRequires: libutf8proc-devel
BuildRequires: patchelf
BuildRequires: python3-base

# since 1.6.0 subversion requires sqlite
# if sqlite_external is enabled subversion will be linked with system's sqlite
# else subversion will use sqlite-amalgamation ($SOURCE9)
%{?_enable_sqlite_external:BuildRequires: libsqlite3-devel >= 3.4.0}
%{?_enable_static:BuildRequires(pre): glibc-devel-static}
%{?_with_gnome_keyring:BuildRequires: libdbus-devel libgnome-keyring-devel}
%{?_with_kwallet:BuildRequires: gcc-c++ libdbus-devel kf5-kdelibs4support qt5-base-devel kf5-kwallet-devel kf5-ki18n-devel kf5-kcoreaddons-devel}
%{?_with_swig_py:BuildRequires(pre): swig rpm-build-python3 python3-devel py3c-devel}
%{?_with_swig_pl:BuildRequires(pre): swig perl-devel perl(PerlIO.pm)}
%{?_with_swig_rb:BuildRequires(pre): swig libruby-devel}
%{?_with_javahl:BuildRequires(pre): gcc-c++ junit java-devel-default /proc}
%{?_with_dav:BuildRequires(pre): apache2-devel}

# For tests
BuildRequires: python3-modules-sqlite3

%add_findprov_lib_path %_libdir/libsvn_swig

%description
The goal of the Subversion project is to build a revision system that is
a compelling replacement for CVS in the open community.  The software is
released under an Apache/BSD-style source license.  See the status page
for current progress.
This package contains command-line subversion utilities: svn and
svnversion. For more utilities please look for package
subversion-server-common.

%package -n lib%name
Summary: Shared libraries required for subversion
Group: System/Libraries
Requires: %apr_name >= %apr_ver
Requires: %apu_name >= %apu_ver
Requires: libaprutil1-libdb = %libdb_soname_req

%description -n lib%name
The goal of the Subversion project is to build a revision system that is
a compelling replacement for CVS in the open community.  The software is
released under an Apache/BSD-style source license.  See the status page
for current progress.

%package -n lib%name-devel
Summary: Development files for applications which will use subversion libraries
Group: Development/C
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release
%{?_with_kwallet:Requires: lib%name-auth-kwallet = %version-%release}
%{?_with_gnome_keyring:Requires: lib%name-auth-gnome-keyring = %version-%release}
Requires: %apr_name-devel >= %apr_ver
Requires: %apu_name-devel >= %apu_ver
Requires: libneon-devel

%description -n lib%name-devel
The goal of the Subversion project is to build a revision system that is
a compelling replacement for CVS in the open community.  The software is
released under an Apache/BSD-style source license.  See the status page
for current progress.

%package -n lib%name-devel-static
Summary: Static libraries for developing statically linked applications which will use subversion libraries
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
The goal of the Subversion project is to build a revision system that is
a compelling replacement for CVS in the open community.  The software is
released under an Apache/BSD-style source license.  See the status page
for current progress.

%package -n lib%name-auth-kwallet
Summary: KDE5 KWallet auth module
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-auth-kwallet
The goal of the Subversion project is to build a revision system that is
a compelling replacement for CVS in the open community.  The software is
released under an Apache/BSD-style source license.  See the status page
for current progress.

This package contains the KDE5 KWallet auth module.

%package -n lib%name-auth-gnome-keyring
Summary: Gnome Keyring auth module
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-auth-gnome-keyring
The goal of the Subversion project is to build a revision system that is
a compelling replacement for CVS in the open community.  The software is
released under an Apache/BSD-style source license.  See the status page
for current progress.

This package contains the Gnome Keyring auth module.

%if_with swig_py
%package python3
Summary: Pyhton bindings for Subversion
Group: Development/Other
Requires: lib%name = %version-%release

%description python3
The goal of the Subversion project is to build a revision system that is
a compelling replacement for CVS in the open community.  The software is
released under an Apache/BSD-style source license.  See the status page
for current progress.
This package contains the files necessary to use the subversion library
functions within python scripts.
%endif

%if_with swig_pl
%package perl
Summary: Perl bindings for Subversion
Group: Development/Other
Requires: lib%name = %version-%release

# The following dependecies where found before 'relaxed' _perl_req_method:
#   perl(File/Temp.pm)
#   perl(IO/Handle.pm)
#   perl(Symbol.pm)
#   perl(overload.pm)
#   perl(warnings.pm) - still found automatically
# Now we need to specify dependencies manually (except thouse still found automatically)
Requires: perl(File/Temp.pm)
Requires: perl(IO/Handle.pm)
Requires: perl(Symbol.pm)
Requires: perl(overload.pm)

%description perl
The goal of the Subversion project is to build a revision system that is
a compelling replacement for CVS in the open community.  The software is
released under an Apache/BSD-style source license.  See the status page
for current progress.
This package contains the files necessary to use the subversion library
functions within perl scripts.
%endif

%if_with swig_rb
%package ruby
Summary: Ruby bindings for Subversion
Group: Development/Other
Requires: lib%name = %version-%release

%description ruby
The goal of the Subversion project is to build a revision system that is
a compelling replacement for CVS in the open community.  The software is
released under an Apache/BSD-style source license.  See the status page
for current progress.
This package contains the files necessary to use the subversion library
functions within ruby scripts.
%endif

%if_with swig_java
%package java
Summary: Java bindings for Subversion
Group: Development/Other
Requires: lib%name = %version-%release
%endif

%if_with javahl
%package javahl
Summary: JavaHL bindings for Subversion
Group: Development/Other
Requires: lib%name = %version-%release

%description javahl
The goal of the Subversion project is to build a revision system that is
a compelling replacement for CVS in the open community.  The software is
released under an Apache/BSD-style source license.  See the status page
for current progress.
This package contains the files necessary to use the subversion library
functions within java.
%endif

%package doc
Summary: Subversion documentation
Group: Books/Other

%description doc
This package contains subversion documentation:
+ the "Version Control with Subversion" book,
+ documents for Subversion programmers,
+ documents for Subversion users.

%package server-common
Summary: Common files required to maintain subversion server
Group: System/Servers
Requires: lib%name = %version-%release

%description server-common
The goal of the Subversion project is to build a revision system that is
a compelling replacement for CVS in the open community.  The software is
released under an Apache/BSD-style source license.  See the status page
for current progress.
This package contains common files required for maintaing subversion
repositories.

%package server-standalone
Summary: Subversion standalone server
Group: System/Servers
Requires: %name-server-common = %version-%release
Requires: /bin/su
BuildArch: noarch

%description server-standalone
The goal of the Subversion project is to build a revision system that is
a compelling replacement for CVS in the open community.  The software is
released under an Apache/BSD-style source license.  See the status page
for current progress.
This package contains scripts for running standalone subversion server.

%package server-dav
Summary: Subversion server module for Apache
Group: System/Servers
Requires: %name-server-common = %version-%release

%description server-dav
The goal of the Subversion project is to build a revision system that is
a compelling replacement for CVS in the open community.  The software is
released under an Apache/BSD-style source license.  See the status page
for current progress.
This package contains the apache2 server shared module for running
subversion server.

%prep
%setup -q -n %name-%version%svn_ver_pre
%if_disabled sqlite_external
install -pD -m644 %SOURCE11 sqlite-amalgamation/sqlite3.c
%endif

%patch4 -p1
%patch5 -p2
#patch6 -p2
%patch16 -p1
%patch17 -p2
%patch20 -p1
%patch21 -p2
%patch22 -p1
%patch23 -p1

%build
%add_optflags %optflags_shared
%if_with kwallet
export KDE_CONFIG=%_libexecdir/kf5/bin/kf5-config
%add_optflags -L%_libdir/kf5/devel
%endif
export PYTHON=%__python3
LIBTOOL_M4=%{_datadir}/libtool/aclocal ./autogen.sh
%autoreconf
%configure \
        %{subst_enable static} --enable-shared \
	--disable-debug \
	--disable-mod-activation \
        --with-custom-libtool=/usr/bin/libtool \
        --with-berkeley-db=db.h:/usr/include/db4:%_libdir:db-4 \
        --with-apr=%prefix --with-apr-util=%prefix \
	--with-apache-libexecdir=%apache2_moduledir \
	--with-swig --with-serf=%prefix \
	--with-sasl \
        %{?_with_gnome_keyring:--with-gnome-keyring} \
        %{subst_with kwallet} \
        %{?_with_dav:--with-apxs=%apache2_apxs} \
        %{?_with_swig_rb:RUBY='%ruby_vendor' --with-ruby-sitelibdir=%ruby_sitelibdir --with-ruby-sitearchdir=%ruby_sitearchdir} \
        %{?_with_javahl:--enable-javahl --with-jdk=/usr/lib/jvm/java --with-jikes=no --with-junit=/usr/share/java/junit.jar} \
        %{!?_with_javahl:--disable-javahl}

%make_build

%if_with swig_py
%make_build libdir=%_libdir/libsvn_swig swig_pydir=%python3_sitelibdir/libsvn swig_pydir_extra=%python3_sitelibdir/svn swig-py
%endif

%if_with swig_pl
%make_build libdir=%_libdir/libsvn_swig swig-pl-lib
%make_build libdir=%_libdir/libsvn_swig autogen-swig-pl

SVN_VER_MAJOR=`awk '/^#define SVN_VER_MAJOR/ {print $3}' subversion/include/svn_version.h`
SVN_VER_MINOR=`awk '/^#define SVN_VER_MINOR/ {print $3}' subversion/include/svn_version.h`
SVN_VER_PATCH=`awk '/^#define SVN_VER_PATCH/ {print $3}' subversion/include/svn_version.h`

pushd subversion/bindings/swig/perl/native
# This does not work (libraries are being build with RPATH entries, #9307)
#%%perl_vendor_build all

perl Makefile.PL INSTALLDIRS=vendor PREFIX=%_prefix
sed -i 's|^\(LD_RUN_PATH =\).*|\1 %_libdir/libsvn_swig|' Makefile Makefile.[a-z]*
%make_build libdir=%_libdir/libsvn_swig all

sed -i "s/\$SVN::Core::VERSION = .*/\$SVN::Core::VERSION = '$SVN_VER_MAJOR.$SVN_VER_MINOR.$SVN_VER_PATCH';/" Core.pm

popd
%endif

%if_with swig_rb
%make_build libdir=%_libdir/libsvn_swig swig-rb
%endif

%if_with javahl
# -j16: java.lang.OutOfMemoryError: unable to create new native thread
#make_build javahl
make javahl
%endif

%if_with doc
# Build subversion documentation
%make XSL_DIR=/usr/share/xml/docbook/xsl-stylesheets \
    doc-all-html doc-all-info

doxygen doc/doxygen.conf
%endif

# Add shebang for python3 executable
subst 's|#!.*python$|#!%__python3|' $(grep -Rl '#!.*python$' *)

%check
# Running tests
%if_enabled check

# There is a workaround to run tests in a chrooted environment
# We need to set LD_LIBRARY_PATH to make all tests executed successfuly
PWD=`pwd`
LDLP=`find subversion -type d -name .libs|while read dir; do echo "$PWD/$dir"; done|xargs echo|tr ' ' ':'`

# Perform generic tests against bdb and fsfs
run_make_check(){
	fs_type=$1
	for ((i=1; i <= %check_lops ; i++))
	do
		LD_LIBRARY_PATH="$LDLP" %make FS_TYPE=$fs_type CLEANUP=true check && return 0 ||:
	done
	exit 1
}

%if_with fsfs_check
run_make_check fsfs
%endif

%if_with bdb_check
run_make_check bdb
%endif

%if %with swig_pl && %with pl_check
LD_LIBRARY_PATH="$LDLP" %make check-swig-pl
%endif

%if %with swig_rb && %with rb_check
LD_LIBRARY_PATH="$LDLP" %make check-swig-rb
%endif

# Perform JavaHL tests
%if %with javahl && %with javahl_check
LD_LIBRARY_PATH="$LDLP" %make JAVA_CLASSPATH=%_javadir/junit.jar check-javahl
%endif

%endif # enabled check

%install
# Setting to relaxed untill #9307 resolved
# The following dependecies where found before 'relaxed':
#   perl(File/Temp.pm)
#   perl(IO/Handle.pm)
#   perl(Symbol.pm)
#   perl(overload.pm)
#   perl(warnings.pm)
%set_perl_req_method relaxed

%make_install DESTDIR=%buildroot INSTALL_LOCALE='install -p -m644 -D' install
mkdir -p %buildroot%_sysconfdir/%name
tar -xf %SOURCE2 -C %buildroot%_sysconfdir/%name

use_svnwrapper()
{
	local destbindir=%buildroot%_bindir
	local target=$1
	local suffix=".bin"
	local wrappername="svnwrapper"
	mv "$destbindir/$target" "$destbindir/$target$suffix"
	ln -s "$wrappername" "$destbindir/$target"
}

# Installing svnwrapper
cp %SOURCE6 %buildroot%_bindir
# Making svnserve to use svnwrapper
# Do not forget to update %%files section if using wrappers for other binaries
use_svnwrapper svnserve
#use_svnwrapper svn
#use_svnwrapper svnadmin

# Create directory for libsvn_swig libraries
mkdir -p %buildroot%_libdir/libsvn_swig

%if_with swig_py
%make_install DESTDIR=%buildroot libdir=%_libdir/libsvn_swig swig_py_libdir=%_libdir/libsvn_swig \
    swig_pydir=%python3_sitelibdir/libsvn swig_pydir_extra=%python3_sitelibdir/svn install-swig-py
rm -f %buildroot%_libdir/libsvn_swig/libsvn_swig_py*.la
cp -r %_builddir/%buildsubdir/subversion/bindings/swig/python/svn %buildroot%python3_sitelibdir
%endif

%if_with swig_pl
%make_install DESTDIR=%buildroot PREFIX=%_prefix INSTALLSITEARCH=%perl_vendor_archlib libdir=%_libdir/libsvn_swig swig_pl_libdir=%_libdir/libsvn_swig install-swig-pl
rm -f %buildroot%_libdir/libsvn_swig/libsvn_swig_pl*.la
%endif

%if_with swig_rb
%make_install DESTDIR=%buildroot swig_rb_libdir=%_libdir/libsvn_swig install-swig-rb
rm -f %buildroot%ruby_sitearchdir/svn/ext/*.la
rm -f %buildroot%_libdir/libsvn_swig/libsvn_swig_ruby*.la
%endif

%if_with swig_java
%make_install DESTDIR=%buildroot install-swig-java
%endif

# Installing javahl bindings
%if_with javahl
%make_install DESTDIR=%buildroot \
	javahl_javadir=%_javadir javahl_javahdir=%_includedir/svn-javahl \
	install-javahl
%endif

%if_with doc
# Installing subversion-doc files
%make_install DESTDIR=%buildroot install-docs
#%make_install XSL_DIR=/usr/share/xml/docbook/xsl-stylesheets \
#    INSTALL_DIR=%buildroot%docdir/doc/book \
#    -C doc/book install-misc-html
%make_install INSTALL_DIR=%buildroot%docdir/ -C ./doc install-misc-html

mkdir -p %buildroot%docdir/book/
#bzip2 -qc9 doc/book/book/book.ps >%buildroot%docdir/doc/book/book.ps.bz2
# TODO: svn-book.{pdf,html} temporary disabled (Hope, until release)
#install -p -m644 doc/book/svn-book.pdf %buildroot%docdir/book/
#install -p -m644 doc/book/svn-book.html %buildroot%docdir/book/
cp -r doc/user %buildroot%docdir/
cp doc/README %buildroot%docdir/DOCS.README
mkdir -p %buildroot%docdir/programmer/design
install -pm644 doc/programmer/*.txt %buildroot%docdir/programmer/
install -pm644 doc/programmer/design/*.html %buildroot%docdir/programmer/design/
#cp -r doc/translations %buildroot%docdir/

install -m644 doc/programmer/design/*.info* %buildroot%_infodir/

# Install API docs
#mkdir %buildroot%docdir/api
cp -r doc/doxygen/html/ %buildroot%docdir/api
%endif

%if_with server
# Installing subversion-server files
mkdir -p %buildroot%svn_repo_dir
mkdir -p %buildroot%_sysconfdir/rc.d/init.d %buildroot%_sysconfdir/sysconfig
install -pm755 %SOURCE3 %buildroot%_sysconfdir/rc.d/init.d/%svn_service
install -pm644 %SOURCE4 %buildroot%_sysconfdir/sysconfig/%svn_service

%if_with dav
install -d -m755 -- %buildroot%apache2_mods_available
install -d -m755 -- %buildroot%apache2_mods_start
install -p -m644 -- %SOURCE9 %buildroot%apache2_mods_available/%module_name.load
install -p -m644 -- %SOURCE5 %buildroot%apache2_mods_available/%module_name.conf
sed -i 's,@a_libexecdir@,%apache2_libexecdir,g' %buildroot%apache2_mods_available/%module_name.load
install -pm644 -- %SOURCE10 %buildroot%apache2_mods_start/100-%module_name.conf

%endif
%endif

# Installing bash-completion file
mkdir -p %buildroot/etc/bash_completion.d
install -pm644 tools/client-side/bash_completion %buildroot/etc/bash_completion.d/svn

# Remove alsolute pathes from RPATH in Perl libraries
%if_with swig_pl
patchelf --set-rpath %_libdir/libsvn_swig %buildroot%perl_vendor_archlib/auto/SVN/*/*.so
%endif

# Remove wrong pkgconfig files
rm -fr %buildroot%_datadir/pkgconfig

%find_lang %name

%pre server-common
/usr/sbin/groupadd -r -f %svn_group
/usr/sbin/useradd -r -g %svn_group -d %svn_repo_dir -s /dev/null -c 'Subversion' %svn_user >/dev/null 2>&1 ||:
if [ $1 -gt 1 ]; then
	/usr/sbin/usermod -d %svn_repo_dir %svn_user
fi

%post server-standalone
%post_service %svn_service

%preun server-standalone
%preun_service %svn_service

%if_with dav
%post server-dav
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:

if [ -e %apache2_mods_enabled/%module_name.load ]; then
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
        service %apache2_dname condrestart ||:
    else
        echo "Some errors detected in Apache2 configuration!"
        echo "To use %modname check configuration and start %apache2_dname service."
    echo
    fi
else
    echo "Apache2 %modname module had been installed, but does't enabled."
    echo "Check %apache2_mods_start directory for files with '%module_name=no' lines."
    echo
fi

%preun server-dav
if [ "$1" = "0" ] ; then # last uninstall
    [ -e %apache2_mods_enabled/%module_name.load ] && %apache2_sbindir/a2dismod %module_name 2>&1 >/dev/null ||:
fi


%postun server-dav
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:
if [ "$1" = "0" ] ; then # last uninstall
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
	service %apache2_dname condrestart ||:
    else
        echo "Some errors detected in Apache2 configuration!"
	echo "To complete %module_name uninstalling check configuration and restart %apache2_dname service."
	echo
    fi
fi
%endif

%files -f %name.lang
%doc BUGS CHANGES COMMITTERS INSTALL LICENSE NOTICE README
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/config
%config(noreplace) %_sysconfdir/%name/servers
%_sysconfdir/%name/README.txt
%_bindir/svn
%_bindir/svnversion
%_bindir/svnrdump
%_bindir/svnsync
%_bindir/svnbench
%_bindir/svnfsfs
%_bindir/svnmucc
%_man1dir/svn.1.*
%_man1dir/svnversion.1.*
%_man1dir/svnrdump.1*
%_man1dir/svnsync.1.*
%_man1dir/svnmucc.1.*
%_sysconfdir/bash_completion.d/svn

%files -n lib%name
%_libdir/libsvn_*-*.so.*
%dir %_libdir/libsvn_swig
%exclude %_libdir/libsvn_auth*

%files -n lib%name-devel
%_libdir/libsvn_*-*.so
%_includedir/%name-1
%exclude %_libdir/libsvn_swig*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/libsvn_*.a
%endif

%if_with gnome_keyring
%files -n lib%name-auth-gnome-keyring
%_libdir/libsvn_auth_gnome_keyring-1.so.*
%endif

%if_with kwallet
%files -n lib%name-auth-kwallet
%_libdir/libsvn_auth_kwallet-1.so.*
%endif

%if_with swig_py
%files python3
%_libdir/libsvn_swig/libsvn_swig_py*.so.*
%python3_sitelibdir/svn
%python3_sitelibdir/libsvn
%endif

%if_with swig_pl
%files perl
%_libdir/libsvn_swig/libsvn_swig_perl*.so.*
%perl_vendor_archlib/SVN
%perl_vendor_autolib/SVN
%endif

%if_with swig_rb
%files ruby
%_libdir/libsvn_swig/libsvn_swig_ruby*.so.*
%dir %ruby_sitelibdir/svn/
%ruby_sitelibdir/svn/*.rb
%dir %ruby_sitearchdir/svn/
%dir %ruby_sitearchdir/svn/ext/
%ruby_sitearchdir/svn/ext/*.so
%endif

%if_with swig-java
%files java
%endif

%if_with javahl
%files javahl
%_libdir/libsvnjavahl*.so*
%_javadir/svn-javahl.jar
%endif

%if_with doc
%files doc
%_infodir/svn-design*
%docdir/DOCS.README
%docdir/book
%docdir/misc-docs
%docdir/programmer
%docdir/user
%docdir/api
%endif

%if_with server
%files server-common
%_bindir/svnserve*
%_bindir/svnadmin
%_bindir/svnlook
%_bindir/svndumpfilter
%_bindir/svnwrapper
%_mandir/man1/svnadmin.1.*
%_mandir/man1/svnlook.1.*
%_mandir/man1/svndumpfilter.1.*
%_mandir/man5/svnserve.conf.5.*
%_mandir/man8/svnserve.8.*
%defattr(640,%svn_user,%svn_group,2710)
%dir %svn_repo_dir

%files server-standalone
%_sysconfdir/rc.d/init.d/%svn_service
%config(noreplace) %_sysconfdir/sysconfig/%svn_service

%if_with dav
%files server-dav
%apache2_libexecdir/*.so
%config(noreplace) %apache2_mods_available/%module_name.conf
%config            %apache2_mods_available/%module_name.load
%config            %apache2_mods_start/100-%module_name.conf
%endif
%endif

%changelog
* Sun Feb 14 2021 Andrey Cherepanov <cas@altlinux.org> 1.14.1-alt1
- New version.
- Fixes:
  + CVE-2020-17525 Remote unauthenticated denial-of-service in Subversion mod_authz_svn

* Sat May 30 2020 Andrey Cherepanov <cas@altlinux.org> 1.14.0-alt1
- New version.
- Build subversion-python3, support for Python 2.x is removed.

* Sun Mar 29 2020 Andrey Cherepanov <cas@altlinux.org> 1.13.0-alt1
- New version (ALT #36518).
- Build with KWallet from KDE5.
- Fix License tag according to SPDX.

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.9.2-alt3.3
- rebuild with new perl 5.28.1

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.2-alt3.2.1
- rebuild with new perl 5.26.1

* Mon Dec 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.2-alt3.2
- NMU: a hack for 16-jobs nodes

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.2-alt3.1
- rebuild with new perl 5.24.1

* Tue Apr 05 2016 Andrey Cherepanov <cas@altlinux.org> 1.9.2-alt3
- Rebuild with new apache2

* Thu Dec 17 2015 Andrey Cherepanov <cas@altlinux.org> 1.9.2-alt2
- Build with SASL support

* Mon Nov 30 2015 Andrey Cherepanov <cas@altlinux.org> 1.9.2-alt1
- New version

* Sat Nov 28 2015 Igor Vlasenko <viy@altlinux.ru> 1.8.13-alt2
- enabled javahl again

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.8.13-alt1.1.1
- rebuild with new perl 5.22.0

* Mon Nov 23 2015 Igor Vlasenko <viy@altlinux.ru> 1.8.13-alt1.1
- disabled javahl for perl 5.22 update - to enable again

* Mon Aug 03 2015 Andrey Cherepanov <cas@altlinux.org> 1.8.13-alt1
- New version 1.8.13 (ALT #29846)

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.8-alt2.1
- rebuild with new perl 5.20.1

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 1.7.8-alt2
- built for perl 5.18

* Wed Feb 27 2013 Andrey Cherepanov <cas@altlinux.org> 1.7.8-alt1
- New version 1.7.8
- Disable svn-push and emacs support
- Remove all contrib tools

* Mon Dec 03 2012 Aleksey Avdeev <solo@altlinux.ru> 1.6.19-alt1
- updated to 1.6.19

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 1.6.17-alt2
- rebuilt for perl-5.16

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.17-alt1.1.1
- Rebuild with Python-2.7

* Sun Oct 16 2011 Alexey Tourbin <at@altlinux.ru> 1.6.17-alt1.1
- rebuilt for perl-5.14

* Wed Jul 20 2011 Dmitry V. Levin <ldv@altlinux.org> 1.6.17-alt1
- Updated to 1.6.17 (fixes CVE-2011-1752, CVE-2011-1783 and CVE-2011-1921
  in mod_dav_svn).
- Packaged some subpackages as noarch.

* Thu Apr 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.16-alt1
- 1.6.16
- CVE-2011-0715

* Thu Apr 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.13-alt2
- repair build

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.6.13-alt1.1
- rebuilt with perl 5.12

* Tue Oct 19 2010 Afanasov Dmitry <ender@altlinux.org> 1.6.13-alt1
- updated to 1.6.13 (CVE-2010-3315, closes: #24284)

* Mon May 31 2010 Afanasov Dmitry <ender@altlinux.org> 1.6.11-alt1
- updated to 1.6.11
- pass svn options through sysconfig file (closes: #23545)

* Wed Feb 24 2010 Afanasov Dmitry <ender@altlinux.org> 1.6.9-alt1
- updated to 1.6.9

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.6-alt2.1
- Rebuilt with python 2.6

* Sat Nov 21 2009 Afanasov Dmitry <ender@altlinux.org> 1.6.6-alt2
- disable JavaHL bindings on ARM.

* Tue Nov 17 2009 Afanasov Dmitry <ender@altlinux.org> 1.6.6-alt1
- Updated to 1.6.6

* Tue Aug 18 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.4-alt1
- Updated to 1.6.4 (CVE-2009-2411; closes: #21097).

* Tue Jun 23 2009 Afanasov Dmitry <ender@altlinux.org> 1.6.3-alt1
- updated to 1.6.3
- detect db4 manually till #20467 will be closed

* Tue Jun 16 2009 Afanasov Dmitry <ender@altlinux.org> 1.6.2-alt1
- updated to 1.6.2

* Tue Jun 16 2009 Afanasov Dmitry <ender@altlinux.org> 1.6.0-alt4
- remove obsolete install_info invocations

* Mon May 25 2009 Afanasov Dmitry <ender@altlinux.org> 1.6.0-alt3
- update kwallet patch to fix build with changed after 4.2.3-alt2 kde4
  link path. patch must be rewritten to accept kde4 macroses.

* Tue Apr 28 2009 Afanasov Dmitry <ender@altlinux.org> 1.6.0-alt2
- backport patch from main svn repository for customizing libtool calling. it
  also fixes build with libtool 2.2.
- build kwallet and gnome-keyring auth modules
  + make patch to fix kwallet detection on ALT
  + define macroses for conditional build
  + move modules to separate packages
- spec cleanup

* Tue Mar 24 2009 Afanasov Dmitry <ender@altlinux.org> 1.6.0-alt1
- updated to 1.6.0
- remove old patches:
  + deb-swig (not used)
  + alt-libsvn_swig-install (not used)
  + alt-linkage-libdb (not used)
  + alt-perl-DESTROY (not used)
  + alt-M24-bdb.patch (not used)
  + deb-out-of-tree-build-fixes (apllied by upstream)
  + alt-linkage-neon (pkg-config is used)
- update gentoo-java-headers
- build with with exterlal sqlite (since this version
  subversion requires sqlite)

* Mon Mar 09 2009 Afanasov Dmitry <ender@altlinux.org> 1.5.6-alt2
- add requires for PerlIO.pm to fix build

* Sat Feb 28 2009 Afanasov Dmitry <ender@altlinux.org> 1.5.6-alt1
- updated to 1.5.6

* Thu Jan 15 2009 Afanasov Dmitry <ender@altlinux.org> 1.5.5-alt2
- fix ssh ControlMaster problem (workaround, closes #18513)
- apply debian patches:
  + ssh-no-controlmaster (closes #18513)
  + out-of-tree-build-fixes

* Wed Dec 24 2008 Afanasov Dmitry <ender@altlinux.org> 1.5.5-alt1
- updated to 1.5.5.

* Fri Dec 12 2008 Afanasov Dmitry <ender@altlinux.org> 1.5.4-alt3
- substitute SVN::Core::VERSION value with a plain version (partially
  closes: #11936).

* Thu Dec 11 2008 Afanasov Dmitry <ender@altlinux.org> 1.5.4-alt2
- change jdk path to /usr/lib/jvm/java
- remove ldconfig calls (obsoleted by filetriggers)

* Mon Nov 01 2008 Afanasov Dmitry <ender@altlinux.org> 1.5.4-alt1
- Updated to 1.5.4
- Remove old patches
- Remove some configure options (e.g. dso, rpath)
- Replace old macroses by new one
- Apply gentoo patch to fix javahl build
- Update buildreq's
- Write /bin/su dependency (#11904)

* Sat Nov 01 2008 Aleksey Avdeev <solo@altlinux.ru> 1.4.4-alt2.3.2
- NMU
- Use java-devel-default for build

* Fri Oct 31 2008 Aleksey Avdeev <solo@altlinux.ru> 1.4.4-alt2.3.1
- NMU
- Add requires libaprutil1-libdb = %%libdb_soname_req in lib%%name subpacage
- Add use java-1.5.0-sun-devel for fix build

* Tue Sep 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.4-alt2.3
- fixed requires for lib%name-devel

* Tue Jun 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.4-alt2.2
- rebuild with libneon.so.27

* Thu Feb 14 2008 Grigory Batalov <bga@altlinux.ru> 1.4.4-alt2.1
- Rebuilt with python-2.5.

* Thu Feb 14 2008 Grigory Batalov <bga@altlinux.ru> 1.4.4-alt2
- Don't require exact python-devel and j2se-devel versions.

* Sun Jun 10 2007 Sviatoslav Sviridov <svd@altlinux.ru> 1.4.4-alt1
- Updated to 1.4.4

* Thu Apr 19 2007 Sviatoslav Sviridov <svd@altlinux.ru> 1.4.3-alt3
- Merged changes from Alexey Morsov to support apache2.2 configuration
  scheme
- dav_svn.load: added dependency to dav module

* Tue Apr 03 2007 Alexey Morsov <swi@altlinux.ru> 1.4.3-alt2.1
- Switch to new apache2 scheme
- fix libdir for jdk (why on x86_64 it's in /usr/lib ?)

* Sun Feb 25 2007 Sviatoslav Sviridov <svd@altlinux.ru> 1.4.3-alt2
- Rebuilt with libapr1/libaprutil1 (required to build with apache 2.2)
- Added dependence: libsubversion-devel requires libaprutil1-devel

* Fri Jan 26 2007 Sviatoslav Sviridov <svd@altlinux.ru> 1.4.3-alt1
- Updated to 1.4.3
- Installed manpage for svnsync(1)

* Sun Dec 10 2006 Sviatoslav Sviridov <svd@altlinux.ru> 1.4.2-alt1
- Updated to 1.4.2

* Tue Nov 07 2006 Sviatoslav Sviridov <svd@altlinux.ru> 1.4.0-alt3
- Added libneon0.25-devel to requires list for libsubversion-devel (#10191)

* Sun Oct 29 2006 Sviatoslav Sviridov <svd@altlinux.ru> 1.4.0-alt2
- Updated subversion-config
- subversion-server-dav now requires apache2-libdb=4.4 instead of
  just apache2
- Updated build requirements for subversion-server-dav:
  BuildPreReq: apache2-devel >= 2.0.59-alt2

* Sat Oct 21 2006 Sviatoslav Sviridov <svd@altlinux.ru> 1.4.0-alt1
- Updated to 1.4.0
- Built with libdb 4.4
- Updated patches
  + alt-linkage-neon
  + alt-linkage-libdb
- Disabled patches
  + alt-bdb (it is able to compile without this patch)
  + alt-gen_make (probably requires update)
  + alt-quote-filenames (probably requires update)
  + alt-buildconf (probably requires update)
  + deb-swig-1.3.27 (probably not needed)
  + alt-configure-swig-ruby (probably requires update)
- New 'svnsync' commandline tool for repository replication is included
  into subversion package
- Updated subversion-tools package
  + removed svncopy.pl
  + added svn-resolve
  + added svn-viewdiff
  + added hook-script: enforcer
- Used vc-svn.el included with subversion package instead of external one

* Tue Oct 10 2006 Grigory Batalov <bga@altlinux.ru> 1.3.1-alt2
- autogen.sh call was commented out.
- Patches for configure.in and *.m4 were updated:
  + subversion-1.3.1-alt-bdb.patch
  + subversion-1.3.1-alt-configure-swig-ruby.patch
  + subversion-1.3.1-alt-libdb-linkage.patch
  + subversion-1.3.1-alt-linkage-neon.patch
- INSTALL_LOCALE was redefined with -D to create leading directories.

* Sun Apr 09 2006 Sviatoslav Sviridov <svd@altlinux.ru> 1.3.1-alt1
- 1.3.1 (official release)
- Added findprov_lib_path %%_libdir/libsvn_swig

* Fri Mar 31 2006 Sviatoslav Sviridov <svd@altlinux.ru> 1.3.1-alt0.6
- Changed BuildPreReq "j2se1.4-sun-devel" to "j2se-devel = 1.4.2"
  (fixes build on x86_64)
- Disabled build of subversion-ruby (failed to build on x86_64)

* Mon Mar 27 2006 Sviatoslav Sviridov <svd@altlinux.ru> 1.3.1-alt0.5
- Updated to 1.3.1 (release candidate, r19032)
- Do not use --enable-dso configuration option by default. This makes
  all tests passed successfuly. This option can be switched on by
  "--enable dso" option for rpmbuild
- Do not exclude 'repos_test' from list of tests for FS_TYPE=bdb
- Do not exclude '6ra' test from the list of tests for perl swig bindings
- Do no specify explicit dependency to libdb4-devel, implicit dependency
  is implied by aprutil-devel
- Added BuildRequires: libaprutil-devel >= 0.9.7-alt3 (libaprutil-devel with
  dependency to libdb4.3-devel)
- Set _perl_req_method to 'relaxed' (until #9307 resolved)
- Manually added requires to subversion-perl

* Tue Mar 21 2006 Sviatoslav Sviridov <svd@altlinux.ru> 1.3.1-alt0.4
- Added subversion-1.3.1-alt-libdb-linkage.patch
- Force configure script to find Berkley DB library by using
  SVN_DB_LIBS variable

* Sun Mar 19 2006 Sviatoslav Sviridov <svd@altlinux.ru> 1.3.1-alt0.3
- Added --with-berkeley-db option for configure script

* Sun Mar 19 2006 Sviatoslav Sviridov <svd@altlinux.ru> 1.3.1-alt0.2
- Updated vc-svn.el from trunk

* Tue Mar 14 2006 Sviatoslav Sviridov <svd@altlinux.ru> 1.3.1-alt0.1
- Updated to 1.3.1 (release candidate, r18866)

* Sat Jan 21 2006 Sviatoslav Sviridov <svd@altlinux.ru> 1.3.0-alt0.5
- Do not perform repos-test for FS_TYPE=bdb

* Mon Jan 16 2006 Sviatoslav Sviridov <svd@altlinux.ru> 1.3.0-alt0.4
- Applied patch for building with swig-1.3.27 (#8801)
- Added subversion-1.3.0-alt-configure-swig-ruby.patch

* Fri Dec 30 2005 Sviatoslav Sviridov <svd@altlinux.ru> 1.3.0-alt0.3
- Updated to 1.3.0

* Thu Dec 15 2005 Sviatoslav Sviridov <svd@altlinux.ru> 1.3.0-alt0.2
- Updated to 1.3.0-rc5

* Wed Nov 30 2005 Sviatoslav Sviridov <svd@altlinux.ru> 1.3.0-alt0.1
- Updated to 1.3.0-rc4
- Do not update load-path in subversion.el (#8406)
- /usr/share/emacs/site-lisp/subversion now belongs to emacs-subversion
  (#8407)
- Do no include svn-book into subversion-doc package (not a part of
  subversion tarball, see http://svnbook.red-bean.com/ instead)
- Building ruby bindings for subversion
- Updated alt-bdb patch (to require libdb4.3-4.3.29)
- Added scripts to subversion-tools
  + svn_all_diffs.pl
  + svn_apply_autoprops.py
  + svn_export_empty_files.py
- Changed scripts in subversion-tools
  + svnmerge replaced with svnmerge.py and svnmerge.sh
- Added --with-junit configure option

* Sat Nov 26 2005 Dmitry V. Levin <ldv@altlinux.org> 1.2.3-alt2.1
- Applied patch from Vladimir Lettiev to fix subversion-perl build.
- Enabled build of subversion-perl subpackage by default.

* Tue Oct 11 2005 Sviatoslav Sviridov <svd@altlinux.ru> 1.2.3-alt2
- /usr/bin/svnwrapper moved to package subversion-server-common (#8191)

* Sat Aug 27 2005 Sviatoslav Sviridov <svd@altlinux.ru> 1.2.3-alt1
- Updated to 1.2.3
- Updated alt-bdb patch

* Mon Aug 22 2005 Aleksey Avdeev <solo@altlinux.ru> 1.2.1-alt0.M24.1
- Backports for M24
- Updated BuildRequires
- Add alt-M24-bdb patch:
  + use bdb 4.2.52

* Tue Aug 16 2005 Sviatoslav Sviridov <svd@altlinux.ru> 1.2.1-alt1
- Updated to 1.2.1 (should fix #7657, #7658)
- Removed subversion-1.2.0-r14754-svnversion.patch (already in upstream)
- Do not build subversion-perl by default
- Fixed installation of svn-push

* Thu Jun 09 2005 Sviatoslav Sviridov <svd@altlinux.ru> 1.2.0-alt1
- Updated to 1.2.0
- Updated BuildRequires
- Updated configure options: added --enable-dso and --enable-shared to
  avoid linkage of libsvn_clien against libsvn_client_* and libsvn_fs
  against libsvn_fs_*
- Used vc-svn.el from subversion-1.1.4 (currently vc-svn.el is excluded
  from subversion repository and is located in FSF Emacs, but it is broken)
- Fixed build configuration (library dependencies for tests and svn-push)
- Rediffed alt-docbook patch
- Updated alt-bdb patch
- Performing javahl tests by default
- Temporary disabled perl bindings tests
- Backported svnversion fix (r14754)
- Reorganized subversion-doc:
  + svn-book packaged as single html file and as pdf file (svn-book sources
    no longer live in subversion repository, just compiled version provided)
  + packaged subversion API (generated with doxygen)
- Workaround used for running tests (setting LD_LIBRARY_PATH to let dlopen
  find required libraries)
- Updated system-wide config to current version
- Repackaged subversion-tools package:
  + executable scritpts installed into /usr/bin
  + not-working or not ready for use OOTB scripts installed into %_docdir
  + packaged svnindex.xsl and svnindex.css
  + packaged svn-push
  + new installation procedure for subversion-tools package (using separate
    makefile)
- New package introduced: bash-completion-svn
- libsubversion-devel now depens on libsubversion (#6755)
- Updated package description for 'subversion' (#6885)

* Tue Jun  7 2005 Sviatoslav Sviridov <svd@altlinux.ru> 1.2.0-alt0.3
- Repackaged subversion-tools package:
- Workaround used for running tests
- Updated system-wide config to current version
  + executable scritpts installed into /usr/bin
  + not-working or not ready for use OOTB scripts installed into %_docdir
  + packaged svnindex.xsl and svnindex.css
  + packaged svn-push
- New installation procedure for subversion-tools package: using separate makefile

* Tue May 31 2005 Sviatoslav Sviridov <svd@altlinux.ru> 1.2.0-alt0.2
- Updated BuildRequires
- Temporary disabled perl bindings tests
- Backported svnversion fix (r14754)
- Reorganized subversion-doc:
  + svn-book packaged as single html file and as pdf file (svn-book sources
    no longer live in subversion repository, just compiled version provided)
  + packaged subversion API (generated with doxygen)

* Mon May 30 2005 Sviatoslav Sviridov <svd@altlinux.ru> 1.2.0-alt0.1
- Updated to 1.2.0
- updated configure options: added --enable-dso and --enable-shared to
  avoid linkage of libsvn_clien against libsvn_client_* and libsvn_fs
  against libsvn_fs_*
- vc-svn.el managed as external resource since it it lives in FSF Emacs now
- Fixed build configuration (library dependencies for tests and svn-push)
- Rediffed alt-docbook patch
- Updated alt-bdb patch
- Performing javahl tests by default

* Thu Apr 07 2005 Sviatoslav Sviridov <svd@altlinux.ru> 1.1.4-alt2
- Fixed linkage for svn_swig libraries (#6426)

* Wed Apr 06 2005 Sviatoslav Sviridov <svd@altlinux.ru> 1.1.4-alt1
- Updated to 1.1.4
- Fixed initscript for svnserve (#6401)
- svnserve config marked as config(noreplace) (#6402)
- #6398 is no longer reproduced

* Tue Mar 15 2005 Sviatoslav Sviridov <svd@altlinux.ru> 1.1.3-alt2
- Rebuild with python 2.4

* Fri Feb 18 2005 Sviatoslav Sviridov <svd@altlinux.ru> 1.1.3-alt1.1
- Workaround for SMP build

* Tue Jan 25 2005 Sviatoslav Sviridov <svd@altlinux.ru> 1.1.3-alt1
- Updated to 1.1.3
- Updated build dependencies
- Updated alt-bdb patch
- Updated patch for svn_load_dir.pl
- Wrap svnserve with shell script that sets umask to 002 before running
  svnserve (#6113)
- Packaged JavaHL bindings (subversion-javahl)
- Purged included_apr staff

* Wed Dec 29 2004 Sviatoslav Sviridov <svd@altlinux.ru> 1.1.2-alt0.M24.3
- fixed dependencies on libapr (using version available in M24 backports
  for M24 branch)

* Mon Dec 27 2004 Sviatoslav Sviridov <svd@altlinux.ru> 1.1.2-alt0.M24.2
- Backport to 2.4 Master

* Mon Dec 27 2004 Sviatoslav Sviridov <svd@altlinux.ru> 1.1.2-alt2
- fixed packaging of subversion-python (included libsvn_swig_py*.so.*)

* Thu Dec 23 2004 Sviatoslav Sviridov <svd@altlinux.ru> 1.1.2-alt1
- Updated to 1.1.2
- Packaged language files
- Packaged more scripts in subversion-tools
- Packaged perl bindings (subversion-perl package)
- Applied patch to quote filenames in svn_load_dirs.pl
- subversion-server-dav:
  + added dependency to apache2
  + config created as A.subversion.conf (#5497)

* Sun Nov 14 2004 Sviatoslav Sviridov <svd@altlinux.ru> 1.1.1-alt1
- Updated to 1.1.1
- Updated default configuration in /etc/subversion

* Fri Oct 15 2004 Sviatoslav Sviridov <svd@altlinux.ru> 1.0.9-alt1
- Updated to 1.0.9

* Wed Sep 22 2004 Dmitry V. Levin <ldv@altlinux.org> 1.0.7-alt1
- Updated to 1.0.7.
- Applied patches from Ben Reser (CAN-2004-0749).

* Wed Aug 18 2004 Dmitry V. Levin <ldv@altlinux.org> 1.0.6-alt2
- Fixed build.
- Relocated documentation.
- Enabled RA_LOCAL tests by default.

* Wed Aug 04 2004 Sviatoslav Sviridov <svd@altlinux.ru> 1.0.6-alt1
- 1.0.6: security fix in mod_authz_svn
- requires neon >= 0.24.7 (fixes wire compression bugs)

* Fri Jun 11 2004 Sviatoslav Sviridov <svd@altlinux.ru> 1.0.5-alt1
- 1.0.5: fixed subversion svn:// protocol string parsing error
  (CAN-2004-0413)
- Added apache2 support
- Changed mode to 2710 for /var/lib/subversion
- Updated BuildRequires
- Do not build static library by default
- Spec cleanup: removed support for cvs2svn package

* Fri May 14 2004 Dmitry V. Levin <ldv@altlinux.org> 1.0.2-alt2
- Fixed subversion sscanf overflow (CAN-2004-0397).

* Wed May 12 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.2-alt1.1
- Rebuilt with openssl-0.9.7d.

* Thu Apr 29 2004 Sviatoslav Sviridov <svd@altlinux.ru> 1.0.2-alt1
- 1.0.2
- updated BuildRequires

* Mon Mar 15 2004 Sviatoslav Sviridov <svd@altlinux.ru> 1.0.1-alt1
- 1.0.1 (bugfix release)
- do not package cvs2svn (moved to its own repository),
  see http://cvs2svn.tigris.org/ for new location

* Mon Feb 23 2004 Sviatoslav Sviridov <svd@altlinux.ru> 1.0.0-alt1
- 1.0.0
- specfile updated:
  + do not package cvs2svn manpage (manpage was not included
    in 1.0.0 release)
  + new subpackage created: subversion-tools

* Fri Feb 20 2004 Sviatoslav Sviridov <svd@altlinux.ru> 0.37.0-alt3
- added new subpackages:
  subversion-server-common, subversion-server-standalone

* Thu Feb 12 2004 Sviatoslav Sviridov <svd@altlinux.ru> 0.37.0-alt2
- rebuild with libdb4.2

* Mon Feb 02 2004 Sviatoslav Sviridov <svd@altlinux.ru> 0.37.0-alt1
- 0.37.0
- conditional build of subversion-doc
- subversion-swig built with python2.3

* Sat Oct 25 2003 Sviatoslav Sviridov <svd@altlinux.ru> 0.32.1-alt1
- 0.32.1

* Tue May 20 2003 Sviatoslav Sviridov <svd@altlinux.ru> 0.23.0-alt1
- 0.23.0
- removed svn-config from libsubversion-devel

* Wed May 14 2003 Sviatoslav Sviridov <svd@altlinux.ru> 0.22.2-alt1
- 0.22.2

* Mon May 12 2003 Sviatoslav Sviridov <svd@altlinux.ru> 0.22.1-alt1
- 0.22.1
- added config dir /etc/subversion with config examples
- added the new 'svndumpfilter' program

* Wed Apr 23 2003 Sviatoslav Sviridov <svd@altlinux.ru> 0.21.0-alt1
- 0.21.0
- fixed group of package cvs2svn

* Fri Apr 04 2003 Sviatoslav Sviridov <svd@altlinux.ru> 0.20.1-alt1
- added documentation to cvs2svn package
- added package subversion-doc
- svn-design.info* moved to subversion-doc
- added package emacs-subversion

* Tue Mar 18 2003 Sviatoslav Sviridov <svd@altlinux.ru> 0.19.1-alt0.1
- 0.19.1
- building python bindings
- building cvs2svn package

* Tue Mar 11 2003 Sviatoslav Sviridov <svd@altlinux.ru> 0.19-alt1
- 0.19

* Sun Feb 23 2003 Sviatoslav Sviridov <svd@altlinux.ru> 0.18-alt1
- 0.18
- Added missing headers to libapr-subversion devel and
  libaprutil-subversion-devel

* Thu Jan 30 2003 Sviatoslav Sviridov <svd@altlinux.ru> 0.17.1-alt1
- first build for ALT Linux
