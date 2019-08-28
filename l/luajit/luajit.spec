Name: luajit
Version: 2.1
Release: alt9

Summary: a Just-In-Time Compiler for Lua
License: MIT
Group: Development/Other
Url: http://luajit.org

Source: %name-%version.tar
Requires: lib%name = %EVR
BuildRequires(pre): rpm-macros-luajit

ExclusiveArch: %luajit_arches

Patch1: luajit-2.1.0-fedora-ppc64le-support.patch

%description
LuaJIT is a Just-In-Time Compiler (JIT) for the Lua programming language.
Lua is a powerful, dynamic and light-weight programming language.
It may be embedded or used as a general-purpose, stand-alone language.

%package -n lib%name
Summary: library for luajit
Group: Development/Other

%description -n lib%name
LuaJIT is a Just-In-Time Compiler (JIT) for the Lua programming language.
Lua is a powerful, dynamic and light-weight programming language.
It may be embedded or used as a general-purpose, stand-alone language.

%package -n lib%name-devel
Summary:  Development package that includes the luajit header files
Group: Development/Other
Requires: lib%name = %EVR

%description -n lib%name-devel
LuaJIT is a Just-In-Time Compiler (JIT) for the Lua programming language.
Lua is a powerful, dynamic and light-weight programming language.
It may be embedded or used as a general-purpose, stand-alone language.

%package -n lib%name-devel-static
Summary: static library for luajit
Group: System/Libraries
Requires: lib%name-devel = %EVR

%description -n lib%name-devel-static
LuaJIT is a Just-In-Time Compiler (JIT) for the Lua programming language.
Lua is a powerful, dynamic and light-weight programming language.
It may be embedded or used as a general-purpose, stand-alone language.

%prep
%setup
%patch1 -p1

%build
%make_build amalg \
	    PREFIX=%_prefix \
	    MULTILIB=%_lib \
	    TARGET_STRIP='@:' \
	    Q=

%install
%makeinstall_std PREFIX=%_prefix \
		 MULTILIB=%_lib \
		 INSTALL_LMOD=%buildroot%_datadir/lua/5.1 \
		 INSTALL_CMOD=%buildroot%_libdir/lua/5.1 \
		 LDCONFIG=true \
		 INSTALL_LIB=%buildroot%_libdir \
		 Q=

mv %buildroot%_bindir/luajit-2.1.0-beta3 %buildroot%_bindir/luajit


%files
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*
%_datadir/%name-*

%files -n lib%name-devel
%doc doc/*
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Thu Jul 4 2019 Vladimir Didenko <cow@altlinux.org> 2.1-alt9
- specify build arches

* Thu Jul 4 2019 Vladimir Didenko <cow@altlinux.org> 2.1-alt8
- patch for ppc64le support

* Thu Mar 21 2019 Vladimir Didenko <cow@altlinux.org> 2.1-alt7
- git20190110

* Wed Jun 13 2018 Vladimir Didenko <cow@altlinux.org> 2.1-alt6
- git20180605 (closes: #35026)

* Wed May 3 2017 Vladimir Didenko <cow@altlinux.org> 2.1-alt5
- v2.1.0-beta3
- luaconf.h: use lua/5.1 instead lua5/

* Thu Feb 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.1-alt4
- NMU: new policy: set:
  * INSTALL_LMOD=%buildroot%_datadir/lua/5.1
  * INSTALL_CMOD=%buildroot%_libdir/lua/5.1

* Fri Jul 29 2016 Vladimir Didenko <cow@altlinux.org> 2.1-alt3
- git20160722

* Mon Jun 27 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt2
- packaged non-versioned luajit binary (closes: #32223)

* Thu Jun 23 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt1
- 2.1 released

* Mon Jul 20 2015 Vladimir Didenko <cow@altlinux.org> 2.0.4-alt2
- git20150717

* Sat May 16 2015 Vladimir Didenko <cow@altlinux.org> 2.0.4-alt1
- 2.0.4

* Tue Feb 24 2015 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt6
- git20150222

* Wed Feb 18 2015 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt5
- use the same path and cpath as plain lua (closes: #30739)

* Mon Jan 12 2015 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt4
- git20150105

* Wed Sep 10 2014 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt3
- git20140908

* Fri Jul 4 2014 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt2
- git20140701

* Thu Mar 20 2014 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt1
- new version

* Sun Apr 14 2013 Dmitry V. Levin <ldv@altlinux.org> 2.0.1-alt1
- NMU: updated v2.0.1-fixed-14-gb1327bc, fixed build.

* Sun Dec 16 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0-alt1
- Build for ALT
