
clean:
	rpmdev-wipetree

all: rpms

rpms: sources kerub.spec
	rpmbuild -ba kerub.spec

rpmdirs:
	rpmdev-setuptree

sources: rpmdirs
	spectool -g -R kerub.spec
	#TODO: this looks like I am doing half of spectool's job
	cp kerub.xml `rpm --eval "%{_sourcedir}"`
