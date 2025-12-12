Summary:	Command line access to Amazon S3, EC2 and SQS
Name:		aws-cli
Version:	2.27.13
Release:	2
License:	GPLv3
Group:		Networking/Other
URL:		https://timkay.com/aws/
Source0:	https://github.com/aws/aws-cli/archive/refs/tags/%{version}.tar.gz
BuildArch: 	noarch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	make

BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(colorama)
BuildRequires:	python%{pyver}dist(docutils)
BuildRequires:	python%{pyver}dist(cryptography)
BuildRequires:	python%{pyver}dist(ruamel.yaml)
BuildRequires:	python%{pyver}dist(ruamel.yaml.clib)
BuildRequires:	python%{pyver}dist(prompt-toolkit)
BuildRequires:	python%{pyver}dist(distro)
BuildRequires:	python%{pyver}dist(awscrt)
BuildRequires:	python%{pyver}dist(python-dateutil)
BuildRequires:	python%{pyver}dist(jmespath)
BuildRequires:	python%{pyver}dist(urllib3)

%patchlist
aws-cli-2.27.13-accept-newer-libs.patch

%description
aws is a command line tool that gives you easy access to 
Amazon EC2, S3 and SQS.  aws is designed to be simple to
install and simple to use.

aws S3 (Simple Storage Service) allows you to create 
buckets/directories, add and remove files and list buckets.  

aws EC2 (Elastic Compute Cloud) allows you to start, 
stop, reboot, and manage EC2 virtual machines.

aws SQS (Simple Queue Service) is used to control queues. 

%prep
%autosetup -p1 -n aws-cli-%{version}

%build
%py_build

%install
%py_install

%files
%defattr(-,root,root)
%{_bindir}/aws
%{_bindir}/aws.cmd
%{_bindir}/aws_bash_completer
%{_bindir}/aws_completer
%{_bindir}/aws_zsh_completer.sh
%{py_sitedir}/awscli-%{version}.dist-info
%{py_sitedir}/awscli
