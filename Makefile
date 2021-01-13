

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


	mkdir -p $(VENDOR_DIR)/remixicon
	cp -r node_modules/remixicon/fonts/*   $(VENDOR_DIR)/remixicon

	rm -rf node_modules

