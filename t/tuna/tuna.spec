# SPDX-License-Identifier: GPL-2.0-only
# SPEC is based on upstream provided `rpm/SPECS/tuna.spec'.
# Versions up to 0.13.1-alt1_3 are maintained until Mon Oct 09 2017
# by Igor Vlasenko <viy@altlinux.ru> in Autoimports repo.
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

# GUI requires python3 with gtk2 which we don't have.
# But, tuna can work w/o GUI.
%filter_from_requires /^python.*(\(pygtk\|pango\|matplotlib.*\|gobject\|gtk.*\))/d

Name: tuna
Version: 0.14.1
Release: alt1
License: GPL-2.0-only
Summary: Thread and IRQ affinity setting GUI and cmd line tool
Group: System/Configuration/Hardware
Url: https://rt.wiki.kernel.org/index.php/Tuna
Vcs: https://git.kernel.org/pub/scm/utils/tuna/tuna.git

Source: %name-%version.tar
BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: gettext-tools
BuildRequires: python3-devel
Provides: python3(tuna)

%description
Provides interface for changing scheduler and IRQ tunables, at whole CPU and at
per thread/IRQ level. Allows isolating CPUs for use by a specific application
and moving threads and interrupts to a CPU by just dragging and dropping them.
Operations can be done on CPU sockets, understanding CPU topology.

Can be used as a command line utility without requiring the GUI libraries to be
installed.

%package -n oscilloscope
Summary: Generic graphical signal plotting tool
Group: System/Configuration/Other
Requires: tuna = %EVR

%description -n oscilloscope
Plots stream of values read from standard input on the screen together with
statistics and a histogram.

Allows to instantly see how a signal generator, such as cyclictest, signaltest
or even ping, reacts when, for instance, its scheduling policy or real time
priority is changed, be it using tuna or plain chrt & taskset.

%prep
%setup

%build
%python3_build

%install
%python3_install

mkdir -p %buildroot/%_sysconfdir/tuna
mkdir -p %buildroot/{%_bindir,%_datadir/tuna/help/kthreads,%_mandir/man8}
mkdir -p %buildroot/%_datadir/polkit-1/actions
install -p -m644 tuna/tuna_gui.glade %buildroot/%_datadir/tuna/
install -p -m755 tuna-cmd.py %buildroot/%_bindir/tuna
#install -p -m755 oscilloscope-cmd.py %buildroot/%_bindir/oscilloscope
install -p -m644 help/kthreads/* %buildroot/%_datadir/tuna/help/kthreads/
install -p -m644 docs/tuna.8 %buildroot/%_mandir/man8/
install -p -m644 etc/tuna/example.conf %buildroot/%_sysconfdir/tuna/
install -p -m644 etc/tuna.conf %buildroot/%_sysconfdir/
#install -p -m644 org.tuna.policy %buildroot/%_datadir/polkit-1/actions/
#desktop-file-install --dir=%buildroot/%_datadir/applications tuna.desktop

# l10n-ed message catalogues
for lng in `cat po/LINGUAS`; do
	po=po/"$lng.po"
	mkdir -p %buildroot/%_datadir/locale/${lng}/LC_MESSAGES
	msgfmt $po -o %buildroot/%_datadir/locale/${lng}/LC_MESSAGES/%name.mo
done

%find_lang %name

%files -f %name.lang
%doc ChangeLog
%_sysconfdir/tuna*
%_bindir/tuna
%_datadir/tuna
%python3_sitelibdir/tuna*
%_mandir/man8/tuna.8*
#%_datadir/polkit-1/actions/org.tuna.policy
#%_datadir/applications/tuna.desktop

%if 0
%files -n oscilloscope
%doc docs/oscilloscope+tuna.*
%_bindir/oscilloscope
%endif

%changelog
* Fri Oct 02 2020 Vitaly Chikunov <vt@altlinux.org> 0.14.1-alt1
- First import of v0.14.1 (2020-10-02) into Sisyphus. CLI only.

