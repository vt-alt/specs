%def_without test
%define nx_version 3.5.2.31

Name:    x2goserver
Version: 4.1.0.3
Release: alt1
Summary: X2Go Server

Group:   System/Servers
License: GPLv2+
URL:     http://www.x2go.org

Source:  %name-%version.tar
#VCS:    git://code.x2go.org/x2goserver
Source1: x2goserver.init

Patch1:  %name-fix-autoreq.patch
Patch2:  %name-alt-Xsession.patch
Patch3:  alt-startkde.patch
Patch4:  %name-fix-tmpfiles.patch

BuildRequires(pre): rpm-build-perl
BuildRequires: desktop-file-utils
BuildRequires: app-defaults
BuildRequires: perl-devel
BuildRequires: perl-Capture-Tiny
BuildRequires: perl-Config-Simple
BuildRequires: perl-DBI
BuildRequires: perl-File-BaseDir
BuildRequires: perl-File-Which
BuildRequires: perl-Pod-Usage
BuildRequires: perl-Switch
BuildRequires: perl-Try-Tiny
# So XSESSIONDIR gets linked
BuildRequires:  xinit

Requires: bc
Requires: grep
Requires: lsof
Requires: net-tools
Requires: openssh-server
Requires: perl-DBD-SQLite
Requires: perl-X2Go-Server = %EVR
Requires: psmisc
Requires: pwgen
Requires: sshfs
Requires: sudo
Requires: fonts-bitmap-misc
Requires: xauth
Requires: xkbutils
Requires: xkeyboard-config
Requires: x2goserver-x2goagent = %EVR
Requires: x2goserver-xsession
Requires: xwininfo

%add_perl_lib_path %_libdir/x2go
%filter_from_requires \,^/etc/lsb-release$,d
%filter_from_requires \,^/etc/X11/Xresources$,d

%description
X2Go is a server based computing environment with
- session resuming
- low bandwidth support
- session brokerage support
- client side mass storage mounting support
- audio support
- authentication by smartcard and USB stick

This package contains the main daemon and tools for X2Go server-side session
administrations.

%package -n perl-X2Go-Server
Summary: Perl X2Go::Server package
Group: Development/Perl
BuildArch: noarch

%description -n perl-X2Go-Server
X2Go is a server based computing environment with
- session resuming
- low bandwidth support
- session brokerage support
- client side mass storage mounting support
- audio support
- authentication by smartcard and USB stick

This package contains the X2Go::Server Perl package.

%package -n perl-X2Go-Server-DB
Summary: Perl X2Go::Server::DB package
Group: Development/Perl

%description -n perl-X2Go-Server-DB
X2Go is a server based computing environment with
- session resuming
- low bandwidth support
- session brokerage support
- client side mass storage mounting support
- audio support
- authentication by smartcard and USB stick

This package contains the X2Go::Server::DB Perl package.

%package -n perl-X2Go-Log
Summary: Perl X2Go::Log package
Group: Development/Perl
BuildArch: noarch

%description -n perl-X2Go-Log
X2Go is a server based computing environment with
- session resuming
- low bandwidth support
- session brokerage support
- client side mass storage mounting support
- audio support
- authentication by smartcard and USB stick

This package contains the X2Go::Log Perl package.

%package fmbindings
Summary:  X2Go Server file manager bindings
Requires: %name = %version-%release
BuildArch: noarch
Requires: xdg-utils
Group:    Communications

%description fmbindings
X2Go is a server based computing environment with
- session resuming
- low bandwidth support
- session brokerage support
- client side mass storage mounting support
- audio support
- authentication by smartcard and USB stick

This package contains generic MIME type information
for X2Go's local folder sharing. It can be used with all
freedesktop.org compliant desktop shells.

However, this package can be superseded by other, more specific
destkop binding components, if installed and being used with the
corresponding desktop shell:
- under LXDE by x2golxdebindings
- under GNOMEv2 by x2gognomebindings
- under KDE4 by plasma-widget-x2go
- under MATE by x2gomatebindings

