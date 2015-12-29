Summary: fixbuf IPFIX implementation library
Name: libfixbuf
Version: 1.6.2
Release: 2%{?dist}
Group: Applications/System
License: LGPL
Source: http://tools.netsa.cert.org/releases/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}
Vendor: http://tools.netsa.cert.org/
Provides: libfixbuf
Provides: libfixbuf.so
Requires: glib2 >= 2.4.7
%if "x" == "x1"
Requires: libsctp
%endif
%if "x" == "x1"
Requires: libspread
%endif
%if "x" == "x1"
Requires: openssl
%endif
BuildRequires: glib2-devel >= 2.4.7
BuildRequires: pkgconfig >= 0.8
%if "x" == "x1"
BuildRequires: libsctp-devel
%endif
%if "x" == "x1"
BuildRequires: libspread-devel
%endif
%if "x" == "x1"
BuildRequires: openssl-devel
%endif
BuildRequires: gcc
BuildRequires: make

%description 
libfixbuf aims to be a compliant implementation of the IPFIX Protocol
and message format, from which IPFIX Collecting Processes and
IPFIX Exporting Processes may be built. 

%package devel
Summary: Static libraries and C header files for libfixbuf
Group: Applications/System
Provides: libfixbuf-devel
Requires: %{name} = %{version}
Requires: pkgconfig >= 0.8

%description devel
Static libraries and C header files for libfixbuf.

%prep
%setup -q -n %{name}-%{version}

%build
./configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
%makeinstall

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so*

%files devel
%defattr(-,root,root)
%doc doc/html
%{_includedir}/*
%{_libdir}/pkgconfig/*

%changelog
* Thu Dec 24 2015 John Siegrist <john@complects.com> - 1.6.2-2
- Added missing build dependencies.

* Tue Jun 02 2015 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 1.6.2-1
- Initial specfile

