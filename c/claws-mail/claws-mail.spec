%define		_oldname	sylpheed-claws
%def_disable 	debug

%def_disable 	appdata
%def_enable 	svg
%ifnarch %e2k
%def_enable 	networkmanager
%else
%def_disable 	networkmanager
%endif

# pligins
%def_enable 	archive
%def_disable	bsfilter
%ifnarch %e2k
%def_disable 	dillo
%def_enable 	fancy
%else
%def_enable 	dillo
%def_disable 	fancy
%endif
%def_enable 	gdata
%def_enable 	litehtmlviewer
%ifnarch %e2k
%def_enable 	python
%else
%def_disable 	python
%endif
%def_enable 	tnef

%define _unpackaged_files_terminate_build 1

Name:   	claws-mail
Version:	3.17.4
Release: 	alt2

Summary:	Claws Mail is a GTK+ based, user-friendly, lightweight, and fast email client.
License: 	%gpl3plus
Group: 		Networking/Mail

Url:		https://www.claws-mail.org

Source: %name-%version.tar
Patch:	%name-%version-%release.patch

# Patches from upstream.
# Must be dropped with new release.
Patch1: Fix-crash-in-litehtml_viewer-when-base-tag-has-no-hr.patch
Patch2: fix-bug-4257-claws-mail-3.17.4-breaks-copy-pasting-f.patch

Obsoletes:	%_oldname < %version
Provides:	%_oldname

BuildRequires(pre): rpm-build-licenses

BuildPreReq:	autoconf-common gettext-tools

BuildRequires: flex libSM-devel libcompface-devel libdbus-glib-devel libenchant2-devel libgnutls-devel libgpgme-devel libldap-devel libstartup-notification-devel libgcrypt-devel zlib-devel
# For experimental SNI support
BuildRequires: libetpan-devel >= 1.9.1-alt3
BuildRequires: libnettle-devel
BuildRequires: libgtk+2-devel
%{?_enable_svg:BuildRequires: librsvg-devel}
%{?_enable_networkmanager:BuildRequires: libnm-devel}

# For plugin-archive:
%if_enabled archive
BuildRequires: libarchive-devel
%endif

# For plugin-fancy, plugin-libravatar, plugin-litehtmlviewer, plugin-rssyl, plugin-spamreport, plugin-vcalendar
BuildRequires: libcurl-devel

# For plugin-fancy
%if_enabled fancy
BuildRequires: libwebkitgtk2-devel
BuildRequires: libsoup-gnome-devel
%endif

# For plugin-gdata
%if_enabled gdata
BuildRequires: libgdata-devel >= 0.17.1
%endif

# For plugin-litehtmlviewer
%if_enabled litehtmlviewer
BuildRequires: gcc-c++
BuildRequires: libcairo-devel
BuildRequires: fontconfig-devel
BuildRequires: libgumbo-devel
%endif

# For plugin-rssyl
BuildRequires: libexpat-devel

# For plugin-pdfviewer
BuildRequires: libpoppler-glib-devel

# For plugin-perl
BuildRequires: perl-devel sed

# For pligin-python
%{?_enable_python:BuildRequires: python-devel python-module-pygtk-devel}

# For plugin-notification
%def_disable indicator
%def_enable hotkeys
BuildRequires: libnotify-devel
BuildRequires: libcanberra-gtk2-devel
%{?_enable_indicator:BuildRequires: libindicate-devel >=  0.3.0}
%{?_enable_hotkeys:BuildRequires: libgio-devel >= 2.15.6}

# For plugin-tnef
%if_enabled tnef
BuildRequires: libytnef-devel
%endif

# For vcalendar
BuildRequires: libical-devel

# For tools
BuildRequires:  python
BuildRequires:	python-modules-encodings
BuildPreReq:	perl-MIME-tools
BuildPreReq:	perl-Text-Iconv
BuildPreReq:	perl-XML-SimpleObject
BuildPreReq:	perl-URI
BuildPreReq: 	perl-libwww
BuildPreReq: 	perl-Text-CSV_XS

%description
Claws Mail is an email client (and news reader), based on GTK+,
featuring

    Quick response
    Graceful, and sophisticated interface
    Easy configuration, intuitive operation
    Abundant features
    Extensibility

The appearance and interface are designed to be familiar to new users
coming from other popular email clients, as well as experienced users.
Almost all commands are accessible with the keyboard.

The messages are managed in the standard MH format, which features fast
access and data security. You'll be able to import your emails from
almost any other email client, and export them just as easily.

Lots of extra functionality, like an RSS aggregator, calendar, or laptop
LED handling, are provided by extra plugins.

Claws Mail is distributed under the GPL.

%package        devel
Summary:        Development environment for %name
Group:          Development/C
Requires:	%name = %version-%release
Obsoletes:	%_oldname-devel < %version
Provides:	%_oldname-devel

%description 	devel
This package contains the header files and libraries for building
program which use %name.

%package	plugins
Summary:	Install all plugins for %name
Group:		Networking/Mail
BuildArch:	noarch
Requires:	%name = %version-%release
Requires:	%name-plugin-acpinotifier = %version-%release
Requires:	%name-plugin-addresskeeper = %version-%release
%if_enabled archive
Requires:	%name-plugin-archive = %version-%release
%endif
Requires:	%name-plugin-attachwarner = %version-%release
Requires:	%name-plugin-attremover = %version-%release
Requires:	%name-plugin-bogofilter = %version-%release
%if_enabled bsfilter
Requires:	%name-plugin-bsfilter = %version-%release
%endif
Requires:	%name-plugin-clamd = %version-%release
%if_enabled dillo
Requires:	%name-plugin-dillo = %version-%release
%endif
%if_enabled fancy
Requires:	%name-plugin-fancy = %version-%release
%endif
Requires:	%name-plugin-fetchinfo = %version-%release
%if_enabled gdata
Requires:	%name-plugin-gdata = %version-%release
%endif
Requires:	%name-plugin-libravatar = %version-%release
%if_enabled litehtmlviewer
Requires:	%name-plugin-litehtmlviewer = %version-%release
%endif
Requires:	%name-plugin-mailmbox = %version-%release
Requires:	%name-plugin-managesieve = %version-%release
Requires:	%name-plugin-newmail = %version-%release
Requires:	%name-plugin-notification = %version-%release
Requires:	%name-plugin-pdfviewer = %version-%release
Requires:	%name-plugin-perl = %version-%release
Requires:	%name-plugin-pgpcore = %version-%release
Requires:	%name-plugin-pgpinline = %version-%release
Requires:	%name-plugin-pgpmime = %version-%release
%if_enabled python
Requires:	%name-plugin-python = %version-%release
%endif
Requires:	%name-plugin-rssyl = %version-%release
Requires:	%name-plugin-smime = %version-%release
Requires:	%name-plugin-spamassassin = %version-%release
Requires:	%name-plugin-spamreport = %version-%release
%if_enabled tnef
Requires:	%name-plugin-tnef = %version-%release
%endif
Requires:	%name-plugin-vcalendar = %version-%release

