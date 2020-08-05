%define appdir  %_datadir/gambas3
%def_enable     opengl
# jit.h is only available prior to llvm 3.6 and gb.jit can only be compiled with those versions.
%def_with   	jit
%def_without sqlite2
%define prov3() \
Provides:  gambas3-%{*} = %EVR \
Obsoletes: gambas3-%{*} < %EVR \
%nil

Name:		gambas
Version:	3.15.1
Release:	alt1

Summary:	IDE based on a basic interpreter with object extensions
Group:		Development/Tools
License:	GPL-2.0+

URL:		http://gambas.sourceforge.net/
Source0:	%name-%version.tar
Source1:	%name.desktop

BuildRequires:	rpm-build-xdg
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzlib-devel
BuildRequires:	fonts-ttf-dejavu
BuildRequires:	gettext
BuildRequires:  gcc-c++
BuildRequires:	glibc-devel
BuildRequires:  gstreamer1.0-devel	
BuildRequires:  gst-plugins1.0-devel	
BuildRequires:	imlib2-devel
BuildRequires:  libalure-devel >= 1.2
BuildRequires:	libcairo-devel
BuildRequires:	libcurl-devel
BuildRequires:	libdbus-devel
BuildRequires:	libffi-devel
%if_enabled opengl
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel
%endif
BuildRequires:	libglew-devel
BuildRequires:	libgmime3.0-devel
BuildRequires:  libgmp-devel
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libgsl-devel
BuildRequires:	libgtk+2-devel
BuildRequires:	libgtk+3-devel
BuildRequires:	libgtkglext-devel
BuildRequires:	libICE-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libmysqlclient-devel
BuildRequires:	libopenal-devel
BuildRequires:	libpcre-devel
BuildRequires:	libpng-devel
BuildRequires:	libpoppler-devel
#BuildRequires:	libqt4-webkit-devel
BuildRequires:	librsvg-devel
BuildRequires:	libSDL-devel
BuildRequires:	libSDL_image-devel
BuildRequires:	libSDL_mixer-devel
BuildRequires:	libSDL_ttf-devel
BuildRequires:	libSDL2-devel
BuildRequires:	libSDL2_image-devel
BuildRequires:	libSDL2_mixer-devel
BuildRequires:	libSDL2_ttf-devel
BuildRequires:	libsqlite3-devel
BuildRequires:	libssl-devel
BuildRequires:	libtool
BuildRequires:	libunixODBC-devel
BuildRequires:	libv4l-devel
BuildRequires:	libXcursor-devel
BuildRequires:	libXft-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	libXtst-devel
BuildRequires:	llvm-devel
BuildRequires:	pkg-config
BuildRequires:	postgresql-devel
#BuildRequires:	qt4-devel
BuildRequires:  qt5-base-devel
BuildRequires:  qt5-svg-devel
BuildRequires:  qt5-webkit-devel
BuildRequires:  qt5-x11extras-devel
BuildRequires:	xdg-utils
BuildRequires:	zlib-devel

BuildRequires:  dumb-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libmpg123-devel
BuildRequires:  libfluidsynth-devel
BuildRequires:  libncurses-devel

Patch1:		%name-2.99.1-nolintl.patch
Patch2:		%name-2.99.1-noliconv.patch
# Use libv4l1
Patch4:		%name-3.12.0-use-libv4l1.patch
Patch5:		%name-3.11.4-alt-libpoppler-bool-type-fix.patch
Patch6:		%name-3.11.4-alt-postgre-bool-type-fix.patch
Patch7:		%name-alt-mysql8-bool-type-fix.patch
Patch8:    	gambas3-3.13.0-poppler-0.73.0.patch
Patch9:	        gambas3-3.14.1-gst1.patch

Provides:       gambas3 = %EVR
Obsoletes:      gambas3 < %EVR
Provides:       %name-full = %version-%release
Obsoletes:      %name-full < %version-%release
Provides:       %name-examples = %version-%release
Obsoletes:      %name-examples < %version-%release
%prov3 examples
%prov3 full

Requires:      %name-runtime = %version-%release
Requires:      %name-ide = %version-%release
# From http://gambasdoc.org/help/howto/package#t1
# It depends on "All gambas components."
Requires:      %name-gb-args = %version-%release
Requires:      %name-gb-cairo = %version-%release
Requires:      %name-gb-chart = %version-%release
Requires:      %name-gb-clipper = %version-%release
Requires:      %name-gb-complex = %version-%release
Requires:      %name-gb-compress = %version-%release
Requires:      %name-gb-crypt = %version-%release
Requires:      %name-gb-data = %version-%release
Requires:      %name-gb-db-form = %version-%release
Requires:      %name-gb-db-mysql = %version-%release
Requires:      %name-gb-db-odbc = %version-%release
Requires:      %name-gb-db-postgresql = %version-%release
Requires:      %name-gb-db-sqlite3 = %version-%release
Requires:      %name-gb-dbus = %version-%release
Requires:      %name-gb-db = %version-%release
Requires:      %name-gb-desktop-gnome = %version-%release
Requires:      %name-gb-desktop = %version-%release
Requires:      %name-gb-eval-highlight = %version-%release
Requires:      %name-gb-form-dialog = %version-%release
Requires:      %name-gb-form-mdi = %version-%release
Requires:      %name-gb-form-stock = %version-%release
Requires:      %name-gb-form = %version-%release
Requires:      %name-gb-gmp = %version-%release
Requires:      %name-gb-gsl = %version-%release
Requires:      %name-gb-gtk = %version-%release
Requires:      %name-gb-gtk-opengl = %version-%release
Requires:      %name-gb-gtk3 = %version-%release
Requires:      %name-gb-gui = %version-%release
Requires:      %name-gb-httpd = %version-%release
Requires:      %name-gb-image = %version-%release
Requires:      %name-gb-image-effect = %version-%release
Requires:      %name-gb-image-imlib = %version-%release
Requires:      %name-gb-image-io = %version-%release
Requires:      %name-gb-inotify = %version-%release
%if_with jit
Requires:      %name-gb-jit = %version-%release
%endif
Requires:      %name-gb-logging = %version-%release
Requires:      %name-gb-map = %version-%release
Requires:      %name-gb-markdown = %version-%release
Requires:      %name-gb-media = %version-%release
Requires:      %name-gb-memcached = %version-%release
Requires:      %name-gb-mime = %version-%release
Requires:      %name-gb-ncurses = %version-%release
Requires:      %name-gb-net-curl = %version-%release
Requires:      %name-gb-net-pop3 = %version-%release
Requires:      %name-gb-net-smtp = %version-%release
Requires:      %name-gb-net = %version-%release
Requires:      %name-gb-openal = %version-%release
%if_enabled opengl
Requires:      %name-gb-opengl = %version-%release
Requires:      %name-gb-opengl-glu = %version-%release
Requires:      %name-gb-opengl-glsl = %version-%release
Requires:      %name-gb-opengl-sge = %version-%release
%endif
Requires:      %name-gb-openssl = %version-%release
Requires:      %name-gb-option = %version-%release
Requires:      %name-gb-pcre = %version-%release
Requires:      %name-gb-pdf = %version-%release
#Requires:      %name-gb-qt4 = %version-%release
#Requires:      %name-gb-qt4-ext = %version-%release
#Requires:      %name-gb-qt4-webkit = %version-%release
#Requires:      %name-gb-qt4-opengl = %version-%release
Requires:      %name-gb-report = %version-%release
Requires:      %name-gb-report2 = %version-%release
Requires:      %name-gb-scanner = %version-%release
Requires:      %name-gb-sdl = %version-%release
Requires:      %name-gb-sdl-sound = %version-%release
Requires:      %name-gb-sdl2 = %version-%release
Requires:      %name-gb-sdl2-audio = %version-%release
Requires:      %name-gb-settings = %version-%release
Requires:      %name-gb-signal = %version-%release
Requires:      %name-gb-util = %version-%release
Requires:      %name-gb-util-web = %version-%release
Requires:      %name-gb-v4l = %version-%release
Requires:      %name-gb-vb = %version-%release
Requires:      %name-gb-xml = %version-%release
Requires:      %name-gb-xml-html = %version-%release
Requires:      %name-gb-xml-libxml = %version-%release
Requires:      %name-gb-xml-rpc = %version-%release
Requires:      %name-gb-xml-xslt = %version-%release
Requires:      %name-gb-web = %version-%release
# New components
Requires:      %name-gb-form-editor = %version-%release
Requires:      %name-gb-qt5 = %version-%release
Requires:      %name-gb-qt5-opengl = %version-%release
Requires:      %name-gb-qt5-webkit = %version-%release
Requires:      %name-gb-qt5-ext = %version-%release
Requires:      %name-gb-form-terminal = %version-%release
Requires:      %name-gb-term = %version-%release
Requires:      %name-gb-test = %version-%release
Requires:      %name-gb-form-print = %version-%release

