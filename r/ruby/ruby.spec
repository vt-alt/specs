%def_without bootstrap
%def_enable shared
%def_enable rubygems
%define ruby_version 2.5.0
%define libdir %_prefix/lib/%name
%define includedir %_includedir
%define ridir %_datadir/ri
%define vendordir %libdir/vendor_%name
%define lname lib%name

Name:     ruby
Version:  2.5.5
Release:  alt3
Summary:  An Interpreted Object-Oriented Scripting Language
License:  BSD 2-clause Simplified License/Ruby
Group:    Development/Ruby
URL:      http://www.%name-lang.org/
Source0:  %name-%version.tar
Source3:  fakeruby.sh
Source4:  miniruby.sh
Requires: %lname = %version-%release
Requires: ruby-stdlibs = %version-%release
Requires: gem irb erb ri rdoc rake bundle

%define obsolete() \
Provides: %1 = %version-%release \
Obsoletes: %1
%define mobsolete() \
%(for m in %*; do \
echo "Provides: %name-module-$m = %version-%release"; \
echo "Obsoletes: %name-module-$m"; \
done)

BuildRequires(pre): rpm-build-ruby >= 1:1.0.0
BuildRequires: doxygen groff-base libdb4-devel libffi-devel
BuildRequires: libgdbm-devel libncursesw-devel libreadline-devel libssl-devel
BuildRequires: zlib-devel libyaml-devel gcc-c++
BuildRequires: valgrind-devel
%{?!_with_bootstrap:BuildRequires: ruby ruby-stdlibs rpm-build-ruby >= 1:1.0.0}
%{?_with_bootstrap:BuildRequires: ruby-miniruby-src = %EVR}

%description
Ruby is an interpreted scripting language for quick and easy object-oriented
programming. It has many features for processing text files and performing
system management tasks (as in Perl). It is simple, straight-forward, and
extensible.

This package contains interpreter of object-oriented scripting language Ruby.


%package -n %lname
Summary: Ruby shared libraries
Group: System/Libraries
Provides: ruby(enumerator)

%description -n %lname
Ruby is an interpreted scripting language for quick and easy object-oriented
programming. It has many features for processing text files and performing system
management tasks (as in Perl). It is simple, straight-forward, and extensible.

This package contains Ruby shared libraries.


%package -n %lname-devel
Summary: Files for compiling extension modules for Ruby
Group: Development/C
%{?_enable_shared:Requires: %lname = %version-%release}
Requires: rpm-build-%name >= 1.0.0

%description -n %lname-devel
Ruby is an interpreted scripting language for quick and easy object-oriented
programming. It has many features for processing text files and performing system
management tasks (as in Perl). It is simple, straight-forward, and extensible.

This package contains files, necessary to make extension library for Ruby.


%package -n %lname-devel-static
Summary: Files for compiling extension modules for Ruby
Group: Development/C
Requires: %lname-devel = %version-%release

%description -n %lname-devel-static
Ruby is an interpreted scripting language for quick and easy object-oriented
programming. It has many features for processing text files and performing system
management tasks (as in Perl). It is simple, straight-forward, and extensible.

This package contains static Ruby library needed for embedding Ruby.

%package -n %name-stdlibs
Summary: Standard Ruby libraries
Group: Development/Ruby
Requires: %lname = %version-%release
Requires: libyaml2 libgdbm libssl1.1 libcrypto1.1
Requires: gem(rubygems-update) >= 3.0.1
Requires: gem(did_you_mean) >= 1.3.0
Requires: gem(minitest) >= 5.11.3
Requires: gem(net-telnet) >= 0.2
Requires: gem(power_assert) >= 1.1.4
Requires: gem(rake) >= 12.3.2
Requires: gem(test-unit) >= 3.2.9
Requires: gem(xmlrpc) >= 0.3.0
Requires: gem(rdoc) >= 6.1.1
Provides: %name-libs = %version-%release
Provides: %name-racc-runtime = %version
Provides: ruby(%ruby_version)
Provides: ruby(thread)
%mobsolete English bigdecimal cgi curses date-time dbm debug digest dl drb e2mmap
%mobsolete erb etc fcntl fileutils gdbm iconv math misc net nkf open3 openssl
%mobsolete optparse patterns pty readline rexml rss sdbm shell socket stringio
%mobsolete strscan syslog tracer uri wait webrick xmlrpc yaml zlib

%description -n %name-stdlibs
Ruby is an interpreted scripting language for quick and easy object-oriented
programming. It has many features for processing text files and performing
system management tasks (as in Perl). It is simple, straight-forward, and
extensible.

This package contains standard Ruby runtime libraries.


%package -n gem
Summary:   Ruby gem executable and framefork
Group:     Development/Ruby
BuildArch: noarch
Requires:  %name-stdlibs = %version
Provides:  %_bindir/gem
Provides:  %{name}gems = 3.0.1
Provides:  %name-tools
Obsoletes: %name-tools

%description -n gem
Ruby gem executable and framework.

%package -n erb
Summary:   ERB template library
Group:     Development/Ruby
BuildArch: noarch
Requires:  %name-stdlibs = %version
Provides:  %_bindir/erb
Obsoletes: %name-tools

%description -n erb
ERB template library executable and manual.

%package -n irb
Summary:   Interactive Ruby Shell
Group:     Development/Ruby
BuildArch: noarch
Requires:  %name-stdlibs = %version
Provides:  %_bindir/irb
Obsoletes: %name-tools
%obsolete  %name-tool-irb

%description -n irb
irb is the REPL(read-eval&print loop) environment for Ruby programs.

%package -n ri-doc
Summary: Ruby ri executable man page
Group: Development/Documentation
BuildArch: noarch
Requires:   %_bindir/ri
Requires:   %name = %version

%description -n ri-doc
Ruby ri executable man page

%package       doc
Summary:       Ruby ri documentation
Group:         Development/Documentation
BuildArch:     noarch
AutoReq:       no
AutoProv:      no
Provides:      %name-doc-ri
Obsoletes:     %name-doc-ri
Requires:      ri
Requires:      ruby = %version-%release

%description   doc
Ruby is an interpreted scripting language for quick and easy object-oriented
programming. It has many features for processing text files and performing system
management tasks (as in Perl). It is simple, straight-forward, and extensible.

This package contains Ruby documentation in ri format.


%if_without bootstrap
%package miniruby-src
Summary: Preprocessed miniruby sources
Group: Development/Ruby
BuildArch: noarch

%description miniruby-src
Contains generated files for preprocessed miniruby sources in patch
format. This files are required for ruby bootstrapping, especially
on different arches.
%endif

