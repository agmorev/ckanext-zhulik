###############################################################################
#                             requirements: start                             #
###############################################################################
ckan_tag = ckan-2.10.1

ext_list = officedocs \
	pdfview \
	search-autocomplete \
	pages \
	comments \
	core_fix

remote-officedocs = https://github.com/DataShades/ckanext-officedocs.git branch py3
remote-pdfview = https://github.com/ckan/ckanext-pdfview.git branch master
remote-search-autocomplete = https://github.com/DataShades/ckanext-search-autocomplete branch master
remote-pages = https://github.com/ckan/ckanext-pages tag v0.5.2
remote-comments = https://github.com/DataShades/ckanext-comments.git branch master
remote-core_fix = https://github.com/mutantsan/ckanext-core-fix branch master


###############################################################################
#                              requirements: end                              #
###############################################################################

_version = master

-include deps.mk

prepare:
	curl -O https://raw.githubusercontent.com/DataShades/ckan-deps-installer/$(_version)/deps.mk
