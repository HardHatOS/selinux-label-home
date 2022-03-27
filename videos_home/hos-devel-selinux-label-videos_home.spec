BuildArch: noarch
BuildRequires: hos-devel-selinux-interfaces, make, selinux-policy-devel
License: AGPLv3+
Name: hos-devel-selinux-label-videos_home
Release: 1%{?dist}
Requires: policycoreutils, libselinux-utils
Source0: videos_home.if
Summary: SELinux access interfaces for the Videos directory
URL: https://github.com/HardHatOS/selinux-label-home/videos_home
Version: 1.0

%description
SELinux access interfaces for the $HOME/Videos directory

%pre
# RPM macro that defines the SELinux directory where the interface files are placed in
%define _contribdir %{_datadir}/selinux/devel/include/contrib

%install
# Copy the SELinux interface file to the proper directory
%{__install} -D -m 0644 %{SOURCE0} -t %{buildroot}%{_contribdir}

%files
%attr(0644,root,root) %{_contribdir}/*.if