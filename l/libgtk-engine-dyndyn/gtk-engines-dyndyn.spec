%define _name dyndyn
%define engine_prefix libgtk-engine

Name: %engine_prefix-%_name
Version: 0.1
Release: alt1.1.qa1

Summary: DynDyn GTK2 engine
Summary(ru_RU.UTF-8):Модуль прорисовки DynDny для GTK2
License: GPL
Group: Graphical desktop/GNOME
Url: http://www.gnome-look.org
Source0: 47474-%_name-%version.tar.bz2
Patch0: gtk-engines-dyndyn-0.1-alt-glib2.patch

%define gtk_ver 2.10.0
%define gtk_binary_ver 2.10.0
%define engines_dir %_libdir/gtk-2.0/%gtk_binary_ver/engines

BuildPreReq: libgtk+2-devel >= %gtk_ver
BuildRequires: gcc-c++ gcc-g77 libgtk+2-devel

%description
A cairo GTK+2 themes that features Dynamic widgets, meaning each widget will be a bit different than the other.

%description -l ru_RU.UTF-8
Модуль прорисовки для GTK+2 и cairo, поддерживающий динамические элементы интерфейса. Кождый из элементов может отличаться от других.

%prep
%setup -q -n %_name-%version
%patch -p2

%build
#%autoreconf
%configure --enable-animation
%make

%install
%makeinstall

%files
%doc AUTHORS README ChangeLog
%engines_dir/*.so

%exclude %engines_dir/*.la

%changelog
* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1.1.qa1
- NMU: applied repocop patch

* Fri Jul 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.1
- Fixed build

* Wed Dec 06 2006 Vyacheslav Dikonov <slava@altlinux.ru> 0.1-alt1
- ALTLinux build
