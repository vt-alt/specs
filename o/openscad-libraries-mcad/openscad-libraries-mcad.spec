Name: openscad-libraries-mcad
Version: 0.1
Release: alt2.git20141104

Summary: MCAD is a library of useful functions for OpenSCAD.
Packager: Dmitry Derjavin <dd@altlinux.org> 
License: LGPL
Group: Engineering
Url: https://github.com/SolidCode/MCAD

Source: %name-%version.tar

BuildArch: noarch

%define openscad_libdir %_datadir/openscad/libraries
%define mcaddir %openscad_libdir/MCAD

Requires: %openscad_libdir

%description
This library contains components commonly used in designing and
mocking up mechanical designs.

%prep
%setup
mv bitmap/README README-bitmap

# remove conflicts with openscad-mcad 2019.05
rm {bearing,gears,nuts_and_bolts,regular_shapes,servos,shapes,teardrop,triangles}.scad

%install
mkdir -p -m755 %buildroot%mcaddir
cp -a *.scad bitmap %buildroot%mcaddir

%files
%doc README.markdown README-bitmap
%mcaddir

%changelog
* Wed Nov 27 2019 Anton Midyukov <antohami@altlinux.org> 0.1-alt2.git20141104
- Do not pack python2 files (needed for testing only)
- Do not pack conflicts files with openscad-mcad 2019.05

* Tue Dec 23 2014 Dmitry Derjavin <dd@altlinux.org> 0.1-alt1.git20141104
- Initial ALT Linux build.