%package x2goagent
Group:     Communications
Summary:   X2Go Server's X2Go Agent
Requires:  nxagent >= %nx_version
Requires:  nxproxy >= %nx_version
Requires:  nx-libs >= %nx_version
Provides:  x2goagent = %EVR
Obsoletes: x2goagent < %EVR

%description x2goagent
X2Go is a server based computing environment with
- session resuming
- low bandwidth support
- session brokerage support
- client side mass storage mounting support
- audio support
- authentication by smartcard and USB stick

X2Go Agent functionality has been completely incorporated into
nxagent's code base. If the nxagent binary is executed under the name
of "x2goagent", the X2Go functionalities get activated.

The x2goserver-x2goagent package is a wrapper that activates X2Go
branding in nxagent. Please refer to the nxagent package's description
for more information on NX.

%package printing
Summary:  X2Go Server printing support
Requires: %name = %version-%release
Group:    Communications
BuildArch: noarch

%description printing
The X2Go Server printing package provides client-side printing support
for X2Go. This package has to be installed on X2Go servers that shall be
able to pass X2Go print jobs on to the X2Go client. This package
co-operates with the cups-x2go CUPS backend. If CUPS server and X2Go
server are hosted on different machines, then make sure you install
this package on the X2Go server(s) (and the cups-x2go package on the CUPS
server).

%package xsession
Summary:  X2Go Server Xsession runner
Requires: %name = %version-%release
# Symlinks to xinit files
Requires: app-defaults
Requires: xinit
Requires: dbus
Group:    Communications
BuildArch: noarch

%description xsession
X2Go is a server based computing environment with
- session resuming
- low bandwidth support
- session brokerage support
- client side mass storage mounting support
- audio support
- authentication by smartcard and USB stick

This X2Go server add-on enables Xsession script handling
when starting desktop sessions with X2Go.

Amongst others the parsing of Xsession scripts will
enable desktop-profiles, ssh-agent startups, gpgagent
startups and many more Xsession related features on
X2Go session login automagically.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# Set path
find -type f | xargs sed -i -r -e '/^LIBDIR=/s,/lib/,/%{_lib}/,'
sed -i -e 's,/lib/,/%{_lib}/,' x2goserver/bin/x2gopath
# Don't try to be root
sed -i -e 's/-o root -g root//' */Makefile

%build
%add_optflags -fPIC
%make_build PREFIX=%_prefix NXLIBDIR=%_libdir/nx INSTALLMAN1DIR=%_man1dir

%install
%makeinstall_std PREFIX=%_prefix NXLIBDIR=%_libdir/nx
make -f Makefile.perl install_vendor DESTDIR=%buildroot

# x2gouser homedir, state dir
mkdir -p %buildroot%_sharedstatedir/x2go
# Create empty session file for %%ghost
touch %buildroot%_sharedstatedir/x2go/x2go_sessions

# Printing spool dir
mkdir -p %buildroot%_spooldir/x2goprint

install -Dm 644 x2goserver.service %buildroot%_unitdir/x2goserver.service
install -Dm 755 %SOURCE1 %buildroot%_initddir/x2goserver

# applications link
ln -s ../..%_desktopdir %buildroot%_sysconfdir/x2go/applications

%pre
getent group x2gouser >/dev/null || groupadd -r x2gouser
getent passwd x2gouser >/dev/null || \
    useradd -r -g x2gouser -d /var/lib/x2go -s /sbin/nologin \
    -c "x2go" x2gouser
exit 0

%pre -n perl-X2Go-Server-DB
getent group x2gouser >/dev/null || groupadd -r x2gouser
getent passwd x2gouser >/dev/null || \
    useradd -r -g x2gouser -d /var/lib/x2go -s /sbin/nologin \
    -c "x2go" x2gouser
exit 0

