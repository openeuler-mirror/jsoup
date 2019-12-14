Name:           jsoup
Version:        1.11.3
Release:        4
Summary:        Java HTML Parser
License:        MIT
URL:            http://jsoup.org/
Source0:        %{name}-%{version}.tar.gz
Source1:        generate-tarball.sh
BuildArch:      noarch

BuildRequires:  maven-local, mvn(org.apache.felix:maven-bundle-plugin)
Provides:       %{name}-javadoc%{?_isa} %{name}-javadoc
Obsoletes:      %{name}-javadoc

%description
jsoup is a Java library for working with real-world HTML. It provides a very convenient API
for extracting and manipulating data, using the best of DOM, CSS, and jquery-like methods.

%prep
%autosetup -n %{name}-%{name}-%{version} -p1

%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE
%{_javadocdir}/%{name}/*

%changelog
* Tue Dec 3 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.11.3-4
- Package init