%description
Gambas3 is a free development environment based on a Basic interpreter
with object extensions, like Visual Basic (but it is NOT a clone !).
With Gambas3, you can quickly design your program GUI, access MySQL or
PostgreSQL databases, pilot KDE applications with DCOP, translate your
program into many languages, create network applications easily, and so
on...

%package runtime
Summary:	Runtime environment for Gambas3
Group:		Development/Tools
%prov3 runtime

%description runtime
Gambas3 is a free development environment based on a Basic interpreter
with object extensions, like Visual Basic. This package contains the
runtime components necessary to run programs designed in Gambas3.

%package devel
Summary:	Development environment for Gambas3
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 devel

%description devel
The gambas3-devel package contains the tools needed to compile Gambas3
projects without having to install the complete development environment
(gambas3-ide).

%package scripter
Summary:	Scripter program that allows the creation of Gambas3 scripts
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
Requires:	%name-devel = %version-%release
%prov3 scripter

%description scripter
This package includes the scripter program that allows the user to
write script files in Gambas.

%package ide
Summary:	The complete Gambas3 Development Environment
Group:		Development/Tools
License:	GPLv2+
Provides:	%name = %version-%release
%prov3 ide

Requires:	tar, gzip, rpm-build, gettext
Requires:	%name-runtime = %version-%release
Requires:	%name-devel = %version-%release
Requires:	%name-gb-args = %version-%release
Requires:	%name-gb-clipper = %version-%release
Requires:	%name-gb-db = %version-%release
Requires:	%name-gb-db-form = %version-%release
Requires:	%name-gb-desktop = %version-%release
Requires:	%name-gb-eval-highlight = %version-%release
Requires:	%name-gb-form = %version-%release
Requires:	%name-gb-form-dialog = %version-%release
Requires:       %name-gb-form-editor = %version-%release
Requires:	%name-gb-form-mdi = %version-%release
Requires:	%name-gb-form-stock = %version-%release
Requires:	%name-gb-gtk = %version-%release
Requires:	%name-gb-gui = %version-%release
Requires:	%name-gb-image = %version-%release
Requires:	%name-gb-image-effect = %version-%release
Requires:	%name-gb-markdown = %version-%release
Requires:	%name-gb-qt5 = %version-%release
Requires:	%name-gb-qt5-webkit = %version-%release
Requires:	%name-gb-settings = %version-%release
Requires:       %name-gb-util = %version-%release
Requires:	%name-gb-net = %version-%release
Requires:	%name-gb-net-curl = %version-%release
%if_with jit
Requires:	%name-gb-jit = %version-%release
%endif
Requires:       %name-gb-test = %version-%release
Requires:	%name-gb-form-print = %version-%release

%description ide
This package includes the complete Gambas3 Development Environment
and the database manager. Installing this package will give you all
of the Gambas3 components.

%package gb-args
Summary:	Gambas3 component package for args
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-args

%description gb-args
This package contains the Gambas3 component package for args.

%package gb-cairo
Summary:	Gambas3 component package for cairo
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-cairo

%description gb-cairo
This package contains the Gambas3 Cario components.

%package gb-chart
Summary:	Gambas3 component package for chart
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-chart

%description gb-chart
This package contains the Gambas3 Chart components.

%package gb-clipper
Summary:	Gambas3 component package for clipper
Group:		Development/Tools
Requires:	%{name}-runtime = %{version}-%{release}
%prov3 gb-clipper

%description gb-clipper
%{summary}

%package gb-complex
Summary:	Gambas3 component package for complex
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-complex

%description gb-complex
This component brings complex numbers support to the interpreter.

%package gb-compress
Summary:	Gambas3 component package for compress
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-compress

%description gb-compress
This component allows you to compress/uncompress data or files
with the bzip2 and zip algorithms.

%package gb-crypt
Summary:	Gambas3 component package for crypt
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-crypt

%description gb-crypt
This component contains cryptography support.

%package gb-data
Summary:	Gambas3 component package for data
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-data

%description gb-data
The gb.data component provides Abstract Datatypes (ADT) which are data
containers with a well-defined interface but variable implementation.

%package gb-db
Summary:	Gambas3 component package for db
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-db

%description gb-db
This component allows you to access many databases management
systems, provided that you install the needed driver packages.

%package gb-db-form
Summary:	Gambas3 component package for db.form
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-db-form

%description gb-db-form
This package contains the Gambas3 Database form components.

%package gb-db-mysql
Summary:	Gambas3 component package for db.mysql
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-db-mysql

%description gb-db-mysql
This component allows you to access MySQL databases.

%package gb-db-odbc
Summary:	Gambas3 component package for db.odbc
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-db-odbc

%description gb-db-odbc
This component allows you to access ODBC databases.

%package gb-db-postgresql
Summary:	Gambas3 component package for db.postgresql
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-db-postgresql

%description gb-db-postgresql
This component allows you to access PostgreSQL databases.