%description	plugins
This virtual package installs all plugins for %name.

%package	plugin-acpinotifier
Summary:	Mail notification via LEDs on some laptops (Acer, ASUS, Fujitsu, IBM).
Group:		Networking/Mail
Requires:	%name = %version-%release

%description	plugin-acpinotifier
The AcpiNotifier plugin handles the email LED found on some laptops.
It makes it possible to see whether you have new emails from the other
side of the room, without even unlocking the screen. The plugin handles
the following types of laptops:

 * ACER,
 * ASUS,
 * IBM,
 * Fujitsu,
 and others.

%package	plugin-addresskeeper
Summary:	Keeps all recipient addresses in an addressbook folder
Group:		Networking/Mail
Requires:	%name = %version-%release

%description	plugin-addresskeeper
This plugin allows saving outgoing addresses to a designated folder
in the address book. Addresses are saved only if not found in the
address book to avoid unwanted duplicates.
Selecting which headers are scanned for keeping addresses is also
supported (Any or several of 'To', 'Cc' or 'Bcc').

%package	plugin-archive
Summary:	Mail archiving functionality for Claws Mail
Group:		Networking/Mail
Requires:	%name = %version-%release

%description	plugin-archive
This plugin adds archiving features to Claws Mail.

%package	plugin-attachwarner
Summary:	Warn when the user is likely to have forgotten to attach a file.
Group:		Networking/Mail
Requires:	%name = %version-%release

%description	plugin-attachwarner
The AttachWarner verifies that you have attached something to your email
if you mentioned attachment in the email's body.

%package	plugin-attremover
Summary:	This plugin lets you remove attachments from emails
Group:		Networking/Mail
Requires:	%name = %version-%release

%description	plugin-attremover
This plugin lets you remove attachments from emails.

%package	plugin-bogofilter
Summary:	Bogofilter plugin for %name
Group:		Networking/Mail
Requires:	%name = %version-%release
Requires:	bogofilter bogofilter-utils
Obsoletes:	%_oldname-plugin-bogofilter < %version
Provides:	%_oldname-plugin-bogofilter

%description	plugin-bogofilter
This plugin for %name provides integration with Bogofilter spam checking
tool.

%package	plugin-bsfilter
Summary:	Check messages for spam using Bsfilter
Group:		Networking/Mail
Requires:	%name = %version-%release
Requires:	bsfilter

%description	plugin-bsfilter
Check all messages that are received from an IMAP, LOCAL or POP account
for spam using Bsfilter.

%package	plugin-clamd
Summary:	This plugin scans messages using clamd (Clam AV)
Group:		Networking/Mail
Requires:	%name = %version-%release
Requires:	clamav

%description	plugin-clamd
This plugin scans all messages that are received from an IMAP, LOCAL or
POP account using clamd (Clam AV).

%package       plugin-dillo
Summary:       Dillo browser plugin for %name
Group:         Networking/Mail
Requires:      %name = %version
Requires:      dillo >= 0.7.2
Obsoletes:     %_oldname-plugin-dillo < %version
Provides:      %_oldname-plugin-dillo

