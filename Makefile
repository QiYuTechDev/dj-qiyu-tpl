copy-static-files:export VENDOR_DIR=dj_qiyu_tpl/static/dj_qiyu_tpl/vendor
copy-static-files:
	rm    -rf $(VENDOR_DIR)

	npm install

	mkdir -p $(VENDOR_DIR)/bulma
	cp -r node_modules/bulma/css/* $(VENDOR_DIR)/bulma

	mkdir -p $(VENDOR_DIR)/darkreader
	cp -r node_modules/darkreader/*.js $(VENDOR_DIR)/darkreader

	mkdir -p $(VENDOR_DIR)/fa
	cp -r node_modules/font-awesome/css   $(VENDOR_DIR)/fa
	cp -r node_modules/font-awesome/fonts $(VENDOR_DIR)/fa

	mkdir -p $(VENDOR_DIR)/fa5
	cp -r node_modules/@fortawesome/fontawesome-free/css      $(VENDOR_DIR)/fa5
	cp -r node_modules/@fortawesome/fontawesome-free/js       $(VENDOR_DIR)/fa5
	cp -r node_modules/@fortawesome/fontawesome-free/svgs     $(VENDOR_DIR)/fa5
	cp -r node_modules/@fortawesome/fontawesome-free/webfonts $(VENDOR_DIR)/fa5


	mkdir -p $(VENDOR_DIR)/remixicon
	cp -r node_modules/remixicon/fonts/*   $(VENDOR_DIR)/remixicon

	rm -rf node_modules

	make collect-rst-static-files

collect-rst-static-files:CWD=$(shell pwd)
collect-rst-static-files:VDIR=$(shell poetry env info | grep Path | awk '{print $$2}')
collect-rst-static-files:DOCUTILS_DIR=$(VDIR)/lib/python3.9/site-packages/docutils
collect-rst-static-files:DEST_DIR=$(shell pwd)/dj_qiyu_tpl/static/dj_qiyu_tpl/vendor/rst
collect-rst-static-files:
	mkdir -p $(DEST_DIR)
	cd $(DOCUTILS_DIR)/writers/html5_polyglot/ && cp *.css $(DEST_DIR)


run-test:
	cd dj_tests && (rm -f dj_qiyu_tpl || true) && ln -s ../dj_qiyu_tpl dj_qiyu_tpl
	cd dj_tests && poetry run pytest -s
