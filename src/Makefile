# @file Makefile
# @date 25.04.2022
# @author Martin Kubicka (xkubic45)
# @author Dominik Petrik (xpetri25)
# @author Matej Macek (xmacek27)
# @brief Makefile script

LOGINS = xkubic45_xpetri25_xmacek27
FILE_SRC = $(wildcard *.py)
DIR_PROFILE = ../profiling

.phony: all pack clean test doc run profile

all:

pack:clean $(FILE_SRC)
	mkdir -p ../../$(LOGINS)/repo && cp -a ../* ../../$(LOGINS)/repo
	mkdir -p ../../$(LOGINS)/doc  && cp -a ./html	../../$(LOGINS)/doc
	mkdir -p ../../$(LOGINS)/install && cp -a ../install/* ../../$(LOGINS)/install
	rm  ../../$(LOGINS)/install/*.py
	rm -rf ../../$(LOGINS)/repo/install
	rm -rf ../../$(LOGINS)/repo/src/html
	rm -rf ../../$(LOGINS)/repo/installer
	cd ../.. && zip -qr $(LOGINS).zip $(LOGINS)

packwis:clean $(FILE_SRC)
	mkdir -p ../../$(LOGINS) && cp -a ../hodnoceni.txt ../../$(LOGINS)
	mkdir -p ../../$(LOGINS)/src/ && cp ./*.py ../../$(LOGINS)/src
	cp -a ../odevzdani.txt ../../$(LOGINS)
	cp -a ../dokumentace.pdf ../../$(LOGINS)
	cd ../.. && zip -qr $(LOGINS).zip $(LOGINS)

clean:
	rm -rf __pycache__ ../doc ../../$(LOGINS) ../../$(LOGINS).zip

test:
	python3 mathTests.py

doc:$(FILE_SRC)
	doxygen

run:$(FILE_SRC)
	python3 AntioznukCalculator.py

profile:$(FILE_SRC)
	@echo --Profile for 10-----------------------------------------------------
	python3 profiling.py < $(DIR_PROFILE)/data10.txt

help:
	@echo "make"
	@echo "	-without specifying the target, 'make all' is performed"
	@echo ""
	@echo "make all"
	@echo "	-translates the project - including a profiling program"
	@echo ""
	@echo "make pack"
	@echo "	-wraps the project so that it can be submitted"
	@echo ""
	@echo "make clean"
	@echo "	-deletes all files that should not be uploaded"
	@echo ""
	@echo "make test"
	@echo "	-runs math library tests"
	@echo ""
	@echo "make doc"
	@echo "	-starts generating documentation"
	@echo ""
	@echo "make run"
	@echo "	-starts the program"
	@echo ""
	@echo "make profile"
	@echo "	-starts the translation of the standard deviation calculation program into profiling"