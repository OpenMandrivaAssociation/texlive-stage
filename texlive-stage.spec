%global tl_name stage
%global tl_revision 62929

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.03
Release:	%{tl_revision}.1
Summary:	A LaTeX class for stage plays
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/stage
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stage.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stage.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stage.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Stage.cls is a LaTeX class for creating plays of any length in a
standard manuscript format for production and submission.