%description   plugin-dillo
This plugin uses the Dillo (http://www.dillo.org) browser to
view text/html MIME parts inside Claws Mail.
See README file for more information.

This plugin only provides very basic HTML
support; if you want something more, consider installing
%name-plugin-fancy package.

%package	plugin-fancy
Summary:	Renders HTML e-mail using the WebKit library
Group:		Networking/Mail
Requires:	%name = %version-%release

%description	plugin-fancy
The Fancy plugin renders html email using the GTK+ port of WebKit
library.

%package	plugin-fetchinfo
Summary:	This plugin inserts headers containing some download information
Group:		Networking/Mail
Requires:	%name = %version-%release

%description	plugin-fetchinfo
This plugin inserts headers containing some download information: UIDL,
Claws' account name, POP server, user ID and retrieval time.

%package	plugin-gdata
Summary:	Access to GData (Google services) for Claws Mail
Group:		Networking/Mail
Requires:	%name = %version-%release

%description	plugin-gdata
Access to GData (Google services) for Claws Mail.
The only currently implemented feature is inclusion of
Google contacts into the Tab-address completion.

%package	plugin-libravatar
Summary:	Pligin displays libravatar/gravatar profiles' images
Group:		Networking/Mail
Requires:	%name = %version-%release

%description	plugin-libravatar
This plugin allows showing the profile picture associated to email
addresses provided by https://www.libravatar.org/. You can read
more about what is this at http://wiki.libravatar.org/description/.
By default missing profiles in the libravatar site are also searched
in http://gravatar.com, so it will also show pictures from gravatar
profiles.

%package	plugin-litehtmlviewer
Summary:	Viewer plugin for HTML emails, using the litehtml library
Group:		Networking/Mail
License:	%gpl3plus,%bsdstyle
Requires:	%name = %version-%release

%description	plugin-litehtmlviewer
Viewer plugin for HTML emails, using the litehtml library
(http://www.litehtml.com/).

%package	plugin-mailmbox
Summary:	This plugin handles mailboxes in mbox format
Group:		Networking/Mail
Requires:	%name = %version-%release

%description	plugin-mailmbox
This plugin handles mailboxes in mbox format.

%package	plugin-managesieve
Summary:	This plugin handles managing Sieve filters
Group:		Networking/Mail
Requires:	%name = %version-%release

%description	plugin-managesieve
The Claws Mail ManageSieve plugin provides an interface for managing
Sieve filters. Sieve filters are used for filtering mail on mail
servers, usually with an IMAP account.

This plugin handles managing Sieve filters, editing them, and checking
their syntax.

To learn how to write Sieve filters, see RFC 5228
https://tools.ietf.org/html/rfc5228
and the Sieve language extensions
http://sieve.info/documents#sieve_language_extensions

%package	plugin-newmail
Summary:	This plugin writes a msg header summary to a log file
Group:		Networking/Mail
Requires:	%name = %version-%release

%description	plugin-newmail
This plugin writes a msg header summary to a log file,
(Default: ~/Mail/NewLog), on arrival of new mail *after* sorting.

%package	plugin-notification
Summary:	Various ways to notify the user of new and unread email
Group:		Networking/Mail
Requires:	%name = %version-%release

%description	plugin-notification
The Notification plugin provides various ways to notify the user of new
and possibly unread mail. Currently, the following modules are
implemented:

    * A mail banner (stocks ticker-like widget)
    * A popup window
    * A command to be issued on new mail arrival

All modules can be activated or deactivated at compilation time, and are
highly configurable at run time. It is possible to include only selected
folders in any module. In general, the notification is executed after
filtering, so it is possible to exclude spam or other unwanted messages
from notification.

%package	plugin-pdfviewer
Summary:	This plugin enables the viewing of PDF and PostScript attachments
Group:		Networking/Mail
Requires:	%name = %version-%release

%description	plugin-pdfviewer
The PDF Viewer plugin renders PDF and Postscript attachments in Claws
Mail. It features:

  * Moving between document pages, sequentially and jumping to
    a specific page
  * Zoom, Rotation, Fit Page, Fit Page Width
  * Displaying information about the document such as Author, Date,
    Creator, etc...
  * Displaying the PDF Index, if available, which allows easily surfing
    the document
  * Search text inside the document
  * Manage links to internal and external documents, if available, such
    as jumping to the paragraph or section and also opening an external
    URL or composing a new mail

The Poppler library and GhostScript are required.

%package	plugin-perl
Summary:	This plugin provides a Perl interface to Claws Mail' filtering mechanism
Group:		Networking/Mail
Requires:	%name = %version-%release
Requires:	perl

%description	plugin-perl
This plugin is intended to extend the filtering possibilities of Claws
Mail. It provides a Perl interface to Claws Mail' filtering mechanism,
allowing the use of full Perl power in email filters.

%package	plugin-pgpcore
Summary:	Core PGP plugin for %name
Group:		Networking/Mail
Requires:	%name = %version-%release
Obsoletes:	%_oldname-plugin-pgpcore < %version
Provides:	%_oldname-plugin-pgpcore

%description	plugin-pgpcore
This plugin for %name provides core PGP functionality. It is used by
other encryption/signing plugins.

%package	plugin-pgpinline
Summary:	PGP/Inline plugin for %name
Group:		Networking/Mail
Requires:	%name = %version-%release
Requires:	%name-plugin-pgpcore = %version-%release
Obsoletes:	%_oldname-plugin-pgpinline < %version
Provides:	%_oldname-plugin-pgpinline

%description	plugin-pgpinline
This plugin for %name lets you create and see messages encrypted/signed
with PGP/Inline.

%package	plugin-pgpmime
Summary:	PGP/MIME plugin for %name
Group:		Networking/Mail
Requires:	%name = %version-%release
Requires:	%name-plugin-pgpcore = %version-%release
Obsoletes:	%_oldname-plugin-pgpmime < %version
Provides:	%_oldname-plugin-pgpmime

%description	plugin-pgpmime
This plugin for %name lets you create and see messages encrypted/signed
with PGP/MIME.

%package	plugin-python
Summary:	This plugin provides Python integration features
Group:		Networking/Mail
Requires:	%name = %version-%release
Requires:	python

%description	plugin-python
This plugin offers Python scripting access to Claws Mail.
Python code can be entered interactively into an embedded Python
console, or stored in scripts.

%package	plugin-rssyl
Summary:	RSS feed aggregator for Claws Mail
Group:		Networking/Mail
Requires:	%name = %version-%release

%description	plugin-rssyl
he RSSyl plugin is an RSS feed aggregator for Claws Mail. It has the
following features:

    * Handling of RSS 1.0, RSS 2.0, and Atom feeds
    * Fetching and threaded display of comment feeds
    * Customisable refresh interval for each feed
    * Customisable number of feed items to keep for each feed

Navigating in your feeds and posts is done in the same way as you would
for emails, which makes feed-reading really fast and enjoyable if Claws
Mail's shortcuts are hardwired into your fingers.
Also, the RSSyl plugin unleashes its full potential when used with an
HTML viewer plugin like Dillo or Gtkhtml2Viewer, as this allows fetching
a post's images and font styles.

%package	plugin-smime
Summary:	S/MIME plugin for %name
Group:		Networking/Mail
Requires:	%name = %version-%release
Requires:	%name-plugin-pgpcore = %version-%release
Requires:   dirmngr gnupg2-common
Obsoletes:	%_oldname-plugin-smime < %version
Provides:	%_oldname-plugin-smime

%description	plugin-smime
This plugin for %name lets you create and see messages encrypted/signed
with S/MIME.

%package	plugin-spamassassin
Summary:	SpamAssassin plugin for %name
Group:		Networking/Mail
Requires:	%name = %version-%release
Requires:	spamassassin
Obsoletes:	%_oldname-plugin-spamassassin < %version
Provides:	%_oldname-plugin-spamassassin

%description	plugin-spamassassin
This plugin for %name provides integration with SpamAssassin.

%package	plugin-spamreport
Summary:	This plugin reports spam to various places
Group:		Networking/Mail
Requires:	%name = %version-%release

%description	plugin-spamreport
This Claws Mail plugin allows you to upload your spams to various spam
reporting places, like http://www.signal-spam.fr/ or http://www.spamcop.net/.

%package	plugin-tnef
Summary:	This plugin enables reading application/ms-tnef attachments
Group:		Networking/Mail
Requires:	%name = %version-%release

%description	plugin-tnef
The TNEF Parser plugins handles TNEF attachments from Outlook.
TNEF attachments have a MIME type of "application/ms-tnef" and
are often named "winmail.dat". They can contain multiple files.
This plugin parses this kind of attachment and displays the real files
in the parts list.

%package	plugin-vcalendar
Summary:	Plugin handles the vCalendar for Claws Mail
Group:		Networking/Mail
Requires:	%name = %version-%release

%description	plugin-vcalendar
This Claws Mail plugin handles the vCalendar format (or rather, the
meeting subset of it). It displays such mails in a nice format, lets you
create and send meetings, and creates a virtual folder with the meetings
you sent or received.

%package	tools
Summary:	Additional tools for %name
Group:		Networking/Mail
Requires:	%name = %version-%release
Requires:	python

BuildArch: noarch

Obsoletes:	%_oldname-tools < %version
Provides:	%_oldname-tools

%description	tools
additional tools for %name.

%prep
%setup

subst "s,\#\!/usr/bin/perl,\#\!/usr/bin/perl -w," tools/OOo2claws-mail.pl
subst "s,%%f,%%N," ./src/prefs_quote.c
echo "Libs: -lenchant-2 -lgnutls" >>%name.pc.in

# set version
echo 'echo "%version"' >./version

%patch -p1
%patch1 -p1
%patch2 -p1

%autoreconf

%build
%add_optflags -fpie
export LDFLAGS=-pie
%configure \
		--disable-static \
		--disable-rpath \
		--with-lib-prefix=%_usr \
		--with-faqdir=%_datadir/%name \
		--with-manualdir=%_datadir/%name \
		--with-config-dir=.%name \
		--disable-manual \
		--disable-jpilot \
		%{subst_enable appdata} \
		%{subst_enable svg} \
		%{subst_enable networkmanager} \
		%if_disabled archive
		--disable-archive-plugin \
		%endif
		%if_disabled bsfilter
		--disable-bsfilter-plugin \
		%endif
		%if_disabled dillo
		--disable-dillo-plugin \
		%endif
		%if_disabled fancy
		--disable-fancy-plugin \
		%endif
		%if_disabled gdata
		--disable-gdata-plugin \
		%endif
		%if_disabled litehtmlviewer
		--disable-litehtml_viewer-plugin \
		%endif
		%if_disabled python
		--disable-python-plugin \
		%endif
		%if_disabled tnef
		--disable-tnef_parse-plugin \
		%endif
		%if_enabled debug
		--enable-crash-dialog
		%else
		--disable-crash-dialog
		%endif
%make_build
%make -C tools

%install
%makeinstall_std
%make -C tools install

mkdir -p %buildroot%_datadir/%name/
cp -va  tools %buildroot%_datadir/%name/
rm -vf  %buildroot%_datadir/%name/tools/README*
rm -vf  %buildroot%_datadir/%name/tools/Makefile*

mkdir -p %buildroot%_pixmapsdir
install -p -m644 %name.png %buildroot%_pixmapsdir/

# XXX: Make sure the path below is the same as the path above.
%define _claws_plugins_path %_libdir/%name/plugins

%if_enabled litehtmlviewer
# Install litehtml BSD 3-clause license
mkdir -p %buildroot%_defaultdocdir/%name-plugin-litehtmlviewer-%version/litehtml/
install -p -m644 src/plugins/litehtml_viewer/litehtml/LICENSE %buildroot%_defaultdocdir/%name-plugin-litehtmlviewer-%version/litehtml/
%endif

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog* COPYING INSTALL NEWS README* TODO* RELEASE_NOTES 
%_bindir/%name
%_man1dir/%name.1.*
%_desktopdir/*.desktop
%if_enabled appdata
%_datadir/appdata/claws-mail.appdata.xml
%endif
%_iconsdir/hicolor/*x*/apps/%name.png
%_pixmapsdir/%name.png
%dir %_libdir/%name
%dir %_claws_plugins_path
%dir %_datadir/%name

%files devel
%_includedir/%name
%_pkgconfigdir/%name.pc

%files plugins

%files plugin-spamassassin
%doc src/plugins/spamassassin/README* src/plugins/spamassassin/NOTICE
%_claws_plugins_path/spamassassin.so
%if_enabled appdata
%_datadir/appdata/claws-mail-spamassassin.metainfo.xml
%endif

%files plugin-bogofilter
%_claws_plugins_path/bogofilter.so
%if_enabled appdata
%_datadir/appdata/claws-mail-bogofilter.metainfo.xml
%endif

%files plugin-pgpcore
%_claws_plugins_path/pgpcore.so
%if_enabled appdata
%_datadir/appdata/claws-mail-pgpcore.metainfo.xml
%endif

%files plugin-pgpmime
%_claws_plugins_path/pgpmime.so
%_claws_plugins_path/pgpmime.deps
%if_enabled appdata
%_datadir/appdata/claws-mail-pgpmime.metainfo.xml
%endif

%files plugin-pgpinline
%_claws_plugins_path/pgpinline.so
%_claws_plugins_path/pgpinline.deps
%if_enabled appdata
%_datadir/appdata/claws-mail-pgpinline.metainfo.xml
%endif

%files plugin-smime
%_claws_plugins_path/smime.so
%_claws_plugins_path/smime.deps
%if_enabled appdata
%_datadir/appdata/claws-mail-smime.metainfo.xml
%endif

%files plugin-acpinotifier
%_claws_plugins_path/acpi_notifier.so
%if_enabled appdata
%_datadir/appdata/claws-mail-acpi_notifier.metainfo.xml
%endif

%files plugin-addresskeeper
%_claws_plugins_path/address_keeper.so
%if_enabled appdata
%_datadir/appdata/claws-mail-address_keeper.metainfo.xml
%endif

%if_enabled archive
%files plugin-archive
%_claws_plugins_path/archive.so
%if_enabled appdata
%_datadir/appdata/claws-mail-archive.metainfo.xml
%endif
%endif

%files plugin-attachwarner
%_claws_plugins_path/attachwarner.so
%if_enabled appdata
%_datadir/appdata/claws-mail-attachwarner.metainfo.xml
%endif

%files plugin-attremover
%_claws_plugins_path/att_remover.so
%if_enabled appdata
%_datadir/appdata/claws-mail-att_remover.metainfo.xml
%endif

%if_enabled bsfilter
%files plugin-bsfilter
%_claws_plugins_path/bsfilter.so
%if_enabled appdata
%_datadir/appdata/claws-mail-bsfilter.metainfo.xml
%endif
%endif

%files plugin-clamd
%_claws_plugins_path/clamd.so
%if_enabled appdata
%_datadir/appdata/claws-mail-clamd.metainfo.xml
%endif

%if_enabled dillo
%files plugin-dillo
%_claws_plugins_path/dillo.so
%if_enabled appdata
%_datadir/appdata/claws-mail-dillo.metainfo.xml
%endif
%endif

%if_enabled fancy
%files plugin-fancy
%_claws_plugins_path/fancy.so
%if_enabled appdata
%_datadir/appdata/claws-mail-fancy.metainfo.xml
%endif
%endif

%files plugin-fetchinfo
%_claws_plugins_path/fetchinfo.so
%if_enabled appdata
%_datadir/appdata/claws-mail-fetchinfo.metainfo.xml
%endif

%if_enabled gdata
%files plugin-gdata
%_claws_plugins_path/gdata.so
%if_enabled appdata
%_datadir/appdata/claws-mail-gdata.metainfo.xml
%endif
%endif

%files plugin-libravatar
%doc src/plugins/libravatar/README*
%_claws_plugins_path/libravatar.so
%if_enabled appdata
%_datadir/appdata/claws-mail-libravatar.metainfo.xml
%endif

%if_enabled litehtmlviewer
%files plugin-litehtmlviewer
%doc %_defaultdocdir/%name-plugin-litehtmlviewer-%version/
%_claws_plugins_path/litehtml_viewer.so
%endif

%files plugin-mailmbox
%_claws_plugins_path/mailmbox.so
%if_enabled appdata
%_datadir/appdata/claws-mail-mailmbox.metainfo.xml
%endif

%files plugin-managesieve
%_claws_plugins_path/managesieve.so
%if_enabled appdata
%_datadir/appdata/claws-mail-managesieve.metainfo.xml
%endif

%files plugin-newmail
%_claws_plugins_path/newmail.so
%if_enabled appdata
%_datadir/appdata/claws-mail-newmail.metainfo.xml
%endif

%files plugin-notification
%_claws_plugins_path/notification.so
%if_enabled appdata
%_datadir/appdata/claws-mail-notification.metainfo.xml
%endif

%files plugin-pdfviewer
%_claws_plugins_path/pdf_viewer.so
%if_enabled appdata
%_datadir/appdata/claws-mail-pdf_viewer.metainfo.xml
%endif

%files plugin-perl
%_claws_plugins_path/perl.so
%if_enabled appdata
%_datadir/appdata/claws-mail-perl.metainfo.xml
%endif

%if_enabled python
%files plugin-python
%_claws_plugins_path/python.so
%if_enabled appdata
%_datadir/appdata/claws-mail-python.metainfo.xml
%endif
%endif

%files plugin-rssyl
%_claws_plugins_path/rssyl.so
%if_enabled appdata
%_datadir/appdata/claws-mail-rssyl.metainfo.xml
%endif

%files plugin-spamreport
%_claws_plugins_path/spamreport.so
%if_enabled appdata
%_datadir/appdata/claws-mail-spam_report.metainfo.xml
%endif

%if_enabled tnef
%files plugin-tnef
%_claws_plugins_path/tnef_parse.so
%if_enabled appdata
%_datadir/appdata/claws-mail-tnef_parse.metainfo.xml
%endif
%endif

%files plugin-vcalendar
%_claws_plugins_path/vcalendar.so
%if_enabled appdata
%_datadir/appdata/claws-mail-vcalendar.metainfo.xml
%endif

%files tools
%doc tools/README*
%_datadir/%name/tools/
%exclude %_datadir/%name/tools/update-po
%exclude %_datadir/%name/tools/check-appstream.sh
%exclude %_datadir/%name/tools/ca-certificates.crt

%exclude %_claws_plugins_path/*.la
%exclude %_datadir/doc/%name/RELEASE_NOTES

%changelog
* Fri Oct 18 2019 Mikhail Efremov <sem@altlinux.org> 3.17.4-alt2
- Patches from upstream:
  + Fix crash in litehtml_viewer when <base> tag has no href.
  + fix bug 4257, 'claws-mail 3.17.4 breaks copy-pasting from
    emacs-gtk3' (closes: #37347).

* Wed Jul 31 2019 Mikhail Efremov <sem@altlinux.org> 3.17.4-alt1
- Package litehtml_viewer plugin.
- Updated to 3.17.4.

* Tue Mar 12 2019 Mikhail Efremov <sem@altlinux.org> 3.17.3-alt3
- Patches from upstream:
  + Fix buf #4166: corrupted double-linked list.
  + Fix possible segmentation fault.
  + Check result of fputs (CID 1440024).
  + Check writting crash-indicator (CID 1440021).
  + Fix a small memory leak in rssyl_remove_msgs().

* Fri Feb 01 2019 Mikhail Efremov <sem@altlinux.org> 3.17.3-alt2
- Patches from upstream:
  + Fix possible stack overflow in vcalendar's Curl data handler.
  + Fix crash when LDAP address source is defined in index, but LDAP
    support is disabled.
  + Make children tracking in execute_actions() more async-aware.
  + Fix an impossible to trigger buffer overflow.
  + fix bug 4143, 'fingerprint in SSL/TLS certificates for ...
    (regress error)'.
  + Fix few (possible) crashes due to missing return code checks.
  + Fix use after free in rare code path in rssyl_subscribe().

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 3.17.3-alt1.1
- rebuild with new perl 5.28.1

* Mon Dec 24 2018 Mikhail Efremov <sem@altlinux.org> 3.17.3-alt1
- Fix Russian translation.
- Drop upstreamed patch.
- Updated to 3.17.3.

* Fri Dec 14 2018 Mikhail Efremov <sem@altlinux.org> 3.17.2-alt1
- Drop sylpheed-claws symlink.
- Drop gtk3 support from spec.
- Updated to 3.17.2.

* Tue Oct 30 2018 Mikhail Efremov <sem@altlinux.org> 3.17.1-alt3
- Add experimental SNI support.

* Mon Oct 22 2018 Mikhail Efremov <sem@altlinux.org> 3.17.1-alt2
- Disable PDA support.

* Mon Aug 27 2018 Mikhail Efremov <sem@altlinux.org> 3.17.1-alt1
- Updated to 3.17.1.

* Fri Aug 17 2018 Mikhail Efremov <sem@altlinux.org> 3.17.0-alt1
- Updated to 3.17.0.

* Thu Jun 28 2018 Mikhail Efremov <sem@altlinux.org> 3.16.0-alt3
- Add libnettle-devel to BR.
- Require libnm-devel instead of NetworkManager-devel.
- Patches from upstream:
  + Fix bug 3895: Port from libnm-util/libnm-glib to libnm.
  + Fix a buffer overflow in password encryption, and allow arbitrary
    password length.
  + require nettle, following removal of libcrypt from glibc.
- Add e2k build support.
- Add knob to disable python plugin.
- Add NetworkManager support knob.

* Fri Feb 02 2018 Mikhail Efremov <sem@altlinux.org> 3.16.0-alt2
- Drop libnsl check.

* Mon Dec 18 2017 Mikhail Efremov <sem@altlinux.org> 3.16.0-alt1
- tools: Don't package acient ca-certificates.crt.
- Highest priority for /etc/pki/tls/certs/ca-bundle.crt.
- Build with -pie.
- tools: Don't pull wget.
- tools: Don't pull ImageMagick-tools.

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 3.15.1-alt1.1
- rebuild with new perl 5.26.1

* Fri Sep 01 2017 Mikhail Efremov <sem@altlinux.org> 3.15.1-alt1
- Updated to 3.15.1.

* Mon Mar 27 2017 Mikhail Efremov <sem@altlinux.org> 3.15.0-alt1
- Add build switch for fancy plugin.
- Spec cleanup.
- Add Dillo pligin support, but disable it for now.
- Enable librsvg support.
- Updated to 3.15.0.

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 3.14.1-alt1.1
- rebuild with new perl 5.24.1

* Thu Nov 10 2016 Mikhail Efremov <sem@altlinux.org> 3.14.1-alt1
- Fix BR (by Repocop Q. A. Robot).
- Move claws-mail.png to %%_pixmapsdir (closes: #32112).
- Updated to 3.14.1.

* Mon Aug 22 2016 Mikhail Efremov <sem@altlinux.org> 3.14.0-alt1
- Fixes from upstream.
- Updated to 3.14.0.

* Thu Jun 16 2016 Mikhail Efremov <sem@altlinux.org> 3.13.2-alt2
- Rebuild with libetpan-1.7.2.

* Tue Jan 19 2016 Mikhail Efremov <sem@altlinux.org> 3.13.2-alt1
- Updated to 3.13.2.

* Mon Jan 18 2016 Mikhail Efremov <sem@altlinux.org> 3.13.1-alt3
- Patch from upstream:
  + fix CVE-2015-8708, bug 3557, 'Remotely exploitable bug.'.

* Mon Dec 28 2015 Mikhail Efremov <sem@altlinux.org> 3.13.1-alt2
- Enable tnef plugin.
- Patches from upstream:
  + fix bug 3584, 'After 3.13.1, characters in some Japanese codec
    are never correctly converted to internal ones'.
  + comment out the paragraphs which no longer apply.
  + late, post-release pt_BR.po update.

* Mon Dec 21 2015 Mikhail Efremov <sem@altlinux.org> 3.13.1-alt1
- Use Russian translation from upstream.
- Updated to 3.13.1.

* Wed Dec 16 2015 Mikhail Efremov <sem@altlinux.org> 3.13.0-alt5
- Enable archive plugin again.

* Fri Dec 11 2015 Mikhail Efremov <sem@altlinux.org> 3.13.0-alt4
- Disable archive plugin.

* Thu Dec 03 2015 Mikhail Efremov <sem@altlinux.org> 3.13.0-alt3
- Patches from upstream:
    + Fix 'end of file' message on checking sign of a key not
      found.
- Don't explicitly specify man page's extension.
- Rebuild with gnutls-3.4.7.

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 3.13.0-alt2.1
- rebuild with new perl 5.22.0

* Fri Nov 20 2015 Igor Vlasenko <viy@altlinux.ru> 3.13.0-alt2
- bugfix for perl 5.22

* Mon Oct 26 2015 Mikhail Efremov <sem@altlinux.org> 3.13.0-alt1
- Patches from upstream:
  + fix syntax error
  + Fix Debian bug #801375 "Segfault when activating
    the plugin with the Code from Google"
  + fix bug 3375, 'Crash (SEGV) at gtkcmctree.c:4514 after deleting
    an unread message'
- Drop geolocation plugin from spec.
- Updated to 3.13.0.

* Mon Oct 05 2015 Mikhail Efremov <sem@altlinux.org> 3.12.0-alt3
- Patches from upstream:
  + Fix several memory leaks in RSSyl.
  + Fix string leaks.
  + managesieve: fix memory leak.
  + fix bug 3531, 'a/z hotkeys crash Claws immediately after startup'.
  + Fix crash on double notification popup.
  + Fix crash in address completion when matching group name.
  + managesieve: close windows when unloading.

* Wed Aug 12 2015 Mikhail Efremov <sem@altlinux.org> 3.12.0-alt2
- Enable gdata plugin again.

* Tue Jul 21 2015 Mikhail Efremov <sem@altlinux.org> 3.12.0-alt1
- Disable gdata plugin (it requires libgdata >= 0.17.1).
- Package new managesieve plugin.
- Use Russian translation again.
- Updated to 3.12.0.

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 3.11.1-alt2.1
- rebuild with new perl 5.20.1

* Thu Nov 06 2014 Mikhail Efremov <sem@altlinux.org> 3.11.1-alt2
- Drop rpm-macros-claws-mail subpackage.
- Drop obsoleted substs.
- Add Russion translation from Serg A. Kotlyarov.

* Tue Oct 28 2014 Mikhail Efremov <sem@altlinux.org> 3.11.1-alt1
- Fixes from upstream git:
  + Recover desktop file installation.
  + Fix categories and recover keywords in desktop file.
- Disable appdata and update BR.
- Updated to 3.11.1.

* Wed Oct 22 2014 Mikhail Efremov <sem@altlinux.org> 3.11.0-alt1
- Fixes from upstream git:
  + Use gnutls_priority override also for POP3 connections.
  + RSSyl: fix markup escaping in one more alertpanel_error in
    rssyl_update_feed().
  + fix bug 3306, 'HTML tag </b> is not always rendered in error
    dialog'.
  + use standard hyphen-less "Claws Mail" in user-facing
    strings.
  + fix some missing whitespace, and standardise the placement of
    the whitespace.
  + some improvement to appdata summaries.
- tools: Don't package check-appstream script.
- Explicitly enable build with appdata.
- Updated BR.
- Updated to 3.11.0.

* Fri Aug 22 2014 Mikhail Efremov <sem@altlinux.org> 3.10.1-alt3
- Rebuild with libetpan-1.5.

* Fri Aug 22 2014 Mikhail Efremov <sem@altlinux.org> 3.10.1-alt2
- Rebuild with libgdata-0.15.2.

* Mon Jun 16 2014 Mikhail Efremov <sem@altlinux.org> 3.10.1-alt1
- Updated to 3.10.1.

* Mon May 26 2014 Mikhail Efremov <sem@altlinux.org> 3.10.0-alt1
- Fixes from upstream git:
    + Fix GCond use with newer Glib.
    + added Esperanto and re-instated Dutch.
- Package README files for spamassassin and libravatar plugins.
- Package appdata helper file.
- Package libravatar plugin.
- Fix menu categories.

* Mon Dec 16 2013 Mikhail Efremov <sem@altlinux.org> 3.9.3-alt1
- Fixes from upstream git:
    + Fix parsing universal time zone in mailmbox.
    + fix typo.
- Updated to 3.9.3.

* Mon Sep 02 2013 Vladimir Lettiev <crux@altlinux.ru> 3.9.2-alt2
- built for perl 5.18

* Mon Jun 17 2013 Mikhail Efremov <sem@altlinux.org> 3.9.2-alt1
- Fixes from upstream git:
    + fix a bunch of compiler warnings.
    + Revert undesired effect of fixing bug #2927.
    + fix debian bug #711864, 'claws-mail-vcalendar-plugin:
       when creating meeting GTK_IS_COMBO_BOX_TEXT failed'.
    + fix double-free crasher in Edit Accounts dialogue.
- Updated to 3.9.2.

* Wed May 15 2013 Mikhail Efremov <sem@altlinux.org> 3.9.1-alt1
- Use strict dependences on Claws Mail in the subpackages.
- Add claws-mail-plugins virtual subpackage.
- Set Claws version.
- Drop obsoleted plugins.
- Updated spec for new version.
- Updated to 3.9.1.

* Tue Dec 25 2012 Mikhail Efremov <sem@altlinux.org> 3.9.0-alt2
- Fix 'paths for SSL certs' patch.
- Patch from upstream:
    + Fix marking mails for deletion.

* Thu Nov 29 2012 Mikhail Efremov <sem@altlinux.org> 3.9.0-alt1
- Drop obsoleted patches.
- Updated to 3.9.0.

* Thu Oct 11 2012 Mikhail Efremov <sem@altlinux.org> 3.8.1-alt4
- Use ALT-specific paths for SSL certs.
- Patches from upstream:
    + Fix null pointer crash in procmime strchr.
    + Fix potential buffer overflow.
    + Fix failure to check peer hostname when checking certificate.
    + Fix segfault when trying to view info about pgp/smime sign.
- Own forgotten directories.

* Thu Jul 12 2012 Mikhail Efremov <sem@altlinux.org> 3.8.1-alt3
- Fix segfault in parse_parameters().

* Tue Jul 03 2012 Mikhail Efremov <sem@altlinux.org> 3.8.1-alt2
- Subpackages tools and rpm-macros-claws-mail are noarch.
- Rebuild against libetpan.so.16.0.0.

* Fri Jun 29 2012 Mikhail Efremov <sem@altlinux.org> 3.8.1-alt1
- Updated to 3.8.1.

* Wed Jan 18 2012 Mikhail Efremov <sem@altlinux.org> 3.8.0-alt1
- Drop obsoleted patches.
- Updated to 3.8.0.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.10-alt1.1
- Rebuild with Python-2.7

* Fri Sep 02 2011 Mikhail Efremov <sem@altlinux.org> 3.7.10-alt1
- Drop module-load-dirty-fix.patch.
- Drop obsoleted patches.
- Fix crash with long MIME type in the header.
- Updated to 3.7.10.

* Tue May 31 2011 Mikhail Efremov <sem@altlinux.org> 3.7.9-alt2
- Rebuild for NM-0.9 support.

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 3.7.9-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * altlinux-policy-rpm-macros-packaging for claws-mail-devel

* Tue May 03 2011 Mikhail Efremov <sem@altlinux.org> 3.7.9-alt1
- Patches from upstream CVS:
   + Don't show message on right click.
   + Work around for a bug in Gnome Shell.
   + Fix segfault on startup (thanks aris@, closes: #25555).
- Minor spec cleanup.
- Sources: tar.bz2 -> tar.
- Updated to 3.7.9 (closes: #25532).

* Mon Apr 04 2011 Mikhail Efremov <sem@altlinux.org> 3.7.8-alt2
- Fix BR: add libgcrypt-devel and zlib-devel.

* Thu Dec 30 2010 Mikhail Efremov <sem@altlinux.org> 3.7.8-alt1
- textviewer.pl: Added 'gz' extension handler.
- Updated to 3.7.8

* Wed Dec 01 2010 Mikhail Efremov <sem@altlinux.org> 3.7.7-alt2
- tools: don't package update-po script
- textviewer.sh: remove color codes from plain text.
- tools: to masquerade huge and unnecessary dependences.

* Mon Nov 29 2010 Mikhail Efremov <sem@altlinux.org> 3.7.7-alt1
- Updated to 3.7.7

* Thu Jul 22 2010 Mikhail Efremov <sem@altlinux.org> 3.7.6-alt1
- new version (closes: #23780).
- fix undo/redo after replace selected text from context menu.

* Fri Jan 15 2010 Alexey Rusakov <ktirf@altlinux.org> 3.7.4-alt1
- new version.
- patch for ru.po went upstream.
- desktop file installation went upstream.

* Mon Oct 26 2009 Alexey Rusakov <ktirf@altlinux.org> 3.7.3-alt1
- new version (3.7.3).
- patch for crashes after editing displayed headers went upstream.

* Tue Sep 01 2009 Alexey Rusakov <ktirf@altlinux.org> 3.7.2-alt1.1
- rebuild with libldap2.4.

* Wed Jul 08 2009 Alexey Rusakov <ktirf@altlinux.org> 3.7.2-alt1
- new version (3.7.2), with a fix for the Russian translation.
- the fix for building with Automake 1.11 went upstream.
- fixed a crash after editing displayed headers (closes ALT bug 10044).

* Tue May 26 2009 Alexey Rusakov <ktirf@altlinux.org> 3.7.1-alt1
- 3.7.1.
- removed obsolete post/postun macros.
- spec cleanup: use better macros in files list, don't use %%__ macros.
- fixed building with Automake 1.11.
- excluded *.a and *.la files from packaging explicitly.
- package .deps files for plugins that depend on other plugins.
- made plugin descriptions more telling, removed periods from Summaries.
- added %%_claws_plugins_path macro.
- packaged S/MIME plugin.
- added proper Libs: clause to the .pc file so that plugins don't have
  to install additional -devel packages just because there's no them in
  claws-mail-devel dependencies.

* Thu Oct 16 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.6.1.cvs5-alt1.2
-  build with fixed libetpan.

* Mon Oct 13 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.6.1.cvs5-alt1.1
-  build with new libgnutls (libgnutls-new).

* Mon Oct 13 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.6.1.cvs5-alt1
-  Remove OpenSSL code (upstream);
-  BuildReq actualization.

* Sat Oct 11 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.6.1.cvs3-alt1
-  some ssl fixes (upstream).

* Fri Oct 10 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.6.1-alt1
-  3.6.1;
-  use gnutls instead of openssl.

* Mon Oct 06 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.6.0.cvs7-alt1
-  3.6.0.

* Mon Aug 11 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.5.0.cvs57-alt1
-  3.5.0.

* Mon May 19 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.4.0.cvs51-alt1
-  3.4.0.cvs51; 
-  build with networkmanager support.

* Thu Apr 24 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.4.0.cvs10-alt1
-  3.4.0.

* Mon Mar 31 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.3.1.cvs47-alt1
-  fix segfault if /home is full (upstream);
-  add support for png themes (upstream);
-  learn bogofilter from whitelist (upstream).

* Tue Mar 18 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.3.1.cvs30-alt1
-  3.3.1.

* Mon Feb 11 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.3.0.cvs5-alt1
-  3.3.0;
-  remove clamav plugin (upstream, see ChangeLog);
-  remove "kostyli" for old autotools. 

* Thu Jan 10 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.2.0.cvs34-alt1
-  3.2.0.

* Fri Nov 23 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.1.0.cvs26-alt1
-  3.1.0;
-  #13127 fix.

* Thu Oct 11 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.0.2.cvs57-alt1
-  lots of bugfixes (upstream).

* Fri Oct 05 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.0.2.cvs13-alt1
-  3.0.2.

* Thu Sep 27 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 3.0.1.cvs35-alt1
-  3.0.1;
-  remove russian translation mistakes patch.

* Fri Aug 24 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.10.0.cvs158-alt1
-  security fixes (POP3 Format String Vulnerability, CVE is unpublished now), 10x to ldv@.
-  #9685 fix. 10x to naf@ and ktirf@.

* Thu Aug 16 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.10.0.cvs125-alt1
-  bugfixes.

* Fri Aug 03 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.10.0.cvs81-alt2
-  dirty fix for load modules with invalid license.

* Tue Jul 31 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.10.0.cvs81-alt1
-  2.10.0.cvs81.

* Wed Jul 25 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.10.0.cvs62-alt1
-  2.10.0.

* Fri May 11 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.9.2.cvs5-alt1
-  2.9.2.

* Thu Apr 19 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.9.1.cvs1-alt1
-  2.9.1.

* Wed Mar 21 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.8.1.cvs27-alt1
-  2.8.1.

* Mon Feb 05 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.7.2.cvs22-alt1
-  build with libSM;
-  all patches for tools package has been removed (10x to upstream :)).

* Mon Jan 29 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.7.2.cvs4-alt1
-  2.7.2;
-  build with jPilot support;
-  trayicon plugin improvements.

* Thu Jan 25 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.7.1.cvs55-alt1
-  2.7.1.cvs55.

* Fri Jan 19 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.7.1.cvs32-alt1
-  2.7.1.cvs32.

* Wed Jan 17 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.7.1.cvs11-alt1
-  2.7.1.

* Thu Jan 11 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.7.0.cvs6-alt1
-  2.7.0.

* Fri Dec 15 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.6.1.cvs37-alt1
-  2.6.1.cvs37. bugfixes.

* Mon Dec 04 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.6.1.cvs1-alt1
-  2.6.1.

* Wed Nov 29 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.6.0.cvs65-alt1
-  2.6.0cvs65.
-  name changed to claws-mail.
-  patch 117 added (locale support fix).

* Wed Oct 25 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.5.6.cvs6-alt1
-  2.5.6.

* Thu Sep 28 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.5.2.cvs12-alt1
-  2.5.2.

* Tue Sep 26 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.5.1.cvs1-alt1
-  2.5.1

* Tue Sep 19 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.4.0.cvs198-alt1
-  lots of bugfixes.

* Wed Sep 06 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.4.0.cvs152-alt1
-  2.4.0.cvs152.
-  new bogofilter plugin.

* Mon Aug 28 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.4.0.cvs102-alt1
- 2.4.0.cvs102.
- require autoconf 2.60.

* Fri Aug 11 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.4.0.cvs40-alt1
-  2.4.0. bugfix.

* Wed Aug 09 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.4.0.cvs34-alt1
-  2.4.0.

* Mon Jun 26 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.3.1.cvs20-alt1
-  2.3.1.

* Mon Jun 19 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.3.0.cvs22-alt1
-  2.3.0.

* Mon Jun 05 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.2.1.cvs1-alt1
-  2.2.1.

* Tue May 30 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.2.0.cvs66-alt1
-  much more speed-up :)

* Wed May 24 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.2.0.cvs52-alt1
-  more speed-up for folder operations.

* Tue May 23 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.2.0.cvs47-alt1
-  speed-up folder operations.

* Fri May 19 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.2.0.cvs35-alt1
-  2.2.0

* Wed Apr 12 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.1.0.cvs32-alt1
-  2.1.0.cvs32. bugfixes.

* Wed Apr 12 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.1.0.cvs24-alt1
- 2.1.0 

* Tue Mar 28 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0.cvs178-alt1
-  2.0.0.cvs178. bugfixes. 

* Mon Mar 20 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0.cvs158-alt1
-  2.0.0.cvs158;
-  build with libetpan 0.43.

* Fri Feb 10 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0.cvs41-alt1
-  2.0.0.cvs41.
-  fixes in tools.

* Tue Feb 07 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0.cvs26-alt1
-  improve perfomance.

* Thu Feb 02 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0.cvs8-alt1
-  2.0.0.cvs8.

* Tue Jan 31 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0.cvs2-alt1
-  2.0.0.

* Mon Jan 16 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.9.100.cvs157-alt1
-  cvs157. HIG'ify.

* Fri Dec 16 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.9.100.cvs93-alt1
-  1.9.100.cvs93.
-  fixes for menu.

* Wed Dec 07 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.9.100.cvs71-alt1
-  1.9.100.cvs71.

* Thu Nov 17 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.9.100.cvs15-alt1
-  1.9.100.cvs15. bugfixes.

* Wed Nov 09 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.9.100.cvs4-alt1
-  1.9.1.

* Fri Oct 28 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.9.15.cvs124-alt1
-  cvs124.
-  temporary disabled tools patches (google, freshmeat and sf search).

* Tue Oct 18 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.9.15.cvs71-alt1
-  1.9.15.cvs71.

* Fri Oct 14 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.9.15.cvs44-alt1
-  1.9.15.cvs44.

* Wed Oct 12 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.9.15.cvs30-alt1
-  1.9.15.cvs30.
-  build for altlinux sisyphus.



