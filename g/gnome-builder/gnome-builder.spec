%def_disable snapshot

%define xdg_name org.gnome.Builder
%define ver_major 3.32
%define _libexecdir %_prefix/libexec
%define api_ver 1.0

%def_with sysprof
%def_with flatpak
%def_with docs
%def_with help
%def_with autotools
%def_with jedi

Name: gnome-builder
Version: %ver_major.4
Release: alt1.1

Summary: Builder - Develop software for GNOME
License: LGPLv2+
Group: Development/GNOME and GTK+
Url: https://wiki.gnome.org/Apps/Builder

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif
Patch0: gnome-builder-3.32.4-meson-0.52.patch

%set_typelibdir %_libdir/%name/girepository-1.0

%define glib_ver 2.53.2
%define gtk_ver 3.22.1
%define gtksourceview_ver 4.0.2
%define git2_ver 0.25.0
%define devhelp_ver 3.30.0
%define gjs_ver 1.42
%define xml_ver 2.9.0
%define vala_ver 0.37
%define sysprof_ver 3.32.0
%define vte_ver 0.46
%define gtkmm_ver 3.20
%define gspell_ver 1.8.0
%define peas_ver 1.21.0
%define json_glib_ver 1.2.0
%define dazzle_ver 3.32.2
%define template_glib_ver 3.32.0

# use python3
AutoReqProv: nopython
%define __python %nil
%add_python3_path %_libdir/%name/plugins
%add_findreq_skiplist %_datadir/%name/plugins/*_templates/resources/*/*.py

Requires(pre): %name-data = %version-%release

%{?_with_autotools:Requires: automake autoconf libtool}
Requires: meson git indent xmllint
Requires: devhelp uncrustify ctags
Requires: libpeas-python3-loader
#%%{?_with_jedi:Requires: python3-module-jedi}

BuildRequires(pre): meson rpm-build-python3 rpm-build-gir
BuildRequires: /proc gcc-c++ flex mm-common yelp-tools gtk-doc
BuildRequires: ctags
BuildRequires: libappstream-glib-devel desktop-file-utils
BuildRequires: llvm-devel clang-devel libgtk+3-devel >= %gtk_ver
BuildRequires: libgtksourceview4-devel >= %gtksourceview_ver
BuildRequires: libgit2-glib-devel >= %git2_ver libdevhelp-devel >= %devhelp_ver
BuildRequires: libpcre-devel libgjs-devel >= %gjs_ver libwebkit2gtk-devel
BuildRequires: libxml2-devel >= %xml_ver libpeas-devel >= %peas_ver libvte3-devel >= %vte_ver
BuildRequires: libjson-glib-devel >= %json_glib_ver
BuildRequires: python3-devel python3-module-pygobject3-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel libvte3-gir-devel
BuildRequires: libgtksourceview4-gir-devel libgit2-glib-gir-devel libpeas-gir-devel
BuildRequires: libjson-glib-gir-devel
BuildRequires: libvala-devel >= %vala_ver vala-tools
BuildRequires: libgspell-devel >= %gspell_ver libenchant2-devel
BuildRequires: libdazzle-devel >= %dazzle_ver libtemplate-glib-devel >= %template_glib_ver libjsonrpc-glib-devel
BuildRequires: libdazzle-gir-devel libtemplate-glib-gir-devel  libjsonrpc-glib-gir-devel
BuildRequires: libgtkmm3-devel >= %gtkmm_ver
BuildRequires: libgladeui2.0-devel
%{?_with_help:BuildRequires: python3-module-sphinx python3-module-sphinx_rtd_theme}
%{?_with_flatpak:BuildRequires: libflatpak-devel libostree-devel}
%{?_with_sysprof:BuildRequires: sysprof-devel >= %sysprof_ver}

%description
Builder attempts to be an IDE for writing software for GNOME. It does not
try to be a generic IDE, but one specialized for writing GNOME software.
We believe that this focus will help us to build something great.

%package data
Summary: Arch independent files for GNOME Builder
Group: Development/GNOME and GTK+
BuildArch: noarch

%description data
This package provides noarch data needed for Gnome Builder to work.


%prep
%setup
%patch0 -p1

%build
%meson \
	%{?_with_docs:-Ddocs=true} \
	%{?_with_help:-Dhelp=true} \
	%{?_without_flatpak:-Dplugin_flatpak=false} \
	%{?_with_autotools:-Dplugin_autotools=true}
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_libexecdir/%name-clang
%dir %_libdir/%name

%dir %_libdir/%name/girepository-1.0
%_libdir/%name/girepository-1.0/Ide-%ver_major.typelib

