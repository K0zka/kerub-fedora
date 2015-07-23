Name:		kerub
Version:	master
Release:	1%{?dist}
Summary:	Kerub is an Infrastructure as a Service prototype

Group:		Cloud Management Tools
License:	Apache license 2.0
URL:		https://github.com/K0zka/kerub
Source0:	https://github.com/K0zka/kerub/archive/master.tar.gz

BuildArch:	noarch
BuildRequires:	maven
Requires:	java-1.8

%description
Kerub is an Infrastructure as a Service prototype project to demonstrate
a set of design concepts.

%prep
echo prep
%setup -q


%build
mvn package


%install
mkdir -p $RPM_BUILD_ROOT/usr/share/kerub/
install target/kerub*.war $RPM_BUILD_ROOT/usr/share/kerub/

%files
%doc
/usr/share/kerub/kerub*.war



%changelog

