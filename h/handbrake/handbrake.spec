# #%define svn git20170409

Name: handbrake
Version: 1.3.1
Release: alt3
Summary: Multithreaded Video Transcoder
Packager: Motsyo Gennadi <drool@altlinux.ru>
Source0: HandBrake-%version.tar.bz2
# #Source0: %name-%svn.tar.bz2

Source101: https://download.handbrake.fr/contrib/libvpx-1.7.0.tar.gz
Source102: https://github.com/FFmpeg/nv-codec-headers/releases/download/n9.0.18.1/nv-codec-headers-9.0.18.1.tar.gz
Source103: https://download.handbrake.fr/handbrake/contrib/libav-12.3.tar.gz
Source104: https://download.videolan.org/pub/videolan/libdvdread/6.0.2/libdvdread-6.0.2.tar.bz2
Source105: https://download.videolan.org/pub/videolan/libdvdnav/6.0.1/libdvdnav-6.0.1.tar.bz2
Source106: https://download.videolan.org/pub/videolan/x265/x265_3.2.1.tar.gz
Source107: https://download.handbrake.fr/handbrake/contrib/ffmpeg-4.2.2.tar.bz2
Source108: https://download.videolan.org/pub/videolan/libbluray/1.1.2/libbluray-1.1.2.tar.bz2
Source109: https://download.handbrake.fr/handbrake/contrib/fdk-aac-2.0.1.tar.gz
Source110: https://code.videolan.org/videolan/dav1d/-/archive/0.5.1/dav1d-0.5.1.tar.bz2

Source200: x265-x32.patch

Url: http://handbrake.fr/
Group: Video
License: GPLv2+

BuildRequires: bzlib-devel doxygen gcc-c++ intltool libass-devel libdbus-glib-devel libfribidi-devel libglademm-devel libgtk+3-devel
BuildRequires: libharfbuzz-devel libjansson-devel liblame-devel libnotify-devel libopus-devel libsamplerate-devel libssl-devel libtheora-devel
BuildRequires: libvorbis-devel libx264-devel libxml2-devel python-modules-json cmake libspeex-devel liblzma-devel libnuma-devel libvpx5-devel
BuildRequires: nasm meson

ExclusiveArch: x86_64

%description
HandBrake is an open-source, GPL-licensed, multiplatform, multithreaded video
transcoder.

%package cli
Summary: Multithreaded Video Transcoder
Group: Video

%description cli
HandBrake is an open-source, GPL-licensed, multiplatform, multithreaded video
transcoder.

This package contains a command-line interface for Handbrake.

%package gtk
Summary: Multithreaded Video Transcoder
Group: Video
Requires: %name-cli = %version-%release

%description gtk
HandBrake is an open-source, GPL-licensed, multiplatform, multithreaded video
transcoder.

This package contains a GTK+ graphical user interface for Handbrake.

%prep
%setup -n HandBrake-%version
# #%setup -n %name-svn

# Copy 3rd party dependencies into expected locations:
%__mkdir download
for f in \
%{S:101} %{S:102} %{S:103} %{S:104} %{S:105} %{S:106} \
%{S:107} %{S:108} %{S:109} %{S:110} \
; do
     %__ln_s "$f" download/
done

%build
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"

%__cp "%{S:200}" contrib/x265/A99-x265-x32.patch
%__cp "%{S:200}" contrib/x265_8bit/A99-x265-x32.patch
%__cp "%{S:200}" contrib/x265_10bit/A99-x265-x32.patch
%__cp "%{S:200}" contrib/x265_12bit/A99-x265-x32.patch

./configure	--prefix="%buildroot%prefix" \
		--snapshot \
		--disable-gtk-update-checks \
		--enable-fdk-aac
pushd build
%__make build
popd

%install
pushd build
%__make install
popd

%__ln_s ghb "%buildroot%_bindir/HandBrakeGUI"

%__rm "%buildroot%_datadir/icons"/*/*.cache

%find_lang --with-gnome ghb

%files cli
%doc AUTHORS.markdown COPYING LICENSE NEWS.markdown README.markdown THANKS.markdown
%_bindir/HandBrakeCLI

%files gtk -f ghb.lang
%_bindir/HandBrakeGUI
%_bindir/ghb
%_desktopdir/*.desktop
%_datadir/icons/*/*/apps/*.svg
%_datadir/metainfo/*.xml

%changelog
* Sat Mar 28 2020 Motsyo Gennadi <drool@altlinux.ru> 1.3.1-alt3
- ExclusiveArch x86_64 only

* Sat Mar 28 2020 Motsyo Gennadi <drool@altlinux.ru> 1.3.1-alt2
- ExcludeArch aarch64

* Sat Mar 28 2020 Motsyo Gennadi <drool@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Fri Mar 01 2019 Motsyo Gennadi <drool@altlinux.ru> 1.2.2-alt2
- build with x265 v2.8

* Fri Mar 01 2019 Motsyo Gennadi <drool@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Sun Jan 06 2019 Motsyo Gennadi <drool@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sun Jan 06 2019 Grigory Ustinov <grenka@altlinux.org> 1.1.2-alt4
- Fixed FTBFS (corrected popd call).

* Thu Nov 15 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.2-alt3
- drop exclusivearch, nothing special was about it

* Wed Nov 14 2018 Motsyo Gennadi <drool@altlinux.ru> 1.1.2-alt2
- build with x265 v2.8

* Wed Nov 14 2018 Motsyo Gennadi <drool@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Mon Apr 17 2017 Motsyo Gennadi <drool@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Sat Apr 01 2017 Motsyo Gennadi <drool@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Jan 26 2017 Motsyo Gennadi <drool@altlinux.ru> 1.0.2-alt1.git20170122
- 1.0.2 (git 22.01.2017)

* Mon Jan 16 2017 Motsyo Gennadi <drool@altlinux.ru> 1.0.1-alt1.git20161229
- 1.0.1 (git 29.12.2016)

* Tue Oct 18 2016 Motsyo Gennadi <drool@altlinux.ru> 0.10.5-alt1.git20161018
- 0.10.5 (git 18.10.2016)

* Sun Feb 16 2014 Motsyo Gennadi <drool@altlinux.ru> 0.9.9.1-alt1.svn6036
- build svn6036

* Sat Feb 15 2014 Motsyo Gennadi <drool@altlinux.ru> 0.9.9.1-alt1.svn6031.1
- fix build

* Sat Feb 15 2014 Motsyo Gennadi <drool@altlinux.ru> 0.9.9.1-alt1.svn6031
- build svn6031

* Wed Feb 12 2014 Motsyo Gennadi <drool@altlinux.ru> 0.9.9.1-alt1.svn6028
- build svn6028

* Tue Feb 04 2014 Motsyo Gennadi <drool@altlinux.ru> 0.9.9.1-alt1.svn6013
- build svn6013 (now GTK3 only)

* Sun Feb 02 2014 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn6011
- build svn6011

* Sun Nov 24 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5903
- build svn5903

* Sat Nov 09 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5891
- build svn5891

* Thu Sep 19 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5787
- build svn5787

* Wed Sep 04 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5767
- build svn5767

* Mon Sep 02 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5764
- build svn5764

* Tue Aug 06 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5693
- build svn5693

* Tue Aug 06 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5690
- build svn5690

* Fri Jun 14 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5577
- build svn5577

* Sun May 19 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5478
- 0.9.9 released
- build svn5433

* Wed May 01 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5433
- build svn5433

* Mon Apr 01 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5369
- build svn5369

* Thu Mar 07 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5307
- build svn5307

* Mon Feb 11 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5245
- build svn5245

* Wed Jan 02 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5127
- build svn5127

* Wed Nov 28 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5086
- build svn5086

* Fri Nov 16 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5065
- build svn5065
- cleanup BuildRequres

* Sat Nov 03 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5042
- build svn5042
- cleanup spec
- cleanup BuildRequres

* Wed Oct 17 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt0.svn5017
- build svn5017

* Wed Oct 10 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt0.svn5010
- build svn5010

* Tue Jun 05 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.5-alt1.3
- fir build for Sisyphus (thank azol@ for help)

* Sun Jun 03 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.5-alt1.2
- test fix for sisyphus

* Sun Jun 03 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.5-alt1.1
- test fix for sisyphus

* Fri Jun 01 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.5-alt1
- initial build for ALT Linux from OpenSUSE package