%package gb-db-sqlite3
Summary:	Gambas3 component package for db.sqlite3
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-db-sqlite3

%description gb-db-sqlite3
This component allows you to access SQLite 3 databases.

%package gb-desktop
Summary:	Gambas3 component package for desktop
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-desktop

%description gb-desktop
This Gambas3 component allows you to operate with XDG-compliant desktop
environmnents.

%package gb-desktop-gnome
Summary:	Gambas3 component package for GNOME desktop
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-desktop-gnome

%description gb-desktop-gnome
This Gambas3 component allows you to operate with GNOME desktop
environmnents.

%package gb-dbus
Summary:	Gambas3 component package for dbus
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-dbus

%description gb-dbus
This package contains the Gambas3 D-bus components.

%package gb-eval-highlight
Summary:	Gambas3 component package for eval highlight
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-eval-highlight

%description gb-eval-highlight
This component implements the eval-highlight componet.

%package gb-form
Summary:	Gambas3 component package for form
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-form

%description gb-form
This component implements the form control.

%package gb-form-dialog
Summary:	Gambas3 component package for form.dialog
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-form-dialog

%description gb-form-dialog
This component implements the form-dialog control.

%package gb-form-mdi
Summary:	Gambas3 component package for form.mdi
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-form-mdi

%description gb-form-mdi
This component implements the form-mdi control.

%package gb-form-stock
Summary:	Gambas3 component package for form.stock
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-form-stock

%description gb-form-stock
This component implements the form-stock control.

%package gb-httpd
Summary:	Gambas3 component package for httpd
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-httpd

%description gb-httpd
Gambas3 component package for httpd.

%package gb-gmp
Summary:	Gambas3 component package for gmp
Group:		Development/Tools
Requires:	%{name}-runtime = %{version}-%{release}
%prov3 gb-gmp

%description gb-gmp
%{summary}

%package gb-gsl
Summary:	Gambas3 component package for gsl
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-gsl

%description gb-gsl
This component aims at providing most of the features
of the Gnu Scientific Library.

%package gb-gtk
Summary:	Gambas3 component package for gtk
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-gtk

%description gb-gtk
This package includes the Gambas3 GTK2 GUI component.

%package gb-gtk3
Summary:	Gambas3 component package for gtk3
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-gtk3

%description gb-gtk3
This package includes the Gambas3 GTK3 GUI component.

%if_enabled opengl
%package gb-gtk-opengl
Summary:	Gambas3 component package for gtk.opengl
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-gtk-opengl

%description gb-gtk-opengl
This component allows to use the gb.opengl component in
GTK+ applications.
%endif

%package gb-gui
Summary:	Gambas3 component package for gui
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-gui

%description gb-gui
This is a component that just loads gb.qt if you are running KDE or
gb.gtk in the other cases.

%package gb-image
Summary:	Gambas3 component package for image
License:	GPLv2 or QPL
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-image

%description gb-image
Image processing component for Gambas3.

%package gb-image-effect
Summary:	Gambas3 component package for image.effect
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-image-effect

%description gb-image-effect
This component allows you to apply various effects to images.

%package gb-image-imlib
Summary:	Gambas3 component package for image.imlib
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-image-imlib

%description gb-image-imlib
This component allows you to manipulate images with imlibs.

%package gb-image-io
Summary:	Gambas3 component package for image.io
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-image-io

%description gb-image-io
This component allows you to perform images input output operations.

%package gb-inotify
Summary:	Gambas3 component package for inotify (unstable)
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-inotify

%description gb-inotify
This component allows you to perform inotify operations.

%if_with jit
%package gb-jit
Summary:	Gambas3 Just In Time compiler
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-jit

%description gb-jit
Gambas3 Just In Time compiler.
%endif

%package gb-logging
Summary:	Gambas3 component package for logging
Group:		Development/Tools
Requires:	%{name}-runtime = %{version}-%{release}
%prov3 gb-logging

%description gb-logging
%{summary}

%package gb-map
Summary:    Gambas3 component package for map
Group:      Development/Tools
Requires:   %name-runtime = %version-%release
%prov3 gb-map

%description gb-map
Gambas3 component package for map

%package gb-markdown
Summary:    Gambas3 component package for markup syntax
Group:      Development/Tools
Requires:   %name-runtime = %version-%release
%prov3 gb-markdown

%description gb-markdown
Gambas3 component package for markup syntax

%package gb-media
Summary:    Gambas3 component package for media
Group:      Development/Tools
Requires:   %name-runtime = %version-%release
%prov3 gb-media

%description gb-media
Gambas3 component package for media

%package gb-memcached
Summary:    Gambas3 component package for memcached
Group:      Development/Tools
Requires:   %name-runtime = %version-%release
%prov3 gb-memcached

%description gb-memcached
Gambas3 component package for memcached

%package gb-mime
Summary:    Gambas3 component package for mime
Group:      Development/Tools
Requires:   %name-runtime = %version-%release
%prov3 gb-mime

%description gb-mime
Gambas3 component package for mime

%package gb-ncurses
Summary:    Gambas3 component package for ncurses
Group:      Development/Tools
Requires:   %name-runtime = %version-%release
%prov3 gb-ncurses

%description gb-ncurses
Gambas3 component package for ncurses

%package gb-net
Summary:	Gambas3 component package for net
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-net

%description gb-net
This Gambas3 component allows you to use TCP/IP and UDP sockets, and to
access any serial ports.

%package gb-net-curl
Summary:	Gambas3 component package for net.curl
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-net-curl

%description gb-net-curl
This Gambas3 component allows your programs to easily become FTP or HTTP
clients.

%package gb-net-pop3
Summary:	Gambas3 component package for net.pop3
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-net-pop3

%description gb-net-pop3
This component implements a POP3 client. It allows to retrieve mails by
following the POP3 protocol. It support SSL/TLS encryption provided
that openssl is installed on your system.

%package gb-net-smtp
Summary:	Gambas3 component package for net.smtp
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-net-smtp

%description gb-net-smtp
This component allows to send mails by using the SMTP protocol.
It supports mail attachments, mail alternatives, and protocol encryption
(SSL or TLS), provided that the openssl program is installed on your
system.

%package gb-openal
Summary:       Gambas3 component package for openal
Group:         Development/Tools
Requires:      %name-runtime = %version-%release
%prov3 gb-openal

%description gb-openal
Gambas3 component package for openal.

%if_enabled opengl
%package gb-opengl
Summary:	Gambas3 component package for opengl
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-opengl

%description gb-opengl
This component allows you to use the Mesa libraries to do 3D operations.

%package gb-opengl-glu
Summary:	Gambas3 component package for opengl.glu
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-opengl-glu

%description gb-opengl-glu
This component allows you to use the Mesa libraries to do 3D operations.

%package gb-opengl-glsl
Summary:	Gambas3 component package for opengl.glsl
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-opengl-glsl

%description gb-opengl-glsl
This component allows you to use the Mesa libraries to do 3D operations.
%endif

