# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 1.0.1-0
%define fname aspell5-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Tswana
%define languagecode tn
# no locale yet
%define lc_ctype tn_XX

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       1.0.1.0
Release:       alt2_15
Group:         Text tools
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.net/
License:	   GPL
Provides: spell-%{languagecode}

BuildRequires: aspell >= %{aspell_ver}
Requires:      aspell >= %{aspell_ver}

# Mageia Stuff
# no tn locale yet
#Requires:      locales-%{languagecode}
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}

Autoreqprov:   no
Source44: import.info

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

chmod 644 Copyright README* doc/*

%files
%doc README* Copyright doc/*
%{_libdir}/aspell/*
%{_datadir}/aspell/*






%changelog
* Tue Oct 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.1.0-alt2_15
- fixed rpm Group:

* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1.0-alt1_15
- update by mgaimport