%dir %_libdir/%name/plugins
%_libdir/%name/plugins/Ide-%ver_major.metadata
%_libdir/%name/plugins/__pycache__
%_libdir/%name/plugins/cargo.plugin
%_libdir/%name/plugins/cargo_plugin.py
%_libdir/%name/plugins/eslint.plugin
%_libdir/%name/plugins/eslint_plugin.py
%_libdir/%name/plugins/find-other-file.plugin
%_libdir/%name/plugins/find_other_file.py
%_libdir/%name/plugins/gjs_symbols.plugin
%_libdir/%name/plugins/gjs_symbols.py
%_libdir/%name/plugins/go-langserv.plugin
%_libdir/%name/plugins/go_langserver_plugin.py
%_libdir/%name/plugins/gradle.plugin
%_libdir/%name/plugins/gradle_plugin.py
%_libdir/%name/plugins/html-preview.plugin
%_libdir/%name/plugins/html_preview.gresource
%_libdir/%name/plugins/html_preview.py
%_libdir/%name/plugins/jedi.plugin
%_libdir/%name/plugins/jedi_plugin.py
%_libdir/%name/plugins/jhbuild.plugin
%_libdir/%name/plugins/jhbuild_plugin.py
%_libdir/%name/plugins/libplugin-vala-pack.so
%_libdir/%name/plugins/make.plugin
%_libdir/%name/plugins/make_plugin.gresource
%_libdir/%name/plugins/make_plugin.py
%_libdir/%name/plugins/maven.plugin
%_libdir/%name/plugins/maven_plugin.py
%_libdir/%name/plugins/meson-templates.plugin
%_libdir/%name/plugins/meson_templates.gresource
%_libdir/%name/plugins/meson_templates.py
%_libdir/%name/plugins/mono.plugin
%_libdir/%name/plugins/mono_plugin.py
%_libdir/%name/plugins/npm.plugin
%_libdir/%name/plugins/npm_plugin.py
%_libdir/%name/plugins/phpize.plugin
%_libdir/%name/plugins/phpize_plugin.py
%_libdir/%name/plugins/python-gi-imports-completion.plugin
%_libdir/%name/plugins/python_gi_imports_completion.py
%_libdir/%name/plugins/rls.plugin
%_libdir/%name/plugins/rls_plugin.py
%_libdir/%name/plugins/rustup.plugin
%_libdir/%name/plugins/rustup_plugin.gresource
%_libdir/%name/plugins/rustup_plugin.py
%_libdir/%name/plugins/vala-pack.plugin
%_libdir/%name/plugins/valgrind.plugin
%_libdir/%name/plugins/valgrind_plugin.gresource
%_libdir/%name/plugins/valgrind_plugin.py
%_libdir/%name/plugins/waf.plugin
%_libdir/%name/plugins/waf_plugin.py
#%{?_with_autotools_templates:%_libdir/%name/plugins/autotools_templates/}
#%{?_with_sysprof:%_libdir/%name/plugins/libsysprof-plugin.so}

%_includedir/%name/
%_includedir/%name-%ver_major/
%dir %_libdir/%name/pkgconfig
%_libdir/%name/pkgconfig/%name-%ver_major.pc
%python3_sitelibdir/gi/overrides/Ide.py
%python3_sitelibdir/gi/overrides/__pycache__/
%doc README* AUTHORS NEWS

%files data
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/org.gnome.builder.build.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.clang.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.code-insight.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.plugins.color_picker_plugin.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.plugins.eslint.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.editor.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.editor.language.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.extension-type.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.gnome-code-assistance.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.plugin.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.project.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.project-tree.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.terminal.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.builder.workbench.gschema.xml
%_datadir/gtksourceview-4/styles/*.xml
%_datadir/gtksourceview-3.0/styles/*.xml
%_datadir/%name/
%_iconsdir/hicolor/*/*/*.*
%_datadir/metainfo/%xdg_name.appdata.xml

%if_with docs
%_datadir/gtk-doc/html/libide/
%{?_with_help:%_datadir/doc/%name/}
%endif

%changelog
* Wed Mar 31 2021 Valery Inozemtsev <shrek@altlinux.ru> 3.32.4-alt1.1
- fixed link_whole usage for meson 0.52.0

* Tue Jul 16 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.4-alt1
- 3.32.4

* Wed Jun 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.3-alt1
- 3.32.3

* Tue May 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Thu Apr 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Wed Mar 13 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Sun Jan 13 2019 Yuri N. Sedunov <aris@altlinux.org> 3.30.3-alt1
- 3.30.3

* Wed Oct 31 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Tue Sep 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Wed Sep 05 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Fri Jul 27 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.4-alt1
- 3.28.4

* Thu Jun 21 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.3-alt1
- 3.28.3

* Tue May 29 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Thu Apr 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.28.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Apr 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Tue Mar 20 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1.1
- rebuilt against libclang.so.6

* Wed Mar 14 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Thu Feb 01 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.4-alt1
- 3.26.4

* Thu Jan 11 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.3-alt1
- 3.26.3

* Wed Nov 01 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Wed Oct 04 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Thu Sep 07 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt2
- rebuilt against libclang.so.4

* Tue May 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Tue Apr 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Mar 14 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.22.4-alt1.1
- Rebuilt with llvm 4.0.

* Thu Dec 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.4-alt1
- 3.22.4

* Tue Nov 29 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Wed Nov 02 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Wed Oct 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Fri May 06 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.4-alt1
- 3.20.4

* Thu Apr 28 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Tue Mar 29 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.20.0-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Mar 23 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Thu Oct 15 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon May 18 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt1
- 3.16.3

* Fri May 01 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt0.1
- 3.16.3_c04d920e

* Fri Apr 17 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Mon Jan 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.4.1-alt1
- first preview for people/gnome

