%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: babel
Version: 2.0.0
Release: alt2.qa2
Summary: Language tool for high-performance scientific computing community
 
License: LGPL v2.1
Group: Sciences/Mathematics
Url: http://www.llnl.gov/CASC/components/babel.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

Requires: %name-common = %version-%release
Requires: lib%name = %version-%release
Requires: lib%name-devel = %version-%release
Requires: %name-j = %version-%release
Requires: python-module-sidl = %version-%release
Requires: python-module-sidlx = %version-%release

Conflicts: openbabel

BuildRequires(pre): rpm-build-compat rpm-build-python
BuildRequires: gcc-fortran gcc-c++ %mpiimpl-devel libltdl7-devel
BuildRequires: libxml2-devel libparsifal-devel
BuildRequires: jpackage-compat java-devel-default jpackage-utils gnu-getopt
BuildRequires: python-devel libnumpy-devel /proc chrpath

%description
  Babel is a language interoperability tool intended for use by
the high-performance scientific computing community.  Developed
by the Components project (http://www.llnl.gov/CASC/components)
at Lawrence Livermore National Laboratory, Babel supports the
Scientific Interface Definition Language (SIDL) for the language-
independent declaration of interfaces associated with scientific
software packages.

  The Babel tool, applied to a SIDL file, results in the automatic
generation of the associated skeleton and stub source files.  The
Babel user then need only add the necessary code to the _Impl source
files to complete the provision of a language-independent interface
to the package described by the SIDL file.  The languages currently
supported by Babel are C, C++, F77, F90, Java and Python.  

This package contains main compiler files. Conflicts with Open Babel, because
contains another file named 'babel' in /usr/bin.

%package -n lib%name
Summary: Shared libraries of Babel
Group: System/Libraries

%description -n lib%name
  Babel is a language interoperability tool intended for use by
the high-performance scientific computing community.  Developed
by the Components project (http://www.llnl.gov/CASC/components)
at Lawrence Livermore National Laboratory, Babel supports the
Scientific Interface Definition Language (SIDL) for the language-
independent declaration of interfaces associated with scientific
software packages.

  The Babel tool, applied to a SIDL file, results in the automatic
generation of the associated skeleton and stub source files.  The
Babel user then need only add the necessary code to the _Impl source
files to complete the provision of a language-independent interface
to the package described by the SIDL file.  The languages currently
supported by Babel are C, C++, F77, F90, Java and Python.  

This package contains shared libraries of Babel.

%package -n lib%name-devel
Summary: Development files for Babel
Group: Development/Other
Requires: %name = %version-%release
Requires: %name-common = %version-%release
Requires: lib%name = %version-%release
Requires: %name-j = %version-%release
Requires: python-module-sidl = %version-%release

%description -n lib%name-devel
  Babel is a language interoperability tool intended for use by
the high-performance scientific computing community.  Developed
by the Components project (http://www.llnl.gov/CASC/components)
at Lawrence Livermore National Laboratory, Babel supports the
Scientific Interface Definition Language (SIDL) for the language-
independent declaration of interfaces associated with scientific
software packages.

  The Babel tool, applied to a SIDL file, results in the automatic
generation of the associated skeleton and stub source files.  The
Babel user then need only add the necessary code to the _Impl source
files to complete the provision of a language-independent interface
to the package described by the SIDL file.  The languages currently
supported by Babel are C, C++, F77, F90, Java and Python.  

This package contains development files for Babel.

%package -n python-module-sidl
Summary: Build Python support extension modules for sidl
Group: Development/Python
Requires: lib%name = %version-%release
%setup_python_module sidl

%description -n python-module-sidl
  Babel is a language interoperability tool intended for use by
the high-performance scientific computing community.  Developed
by the Components project (http://www.llnl.gov/CASC/components)
at Lawrence Livermore National Laboratory, Babel supports the
Scientific Interface Definition Language (SIDL) for the language-
independent declaration of interfaces associated with scientific
software packages.

  The Babel tool, applied to a SIDL file, results in the automatic
generation of the associated skeleton and stub source files.  The
Babel user then need only add the necessary code to the _Impl source
files to complete the provision of a language-independent interface
to the package described by the SIDL file.  The languages currently
supported by Babel are C, C++, F77, F90, Java and Python.  

This package contains python support extension modules for sidl.

%package -n python-module-sidlx
Summary: Build Python support experimental extension modules for sidl
Group: Development/Python
Requires: lib%name = %version-%release
%setup_python_module sidlx

%description -n python-module-sidlx
  Babel is a language interoperability tool intended for use by
the high-performance scientific computing community.  Developed
by the Components project (http://www.llnl.gov/CASC/components)
at Lawrence Livermore National Laboratory, Babel supports the
Scientific Interface Definition Language (SIDL) for the language-
independent declaration of interfaces associated with scientific
software packages.

  The Babel tool, applied to a SIDL file, results in the automatic
generation of the associated skeleton and stub source files.  The
Babel user then need only add the necessary code to the _Impl source
files to complete the provision of a language-independent interface
to the package described by the SIDL file.  The languages currently
supported by Babel are C, C++, F77, F90, Java and Python.  

This package contains python support experimental extension modules for sidl.

%package j
Summary: Babel java packages
Group: Development/Java
BuildArch: noarch
Requires: lib%name = %version-%release
Requires: java >= 1.5.0

%description j
  Babel is a language interoperability tool intended for use by
the high-performance scientific computing community.  Developed
by the Components project (http://www.llnl.gov/CASC/components)
at Lawrence Livermore National Laboratory, Babel supports the
Scientific Interface Definition Language (SIDL) for the language-
independent declaration of interfaces associated with scientific
software packages.

  The Babel tool, applied to a SIDL file, results in the automatic
generation of the associated skeleton and stub source files.  The
Babel user then need only add the necessary code to the _Impl source
files to complete the provision of a language-independent interface
to the package described by the SIDL file.  The languages currently
supported by Babel are C, C++, F77, F90, Java and Python.  

This package contains Babel java packages.

%package common
Summary: Babel common files
Group: Development/Other
BuildArch: noarch

%description common
  Babel is a language interoperability tool intended for use by
the high-performance scientific computing community.  Developed
by the Components project (http://www.llnl.gov/CASC/components)
at Lawrence Livermore National Laboratory, Babel supports the
Scientific Interface Definition Language (SIDL) for the language-
independent declaration of interfaces associated with scientific
software packages.

  The Babel tool, applied to a SIDL file, results in the automatic
generation of the associated skeleton and stub source files.  The
Babel user then need only add the necessary code to the _Impl source
files to complete the provision of a language-independent interface
to the package described by the SIDL file.  The languages currently
supported by Babel are C, C++, F77, F90, Java and Python.  

This package contains Babel common files.

%package javadoc
Summary: Javadoc for Babel
Group: Development/Documentation
BuildArch: noarch

%description javadoc
  Babel is a language interoperability tool intended for use by
the high-performance scientific computing community.  Developed
by the Components project (http://www.llnl.gov/CASC/components)
at Lawrence Livermore National Laboratory, Babel supports the
Scientific Interface Definition Language (SIDL) for the language-
independent declaration of interfaces associated with scientific
software packages.

  The Babel tool, applied to a SIDL file, results in the automatic
generation of the associated skeleton and stub source files.  The
Babel user then need only add the necessary code to the _Impl source
files to complete the provision of a language-independent interface
to the package described by the SIDL file.  The languages currently
supported by Babel are C, C++, F77, F90, Java and Python.  

This package contains Javadoc for Babel.

%package manual
Summary: User manual for Babel
Group: Development/Documentation
BuildArch: noarch

%description manual
  Babel is a language interoperability tool intended for use by
the high-performance scientific computing community.  Developed
by the Components project (http://www.llnl.gov/CASC/components)
at Lawrence Livermore National Laboratory, Babel supports the
Scientific Interface Definition Language (SIDL) for the language-
independent declaration of interfaces associated with scientific
software packages.

  The Babel tool, applied to a SIDL file, results in the automatic
generation of the associated skeleton and stub source files.  The
Babel user then need only add the necessary code to the _Impl source
files to complete the provision of a language-independent interface
to the package described by the SIDL file.  The languages currently
supported by Babel are C, C++, F77, F90, Java and Python.  

This package contains user manual for Babel.


%prep
%setup
find -name Makefile.in -exec sed 's/-traditional/& -Ubool -Uvector/' -i {} \;

%build
export JAVAPREFIX="%_libexecdir/jvm/java"
export CLASSPATH=".:$(build-classpath gnu-getopt):$(pwd)/compiler"
export JAVACFLAGS="-classpath $CLASSPATH"
export JAVAFLAGS=""
export MPI_VENDOR=%mpiimpl
source %mpidir/bin/mpivars.sh

%configure \
	--enable-pure-static-runtime=no \
	--enable-static=no \
	--with-gnu-ld \
	--with-F90-vendor=GNU \
	--with-libparsifal=%prefix \
	--with-libxml2=%prefix \
	--with-mpi=%mpidir/bin \
	--with-ltdl-lib=%_libdir \
	--with-ltdl-include=%_includedir \
	--enable-java=$JAVAPREFIX

%install
source %mpidir/bin/mpivars.sh
%make_build
touch bin/revision.txt
%makeinstall_std

rm -f %buildroot%_includedir/c
install -d %buildroot%_includedir/c

# fix bin files

sed -i \
	-e 's/^\(JAVA\)\=.*/\1="java"/' \
	-e 's/^\(is_installed\)\=.*/\1="true"/' \
	-e 's/xerces\-2\.9\.1/xerces-j2/g' \
	-e 's/\-I\ /-I. /g' \
	-e 's/\-I\"/-I."/g' \
	%buildroot%_bindir/babel*
sed -i 's|\${prefix}/lib|%_javadir|g' %buildroot%_bindir/babel*

install -d %buildroot%_docdir/%name
mv %buildroot%_docdir/%name-%version/* %buildroot%_docdir/%name/

# rename conflicted files

mv %buildroot%_datadir/aclocal/libtool.m4 \
	%buildroot%_datadir/aclocal/libtool-%name.m4
mv %buildroot%_datadir/aclocal/ltdl.m4 \
	%buildroot%_datadir/aclocal/ltdl-%name.m4

# prepare libs

install -d %buildroot%_javadir
pushd %buildroot%_libexecdir
rm -f xerces* xalan.*
mv LICENSE-SAX.html java-getopt.INFO java-getopt.LICENSE $OLDPWD/
mv *.jar %buildroot%_javadir/
popd

# javadoc

install -d %buildroot%_javadocdir/%name-%version
mv %buildroot%_docdir/%name/compiler-javadoc \
	%buildroot%_javadocdir/%name-%version/

sed -i -e 's/^\(predep_objects\|postdep_objects\|compiler_lib_search_path\)=.*/\1=""/' \
       -e 's/^\(archive\(_expsym\)\?_cmds=\".*\) -nostdlib /\1 /' \
	%buildroot%_bindir/%name-libtool
out="\$(\$CC -print-search-dirs |\$SED -e '/^libraries: *=/!d;s///;s!/:!:!g;s!/\$!!;s/:/ /g')"
sed -i 's#^\(compiler_lib_search_dirs="\)/.*#\1'"$out"'"#' \
	%buildroot%_bindir/%name-libtool

sed -i 's|%buildroot||' %buildroot%_libdir/libsidl*.scl

for i in %buildroot%_libdir/*.so
do
	chrpath -d $i ||:
done

%files
%doc ANNOUNCE BUGS CHANGES COPYRIGHT LICENSE README THANKS
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/*-%version.so

%files -n lib%name-devel
#doc DEVELOPER.README HOWTO_RELEASE_PATCH.html coding_standards.html
%_includedir/*
%_libdir/*.so
%exclude %_libdir/*-%version.so
%_libdir/*.scl
%_aclocaldir/*
%_pkgconfigdir/*

%files -n python-module-sidl
%python_sitelibdir/llnl_babel-*
%python_sitelibdir/sidl*
%exclude %python_sitelibdir/sidlx*

%files -n python-module-sidlx
%python_sitelibdir/llnl_babel_sidl_sidlx-*
%python_sitelibdir/sidlx*

%files j
%_javadir/*

%files common
%_datadir/*.sidl
%_datadir/%name-runtime-%version
%_datadir/%name-%version
%dir %_datadir/sgml
%_datadir/sgml/%name-%version

%files javadoc
%_javadocdir/*

%files manual
%_docdir/%name

%changelog
* Thu Oct 03 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.0.0-alt2.qa2
- Fixed build on ppc64le.

* Fri Nov 30 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.0.0-alt2.qa1
- Removed redundant BR: w3c-libwww-devel.

* Mon Feb 29 2016 Denis Medvedev <nbr@altlinux.org> 2.0.0-alt2
- Documentation recompiled without doclint.

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1.1
- NMU: clean-up of java deps

* Fri Nov 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Version 2.0.0

* Wed Nov 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt9.svn20090721
- Fixed build

* Sun Jun 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt8.svn20090721
- Fixed RPATH

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.0-alt7.svn20090721.1
- Rebuild to remove redundant libpython2.7 dependency

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt7.svn20090721
- Fixed RPATH
- Disabled devel-static package

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.0-alt6.svn20090721.11.1
- Rebuild with Python-2.7

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt6.svn20090721.11
- Rebuilt for debuginfo (with python)

* Thu Feb 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt6.svn20090721.10
- Rebuilt for debuginfo (except python)

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt6.svn20090721.9
- Rebuilt for soname set-versions

* Thu Aug 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt6.svn20090721.8
- Removed paths to buildroot

* Sat Feb 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt6.svn20090721.7
- Rebuilt with reformed NumPy

* Tue Dec 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt6.svn20090721.6
- Release up

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt6.svn20090721.5
- Rebuilt with python 2.6

* Mon Sep 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt6.svn20090721.4
- Disabled embedded libltdl
- Fixed babel-libtool (get from libtool_2.2, thnx ldv@)

* Tue Sep 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt6.svn20090721.3
- Oops! Previous is wrong, restored *dep_objects and fixed by rebuild
  with new gcc

* Tue Sep 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt6.svn20090721.2
- Fixed babel-libtool: removed (pre|post)dep_objects

* Mon Jul 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt6.svn20090721.1
- Snapshot 20090721
- Resolved conflict with cca-spec-babel

* Thu May 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt5
- Rebuild with gcc 4.4 & OpenMPI & libltdl7

* Tue May 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt3.M50.1
- Port for Branch 5.0

* Tue May 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt4
- Rename python module (%name -> sidl) (ALT #19915)

* Tue Apr 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt3
- Add dependence on libtool_1.5

* Sat Apr 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.1
- Fix wrong java paths in scripts

* Sat Apr 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2
- Add missing babel script

* Fri Apr 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus

