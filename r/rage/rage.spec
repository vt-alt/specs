Name: rage
Version: 0.3.1
Release: alt1

Summary: EFL Video Player
License: BSD
Group: Video
Url: http://www.enlightenment.org/
Packager: Michael Shigorin <mike@altlinux.org>

Source: http://download.enlightenment.org/releases/%name-%version.tar
#Patch: %name-%version-%release.patch

# default engine is GStreamer
Requires: gst-plugins-base1.0
Requires: gst-plugins-good1.0
Requires: gst-plugins-bad1.0
Requires: gst-plugins-ugly1.0
Requires: gst-libav

BuildRequires(pre): meson
BuildRequires: efl-libs-devel >= 1.22.3
BuildRequires: libelementary-devel >= 1.22.3

%description
Rage is a video and audio player written with Enlightenment
Foundation Libraries with some extra bells and whistles.

It is a simple video and audio player intended to be slick yet
simplistic, much like Mplayer. You can provide 1 or more files to
play on the command-line or just DND files onto the rage window
to insert them into the playlist. You can get a visual
representation of everything on the playlist by hitting the /
key, or just hovering your mouse over the right side of the
window. Mouse back over the left side of the window ti dismiss it
or press the key again. It has a full complement of key controls
if you see the README for the full list. It will automatically
search for album art for music files, if not already cached, and
display that. It even generates thumbnails for the timeline of a
video and allows you to preview the position on mouseover of the
position bar at the bottom of the window.

Here is a list of all the things it can do:

* Play video and audio files
* Support a playlist via command-line
* Insert to playlist via DND
* Controls hide on mouse idle, and appear on mouse movement
* Fullscreen mode support with automatic "no blank" support
* Playlist visual previews and controls
* Subtitle file support
* Supports Gstreamer 1.x, Xine and VLC
  as media engines via Emotion modules
* Selection of media back-end via command-line
* Album art fetch and caching
* Video thumbnail timeline generation and caching
* Works with any Evas engine (OpenGL acceleration, pure software etc.)
* Works in X11, Wayland and Framebuffer direct support
* Accelerated seek on keyboard fowrard/reverse
* Drag gestures for seeking
* Special different UI modes for pure audio and video

%prep
%setup
#%%patch -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc AUTHORS COPYING README
%_bindir/%name
%_libdir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%_iconsdir/hicolor/*x*/apps/%name.png

%changelog
* Sat Aug 24 2019 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Fri Jun 21 2019 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt3
- build current snapshot

* Fri Dec 07 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt2
- build current snapshot

* Fri Dec 29 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt3
- current snapshot

* Mon Apr 03 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt2
- build current snapshot

* Fri Sep 30 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Mon Sep 22 2014 Michael Shigorin <mike@altlinux.org> 0.1.0-alt2
- built for sisyphus (rebased upon ge1184db)

* Wed Aug 27 2014 Michael Shigorin <mike@altlinux.org> 0.1.0-alt1
- built for ALT Linux

