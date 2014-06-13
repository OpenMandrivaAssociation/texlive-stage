# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/stage
# catalog-date 2006-11-06 12:20:58 +0100
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-stage
Version:	20061106
Release:	7
Summary:	A LaTeX class for stage plays
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stage
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stage.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Stage.cls is a LaTeX class for creating plays of any length in
a standard manuscript format for production and submission.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/stage/stage.cls
%doc %{_texmfdistdir}/doc/latex/stage/README
%doc %{_texmfdistdir}/doc/latex/stage/stage-documentation.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061106-2
+ Revision: 756166
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061106-1
+ Revision: 719576
- texlive-stage
- texlive-stage
- texlive-stage
- texlive-stage

