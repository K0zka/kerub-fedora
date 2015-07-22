Name:		kerub
Version:	0.0.1.SNAPSHOT
Release:	1%{?dist}
Summary:	Kerub is an Infrastructure as a Service prototype

Group:		Cloud Management Tools
License:	Apache license 2.0
URL:		https://github.com/K0zka/kerub
Source0:	https://github.com/K0zka/kerub/archive/master.tar.gz

BuildRequires:	maven
Requires:	java-1.8

%description
Kerub is an Infrastructure as a Service prototype project to demonstrate
a set of design concepts.

%prep
echo prep
%setup -q


%build
echo build
make %{?_smp_mflags}


%install
%make_install


%files
%doc



%changelog