%prep
%setup -q
# More strict shebang
sed -i '1s|^#!/usr/bin/env ruby|#!%_bindir/%name|' bin/*
# Remove $ruby_version from libs path
sed -i 's|/\$(ruby_version)||g;s|\(/%name/\)#{version}/|\1|g' tool/mkconfig.rb
sed -i 's|/\${ruby_version}||' template/%name.pc.in configure.ac
sed -i -r "/ridatadir[[:blank:]]*=/s/[[:blank:]]+CONFIG\['ruby_version'\],//" tool/rbinstall.rb
sed -i 's|[[:blank:]]*"/"RUBY_LIB_VERSION$||' version.c
# capi-docs
sed -i -e '/doc\/capi/s|"/capi|"/html/capi|' -e '/doc\/capi/s|doc/capi|&/html|' tool/rbinstall.rb
# put config.guess and config.sub from /usr/share/gnu-config
cp -a /usr/share/gnu-config/config.* tool

%build
%define ruby_arch %(echo %_target | sed 's/^ppc/powerpc/')%([ -z "%_gnueabi" ] || echo "-eabi")
%autoreconf
%__setup_rb config --gem-version-replace="$RPM_RUBY_GEMVERSION_REPLACE_LIST" --use=rdoc --join=doc:lib
my_configure() {
    %configure \
        %{subst_enable shared} \
        %{subst_enable valgrind} \
        %{subst_enable rubygems} \
        --with-rubylibprefix=%libdir \
        --with-rubyhdrdir=%includedir \
        --with-sitearchdir=%libdir/site_ruby/%version/%ruby_arch \
        --with-vendorarchdir=%libdir/vendor_ruby/%version/%ruby_arch \
        --with-ridir=%ridir \
        --docdir=%_docdir/%name-%version \
        %{?ruby_version:--with-ruby-version=%ruby_version} \
        --disable-rpath "$@"
}

%if_with bootstrap
# *** 1st stage ***
# Build miniruby with preprocessed files from miniruby-src in a
# separate directory

cd %_builddir
cp -a %name-%version %name-%version-miniruby
cd %name-%version-miniruby
cp %SOURCE3 %SOURCE4 .

my_configure --with-baseruby=$PWD/fakeruby.sh
patch -p1 -l < %_datadir/%name-%version-miniruby/miniruby-src.patch
%make_build miniruby

# *** 2nd stage ***
# Build ruby with host miniruby frome 1st stage as baseruby
cd %_builddir/%name-%version
my_configure --with-baseruby=%_builddir/%name-%version-miniruby/miniruby.sh

%else #_with_bootstrap
my_configure

# Copy sources after configure, so that generated files for
# miniruby can be extracted later to facilitate bootstrapping.
cp -a %_builddir/%name-%version %_builddir/%name-%version-configured

# Build miniruby only, so that we can diff only minimal generated data.
%make_build miniruby

# Create diff for changed sources files with non-essential filtered out.
# For diff !0 exit status is normal.
pushd %_builddir
diff -Nur -x "*.o" -x miniruby -x "*.log" -x autom4te.cache \
    %name-%version-configured %name-%version > miniruby-src.patch || :
popd
%endif #_with_bootstrap

%make_build

%install
%makeinstall_std
echo "VENDOR_SPECIFIC=true" > %buildroot%vendordir/vendor-specific.rb
install -Dm 0755 %lname-static.a %buildroot%_libdir/%lname-static.a
ln -s %lname-static.a %buildroot%_libdir/%lname.a
mv %buildroot%_pkgconfigdir/%name{*,}.pc
install -d -m 0755 %buildroot%_docdir/%name-%version
mkdir -p %buildroot%ridir/%ruby_version
mv %buildroot%ridir/system %buildroot%ridir/%ruby_version/
install -d -m 0755 %buildroot%ridir/%ruby_version/site
install -p -m 0644 COPYING* LEGAL NEWS README* %buildroot%_docdir/%name-%version/
# install compiled header config.h
install -D .ext/include/%ruby_arch/ruby/config.h %buildroot%ruby_includedir/ruby/config.h

%define ruby_libdir %libdir
%define __ruby env LD_LIBRARY_PATH=%buildroot%_libdir RUBYLIB=%buildroot%libdir:%buildroot%libdir/site_ruby/%version/%ruby_arch %buildroot%_bindir/%name
export RUBYLIB=%buildroot%libdir:%buildroot%libdir/site_ruby/%version/%ruby_arch
export LD_LIBRARY_PATH=%buildroot%_libdir:%buildroot%_libdir/site_ruby/%version%ruby_arch

%add_findreq_skiplist %libdir/gems/*/gems/*/bin/*
%add_findreq_skiplist %libdir/*

%if_without bootstrap
mkdir -p %buildroot%_datadir/%name-%version-miniruby
mv %_builddir/miniruby-src.patch %buildroot%_datadir/%name-%version-miniruby/
%endif

# Make empty dir for ri documentation
mkdir -p %buildroot%_datadir/ri/site/%version
rm -rf %buildroot%_bindir/{ri,rdoc}

%check
%make_build test
%gem_test

%files
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/COPYING
%doc %_docdir/%name-%version/LEGAL
%doc %_docdir/%name-%version/NEWS
%doc %_docdir/%name-%version/README.*
%lang(ja) %doc %_docdir/%name-%version/*.ja
%_bindir/%name
%_man1dir/%name.*
%dir %_datadir/ri

%files -n %lname
%{?_enable_shared:%_libdir/*.so.*}

%files -n %lname-devel
%_pkgconfigdir/*
%includedir/*
%{?_enable_shared:%_libdir/*.so}

%files -n %lname-devel-static
%_libdir/*.a

%files stdlibs
%libdir

%files -n gem
%_bindir/gem

%files -n erb
%_bindir/erb
%_man1dir/erb.*

%files -n irb
%lang(ja) %doc doc/irb/*.ja
%_bindir/irb
%_man1dir/irb.*

%files         doc
%dir %ridir/%ruby_version/site
%ridir/*

%files -n ri-doc
%_man1dir/ri.*

%if_without bootstrap
%files miniruby-src
%_datadir/%name-%version-miniruby/miniruby-src.patch
%endif

%changelog
* Mon Jun 03 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.5.5-alt3
- Fixed build on ppc64le architecture.
- spec: bootstrap: fixed miniruby version.

* Thu May 02 2019 Pavel Skrylev <majioa@altlinux.org> 2.5.5-alt2
- Fixed ri documentation placement (closes: #36294)

* Sat Apr 06 2019 Pavel Skrylev <majioa@altlinux.org> 2.5.5-alt1
- Bump to 2.5.5
- Added config.h to installation

* Fri Feb 01 2019 Pavel Skrylev <majioa@altlinux.org> 2.5.4-alt3
- Allow provide ruby version.

* Thu Jan 17 2019 Pavel Skrylev <majioa@altlinux.org> 2.5.4-alt2
- Added some gem dependencies to spec.

* Fri Dec 28 2018 Pavel Skrylev <majioa@altlinux.org> 2.5.4-alt1
- Bump to 2.5.4;
- Russian description;
- Split tools to separate modules;
- Fixes:
  + CVE-2018-16396: Tainted flags are not propagated in Array#pack and
    String#unpack with some directives;
  + CVE-2018-16395: OpenSSL::X509::Name equality check does not work correctly;
- Modules pilled-out from the package:
  + json
  + minitest
  + update_rubygems
  + did_you_mean
  + net-telnet
  + power_assert
  + rake
  + test-unit
  + xmlrpc
  + rdoc

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.1-alt4
- Rebuild with new ruby autoreq.
- ruby requires ruby-stdlibs.
- Provides bundled gems.

* Tue Jul 10 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.1-alt3
- Fix version in provides.

* Mon May 28 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.1-alt2
- Package %ruby_ridir and %ruby_ri_sitedir directories in ruby.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.1-alt1
- New version.
- Fixes:
  + CVE-2017-17742: HTTP response splitting in WEBrick
  + CVE-2018-6914: Unintentional file and directory creation with directory traversal in tempfile and tmpdir
  + CVE-2018-8777: DoS by large request in WEBrick
  + CVE-2018-8778: Buffer under-read in String#unpack
  + CVE-2018-8779: Unintentional socket creation by poisoned NUL byte in UNIXServer and UNIXSocket
  + CVE-2018-8780: Unintentional directory traversal by poisoned NUL byte in Dir

* Mon Mar 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- New version.
- Fixes:
  + CVE-2017-17405 Command injection vulnerability in Net::FTP
- Update Rubygems to 2.7.6 with security fixes (see https://blog.rubygems.org/2018/02/15/2.7.6-released.html)

* Thu Dec 21 2017 Andrew Savchenko <bircoph@altlinux.org> 2.4.2-alt4
- Properly check for __uint128_t.

* Mon Dec 18 2017 Andrew Savchenko <bircoph@altlinux.org> 2.4.2-alt3
- Add miniruby-src subpackage.
- Bootstrap miniruby without ruby using miniruby-src.

* Thu Oct 12 2017 Andrey Cherepanov <cas@altlinux.org> 2.4.2-alt2
- Merge rubygems-2.6.14 changes
- Fixes:
  + CVE-2017-0903 Unsafe Object Deserialization Vulnerability in RubyGems

* Sat Sep 16 2017 Andrey Cherepanov <cas@altlinux.org> 2.4.2-alt1
- New version 2.4.2
- Security fixes:
  + CVE-2017-0898: Buffer underrun vulnerability in Kernel.sprintf
  + CVE-2017-10784: Escape sequence injection vulnerability in the Basic authentication of WEBrick
  + CVE-2017-14033: Buffer underrun vulnerability in OpenSSL ASN1 decode
  + CVE-2017-14064: Heap exposure in generating JSON

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1
- New version 2.4.1 with gems 2.6.13
- Security fixes:
  + CVE-2017-0902 a DNS request hijacking vulnerability
  + CVE-2017-0899 an ANSI escape sequence vulnerability
  + CVE-2017-0900 a DoS vulnerability in the query command
  + CVE-2017-0901 a vulnerability in the gem installer that allowed a malicious gem to overwrite arbitrary files
- ext/tk: Tk is removed from stdlib. [Feature #8539]

* Fri Mar 24 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.3.1-alt2.qa1
- Rebuilt against Tcl/Tk 8.6

* Tue Mar 07 2017 Denis Medvedev <nbr@altlinux.org> 2.3.1-alt2
- Fix ruby library path

* Thu Sep 08 2016 Denis Medvedev <nbr@altlinux.org> 2.3.1-alt1
- new version

* Tue Jul 01 2014 Led <led@altlinux.ru> 2.0.0-alt10
- p510 upstream patchlevel

* Fri Jun 27 2014 Led <led@altlinux.ru> 2.0.0-alt9
- p499 upstream patchlevel

* Sat May 31 2014 Led <led@altlinux.ru> 2.0.0-alt8
- p490 upstream patchlevel

* Fri May 09 2014 Led <led@altlinux.ru> 2.0.0-alt7
- p481 upstream patchlevel

* Wed May 07 2014 Led <led@altlinux.ru> 2.0.0-alt6
- p480 upstream patchlevel

* Thu May 01 2014 Led <led@altlinux.ru> 2.0.0-alt5
- p477 upstream patchlevel

* Mon Mar 31 2014 Led <led@altlinux.ru> 2.0.0-alt4
- p466 upstream patchlevel

* Sat Mar 22 2014 Led <led@altlinux.ru> 2.0.0-alt3
- p462 upstream patchlevel
- excluded filetrigger for site ri cache update

* Thu Mar 20 2014 Led <led@altlinux.ru> 2.0.0-alt2
- p461 upstream patchlevel

* Wed Mar 19 2014 Led <led@altlinux.ru> 2.0.0-alt1
- 2.0.0 p458 upstream patchlevel

* Mon Feb 24 2014 Led <led@altlinux.ru> 1.9.3-alt47
- p545 upstream patchlevel

* Sat Feb 22 2014 Led <led@altlinux.ru> 1.9.3-alt46
- p541 upstream patchlevel

* Tue Feb 18 2014 Led <led@altlinux.ru> 1.9.3-alt45
- p537 upstream patchlevel

* Tue Feb 18 2014 Led <led@altlinux.ru> 1.9.3-alt44
- p535 upstream patchlevel

* Fri Feb 14 2014 Led <led@altlinux.ru> 1.9.3-alt43
- p534 upstream patchlevel

* Thu Feb 06 2014 Led <led@altlinux.ru> 1.9.3-alt42
- p515 upstream patchlevel

* Wed Feb 05 2014 Led <led@altlinux.ru> 1.9.3-alt41
- p514 upstream patchlevel

* Sat Feb 01 2014 Led <led@altlinux.ru> 1.9.3-alt40
- p511 upstream patchlevel

* Thu Jan 30 2014 Led <led@altlinux.ru> 1.9.3-alt39
- p510 upstream patchlevel

* Thu Jan 30 2014 Led <led@altlinux.ru> 1.9.3-alt38
- p503 upstream patchlevel

* Thu Jan 09 2014 Led <led@altlinux.ru> 1.9.3-alt37
- p489 upstream patchlevel

* Tue Dec 24 2013 Led <led@altlinux.ru> 1.9.3-alt36
- p488 upstream patchlevel

* Sun Nov 24 2013 Led <led@altlinux.ru> 1.9.3-alt35
- p483 upstream patchlevel

* Thu Oct 31 2013 Led <led@altlinux.ru> 1.9.3-alt34
- p482 upstream patchlevel

* Tue Sep 03 2013 Led <led@altlinux.ru> 1.9.3-alt33
- p470 upstream patchlevel

* Wed Aug 21 2013 Led <led@altlinux.ru> 1.9.3-alt32
- p469 upstream patchlevel

* Wed Aug 14 2013 Led <led@altlinux.ru> 1.9.3-alt31
- p465 upstream patchlevel

* Sun Aug 11 2013 Led <led@altlinux.ru> 1.9.3-alt30
- p464 upstream patchlevel

* Sun Aug 04 2013 Led <led@altlinux.ru> 1.9.3-alt29
- p458 upstream patchlevel

* Thu Jul 18 2013 Led <led@altlinux.ru> 1.9.3-alt28
- p455 upstream patchlevel

* Fri Jul 12 2013 Led <led@altlinux.ru> 1.9.3-alt27
- p452 upstream patchlevel

* Thu Jul 11 2013 Led <led@altlinux.ru> 1.9.3-alt26
- p451 upstream patchlevel

* Mon Jul 01 2013 Led <led@altlinux.ru> 1.9.3-alt25
- p448 upstream patchlevel

* Wed May 29 2013 Led <led@altlinux.ru> 1.9.3-alt24
- p432 upstream patchlevel

* Thu May 16 2013 Led <led@altlinux.ru> 1.9.3-alt23
- p430 upstream patchlevel

* Wed May 15 2013 Led <led@altlinux.ru> 1.9.3-alt22
- p429 upstream patchlevel

* Mon Apr 15 2013 Led <led@altlinux.ru> 1.9.3-alt21
- p415 upstream patchlevel

* Fri Apr 05 2013 Led <led@altlinux.ru> 1.9.3-alt20
- p411 upstream patchlevel

* Wed Apr 03 2013 Led <led@altlinux.ru> 1.9.3-alt19
- p408 upstream patchlevel

* Sat Mar 30 2013 Led <led@altlinux.ru> 1.9.3-alt18
- p401 upstream patchlevel

* Sat Mar 23 2013 Led <led@altlinux.ru> 1.9.3-alt17
- p394 upstream patchlevel

* Thu Feb 28 2013 Led <led@altlinux.ru> 1.9.3-alt16
- p393 upstream patchlevel

* Mon Feb 25 2013 Led <led@altlinux.ru> 1.9.3-alt15
- p392 upstream patchlevel

* Thu Feb 14 2013 Led <led@altlinux.ru> 1.9.3-alt14
- p386 upstream patchlevel:
  + JSON updated to 1.5.5

* Sun Feb 10 2013 Led <led@altlinux.ru> 1.9.3-alt13
- fixed BuildRequires (ALT#28533)

* Fri Feb 08 2013 Led <led@altlinux.ru> 1.9.3-alt12
- p385 upstream patchlevel

* Fri Feb 01 2013 Led <led@altlinux.ru> 1.9.3-alt11
- moved ri to separate subpackage
- moved rdoc to ruby-tools subpackage
- removed rdoc subpackage
- added strict requires of ri for ruby-doc-ri (ALT#28451)

* Tue Jan 15 2013 Led <led@altlinux.ru> 1.9.3-alt10
- p374 upstream patchlevel

* Sat Jan 12 2013 Led <led@altlinux.ru> 1.9.3-alt9
- p367 upstream patchlevel

* Tue Dec 25 2012 Led <led@altlinux.ru> 1.9.3-alt8
- p362 upstream patchlevel

* Sun Dec 16 2012 Led <led@altlinux.ru> 1.9.3-alt7
- p341 upstream patchlevel

* Sat Dec 15 2012 Led <led@altlinux.ru> 1.9.3-alt6
- %%files: fixed %%ruby_arch (for arches with the suffix "-eabi")

* Thu Dec 13 2012 Led <led@altlinux.ru> 1.9.3-alt5
- %%install: fixed %%ruby_arch (for arches with the suffix "-eabi")

* Wed Dec 12 2012 Led <led@altlinux.ru> 1.9.3-alt4
- fixed ruby libpath
- fixed BuildRequires

* Tue Dec 11 2012 Led <led@altlinux.ru> 1.9.3-alt3
- %%name-stdlibs: fixed Provides
- fixed requires
- built with default ruby_version

* Mon Dec 10 2012 Led <led@altlinux.ru> 1.9.3-alt2
- added more Provides/Obsoletes

* Sat Dec 08 2012 Led <led@altlinux.ru> 1.9.3-alt1
- 1.9.3

* Fri Apr 22 2011 Andriy Stepanov <stanv@altlinux.ru> 1.9.2-alt2.r31204.1
- Adopt Conflicts.

* Thu Apr 21 2011 Andriy Stepanov <stanv@altlinux.ru> 1.9.2-alt1.r31204.1
- SVN revision 31204.

* Fri Mar 18 2011 Andriy Stepanov <stanv@altlinux.ru> 1.9.2-alt1.r30896.1
- SVN revision 30896.
- Tests runs on single CPU. XXX: fix this one.

* Fri Dec 31 2010 Alexey I. Froloff <raorn@altlinux.org> 1.9.2-alt1.r30363.1
- SVN revision 30363 AKA 1.9.2p136
- Resurrected pager selection patch for ri
- Added filetrigger for site ri cache update

* Mon Nov 29 2010 Alexey I. Froloff <raorn@altlinux.org> 1.9.2-alt1.r29921.1
- SVN revision 29921 AKA 1.9.2p53

* Sat Oct 16 2010 Alexey I. Froloff <raorn@altlinux.org> 1.9.2-alt1.r29393.1
- SVN revision 29393 AKA 1.9.2p14

* Sat Sep 25 2010 Alexey I. Froloff <raorn@altlinux.org> 1.9.2-alt1.r29034.1
- SVN revision 29034 AKA 1.9.2p0
  + Incompatible changes:
    * $: no longer includes the current directory, use require_relative
    * Symbol with an invalid encoding is forbidden to exist.
    * Enumerator#rewind now calls the "rewind" method of the enclosed
      object if defined.
    * Enumerator#next doesn't clear the position at end.
    * Kernel#instance_eval yields the receiver.
    * The year argument of Time.{utc,gm,local,mktime} is now interpreted
      as the value itself.  For example, Time.utc(99) means the year 99
      AD, not 1999 AD.
    * Socket#{recvfrom,recvfrom_nonblock,accept,accept_nonblock,sysaccept}
      returns a sender address as Addrinfo object instead of a binary
      sockaddr string.  Addrinfo#to_s returns the old binary sockaddr
      string.
    * BasicSocket#getsockopt returns Socket::Option object instead of a
      binary string.  Socket::Option#to_s returns the old binary string.
    * Socket.do_not_reverse_lookup is turned on by default now.
    * Time.parse raises ArgumentError when no date information.
    * Regexp properties (\p{}) names now ignore underscores, spaces, and
      case, so \p{ol chiki} is the same as \p{Ol_Chiki}
    * Regexps now support Unicode 5.2 (new characters and scripts)
    * \d, \s, and \w are now ASCII only; use POSIX bracket classes and
      \p{} for Unicode semantics
  + See NEWS for more info...

* Tue Dec 29 2009 Alexey I. Froloff <raorn@altlinux.org> 1.9.1-alt1.r26040.1
- Fix String#ljust, String#rjust and String#center breakage after
  CVE-2009-4124 fix

* Wed Dec 09 2009 Alexey I. Froloff <raorn@altlinux.org> 1.9.1-alt1.r26040
- SVN revision 26040 AKA 1.9.1p376 (2009-12-07)
  + CVE-2009-4124

* Sun Nov 29 2009 Alexey I. Froloff <raorn@altlinux.org> 1.9.1-alt1.r25953
- SVN revision 25953 AKA 1.9.1p355 (2009-11-27)
- Backported fix for REXML formatter exception when duplicate namespaced
  attributes exist

* Thu Nov 26 2009 Alexey I. Froloff <raorn@altlinux.org> 1.9.1-alt1.r25816.1
- Make tests pass on ARM

* Wed Nov 18 2009 Alexey I. Froloff <raorn@altlinux.org> 1.9.1-alt1.r25816
- SVN revision 25816 AKA 1.9.1p339 (2009-11-17)
- Backported fix for String#[] issues with short UTF-8 strings

* Tue Nov 10 2009 Alexey I. Froloff <raorn@altlinux.org> 1.9.1-alt1.20091101
- SVN snapshot 20091101 AKA 1.9.1-p333
- Execute full test suite in %%check

* Sat Sep 26 2009 Alexey I. Froloff <raorn@altlinux.org> 1.9.1-alt1.20090809
- SVN snapshot 20090809 AKA 1.9.1-p281
 + digest/sha2: Update to 1.0 RELEASE which fixes an off-by-one bug in
   SHA-256 hashing.

* Tue Jul 28 2009 Alexey I. Froloff <raorn@altlinux.org> 1.9.1-alt1.20090727
- SVN snapshot 20090727 AKA 1.9.1-p252
- Fixed "warning: `*' interpreted as argument prefix" in pathname.rb

* Mon Jul 06 2009 Alexey I. Froloff <raorn@altlinux.org> 1.9.1-alt1.20090625
- SVN snapshot 20090625 AKA 1.9.1.203
  + CVE-2009-1904: DoS vulnerability in BigDecimal module
- All ruby-module-*'s merged back to ruby-stdlibs and ruby-stdlibs-tk
- Shared library moved back from /%%_lib to %%_libdir
- Disabled rubygems by default, use ruby option "--enable gems" to enable
- All packages with RI documentation should depend on ruby-doc-ri
- Modules excluded from stdlibs (packaged separately):
  + json
  + minitest
  + racc
  + rake
  + rubygems
  + test/unit

* Sun Aug 31 2008 Sir Raorn <raorn@altlinux.ru> 1.8.7-alt7
- Use config.sub when guessing target architecture
- Use files.req for directory provides (needs updated rpm-build-ruby)

* Tue Aug 12 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.8.7-alt6
- 1.8.7.72
  + Multiple vulnerabilities
    + Several vulnerabilities in safe level
      + untrace_var is permitted at safe level 4
      + $PROGRAM_NAME may be modified at safe level 4
      + insecure methods may be called at safe level 1-3
      + syslog operations are permitted at safe level 4
    + DoS vulnerability in WEBrick
    + Lack of taintness check in dl
    + CVE-2008-1447: DNS spoofing vulnerability in resolv.rb

* Thu Jul 10 2008 Sir Raorn <raorn@altlinux.ru> 1.8.7-alt5
- 1.8.7.51
- Fix FHS patch which was broken in 1.8.7-alt3
- Put ruby binary and libruby back to /usr/

* Fri Jun 20 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.8.7-alt4
- 1.8.7.22
  + CVE-2008-2726

* Thu Jun 19 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.8.7-alt3
- 1.8.7.19
- Built with libdb4.7

* Tue Jun 03 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.8.7-alt2
- 1.8.7.3
  + lib/erb.rb: works fine without strscan

* Sun Jun 01 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.8.7-alt1
- 1.8.7
  + Enumerator is now a built-in module

* Sat Mar 29 2008 Sir Raorn <raorn@altlinux.ru> 1.8.6-alt8
- Built with new rpm-build-ruby:
 + Removed rpm-build-ruby subpackage
 + Removed all manual dependencies
- Switched to Tcl/Tk stubs (8.5) instead of direct linking (sbolshakov@)

* Thu Mar 06 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.8.6-alt7
- update to 1.8.6.114
  + fix file access vulnerability of WEBrick

* Wed Feb 06 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.8.6-alt6
- rubynode updated to 0.1.5
  + Fix a possible segfault with OP_ASGN2 nodes
- synced with Debian ruby1.8-1.8.6.111-4
  + rcov may crash because of backwards incompatibility.
    This fix is a back port from the upstream (r14826-15141).
- temporary build with tk8.4 to avoid crash

* Sun Feb 03 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.8.6-alt5
- remove non-ascii symbols from description and summary

* Sat Feb 02 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.8.6-alt4
- ruby-module-rubynode: rubynode 0.1.4 integrated into ruby tree
- select first valid pager, not last (raorn@)

* Fri Jan 11 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.8.6-alt3
- branch based git repository
- update to ruby_1_8_6 svn branch (revision 14091)
- sync with debian 1.8.6.111-2
  + CVE-2007-5162
- install libruby.so into %%_libdir (bug #13951)
- move arch-depended site_ruby to /usr/local/ (raorn@)
- update macros (bug #13933)
- add missing deps to ruby-module-rexml

* Wed Apr 11 2007 Kirill A. Shutemov <kas@altlinux.ru> 1.8.6-alt2
- generation rdoc documentation:
  + add make rdoc

* Sun Apr 01 2007 Kirill A. Shutemov <kas@altlinux.ru> 1.8.6-alt1
- build without debug

* Sun Mar 25 2007 Kirill A. Shutemov <kas@altlinux.ru> 1.8.6-alt0
- 1.8.6

* Thu Feb 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.8.5-alt4.1
- added rpm-build-ruby subpackage, moved rpm macros to it.

* Thu Jan 11 2007 Kirill A. Shutemov <kas@altlinux.ru> 1.8.5-alt4
- /usr/inculde/ruby added to libruby-devel(bug #10506)

* Fri Jan 05 2007 Sir Raorn <raorn@altlinux.ru> 1.8.5-alt3.1
- Do not handle html-style comments in code as specials

* Tue Dec 05 2006 Kirill A. Shutemov <kas@altlinux.ru> 1.8.5-alt3
- 1.8.5-p2
- ri pager selection fixing

* Tue Oct 24 2006 Sir Raorn <raorn@altlinux.ru> 1.8.5-alt2.1
- Re-added ruby-stdlibs - pure virtual package with all requires
- mkmf.rb moved to libruby-devel
- base64.rb moved to module-digest
- pstore.rb moved to module-fileutils
- module-stdlibs renamed to module-misc
- libruby-devel requires tool-rdoc
- Hardened requires on libruby for module-*
- Re-added lost %%ruby_configure macro
- Added macroses for "setup.rb"-based modules
- Added %%ruby_vendor macro - ruby -rvendor-specific

* Mon Oct 09 2006 Kirill A. Shutemov <kas@altlinux.ru> 1.8.5-alt2
- spec rewrite from scratch
- stdlibs sparate to many packages
- new packages naming strategy
- ruby executable moved to /bin
- ruby library moved to /%%_lib
- headers moved to /usr/include/ FHS
- and many others

* Tue Sep 26 2006 Kirill A. Shutemov <kas@altlinux.ru> 1.8.5-alt1
- 1.8.5
- debian 1.8.5-2 synced
- warnings in core removed

* Thu Apr 13 2006 Sir Raorn <raorn@altlinux.ru> 1.8.4-alt5
- Fixed x86_64 filelist and fhs patch (closes: #9401)
- rdocall script dropped

* Sat Mar 25 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.8.4-alt4.1
- Rebuilt with libdb4.4.

* Fri Mar 03 2006 Kirill A. Shutemov <kas@altlinux.ru> 1.8.4-alt4
- patching order changed
- Patch ported from FC ruby-1.8-fc-no-eaccess.patch:
    backported from ruby CVS to avoid conflict  between newer glibc.
- ruby-1.8-alt-ri-DESTDIR.patch removed

* Fri Mar 03 2006 Kirill A. Shutemov <kas@altlinux.ru> 1.8.4-alt3
- Patches ported from debian:
  * ruby-1.8-deb-delegate.rb.patch
   - delegate.rb should use Kernel::raise for Thread.
     [ruby-dev:22681][ruby-dev:22684]
   - delegate.rb should not delegate singleton_method_added.
  * ruby-1.8-deb-.document.patch
   - rdoc processes net/* and some libraries.
  * ruby-1.8-deb-yaml_bignum.patch
   - YAML.dump/load cannot handle Bignum. [ruby-core:6159]
   - patch from Michael Ablassmeier
  * ruby-1.8-deb-yaml_symbol.patch
   - YAML loading of quoted symbols is broken

* Mon Feb 27 2006 Kirill A. Shutemov <kas@altlinux.ru> 1.8.4-alt2
- FHS patch updated:
  * DESTDIR processing fixed
  * rbconfig back to archlibdir
- Generating system-wide documentation for ri using make

* Tue Feb 14 2006 Kirill A. Shutemov <kas@altlinux.ru> 1.8.4-alt1
- spec cleanups
- FHS patch updated: headers in /usr/include/ruby/%%subver

* Mon Jan 23 2006 Sir Raorn <raorn@altlinux.ru> 1.8.4-alt0
- [1.8.4]

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.8.2-alt7.1
- Rebuilt with libreadline.so.5.

* Wed Jun 08 2005 Kirill A. Shutemov <kas@altlinux.ru> 1.8.2-alt7
- rebuild

* Fri Apr 15 2005 Anton D. Kachalov <mouse@altlinux.org> 1.8.2-alt6.1
- multilib support

* Mon Feb 28 2005 Kirill A. Shutemov <kas@altlinux.ru> 1.8.2-alt6
- %%configure --with-vendordir
- Change default DESTDIR in rbconfig.rb

* Thu Feb 10 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.8.2-alt5.1.1
- Updated libdb4 build dependencies.
- Rebuilt with libdb4.3.

* Mon Jan 24 2005 Sir Raorn <raorn@altlinux.ru> 1.8.2-alt5.1
- Some spec cleanups
- Use --disable-rpath
- Use `%%_lib' instead of `lib' (maybe-x86_64-fixes)
- Do not set LD_LIBRARY_PATH - rubytest.rb does it for us
- Create created.rid file in RI site dir so it will look like doc dir
- Use rdoc -a by default

* Mon Jan 10 2005 Kirill A. Shutemov <kas@altlinux.ru> 1.8.2-alt5
- 1.8.2 release
- ruby-1.8.2-alt-extdoc.patch in upstream now

* Sun Sep 12 2004 Kirill A. Shutemov <kas@altlinux.ru> 1.8.2-alt4
- Move extensions docs from extensions/ext to extensions

* Sat Sep 11 2004 Sir Raorn <raorn@altlinux.ru> 1.8.2-alt3.2
- %%dir'ed ri_sitedir

* Sat Sep 11 2004 Sir Raorn <raorn@altlinux.ru> 1.8.2-alt3.1
- Changed %%ruby_ri_systemdir to %%ruby_ri_sitedir (points to
  %%_datadir/ri/%%subver/site)
- Document more external modules (which have it's own documentation):
  + iconv
  + io/wait
  + strscan
  + zlib

* Sun Sep 05 2004 Kirill A. Shutemov <kas@altlinux.ru> 1.8.2-alt3
- Add %%ruby_ri_systemdir and %%rdoc macros
- Now --ri-site defers DESTDIR (patch by Alexey I. Froloff)
- Add script 'rdocall' for generate all rdoc documentation

* Sat Aug 14 2004 Kirill A. Shutemov <kas@altlinux.ru> 1.8.2-alt2
- 1.8.2-preview2

* Sun Jul 18 2004 Kirill A. Shutemov <kas@altlinux.ru> 1.8.2-alt1
- 1.8.2-preview1
- New patch to fix 3506 by Sean Russell

* Tue Jul 06 2004 Kirill A. Shutemov <kas@altlinux.ru> 1.8.1-alt9
- Add %%ruby_begin and %%ruby_end macros
- Add README.ALT-CP1251 and README.ALT-KOI8

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.8.1-alt8.1
- Rebuilt with openssl-0.9.7d.

* Tue Apr 20 2004 Kirill A. Shutemov <kas@altlinux.ru> 1.8.1-alt8
- Fixed bug #3506(REXML)

* Wed Mar 24 2004 Alexander Bokovoy <ab@altlinux.ru> 1.8.1-alt7
- Snapshot as of 2004/03/24
- Fixed:
    + socket extension build in chrooted environment

* Tue Mar 09 2004 Alexander Bokovoy <ab@altlinux.ru> 1.8.1-alt6
- Snapshot as of 2004/03/08

* Mon Feb 16 2004 Alexander Bokovoy <ab@altlinux.ru> 1.8.1-alt5
- Snapshot as of 2004/02/15
- Rebuild against libdb4.2

* Sun Dec 28 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8.1-alt4
- Snapshot as of 2003/12/28 of ruby_1_8 branch
- Removed:
    + patch for rdoc fixes (integrated to upstream)
- Fixed:
    + segfault in Syck's emitter (matz)

* Thu Dec 25 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8.1-alt3
- Fixed:
    + rdoc's simple markup ToFlow class
- We obsolete 'ri' package now but do not package rdoc-ed
  'ri' metainfo for standard libs so far (nothing to package yet)

* Wed Dec 24 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8.1-alt2
- Fixed:
    + rdoc's simple markup classes

* Wed Dec 24 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Thu Dec 18 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt11
- Snapshot as of 2003/12/18
- REXML support for iconv(3) is in upstream now

* Sat Sep 27 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt10
- Snapshot as of 2003/09/27
- All external documentation moved to ruby-doc-extra package

* Thu Aug 21 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt9
- Snapshot as of 2003/08/21

* Wed Aug 06 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt8
- Fixed:
  + REXML now falls back to iconv(3) when there is no native
    support for specified encoding (ab)

* Tue Aug 05 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt7
- Final Ruby 1.8.0 + post-release fixes from CVS

* Sat Aug 02 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt6
- 2003/08/02
- OpenSSL support integrated, thus ruby-openssl is obsolete now

* Tue Jul 22 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt5
- Snapshot as of 2003/07/22

* Mon Jul 07 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt4
- Test::Unit is included into stdlibs, ruby-stdlibs package
  obsoletes ruby-testunit now and provides it for backward
  compatibility

* Sun Jul 06 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt3
- Tag release in BTE
- Remove tinfo patch for curses, integrated into upstream

* Sat Jul 05 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt2
- 1.8 CVS snapshot (2003/07/05)

* Sun Jun 29 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt1
- 1.8 CVS snapshot (2003/06/29)
- Patches updated, CGI patch excluded (already in upstream)
- Add %%_libdir/%%name/vendor_ruby/%%subver/%%{_target_cpu}-%%{_host_os} to the list
  of owned directories for stdlibs-core
- Enhance dependencies between subpackages:
    + lib%%name is a base package, everything else requires it (through a chain),
      it also owns a Ruby subtree directories
    + %%name-stdlibs prerequires lib%%name
    + %%name-stdlibc-tk prerequires %%name-stdlibs
    + every third-party Ruby package *should* prerequire lib%%name
      if it is installable into Ruby subtree
- Clean up spec file:
    + Fix miniruby calls to use non-Perlish variable notation only
- Removed:
    + %%name-stdlib-core package merged with lib%%name
- Major review of packaged documentation:
    + Ruby FAQ is now in A4 PDF
    + Hal Fulton's "Rubyesque API" from EuRuKo03
    + Tobias Peters' "Garbage in Ruby Extensions" from EuRuKo03
    + Features of Ruby 1.8 since Ruby 1.6 from ruby-shim project

* Tue Dec 10 2002 Alexander Bokovoy <ab@altlinux.ru> 1.7.3-alt9
- Fixed:
    + Readline extension was lost due wrong check for libtermcap instead
      of libtinfo
    + fileutils.rb incorrect behaviour for symlinks (mouse@altlinux.ru)

* Fri Nov 22 2002 Alexander Bokovoy <ab@altlinux.ru> 1.7.3-alt8
- Fixed:
    + IRB code to not use #initialize publicly as it is a private method
      in Ruby 1.7 since 2002-11-14.
- Removed:
    + Proxy-Authorization support in Net::HTTP patch (integrated into upstream)

* Tue Nov 19 2002 Alexander Bokovoy <ab@altlinux.ru> 1.7.3-alt7
- Changed:
    + Installation splitted between %%_datadir and %%_libdir
      in order to be more conformant to FHS
    + Directory structure is stored in %%name-stdlibs-core package
    + vendordir/vendorarchdir added as /usr/{lib,share}/ruby/vendor_ruby
      and site-specific dirs moved to /usr/local
- Fixed:
    + curses modules build fixed
    + mkmf.rb to successuly configure C++ exetnsions

* Tue Oct 29 2002 Alexander Bokovoy <ab@altlinux.ru> 1.7.3-alt6
- Removed:
    + misc/*.el as now they are part of (X)Emacs prog-modes
- Added:
    + Patch to fix CGI and Cookies to follow 1.7's split() behaviour
    + Gdbm module support
- Fixed:
    + Getaddrinfo detection code in mkmf
- ToDo:
    + Fix mkmf to run run_test() against locally compiled libruby.so
      when dealing with extensions, not against (non-)existent system-wide one

* Sat Oct 26 2002 Alexander Bokovoy <ab@altlinux.ru> 1.7.3-alt5
- News snapshot (2002/10/26)
- Fixed BuildReq to allow build of gdbm module
- Group changed to Development/Ruby
- Remove ruby-stdlibs-win32ole as it seems tend to not work

* Wed Oct 09 2002 Alexander Bokovoy <ab@altlinux.ru> 1.7.3-alt4
- New snapshot (2002/10/09)
- Changed:
    + Emacs support moved to %%name-doc and placed in %%_docdir/%%name-%%version/misc
      unless XEmacs and GNU Emacs maintaining teams decide where and how
      to put third-party program modes. Also, XEmacs already has (an outdated)
      ruby-mode.

* Thu Sep 26 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.7.3-alt3
- rebuilt with tcl 8.4

* Thu Sep 19 2002 Alexander Bokovoy <ab@altlinux.ru> 1.7.3-alt2
- New snapshot (2002/09/19)
- Added:
    + Patch to support proxy authorization in Net::HTTP (Alexander Bokovoy)
    + Win32ole support using Wine as ruby-stdlibs-win32ole
    + db module using libdb4
- Fixed:
    + Build requires to include Readline

* Mon Sep 09 2002 Alexander Bokovoy <ab@altlinux.ru> 1.7.3-alt1
- Initial build of 1.7.x
- Standard library splitted off to ruby-stdlibs
- More libification:
    + Dynamic library splitted off to libruby
    + ruby-devel renamed to libruby-devel
    + ruby-devel-static renamed to libruby-devel-static
- Tcl/Tk extensions work now and split off to ruby-stdlibs-tk
- Documentation extended

* Wed Aug  7 2002 Grigory Milev <week@altlinux.ru> 1.6.7-alt1
- minor spec cleanup

* Tue May 07 2002 Alexander Bokovoy <ab@altlinux.ru> 1.6.7-alt1
- 1.6.7 + post release fixes

* Fri Feb 08 2002 Alexander Bokovoy <ab@altlinux.ru> 1.6.6-alt3
- Dependencies for ruby-doc package refined

* Mon Jan 28 2002 Stanislav Ievlev <inger@altlinux.ru> 1.6.6-alt2
- rebuild with new python

* Wed Dec 26 2001 Alexander Bokovoy <ab@altlinux.ru> 1.6.6-alt1
- 1.6.6
- Removed:
    + mkmf patch (integrated into upstream)
    + Regexp patch (integrated into upstream)

* Thu Dec 20 2001 Alexander Bokovoy <ab@altlinux.ru> 1.6.5-alt6
- Fixed:
    + mkmf patch updated to one from Nobu Nakada

* Thu Dec 13 2001 Alexander Bokovoy <ab@altlinux.ru> 1.6.5-alt5
- Fixed:
    + Regexp UTF-8 handling (backport from 1.7.x)
    + %%_libdir/ruby/site_ruby/%%subver added

* Wed Dec 05 2001 Alexander Bokovoy <ab@altlinux.ru> 1.6.5-alt4
- Updated:
    + Programming Ruby up to 0.3a
    + URL for Ruby FAQ
- Fixed:
    + Programming Ruby html structure

* Fri Nov 30 2001 Alexander Bokovoy <ab@altlinux.ru> 1.6.5-alt3
- Fixed:
    + mkmf to allow full usage of $(DESTDIR), this is required to
      properly build extension packages

* Tue Oct 16 2001 Alexander Bokovoy <ab@altlinux.ru>   1.6.5-alt2
- Enable shared library build
- Move static library to devel-static

* Fri Sep 28 2001 Stanislav Ievlev <inger@altlinux.ru> 1.6.5-alt1
- 1.6.5

* Thu Jun 14 2001 Stanislav Ievlev <inger@altlinux.ru> 1.6.4-alt1
- 1.6.4

* Mon May 28 2001 Stanislav Ievlev <inger@altlinux.ru> 1.6.3-alt3
- New patches from Mandrake.

* Mon Apr 23 2001 Stanislav Ievlev <inger@altlinux.ru> 1.6.3-alt2
- Fix extentions. Thanks to Pixel.

* Wed Apr 18 2001 Stanislav Ievlev <inger@altlinux.ru> 1.6.3-alt1
- Up to 1.6.3

* Tue Jan 16 2001 AEN <aen@logic.ru>
- RE adaptations

* Mon Nov 27 2000 Pixel <pixel@mandrakesoft.com> 1.6.1-4mdk
- build again full optflags

* Wed Nov  8 2000 Pixel <pixel@mandrakesoft.com> 1.6.1-3mdk
- build without -fomit-frame-pointer for time being
- capitalize summaries

* Mon Oct  2 2000 Pixel <pixel@mandrakesoft.com> 1.6.1-2mdk
- fix mispelling

* Thu Sep 28 2000 Pixel <pixel@mandrakesoft.com> 1.6.1-1mdk
- new version
- remove "--with-default-kcode=none", not more needed
- remove setting optflags to -O2, ruby doesn't crashes any more

* Tue Sep 19 2000 Pixel <pixel@mandrakesoft.com> 1.6.0-1mdk
- new version

* Wed Aug 23 2000 Pixel <pixel@mandrakesoft.com> 1.4.6-6mdk
- add packager

* Tue Aug 22 2000 Pixel <pixel@mandrakesoft.com> 1.4.6-5mdk
- nicer site-start.d/ruby.el (use add-to-list)

* Tue Aug 22 2000 Pixel <pixel@mandrakesoft.com> 1.4.6-4mdk
- fix missing %%config

* Tue Aug 22 2000 Pixel <pixel@mandrakesoft.com> 1.4.6-3mdk
- use %%_sysconfdir/emacs/site-start.d for the ruby-mode.el

* Fri Aug 18 2000 Pixel <pixel@mandrakesoft.com> 1.4.6-2mdk
- rebuild (fredlsux)

* Fri Aug 18 2000 Pixel <pixel@mandrakesoft.com> 1.4.6-1mdk
- new version
- remove menu

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.4.5-6mdk
- automatically added BuildRequires

* Wed Jul 19 2000 Pixel <pixel@mandrakesoft.com> 1.4.5-5mdk
- rebuild with clean clean_menus

* Wed Jul 19 2000 Pixel <pixel@mandrakesoft.com> 1.4.5-4mdk
- macroization
- BM

* Thu Jul 13 2000 Pixel <pixel@mandrakesoft.com> 1.4.5-3mdk
- fix %%URL

* Sun Jun 25 2000 Pixel <pixel@mandrakesoft.com> 1.4.5-2mdk
- rebuild (src.rpm got lost :( )

* Fri Jun 23 2000 Pixel <pixel@mandrakesoft.com> 1.4.5-1mdk
- new version

* Wed Jun 14 2000 Pixel <pixel@mandrakesoft.com> 1.4.4-1mdk
- new version

* Mon Apr 10 2000 Pixel <pixel@mandrakesoft.com> 1.4.3-6mdk
- fix group for doc

* Mon Mar 27 2000 Pixel <pixel@mandrakesoft.com> 1.4.3-5mdk
- add menu

* Sat Mar 25 2000 Pixel <pixel@mandrakesoft.com> 1.4.3-4mdk
- new group + cleanup

* Wed Feb 16 2000 Pixel <pixel@mandrakesoft.com> 1.4.3-3mdk
- build with no charset conversion (was kanji :)

* Mon Feb 14 2000 Pixel <pixel@mandrakesoft.com> 1.4.3-2mdk
- added the reference manual and FAQ in doc
- moved the lib/README in ext

* Mon Feb 14 2000 Pixel <pixel@mandrakesoft.com> 1.4.3-1mdk
- mandrake adaptation and spliting in -/doc/extensions

* Wed Dec 08 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- Updated to version 1.4.3

* Mon Sep 20 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- Updated to version 1.4.2 (Sep 18)

* Fri Sep 17 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- Updated to version 1.4.2

* Tue Aug 17 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- Updated to version 1.4.0

* Fri Jul 23 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- 2nd release
- Updated to version 1.2.6(15 Jul 1999)
- striped %%prefix/bin/ruby

* Mon Jun 28 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- Updated to version 1.2.6(21 Jun 1999)

* Wed Apr 14 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- Updated to version 1.2.5

* Fri Apr 09 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- Updated to version 1.2.4

* Fri Dec 25 1998 Toru Hoshina <hoshina@best.com>
- Version up to 1.2 stable.

* Fri Nov 27 1998 Toru Hoshina <hoshina@best.com>
- Version up to 1.1c9.

* Thu Nov 19 1998 Toru Hoshina <hoshina@best.com>
- Version up to 1.1c8, however it appear short life :-P

* Fri Nov 13 1998 Toru Hoshina <hoshina@best.com>
- Version up.
