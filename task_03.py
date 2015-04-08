#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Dictionaries copy, add and remove values."""

import data


CORRECTED = data.BANDS.copy()
CORRECTED['Bob Dylan'] = ['vocals', 'guitar', 'harmonic']
del CORRECTED['Van Halen']['David Lee Roth']
CORRECTED['Van Halen'] = {'Sammy Hager': 'vocals'}
print CORRECTED['Van Halen'].keys()
