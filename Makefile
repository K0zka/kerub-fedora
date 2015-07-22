
clean:
	rpmdev-wipetree

all: rpms

rpms: sources kerub.spec
	rpmbuild -ba kerub.spec

rpmdirs:
	rpmdev-setuptree

sources: rpmdirs
	spectool -g -R kerub.spec
