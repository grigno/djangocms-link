#!/usr/bin/env python
# -*- coding: utf-8 -*-

HELPER_SETTINGS = {
    'INSTALLED_APPS': [
        'django_select2',
        'djangocms_text_ckeditor',
    ],
    'ALLOWED_HOSTS': ['localhost'],
    'CMS_LANGUAGES': {
        1: [{
            'code': 'en',
            'name': 'English',
        }]
    },
    'LANGUAGE_CODE': 'en',
}

def run():
    from djangocms_helper import runner
    runner.cms('djangocms_link')

if __name__ == '__main__':
    run()
