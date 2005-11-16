Summary:	libnetfilter_conntrack - a userspace library to the in-kernel connection tracking state table
Name:		libnetfilter_conntrack
Version:	0.0.27
Release:	0.1@%{_kernel_ver_str}
License:	GPL v2
Group:		Libraries
Source0:	ftp://ftp.netfilter.org/pub/libnetfilter_conntrack/%{name}-%{version}.tar.bz2
# Source0-md5:	c9965daa920d74e6899a41bc27222981
URL:		http://www.netfilter.org/projects/libnetfilter_conntrack/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libnfnetlink-devel
%requires_releq	libnfnetlink
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libnetfilter_conntrack is a userspace library providing a programming
interface (API) to the in-kernel connection tracking state table.

Main features:
- listing/retrieving entries from the kernel connection tracking table
- inserting/modifying/deleting entries from the kernel connection
  tracking table
- listing/retrieving entries from the kernel expect table
- inserting/modifying/deleting entries from the kernel expect table

%package devel
Summary:	Header files for libnetfilter_conntrack library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libnfnetlink-devel

%description devel
Header files for libnetfilter_conntrack library.

%package static
Summary:	Static libnetfilter_conntrack library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnetfilter_conntrack library.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/nfct_proto_*-*.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/%{name}/nfct_proto_*.la
%attr(755,root,root) %{_libdir}/%{name}/nfct_proto_*.so
%attr(755,root,root) %exclude %{_libdir}/%{name}/nfct_proto_*-*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/%{name}/nfct_proto_*.a
%{_libdir}/lib*.a
