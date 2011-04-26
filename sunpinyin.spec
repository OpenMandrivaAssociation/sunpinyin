Name: sunpinyin
Summary: A statistical language model based Chinese input method
Version: 2.0.3
Release: %mkrel 1
Group: System/Internationalization
License: LGPLv2+
URL: http://code.google.com/p/sunpinyin
Source0: http://sunpinyin.googlecode.com/files/%{name}-%{version}.tar.gz
Source1: http://open-gram.googlecode.com/files/lm_sc.t3g.arpa.tar.bz2
Source2: http://open-gram.googlecode.com/files/dict.utf8.tar.bz2
Patch0: http://sunpinyin.googlecode.com/files/force-switch-updated.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%setup -qDT
%patch0 -p1
cp %{SOURCE1} raw
cp %{SOURCE2} raw

%build
%setup_compile_flags
scons --prefix=%_prefix --libdir=%_libdir --libdatadir=%_datadir

%install
rm -rf %{buildroot}
%setup_compile_flags
scons install --prefix=%_prefix --libdir=%_libdir --libdatadir=%_datadir --install-sandbox=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_datadir/sunpinyin

%files -n %libname
%defattr(-,root,root)
%_libdir/*.so.%major
%_libdir/*.so.%major.*

%files -n %develname
%defattr(-,root,root)
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_includedir/*
