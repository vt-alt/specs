Name:     jitterdebugger
Version:  0.3.0.60.gb90ff3a
Release:  alt1

Summary:  Real time response messaurement tool
License:  MIT
Group:    System/Kernel and hardware
Url:      https://github.com/igaw/jitterdebugger

Source:   %name-%version.tar
BuildRequires: rpm-build-python3

BuildRequires: libhdf5-devel /usr/bin/h5cc

%description
jitterdebugger measures wake up latencies. jitterdebugger starts a thread on
each CPU which programs a timer and measures the time it takes from the timer
expiring until the thread which set the timer runs again.

This tool is a re-implementation of cyclictest. It doesn't have all the command
line options as cyclictest which results are easy to get wrong and therefore an
invalid latency report.

The default settings of jitterdebugger will produce a correct measurement out
of the box.

Furthermore, the tool supports storing all samples for post processing.

%prep
%setup

%build
%make_build

%install
install -D jitterdebugger %buildroot/%_bindir/jitterdebugger
install -D jitterplot     %buildroot/%_bindir/jitterplot
install -D jittersamples  %buildroot/%_bindir/jittersamples
install -D man/jitterdebugger.1 %buildroot/%_man1dir/jitterdebugger.1
install -D man/jitterplot.1     %buildroot/%_man1dir/jitterplot.1
install -D man/jittersamples.1  %buildroot/%_man1dir/jittersamples.1

%files
%doc README.rst LICENSE
%_bindir/jitterdebugger
%_bindir/jitterplot
%_bindir/jittersamples
%_man1dir/*.1*

%changelog
* Fri Mar 06 2020 Vitaly Chikunov <vt@altlinux.org> 0.3.0.60.gb90ff3a-alt1
- jitterdebugger: Allow to override the affinity mask (github issue #18).

* Sat Nov 30 2019 Vitaly Chikunov <vt@altlinux.org> 0.3.0.59.gdaeff0a-alt1
- Fix gettid error.

* Sun Oct 06 2019 Vitaly Chikunov <vt@altlinux.org> 0.3.0.53.g3a24505-alt2
- Build with HDF5 (hack to use older API).

* Sun Oct 06 2019 Vitaly Chikunov <vt@altlinux.org> 0.3.0.53.g3a24505-alt1
- Initial import of 0.3-53-g3a24505 (Without HDF5 support).
