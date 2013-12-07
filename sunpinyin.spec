Name: sunpinyin
Summary: A statistical language model based Chinese input method
Version: 2.0.3
Release: 4
Group: System/Internationalization
License: LGPLv2+
URL: http://code.google.com/p/sunpinyin
Source0: http://sunpinyin.googlecode.com/files/%{name}-%{version}.tar.gz
Source1: http://open-gram.googlecode.com/files/lm_sc.t3g.arpa.tar.bz2
Source2: http://open-gram.googlecode.com/files/dict.utf8.tar.bz2
Patch0: http://sunpinyin.googlecode.com/files/force-switch-updated.patch
Patch1: sunpinyin-2.0.3-unistd.patch
BuildRequires: sqlite3-devel
BuildRequires: scons

%description
SunPinyin is a statistical language model based Chinese input method,
which was firstly developed by Sun Beijing Globalization team, and
opensource'd to community with opensolaris project, with LGPLv2 and
CDDL dual-licenses.

%define major 3
%define libname %mklibname %name %major

%package -n %libname
Summary: Shared library for %name
Group: System/Internationalization
Requires: %name = %version

%description -n %libname
SunPinyin is a statistical language model based Chinese input method,
which was firstly developed by Sun Beijing Globalization team, and
opensource'd to community with opensolaris project, with LGPLv2 and
CDDL dual-licenses.

This package contains shared library for %name.

%define develname %mklibname -d %name

%package -n %develname
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}

%description -n %develname
SunPinyin is a statistical language model based Chinese input method,
which was firstly developed by Sun Beijing Globalization team, and
opensource'd to community with opensolaris project, with LGPLv2 and
CDDL dual-licenses.

This package contains all necessary files to compile or develop
programs/libraries that use %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
cp %{SOURCE1} raw
cp %{SOURCE2} raw

%build
%setup_compile_flags
scons --prefix=%_prefix --libdir=%_libdir --libdatadir=%_datadir

%install
%setup_compile_flags
scons install --prefix=%_prefix --libdir=%_libdir --libdatadir=%_datadir --install-sandbox=%{buildroot}

%files
%_datadir/sunpinyin

%files -n %libname
%_libdir/*.so.%major
%_libdir/*.so.%major.*

%files -n %develname
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_includedir/*


%changelog
* Tue Apr 26 2011 Funda Wang <fwang@mandriva.org> 2.0.3-1mdv2011.0
+ Revision: 659316
- import sunpinyin

