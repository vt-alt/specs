Name: rpm-build-gir
Version: 0.7.3
Release: alt2

Summary: RPM helper macros and dependency utils to build GObject Introspection packages
License: GPL
Group: Development/Other

Source: %name-%version.tar

BuildArch: noarch
Requires: xml-utils

%description
These helper macros and dependency calculation utils facilitate creation of
RPM packages containing GObject Introspection files.

%prep
%setup

%install
mkdir -p %buildroot{%_rpmlibdir,%_rpmmacrosdir}
install -pD -m644 rpm-build-gir.macros %buildroot%_rpmmacrosdir/gobject-introspection
install -p -m755 typelib.env %buildroot%_rpmmacrosdir/typelib.env

for f in gir.req* gir.prov* typelib.req* typelib.prov* gir-js.req* gir-python.req* rpm-build-gir.functions; do
  install -m755 -p "$f" "%buildroot%_rpmlibdir/$f"
done

ln -s typelib.prov.files %buildroot%_rpmlibdir/typelib.req.files
ln -s gir.prov.files %buildroot%_rpmlibdir/gir.req.files


%files
%_rpmmacrosdir/gobject-introspection
%_rpmmacrosdir/typelib.env
%_rpmlibdir/%name.functions
%_rpmlibdir/gir*
%_rpmlibdir/typelib*

%changelog
* Sun Jul 07 2019 Yuri N. Sedunov <aris@altlinux.org> 0.7.3-alt2
- gir-js.req: fixed for "let X = imports.gi.X"

* Fri Jun 28 2019 Yuri N. Sedunov <aris@altlinux.org> 0.7.3-alt1
- gir-js.req: modified to support more JS expressions (ALT #36929)

* Sun Jun 02 2019 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt5
- gir-js.req: fixed regexp for syntax without semicolon at end of lines

* Sat Aug 18 2018 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt4
- gir-js.req: support for new "const {X, Y, Z, ... } = imports.gi;" expression

* Sun Mar 12 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt3
- gir-python.req.files: fix for "python3 script text executable"

* Sun Jan 26 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt2
- modified gir-js.req using TypeLibReq_Skip() too

* Fri Mar 08 2013 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- rpm-build-gir.macros: added %%set_girdir macros
- typelib.env: exported RPM_GIRDIR variable
- modified gir.prov.files using RPM_GIRDIR variable

* Thu Jan 10 2013 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt7.1
- typelib.req: fix related of previous release

* Wed Jan 09 2013 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt7
- rpm-build-gir.macros: added %%add_typelib_req_skiplist macros
- typelib.env: exported RPM_TYPELIB_REQ_SKIPLIST variable
- rpm-build-gir.functions: implemented TypeLibReq_Skip()
- modified {gir-python,typelib}.req using TypeLibReq_Skip()

* Tue Jun 12 2012 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt6
- rpm-build-gir.macros: added %%{set,add}_typelibdir macros
- exported RPM_TYPELIBDIR variable (new typelib.env file)
- modified typelib.prov.files and typelib.req using RPM_TYPELIBDIR variable

* Mon Oct 31 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.1-alt5
- find in first 50 lines of *.typelib

* Thu Oct 06 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt4
- another small fix in gir-python.req

* Thu Sep 15 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt3
- small fix in gir-python.req

* Wed Sep 14 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.1-alt2
- build to Sisyphus

* Sun Sep 04 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- improved gir-python.req (ALT #25754)

* Tue Jun 14 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7-alt1
- fixed gir-python.req - delete all after "as" (ALT #25754)

* Tue Jun 07 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6-alt1
- another fixed gir-python.req

* Tue Apr 19 2011 Yuri N. Sedunov <aris@altlinux.org> 0.5-alt2
- fixed gir-python.req

* Fri Apr 08 2011 Alexey Shabalin <shaba@altlinux.ru> 0.5-alt1
- add gir autoreq for python files
- if find "imports.gi.Peas" in javascript files then need libpeas-js-loader
- if find "gi.repository import Peas" in python files then need libpeas-python-loader

* Wed Mar 09 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4.2-alt1
- update filter for javascript files

* Fri Mar 04 2011 Alexey Tourbin <at@altlinux.ru> 0.4.1-alt1
- gir.prov.files: fixed gir files detection

* Mon Feb 14 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4-alt1
- add autoreq for javascript files

* Mon Jul 19 2010 Alexey Shabalin <shaba@altlinux.ru> 0.3-alt1
- fix build gobject-introspection with changed soname

* Tue Mar 30 2010 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt1
- change scheme req and prov for gir and typelib from gir(Foo-1.0) to gir(Foo) = 1.0

* Sun Mar 07 2010 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1
- Initial release