%post
# Initialize the session database
[ ! -s %_sharedstatedir/x2go/x2go_sessions ] &&
    grep -E "^backend=sqlite.*" /etc/x2go/x2gosql/sql >/dev/null 2>&1 &&
    %_sbindir/x2godbadmin --createdb >/dev/null 2>&1 || :

# create /etc/x2go/applications symlink if not already there
# as a regular file, as a symlink, as a special file or as a directory
if ! [ -e %_sysconfdir/x2go/applications ]; then
    ln -s ../..%_datadir/applications %_sysconfdir/x2go/applications
fi
%post_service x2goserver

%preun
if [ "$1" = 0 ]; then
    if [ -L %{_sysconfdir}/x2go/applications ]; then
        rm -f %{_sysconfdir}/x2go/applications
    fi
fi
%preun_service x2goserver

%pre printing
getent group x2goprint >/dev/null || groupadd -r x2goprint
getent passwd x2goprint >/dev/null || \
    useradd -r -g x2goprint -d /var/spool/x2goprint -s /sbin/nologin \
    -c "x2go" x2goprint
exit 0

%files
%config(noreplace) %_sysconfdir/logcheck/ignore.d.server/x2goserver
%config(noreplace) %_sysconfdir/sudoers.d/x2goserver
%dir %_sysconfdir/x2go/
%dir %_sysconfdir/x2go/x2gosql
%dir %_sysconfdir/x2go/x2gosql/passwords
%ghost %config(noreplace) %_sysconfdir/x2go/applications
%config(noreplace) %_sysconfdir/x2go/x2go_logout
%config(noreplace) %_sysconfdir/x2go/x2go_logout.d/
%config(noreplace) %_sysconfdir/x2go/x2goserver.conf
%config(noreplace) %_sysconfdir/x2go/x2gosql/sql
%config(noreplace) %_tmpfilesdir/x2goserver.conf
%_bindir/x2go*
%exclude %_bindir/x2gofm
%exclude %_bindir/x2goprint
%exclude %_bindir/x2goagent
%dir %_libdir/x2go
%_libdir/x2go/extensions
%_libdir/x2go/x2gochangestatus
%_libdir/x2go/x2gocheckport
%_libdir/x2go/x2gocreatesession
%_libdir/x2go/x2gocreateshadowsession
%_libdir/x2go/x2gogetagent
%_libdir/x2go/x2gogetagentstate
%_libdir/x2go/x2gogetdisplays
%_libdir/x2go/x2gogetfreeport
%_libdir/x2go/x2gogetports
%_libdir/x2go/x2gogetrandomport
%_libdir/x2go/x2gogetstatus
%_libdir/x2go/x2goinsertport
%_libdir/x2go/x2goinsertsession
%_libdir/x2go/x2goinsertshadowsession
%_libdir/x2go/x2goistrue
%_libdir/x2go/x2golistsessions_sql
%_libdir/x2go/x2gologlevel
%_libdir/x2go/x2goqueryconfig
%_libdir/x2go/x2goresume
%_libdir/x2go/x2gormforward
%_libdir/x2go/x2gormport
%_libdir/x2go/x2gosuspend-agent
%_libdir/x2go/x2gosyslog
%_sbindir/x2go*
%dir %_datadir/x2go/
%dir %_datadir/x2go/versions
%_datadir/x2go/versions/VERSION.x2goserver
%_datadir/x2go/versions/VERSION.x2goserver-common
%_datadir/x2go/versions/VERSION.x2goserver-extensions
%dir %_datadir/x2go/x2gofeature.d
%_datadir/x2go/x2gofeature.d/x2goserver.features
%_datadir/x2go/x2gofeature.d/x2goserver-extensions.features
%attr(0775,root,x2gouser) %dir %_sharedstatedir/x2go/
%ghost %attr(0660,root,x2gouser) %_sharedstatedir/x2go/x2go_sessions
%_unitdir/x2goserver.service
%_initddir/x2goserver
%_man5dir/x2go*.5*
%_man8dir/x2go*.8*
%exclude %_man8dir/x2gofm.8*
%exclude %_man8dir/x2goprint.8*

