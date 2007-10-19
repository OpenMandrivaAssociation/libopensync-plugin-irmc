%define name	libopensync-plugin-irmc
%define version	0.33
%define release %mkrel 1

Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	IRMC plugin for opensync synchronization tool
License:	GPL
Group:		Office
URL:		http://www.opensync.org
Source:		http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	opensync-devel >= %{version}
BuildRequires:	openobex-devel
BuildRequires:	scons
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
This plugin allows applications using OpenSync to synchronise to and from
Sony Ericsson phones.

%prep
%setup -q

%build
scons prefix=%{_prefix}

%install
rm -rf %{buildroot}
scons install DESTDIR=%{buildroot}

%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*
