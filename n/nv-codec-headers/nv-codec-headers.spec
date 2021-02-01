Name: nv-codec-headers
Version: 11.0.10.0
Release: alt1
Group: Development/C
License: MIT
Summary: FFmpeg version of headers required to interface with Nvidias codec APIs
Url: https://git.videolan.org/?p=ffmpeg/nv-codec-headers.git

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
FFmpeg version of headers required to interface with Nvidias codec APIs

%prep
%setup
%patch -p1

%build
make PREFIX=/usr .
sed -n '4,25p' include/ffnvcodec/nvEncodeAPI.h > LICENSE # Extract license
sed -i '1,22s/^.\{,3\}//' LICENSE # Delete C comments

%install
make PREFIX=/usr LIBDIR=share DESTDIR=%buildroot install

%files
%_includedir/*
%_datadir/pkgconfig/*.pc
%doc LICENSE

%changelog
* Mon Dec 07 2020 L.A. Kostis <lakostis@altlinux.ru> 11.0.10.0-alt1
- Initial build for Sisyphus.
