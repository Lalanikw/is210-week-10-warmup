#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Dictionaries add and remove values."""

import data


CORRECTED = data.BANDS['Bob Dylan'] = ['vocals', 'guitar', 'harmonica']
del data.BANDS['Van Halen']['David Lee Roth']
CORRECTED = data.BANDS['van Halen'] = {'sammy Hager': 'vocals'}