%package gb-opengl-sge
Summary:	Gambas3 component package for opengl-sge
Group:		Development/Tools
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-opengl = %{version}-%{release}
%prov3 gb-opengl-sge

%description gb-opengl-sge
%{summary}

%package gb-openssl
Summary:	Gambas3 component package for openssl
Group:		Development/Tools
Requires:	%{name}-runtime = %{version}-%{release}
%prov3 gb-openssl

%description gb-openssl
%{summary}

%package gb-option
Summary:	Gambas3 component package for option
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-option

%description gb-option
This component allows you to interpret command-line options.

%package gb-pcre
Summary:	Gambas3 component package for pcre
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-pcre

%description gb-pcre
This component allows you to use Perl compatible regular expresions
within Gambas code.

%package gb-pdf
Summary:	Gambas3 component package for pdf
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-pdf

%description gb-pdf
This component allows you to manipulate pdf files with Gambas code.

%package gb-qt4
Summary:	Gambas3 component package for qt4
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-qt4

%description gb-qt4
This package includes Gambas3 QT4 GUI component.

%package gb-qt4-ext
Summary:	Gambas3 component package for qt4.ext
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-qt4-ext

%description gb-qt4-ext
This package contains the Gambas3 qt-ext components.

%package gb-qt4-opengl
Summary:	Gambas3 component package for qt4-opengl
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-qt4-opengl

%description gb-qt4-opengl
This package contains the Gambas3 qt-opengl components.

%package gb-qt4-webkit
Summary:	Gambas3 component package for qt4-webkit
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-qt4-webkit

%description gb-qt4-webkit
This package contains the Gambas3 qt-webkit components.

%package gb-report
Summary:	Gambas3 component package for report
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-report

%description gb-report
This package contains the Gambas3 Report components.

%package gb-report2
Summary:	Gambas3 new component package for report
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-report2

%description gb-report2
This package contains the new and better implementation of the Gambas3
reporting component.

%package gb-scanner
Summary:	Gambas3 component package for work with scanners
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
Requires:	sane
%prov3 gb-scanner

%description gb-scanner
This package contains the component based on SANE to help dealing with
scanners.

%package gb-sdl
Summary:	Gambas3 component package for sdl
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
Requires:	fonts-ttf-dejavu
%prov3 gb-sdl

%description gb-sdl
This component use the sound, image and TTF fonts parts of the SDL
library. It allows you to simultaneously play many sounds and music
stored in a file. If OpenGL drivers are installed it uses them to
accelerate 2D and 3D drawing.

%package gb-sdl-sound
Summary:	Gambas3 component package for sdl.sound
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-sdl-sound

%description gb-sdl-sound
This component allows you to play sounds in Gambas. This component
manages up to 32 sound tracks that can play sounds from memory, and
one music track that can play music from a file. Everything is mixed
in real time.

%package gb-sdl2
Summary:	Gambas3 component for sdl2
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-sdl2

%description gb-sdl2
Gambas3 component for sdl2

%package gb-sdl2-audio
Summary:	Gambas3 component for sdl2-audio
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-sdl2-audio

%description gb-sdl2-audio
Gambas3 component for sdl2-audio.

%package gb-settings
Summary:	Gambas3 component package for settings
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-settings

%description gb-settings
This components allows you to deal with configuration files.

%package gb-signal
Summary:	Gambas3 component package for signal
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-signal

%description gb-signal
This package contains the Gambas3 Signal components.

%package gb-util
Summary:	Component written in Gambas3 that provides utility functions to the interpreter
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-util

%description gb-util
Component written in Gambas3 that provides utility functions to the
interpreter.

%package gb-util-web
Summary:	Component written in Gambas3 that provides utility functions to web applications
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-util-web

%description gb-util-web
Component written in Gambas3 that provides utility functions to the
web applications.

%package gb-v4l
Summary:	Gambas3 component package for v4l
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-v4l

%description gb-v4l
This component allows access to Video4Linux devices.

%package gb-vb
Summary:	Gambas3 component package for vb
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-vb

%description gb-vb
This Gambas3 component aims at including some functions that imitate
the behaviour of Visual Basic(tm) functions. Use it only if you try
to port some VB projects.

%package gb-web
Summary:	Gambas3 component package for web
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-web

%description gb-web
This components allows you to make CGI web applications using Gambas,
with an ASP-like interface.

%package gb-xml
Summary:	Gambas3 component package for xml
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-xml

%description gb-xml
These components brings the power of the libxml and libxslt libraries to
Gambas3 for XML processing.

%package gb-xml-html
Summary:	Gambas3 component package for xml.html
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-xml-html

%description gb-xml-html
These component allows to process XHTML documents.

%package gb-xml-libxml
Summary:	Gambas3 component package for libxml
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-xml-libxml

%description gb-xml-libxml
Gambas3 component package for libxml.

%package gb-xml-rpc
Summary:	Gambas3 component package for xml.rpc
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-xml-rpc

%description gb-xml-rpc
This component allows you to use xml-rpc.

%package gb-xml-xslt
Summary:	Gambas3 component package for xml.xslt
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-xml-xslt

%description gb-xml-xslt
This component allows you to use xml-xslt.

%package gb-form-editor
Summary:	Gambas3 component package for form.editor
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-form-editor

%description gb-form-editor
This package contains form.editor component.

%package gb-qt5
Summary:	Gambas3 component package for qt5
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-qt5

%description gb-qt5
This package includes Gambas3 QT5 GUI component.

%package gb-qt5-opengl
Summary:	Gambas3 component package for qt5-opengl
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-qt5-opengl

%description gb-qt5-opengl
This package contains the Gambas3 qt5-opengl components.

%package gb-qt5-webkit
Summary:	Gambas3 component package for qt5-webkit
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-qt5-webkit

%description gb-qt5-webkit
This package contains the Gambas3 qt5-webkit components.

%package gb-qt5-ext
Summary:	Gambas3 component package for qt5 (additional)
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-qt5-ext

%description gb-qt5-ext
This package contains the Gambas3 qt5 component with additional stuff.

%package gb-form-terminal
Summary:	Gambas3 component package for terminal in forms
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-form-terminal

%description gb-form-terminal
This package contains the Gambas3 component for terminal in form.

%package gb-term
Summary:	Gambas3 component package for making the GUI of terminal applications
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-term

%description gb-term
This package contains the Gambas3 component for making the GUI of
terminal applications.

%package gb-test
Summary:	Gambas3 component package for tests
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-test

%description gb-test
This package contains the Gambas3 component for tests.

%package gb-form-print
Summary:	Gambas3 component package for print form
Group:		Development/Tools
Requires:	%name-runtime = %version-%release
%prov3 gb-form-print

%description gb-form-print
This package contains the Gambas3 component for print form.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p0
%patch6 -p0
%patch7 -p1
%patch8 -p1
%patch9 -p1

