Name:		harminv
Version:	1.4.1
Release:	alt1
Summary:	Harmonic Inversion of Time Signals by the Filter Diagonalization Method
License:	GPLv2
Group:		Sciences/Physics
URL:		https://github.com/NanoComp/harminv
Source:		%name-%version.tar.gz

# Automatically added by buildreq on Mon Aug 05 2019
# optimized out: glibc-kernheaders-generic libgfortran-devel libopenblas-devel libquadmath-devel libstdc++-devel perl python-base sh4
BuildRequires: gcc-c++ gcc-fortran liblapack-devel

%description
Harminv is a free program (and accompanying library) to solve the
problem of "harmonic inversion." Given a discrete, finite-length signal
that consists of a sum of finitely-many sinusoids (possibly
exponentially decaying), it determines the frequencies, decay constants,
amplitudes, and phases of those sinusoids.

%package -n libharminv
Group:		System/Libraries
Summary:	Main library for harminv, %summary
%description -n libharminv
%summary

%package -n libharminv-devel
Group:		Development/C
Summary:	Development files for libharminv
%description -n libharminv-devel
%summary

%prep
%setup

%build
%autoreconf
%configure --enable-shared --disable-static
%make_build

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*

%files -n libharminv
%doc *.md
%_libdir/*.so.*

%files -n libharminv-devel
%doc doc sines.c sines*.sh
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%changelog
* Mon Aug 05 2019 Fr. Br. George <george@altlinux.ru> 1.4.1-alt1
- Initial build for ALT

