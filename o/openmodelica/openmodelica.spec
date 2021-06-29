%set_verify_elf_method unresolved=relaxed
%def_without includes
%define llvm_version 11.0

Name:     openmodelica
Version:  1.17.0
Release:  alt1

Summary:  OpenModelica is an open-source Modelica-based modeling and simulation environment intended for industrial and academic usage
License:  GPL-3.0+ and OSMC-PL
Group:    Sciences/Mathematics
Url:      https://openmodelica.org/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: OpenModelica-%version.tar
Source1: OMOptim.tar
Source2: OMLibraries.tar
Source3: OMSimulator.tar
Source4: OMCompiler-3rdParty.tar
Source5: OMSens.tar
Source6: OMSens_Qt.tar
Source7: OMTLMSimulator.tar
Source8: OMSimulator-3rdParty.tar
Source9: external-libraries.tar

Patch1: openmodelica-alt-not-retrieve-libraries.patch
Patch2: openmodelica-alt-disable-tests-for-FMIL.patch
Patch3: openmodelica-alt-disable-FFLAGS-check-in-sundials.patch
Patch4: openmodelica-alt-adapt-script-to-python3.patch
Patch5: openmodelica-alt-fix-lib64-in-rpath.patch
Patch6: openmodelica-alt-installdir-in-settings.patch

BuildRequires(pre): cmake
BuildRequires(pre): qt5-base-devel
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-python
BuildRequires: gcc-c++
BuildRequires: gcc-fortran
BuildRequires: qt5-tools
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-lockfree-devel
BuildRequires: boost-program_options-devel
BuildRequires: boost-asio-devel
BuildRequires: clang%llvm_version-devel
BuildRequires: llvm%llvm_version-devel
BuildRequires: libcurl-devel
BuildRequires: libexpat-devel
BuildRequires: libhdf5-devel
BuildRequires: libhwloc-devel
BuildRequires: liblapack-devel
BuildRequires: libblas-devel
BuildRequires: java-devel
BuildRequires: liblpsolve-devel
BuildRequires: libomniORB-devel
BuildRequires: libffi-devel
BuildRequires: libreadline-devel
BuildRequires: libncurses-devel
BuildRequires: doxygen
BuildRequires: flex
BuildRequires: libossp-uuid-devel
BuildRequires: libuuid-devel
BuildRequires: graphviz
BuildRequires: qt5-svg-devel
BuildRequires: qt5-webkit-devel
BuildRequires: qt5-xmlpatterns-devel
BuildRequires: chrpath

%add_python3_lib_path %_libdir/OMSimulator
%add_findprov_skiplist %_libexecdir/omlibrary/

ExclusiveArch: %ix86 x86_64

%description
OPENMODELICA is an open-source Modelica-based modeling and simulation
environment intended for industrial and academic usage. Its long-term
development is supported by a non-profit organization - the Open Source
Modelica Consortium (OSMC).

The goal with the OpenModelica effort is to create a comprehensive Open Source
Modelica modeling, compilation and simulation environment based on free
software distributed in binary and source code form for research, teaching, and
industrial usage. We invite researchers and students, or any interested
developer to participate in the project and cooperate around OpenModelica,
tools, and applications.

%prep
%setup -n OpenModelica-%version
tar xf %SOURCE1
tar xf %SOURCE2
tar xf %SOURCE3
tar xf %SOURCE4
tar xf %SOURCE5
tar xf %SOURCE6
tar xf %SOURCE7
tar xf %SOURCE8
tar xf %SOURCE9
# Use common subdirectory from as submodule path
for i in OMSens_Qt OMOptim; do rm -rf $i/common; ln -s ../common $i;done
# Put package version
echo -e "#!/bin/sh\necho %version" > OMCompiler/common/semver.sh
# Do not get external libraries from their git repositories
%patch1 -p1 -d libraries
%patch2 -p1 -d OMSimulator/3rdParty
%patch3 -p1 -d OMCompiler/3rdParty
%patch4 -p1
%patch5 -p1
%patch6 -p1

# Use %%_lib in CMakeLists.txt
#find OMSimulator -name CMakeLists.txt | xargs subst 's,\(CMAKE_INSTALL_RPATH.*/\)lib/${HOST_SHORT},\1%_lib/${HOST_SHORT},g'

# Do not build testsuite
rm testsuite/Makefile

%build
export PATH=%_qt5_prefix/bin:$PATH
%autoreconf
%configure \
    --with-cppruntime \
    --with-omlibrary=core \
    CC=clang \
    CXX=clang++
%make_build

%install 
%makeinstall_std
# Remove wrong rpath from libipopt.so.0.0.0 and executables
chrpath -d %buildroot%_libdir/%{_target}-gnu/omc/libipopt.so.0.0.0
chrpath -r '$ORIGIN/../%_lib/%{_target}-gnu/omc/omsicpp' %buildroot%_bindir/OMCppOSUSimulation
chrpath -r '$ORIGIN/../%_lib/%{_target}-gnu/omc' %buildroot%_bindir/{OMSimulator,omc}

# Make include symlinks to boost relative
for i in cpp omsicpp;do
    rm -f %buildroot%_includedir/omc/$i/boost
    ln -s ../../boost %buildroot%_includedir/omc/$i/boost
done
# Remove all includes
%if_without includes
rm -rf %buildroot%_includedir
%endif
# Remove duplicate libraries
rm -r %buildroot%_libdir/OMSimulator/%{_target}-gnu

# Move builtin .mo files
%ifarch x86_64 aarch64 ppc64le
mkdir -p %buildroot%_libexecdir
mv %buildroot%_libdir/omc %buildroot%_libexecdir
%endif

# Copy core libraries
mkdir -p %buildroot%_libexecdir/omlibrary
cp -a libraries/build/* %buildroot%_libexecdir/omlibrary

%files
%doc *.md OSMC-License.txt
%_bindir/*
%_libdir/OMSimulator
%_libexecdir/omc
%_libexecdir/omlibrary
%_libdir/%{_target}-gnu/omc
%_datadir/omc
%_datadir/omedit
%_datadir/omnotebook
%_datadir/omshell
%doc %_defaultdocdir/omc
%if_with includes
%_includedir/*.h
%_includedir/omc
%_includedir/omplot
%_includedir/%{_target}-gnu/omc
%endif

%changelog
* Fri Jun 04 2021 Andrey Cherepanov <cas@altlinux.org> 1.17.0-alt1
- Initial build for Sisyphus.