%files -n perl-X2Go-Log
%perl_vendorlib/X2Go/Log.pm
#%%_man3dir/X2Go::Log.*

%files -n perl-X2Go-Server
%perl_vendorlib/X2Go/Config.pm
%perl_vendorlib/X2Go/Server.pm
%perl_vendorlib/X2Go/SupeReNicer.pm
%perl_vendorlib/X2Go/Utils.pm
%perl_vendorlib/X2Go/Server/Agent*
#%%_man3dir/X2Go::Config.*
#%%_man3dir/X2Go::Server.*
#%%_man3dir/X2Go::SupeReNicer.*
#%%_man3dir/X2Go::Utils.*
#%%_man3dir/X2Go::Server::Agent.*
#%%_man3dir/X2Go::Server::Agent::*

%files -n perl-X2Go-Server-DB
%perl_vendorlib/X2Go/Server/DB*
%attr(02711,root,x2gouser) %_libdir/x2go/libx2go-server-db-sqlite3-wrapper
%_libdir/x2go/libx2go-server-db-sqlite3-wrapper.pl
#%%_man3dir/X2Go::Server::DB.*
#%%_man3dir/X2Go::Server::DB::*

%files fmbindings
%_bindir/x2gofm
%_desktopdir/x2gofm.desktop
%_datadir/mime/packages/sshfs-x2go.xml
%_datadir/x2go/versions/VERSION.x2goserver-fmbindings
%_datadir/x2go/x2gofeature.d/x2goserver-fmbindings.features
%_man8dir/x2gofm.8*

%files x2goagent
%config(noreplace) %_sysconfdir/x2go/x2goagent.keyboard
%config(noreplace) %_sysconfdir/x2go/x2goagent.options
%config(noreplace) %_sysconfdir/x2go/keystrokes.cfg
#%%config(noreplace) %%_sysconfdir/x2go/rgb
%_bindir/x2goagent
%_libdir/nx/bin/x2goagent
#%%_datadir/x2go/versions/VERSION.x2goserver-x2goagent
#%%_datadir/x2go/rgb
%_pixmapsdir/x2goagent.xpm
%_datadir/x2go/x2gofeature.d/x2goserver-x2goagent.features
%_man1dir/x2goagent.1*

%files printing
%_bindir/x2goprint
%_datadir/x2go/versions/VERSION.x2goserver-printing
%_datadir/x2go/x2gofeature.d/x2goserver-printing.features
%attr(0700,x2goprint,x2goprint) %_spooldir/x2goprint
%_man8dir/x2goprint.8*

%files xsession
%_sysconfdir/x2go/xinitrc.d
%_sysconfdir/x2go/Xclients.d
%_sysconfdir/x2go/Xresources
%config(noreplace) %_sysconfdir/x2go/Xsession
%_datadir/x2go/x2gofeature.d/x2goserver-xsession.features
%_datadir/x2go/versions/VERSION.x2goserver-xsession

%changelog
* Thu Jul 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.1.0.3-alt1
- version updated to 4.1.0.3

* Mon Jun 01 2019 Oleg Solovyov <mcpain@altlinux.org> 4.1.0.2-alt2
- fix tmpfiles

* Mon Oct 15 2018 Oleg Solovyov <mcpain@altlinux.org> 4.1.0.2-alt1
- New version

* Mon Apr 16 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.0.0-alt2
- Correct run KDE5 session (thanks zerg@ for the patch).

* Thu Apr 12 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.0.0-alt1
- New version.
- Use nx-libs >= 3.5.2.31.
- Adapt Xsession for ALT.

* Mon Feb 19 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.1.22-alt1
- New version.
- Fix spool path and unsafe suid/sgid file permissions.
- Fix path to trusted x2gosqlitewrapper.

* Tue Jan 30 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.1.20-alt1
- Initial build in Sisyphus (thanks Fedora for spec)
- Complete rewrite x2gocleansessions init script