# We used to patch these out, but this is simpler.
for i in `find . |grep acinclude.m4`; do
	sed -i 's|$AM_CFLAGS -O3|$AM_CFLAGS|g' $i
	sed -i 's|$AM_CXXFLAGS -Os -fno-omit-frame-pointer|$AM_CXXFLAGS|g' $i
	sed -i 's|$AM_CFLAGS -Os|$AM_CFLAGS|g' $i
	sed -i 's|$AM_CFLAGS -O0|$AM_CFLAGS|g' $i
	sed -i 's|$AM_CXXFLAGS -O0|$AM_CXXFLAGS|g' $i
done
# Need this for gcc44
sed -i 's|-fno-exceptions||g' gb.db.sqlite3/acinclude.m4
# fix build against libmysqlclient21
sed -i 's| my_config\.h||g' gb.db.mysql/configure.ac
./reconf-all

# clean up some spurious exec perms
chmod -x main/gbx/gbx_local.h
chmod -x main/gbx/gbx_subr_file.c
chmod -x gb.qt4/src/CContainer.cpp
chmod -x main/lib/option/getoptions.*
chmod -x main/lib/option/main.c

%build
# Gambas can't deal with -Wp,-D_FORTIFY_SOURCE=2
MY_CFLAGS=`echo $RPM_OPT_FLAGS | sed -e 's/-Wp,-D_FORTIFY_SOURCE=2//g'`
%configure \
	--datadir="%_datadir" \
	--enable-intl \
	--enable-conv \
	--disable-qt4 \
	--enable-qt5 \
	--enable-kde \
	--enable-net \
	--enable-curl \
	--enable-postgresql \
	--enable-mysql \
	--enable-sqlite3 \
	--enable-sdl \
	--enable-vb \
	--enable-pdf \
	--with-ffi-includes=`pkg-config libffi --variable=includedir` \
	--with-ffi-libraries=`pkg-config libffi --variable=libdir` \
	--with-mysql-libraries=%_libdir/mysql \
	--disable-static \
	AM_CFLAGS="$MY_CFLAGS" AM_CXXFLAGS="$MY_CFLAGS"
# rpath removal
for i in main; do
	sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' $i/libtool
	sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' $i/libtool
done
# for some unholy reason, using system libtool breaks on qt5. so we don't.
pushd gb.qt5
make %{?_smp_mflags}
popd
make LIBTOOL=%_bindir/libtool %{?_smp_mflags}

%install
export PATH=%buildroot%_bindir:$PATH
make LIBTOOL=%_bindir/libtool DESTDIR=%buildroot INSTALL="install -p" install
# Yes, I know. Normally we'd nuke the .la files, but Gambas is retar^Wspecial.
# rm -rf %%buildroot%%_libdir/gambas3/*.la
install -m644 -pD ./app/desktop/gambas3.png %buildroot%_pixmapsdir/gambas3.png
install -m644 -pD %SOURCE1 %buildroot%_desktopdir/gambas3.desktop

# Make symlink /usr/bin/gambas to gambas3
ln -s gambas3 %buildroot%_bindir/gambas

# Upstream says we don't need those files. Not sure why they install them then. :/
rm -rf %buildroot%_libdir/gambas3/gb.la %buildroot%_libdir/gambas3/gb.so*

