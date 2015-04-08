#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Dictionaries merge using update."""

import data

BN = {'Lindsey Buckingham': ['guitar', 'vocals'],
      'Stevie Nicks': ['vocals', 'tambourine']}
data.BANDS['Fleetwood Mac'].update(BN)
