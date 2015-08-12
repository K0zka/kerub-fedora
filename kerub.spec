%global logdir		%{_localstatedir}/log/%{name}
%global datadir		%{_sharedstatedir}/%{name}
%global configdir	%{_sysconfdir}/%{name}
%global loc_configdir	%{_sysconfdir}/%{name}/local
%global cls_configdir	%{_sysconfdir}/%{name}/cluster
%global wardir		%{_datadir}/%{name}


Name:		kerub
Version:	master
Release:	0.1
Summary:	Kerub is an Infrastructure as a Service prototype

Group:		Cloud Management Tools
License:	Apache license 2.0
URL:		https://github.com/K0zka/kerub
Source0:	https://github.com/K0zka/%{name}/archive/%{version}.tar.gz
Source2:	kerub.xml

BuildArch:	noarch
BuildRequires:	maven
Requires:	java-1.8,jetty

%description
Kerub is an Infrastructure as a Service prototype project to demonstrate
a set of design concepts.

%prep
echo prep
%setup -q


%build
mvn package


%install
install -dm 755 %{buildroot}%{logdir}
install -dm 755 %{buildroot}%{datadir}
install -dm 755 %{buildroot}%{configdir}
install -dm 755 %{buildroot}%{configdir}/local
install -dm 755 %{buildroot}%{configdir}/config
install -dm 755 %{buildroot}%{loc_configdir}
install -dm 755 %{buildroot}%{cls_configdir}
install -dm 755 %{buildroot}%{wardir}
install -dm 755 %{buildroot}%{_datadir}/jetty/etc

install -pm 644 target/${name}*.war %{buildroot}%{wardir}/%{name}.war
install -pm 644 %{_sourcedir}/kerub.xml %{buildroot}%{_datadir}/jetty/etc

install -pm 644 %{_sourcedir}/shiro.ini %{buildroot}%{configdir}
install -pm 644 %{_sourcedir}/kerub.properties.local %{buildroot}%{configdir}/local/kerub.properties
install -pm 644 %{_sourcedir}/kerub.properties.cluster %{buildroot}%{configdir}/cluster/kerub.properties

%files
%doc
%{_datadir}/kerub/kerub.war
%{_datadir}/jetty/etc/kerub.xml
%{configdir}
%{configdir}/shiro.ini
%{configdir}/local
%{configdir}/local/kerub.properties
%{configdir}/cluster
%{configdir}/cluster/kerub.properties

%changelog