# No need for the static libs
rm -rf %buildroot%_libdir/gambas3/*.a

# Remove man page for gbh3
rm -f %buildroot%_man1dir/gbh3.1* 

# Mime types.
mkdir -p %buildroot%_datadir/mime/packages/
install -m 0644 -p app/mime/application-x-gambasscript.xml %buildroot%_xdgmimedir/packages/
install -m 0644 -p main/mime/application-x-gambas3.xml %buildroot%_xdgmimedir/packages/

%files

%files runtime
%doc COPYING INSTALL README
%dir %_libdir/gambas3/
%_libdir/gambas3/gb.component
%_libdir/gambas3/gb.debug.*
%_libdir/gambas3/gb.draw.*
%_libdir/gambas3/gb.geom.*
%_libdir/gambas3/gb.eval.component
%_libdir/gambas3/gb.eval.so*
%_libdir/gambas3/gb.eval.la
#_bindir/gbh3
#_bindir/gbh3.gambas
%_bindir/gbr3
%_bindir/gbx3
%_datadir/pixmaps/gambas3.png
%_desktopdir/*.desktop
%_datadir/gambas3/template/
%_datadir/appdata/gambas3.appdata.xml
%_datadir/metainfo/gambas3.appdata.xml
%dir %appdir/
%dir %appdir/info/
%appdir/info/gb.debug.*
%appdir/info/gb.eval.list
%appdir/info/gb.eval.info
%appdir/info/gb.info
%appdir/info/gb.list
%dir %appdir/icons/
%appdir/icons/application-x-gambas3.png
%_xdgmimedir/packages/application-x-gambas3.xml
%appdir/icons/application-x-gambasserverpage.png
%_man1dir/gbr3.1*
%_man1dir/gbx3.1*

%files devel
%doc COPYING
%_bindir/gbc3
%_bindir/gba3
%_bindir/gbi3
%_man1dir/gbc3.1*
%_man1dir/gba3.1*
%_man1dir/gbi3.1*

%files scripter
%_bindir/gbs3
%_bindir/gbs3.gambas
%_bindir/gbw3
%appdir/icons/application-x-gambasscript.png
%_xdgmimedir/packages/application-x-gambasscript.xml
%_man1dir/gbs3.1*
%_man1dir/gbw3.1*

%files ide
%_bindir/gambas
%_bindir/gambas3
%_bindir/gambas3.gambas
%_man1dir/gambas3.1*

%files gb-args
%_libdir/gambas3/gb.args.*
%appdir/info/gb.args.*

%files gb-cairo
%_libdir/gambas3/gb.cairo.*
%appdir/info/gb.cairo.*

%files gb-chart
%_libdir/gambas3/gb.chart.*
%appdir/info/gb.chart.*

%files gb-clipper
%_libdir/gambas3/gb.clipper.*
%appdir/info/gb.clipper.*

%files gb-complex
%_libdir/gambas3/gb.complex.*
%appdir/info/gb.complex.*

%files gb-compress
%_libdir/gambas3/gb.compress.*
%appdir/info/gb.compress.*

%files gb-crypt
%_libdir/gambas3/gb.crypt.*
%appdir/info/gb.crypt.*

%files gb-data
%_libdir/gambas3/gb.data.*
%appdir/info/gb.data.*

%files gb-db
%_libdir/gambas3/gb.db.component
%_libdir/gambas3/gb.db.gambas
%_libdir/gambas3/gb.db.la
%_libdir/gambas3/gb.db.so*
%appdir/info/gb.db.info
%appdir/info/gb.db.list

%files gb-db-form
%_libdir/gambas3/gb.db.form.*
%appdir/control/gb.db.form/
%appdir/info/gb.db.form.*

%files gb-db-mysql
%_libdir/gambas3/gb.db.mysql.*
%_libdir/gambas3/gb.mysql.*
%appdir/info/gb.db.mysql.*
%appdir/info/gb.mysql.*

%files gb-db-odbc
%_libdir/gambas3/gb.db.odbc.*
%appdir/info/gb.db.odbc.*

%files gb-db-postgresql
%_libdir/gambas3/gb.db.postgresql.*
%appdir/info/gb.db.postgresql.*

%files gb-db-sqlite3
%_libdir/gambas3/gb.db.sqlite3.*
%appdir/info/gb.db.sqlite3.*

%files gb-dbus
%_libdir/gambas3/gb.dbus.*
%appdir/info/gb.dbus.*

%files gb-desktop
%_libdir/gambas3/gb.desktop.*
%exclude %_libdir/gambas3/gb.desktop.gnome.*
%appdir/control/gb.desktop/
%appdir/info/gb.desktop.*

%files gb-desktop-gnome
%_libdir/gambas3/gb.desktop.gnome.*

%files gb-eval-highlight
%_libdir/gambas3/gb.eval.highlight.*
%appdir/info/gb.eval.highlight.*

%files gb-form
%_libdir/gambas3/gb.form.component
%_libdir/gambas3/gb.form.gambas
%appdir/control/gb.form/
%appdir/info/gb.form.info
%appdir/info/gb.form.list

%files gb-form-dialog
%_libdir/gambas3/gb.form.dialog.component
%_libdir/gambas3/gb.form.dialog.gambas
%appdir/info/gb.form.dialog.info
%appdir/info/gb.form.dialog.list

%files gb-form-mdi
%_libdir/gambas3/gb.form.mdi.component
%_libdir/gambas3/gb.form.mdi.gambas
%appdir/control/gb.form.mdi/
%appdir/info/gb.form.mdi.info
%appdir/info/gb.form.mdi.list

%files gb-form-stock
%_libdir/gambas3/gb.form.stock.component
%_libdir/gambas3/gb.form.stock.gambas
%appdir/info/gb.form.stock.info
%appdir/info/gb.form.stock.list

%files gb-httpd
%_libdir/gambas3/gb.httpd.*
%appdir/info/gb.httpd.*

%files gb-gmp
%_libdir/gambas3/gb.gmp.*
%appdir/info/gb.gmp.*

%files gb-gsl
%_libdir/gambas3/gb.gsl.*
%appdir/info/gb.gsl.*

%files gb-gtk
%_libdir/gambas3/gb.gtk.component
%_libdir/gambas3/gb.gtk.so*
%_libdir/gambas3/gb.gtk.la
%appdir/info/gb.gtk.info
%appdir/info/gb.gtk.list

%files gb-gtk3
%_libdir/gambas3/gb.gtk3.component
%_libdir/gambas3/gb.gtk3.so*
%_libdir/gambas3/gb.gtk3.la
%appdir/info/gb.gtk3.info
%appdir/info/gb.gtk3.list

%if_enabled opengl
%files gb-gtk-opengl
%_libdir/gambas3/gb.gtk.opengl.*
%appdir/info/gb.gtk.opengl.*
%endif

%files gb-gui
%_libdir/gambas3/gb.gui.*
%appdir/info/gb.gui.*

%files gb-image
%_libdir/gambas3/gb.image.component
%_libdir/gambas3/gb.image.so*
%_libdir/gambas3/gb.image.la
%appdir/info/gb.image.info
%appdir/info/gb.image.list

%files gb-image-effect
%_libdir/gambas3/gb.image.effect.*
%appdir/info/gb.image.effect.*

%files gb-image-imlib
%_libdir/gambas3/gb.image.imlib.*
%appdir/info/gb.image.imlib.*

%files gb-image-io
%_libdir/gambas3/gb.image.io.*
%appdir/info/gb.image.io.*

%files gb-inotify
%_libdir/gambas3/gb.inotify.*
%appdir/info/gb.inotify.*

%if_with jit
%files gb-jit
%_libdir/gambas3/gb.jit.*
%appdir/info/gb.jit.*
%endif

%files gb-logging
%_libdir/gambas3/gb.logging.*
%appdir/info/gb.logging.*

%files gb-map
%_libdir/gambas3/gb.map.*
%appdir/info/gb.map.*
%appdir/control/gb.map/

%files gb-markdown
%_libdir/gambas3/gb.markdown.*
%appdir/info/gb.markdown.*

%files gb-media
%_libdir/gambas3/gb.media.*
%appdir/info/gb.media.*
%appdir/control/gb.media.form/

%files gb-memcached
%_libdir/gambas3/gb.memcached.*
%appdir/info/gb.memcached.*

%files gb-mime
%_libdir/gambas3/gb.mime.*
%appdir/info/gb.mime.*

%files gb-ncurses
%_libdir/gambas3/gb.ncurses.*
%appdir/info/gb.ncurses.*

%files gb-net
%_libdir/gambas3/gb.net.component
%_libdir/gambas3/gb.net.so*
%_libdir/gambas3/gb.net.la
%appdir/info/gb.net.info
%appdir/info/gb.net.list
%appdir/control/gb.net.pop3/
%appdir/control/gb.net.smtp/

%files gb-net-curl
%_libdir/gambas3/gb.net.curl.*
%appdir/info/gb.net.curl.*

%files gb-net-pop3
%_libdir/gambas3/gb.net.pop3.*
%appdir/info/gb.net.pop3.*

%files gb-net-smtp
%_libdir/gambas3/gb.net.smtp.*
%appdir/info/gb.net.smtp.*

%files gb-openal
%_libdir/gambas3/gb.openal.*
%appdir/info/gb.openal.*

%if_enabled opengl
%files gb-opengl
%_libdir/gambas3/gb.opengl.component
%_libdir/gambas3/gb.opengl.so*
%_libdir/gambas3/gb.opengl.la
%appdir/info/gb.opengl.info
%appdir/info/gb.opengl.list

%files gb-opengl-sge
%_libdir/gambas3/gb.opengl.sge.*
%appdir/info/gb.opengl.sge.*

%files gb-opengl-glu
%_libdir/gambas3/gb.opengl.glu.*
%appdir/info/gb.opengl.glu.*

%files gb-opengl-glsl
%_libdir/gambas3/gb.opengl.glsl.*
%appdir/info/gb.opengl.glsl.*
%endif

%files gb-openssl
%_libdir/gambas3/gb.openssl.*
%appdir/info/gb.openssl.*

%files gb-option
%_libdir/gambas3/gb.option.*
%appdir/info/gb.option.*

%files gb-pcre
%_libdir/gambas3/gb.pcre.*
%appdir/info/gb.pcre.*

%files gb-pdf
%_libdir/gambas3/gb.pdf.component
%_libdir/gambas3/gb.pdf.so*
%_libdir/gambas3/gb.pdf.la
%appdir/info/gb.pdf.info
%appdir/info/gb.pdf.list

#files gb-qt4
#_libdir/gambas3/gb.qt4.component
#_libdir/gambas3/gb.qt4.so*
#_libdir/gambas3/gb.qt4.la
#appdir/info/gb.qt4.info
#appdir/info/gb.qt4.list

#files gb-qt4-ext
#_libdir/gambas3/gb.qt4.ext.*
#appdir/info/gb.qt4.ext.*

#files gb-qt4-opengl
#_libdir/gambas3/gb.qt4.opengl.*
#appdir/info/gb.qt4.opengl.*

#files gb-qt4-webkit
#_libdir/gambas3/gb.qt4.webkit.*
#appdir/info/gb.qt4.webkit.*
#appdir/control/gb.qt4.webkit/webview.png

%files gb-report
%_libdir/gambas3/gb.report.*
%appdir/control/gb.report/
%appdir/info/gb.report.*

%files gb-report2
%_libdir/gambas3/gb.report2.*
%appdir/control/gb.report2/
%appdir/info/gb.report2.*

%files gb-scanner
%_libdir/gambas3/gb.scanner.*
%appdir/info/gb.scanner.*

%files gb-sdl
%_libdir/gambas3/gb.sdl.component
%_libdir/gambas3/gb.sdl.so
%_libdir/gambas3/gb.sdl.so.*
%_libdir/gambas3/gb.sdl.la
%appdir/info/gb.sdl.info
%appdir/info/gb.sdl.list

%files gb-sdl-sound
%_libdir/gambas3/gb.sdl.sound.*
%appdir/info/gb.sdl.sound.*

%files gb-sdl2
%_libdir/gambas3/gb.sdl2.component
%_libdir/gambas3/gb.sdl2.so
%_libdir/gambas3/gb.sdl2.so.*
%_libdir/gambas3/gb.sdl2.la
%appdir/info/gb.sdl2.info
%appdir/info/gb.sdl2.list

%files gb-sdl2-audio
%_libdir/gambas3/gb.sdl2.audio.component
%_libdir/gambas3/gb.sdl2.audio.so
%_libdir/gambas3/gb.sdl2.audio.so.*
%_libdir/gambas3/gb.sdl2.audio.la
%appdir/info/gb.sdl2.audio.info
%appdir/info/gb.sdl2.audio.list

%files gb-settings
%_libdir/gambas3/gb.settings.*
%appdir/info/gb.settings.*

%files gb-signal
%_libdir/gambas3/gb.signal.*
%appdir/info/gb.signal.*

%files gb-util
%_libdir/gambas3/gb.util.component
%_libdir/gambas3/gb.util.gambas
%appdir/info/gb.util.info
%appdir/info/gb.util.list

%files gb-util-web
%_libdir/gambas3/gb.util.web.*
%appdir/info/gb.util.web.*
%appdir/control/gb.util.web/

%files gb-v4l
%_libdir/gambas3/gb.v4l.*
%appdir/info/gb.v4l.*

%files gb-vb
%_libdir/gambas3/gb.vb.*
%appdir/info/gb.vb.*

%files gb-web
%_libdir/gambas3/gb.web.*
%appdir/info/gb.web.*
%appdir/control/gb.web.*

%files gb-xml
%_libdir/gambas3/gb.xml.component
%_libdir/gambas3/gb.xml.gambas
%_libdir/gambas3/gb.xml.so*
%_libdir/gambas3/gb.xml.la
%appdir/info/gb.xml.info
%appdir/info/gb.xml.list

%files gb-xml-html
%_libdir/gambas3/gb.xml.html.*
%appdir/info/gb.xml.html.*

%files gb-xml-libxml
%_libdir/gambas3/gb.libxml.*
%appdir/info/gb.libxml.*

%files gb-xml-rpc
%_libdir/gambas3/gb.xml.rpc.*
%appdir/info/gb.xml.rpc.*

%files gb-xml-xslt
%_libdir/gambas3/gb.xml.xslt.*
%appdir/info/gb.xml.xslt.*

%files gb-form-editor
%_libdir/gambas3/gb.form.editor.*
%appdir/info/gb.form.editor.*
%appdir/control/gb.form.editor/

%files gb-qt5
%_libdir/gambas3/gb.qt5.component
%_libdir/gambas3/gb.qt5.so*
%_libdir/gambas3/gb.qt5.la
%appdir/info/gb.qt5.info
%appdir/info/gb.qt5.list

%files gb-qt5-opengl
%_libdir/gambas3/gb.qt5.opengl.*
%appdir/info/gb.qt5.opengl.*

%files gb-qt5-webkit
%_libdir/gambas3/gb.qt5.webkit.*
%appdir/info/gb.qt5.webkit.*
%appdir/control/gb.qt5.webkit/webview.png

%files gb-qt5-ext
%_libdir/gambas3/gb.qt5.ext.*
%appdir/info/gb.qt5.ext.*

%files gb-form-terminal
%_libdir/gambas3/gb.form.terminal.*
%appdir/info/gb.form.terminal.*
%appdir/control/gb.form.terminal/
%appdir/control/gb.term.form/

%files gb-term
%_libdir/gambas3/gb.term.*
%appdir/info/gb.term.*

%files gb-test
%_libdir/gambas3/gb.test.*
%appdir/info/gb.test.*

%files gb-form-print
%_libdir/gambas3/gb.form.print.*
%appdir/info/gb.form.print.*

%changelog
* Sat Aug 01 2020 Andrey Cherepanov <cas@altlinux.org> 3.15.1-alt1
- New version.

* Sun Jul 05 2020 Andrey Cherepanov <cas@altlinux.org> 3.15.0-alt1
- New version.
- New component gambas-gb-test.

* Sat Apr 18 2020 Andrey Cherepanov <cas@altlinux.org> 3.14.3-alt2
- Fix build (use patches for new poppler).
- Remove diplicate description.
- Do not build gambas-gb-db-sqlite2 because sqlite2 is deprecated.

* Fri Jan 24 2020 Vitaly Lipatov <lav@altlinux.ru> 3.14.3-alt1
- new version 3.14.3

* Fri Jan 24 2020 Vitaly Lipatov <lav@altlinux.ru> 3.14.2-alt2
- NMU: build without sqlite2

* Mon Dec 02 2019 Andrey Cherepanov <cas@altlinux.org> 3.14.2-alt1
- New version.

* Tue Nov 05 2019 Andrey Cherepanov <cas@altlinux.org> 3.14.1-alt1
- New version.

* Mon Oct 07 2019 Andrey Cherepanov <cas@altlinux.org> 3.14.0-alt1
- New version.
- Fix build with PostgreSQL 12.
- New component gambas-gb-form-print.

* Thu Sep 19 2019 Sergey V Turchin <zerg@altlinux.org> 3.13.0-alt2.1
- NMU: fix compile with new poopler
- NMU: fix compile on ppc64 (thanks glebfm@alt)

* Thu May 16 2019 Andrey Cherepanov <cas@altlinux.org> 3.13.0-alt2
- Build without Qt4, only with with Qt5 used for IDE by default.
- Build with libgmime3.0.

* Thu Apr 11 2019 Andrey Cherepanov <cas@altlinux.org> 3.13.0-alt1
- New version.

* Sun Mar 24 2019 Andrey Cherepanov <cas@altlinux.org> 3.12.3-alt1
- New version.

* Mon Mar 04 2019 Nikolai Kostrigin <nickel@altlinux.org> 3.12.2-alt2
- Fix FTBFS due to libpoppler Guint type issue

* Sun Jan 13 2019 Andrey Cherepanov <cas@altlinux.org> 3.12.2-alt1
- New version.

* Sun Jan 06 2019 Andrey Cherepanov <cas@altlinux.org> 3.12.1-alt1
- New version.

* Fri Dec 28 2018 Andrey Cherepanov <cas@altlinux.org> 3.12.0-alt1
- New version.
- Rename gambas-full to gambas.
- Make symlink /usr/bin/gambas to gambas3.
- Use jit.

* Wed Dec 12 2018 Nikolai Kostrigin <nickel@altlinux.org> 3.11.4-alt2
- Fix FTBFS due to bool types issues

* Wed Sep 12 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.4-alt1.1
- Rebuild with openssl 1.1.

* Tue Aug 21 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.4-alt1
- New version.

* Wed Jul 25 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.3-alt1
- New version.
- Rename from gambas3 to gambas.

* Thu Jul 20 2017 Andrey Cherepanov <cas@altlinux.org> 3.10.0-alt1
- New version (http://gambaswiki.org/wiki/doc/release/3.10.0)
- New component gambas3-gb-term

* Wed May 10 2017 Andrey Cherepanov <cas@altlinux.org> 3.9.2-alt2
- Add Russian GenericName in desktop file

* Fri Dec 30 2016 Andrey Cherepanov <cas@altlinux.org> 3.9.2-alt1
- New version (http://gambaswiki.org/wiki/doc/release/3.9.2)

* Tue Sep 06 2016 Andrey Cherepanov <cas@altlinux.org> 3.9.1-alt1
- New version (http://gambaswiki.org/wiki/doc/release/3.9.1)

* Mon Aug 22 2016 Andrey Cherepanov <cas@altlinux.org> 3.9.0-alt1
- New version (http://gambaswiki.org/wiki/doc/release/3.9.0)
- New components: gb.qt5.ext, gb.form.terminal

* Mon Apr 04 2016 Andrey Cherepanov <cas@altlinux.org> 3.8.4-alt2
- Rebuild with new poppler
- Fix build with GCC

* Wed Dec 16 2015 Andrey Cherepanov <cas@altlinux.org> 3.8.4-alt1
- New version (http://gambaswiki.org/wiki/doc/release/3.8.4)

* Thu Nov 05 2015 Andrey Cherepanov <cas@altlinux.org> 3.8.3-alt1
- New version (http://gambaswiki.org/wiki/doc/release/3.8.3)

* Wed Oct 07 2015 Andrey Cherepanov <cas@altlinux.org> 3.8.2-alt1
- New version (http://gambaswiki.org/wiki/doc/release/3.8.2)

* Sat Sep 05 2015 Andrey Cherepanov <cas@altlinux.org> 3.8.1-alt1
- New version (http://gambaswiki.org/wiki/doc/release/3.8.1)

* Sun Aug 16 2015 Andrey Cherepanov <cas@altlinux.org> 3.8.0-alt1
- New version (http://gambaswiki.org/wiki/doc/release/3.8.0)
- New components: gb.form.editor, gb.qt5, gb.qt5.opengl, gb.qt5.webkit
- Remove trailing spaces in spec file
- Add support for GTK+3 and SDL2 components
- Build without gb.jit

* Wed Apr 01 2015 Andrey Cherepanov <cas@altlinux.org> 3.7.1-alt1
- New version (http://gambaswiki.org/wiki/doc/release/3.7.1)
- Remove gambas3-examples package because IDE use online access for
  examples

* Tue Mar 17 2015 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- New version (http://gambaswiki.org/wiki/doc/release/3.7.0)
- New components:
  + gb.report2 is a new and better implementation of the reporting
    component.
  + gb.scanner is a new component based on SANE to help dealing with
    scanners.
  + gb.util is a new component written in Gambas that provides utility
    functions to the interpreter.
  + gb.util.web is a new component written in Gambas that provides
    utility functions to web applications.

* Mon Dec 01 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.6.2-alt2
- Rebuilt with llvm 3.5.0.

* Fri Nov 14 2014 Andrey Cherepanov <cas@altlinux.org> 3.6.2-alt1
- New version

* Tue Oct 14 2014 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version
- New subpackages: gambas3-gb-inotify and gambas3-gb-markdown

* Wed Jul 09 2014 Andrey Cherepanov <cas@altlinux.org> 3.5.4-alt1
- New version
- Drop obsoleted patch

* Tue Apr 15 2014 Andrey Cherepanov <cas@altlinux.org> 3.5.3-alt1
- New version

* Tue Apr 08 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.5.2-alt1.2
- Rebuilt with LLVM 3.4.

* Wed Apr 02 2014 Alexei Takaseev <taf@altlinux.org> 3.5.2-alt1.1
- Fix BuildReq postgresql-devel9.1 to postgresql-devel

* Mon Jan 13 2014 Andrey Cherepanov <cas@altlinux.org> 3.5.2-alt1
- New version

* Wed Nov 27 2013 Andrey Cherepanov <cas@altlinux.org> 3.5.1-alt1
- New version

* Fri Oct 25 2013 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt1
- New version

* Wed Aug 28 2013 Andrey Cherepanov <cas@altlinux.org> 3.4.2-alt2
- Rebuild with llvm-3.3

* Tue Jul 30 2013 Andrey Cherepanov <cas@altlinux.org> 3.4.2-alt1
- New version 3.4.2
- Add gambas3-gb-gui for gambas3-ide

* Thu Jun 06 2013 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt3
- Rebuild with new version of unixODBC

* Wed Apr 24 2013 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt2
- Rebuild with new version of poppler

* Sun Apr 07 2013 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt1
- New version 3.4.1

* Tue Mar 05 2013 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt3
- Remove dependence on llvm3.1

* Tue Feb 26 2013 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt2
- Remove missed .gambas files
- Add new components: gb.args, gb.httpd, gb.map, gb.memcached

* Mon Feb 25 2013 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version 3.4.0

* Mon Jan 21 2013 Andrey Cherepanov <cas@altlinux.org> 3.3.4-alt1
- New version 3.3.4

* Wed Feb 01 2012 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt4
- gambas3-examples  provides gambas3-full to complete installation

* Tue Jan 31 2012 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt3
- Disable OpenGL support

* Wed Jan 25 2012 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt2
- Set gambas3-examples as noarch
- Fix dependences on DejaVu font

* Mon Jan 23 2012 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus
