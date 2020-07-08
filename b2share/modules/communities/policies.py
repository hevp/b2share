# -*- coding: utf-8 -*-
#
# This file is part of EUDAT B2Share.
# Copyright (C) 2016 CERN.
#
# B2Share is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# B2Share is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with B2Share; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""B2Share Communities Policies """

from .workflows import publication_workflows

class InvalidCommunityPolicy(Exception):
    """Exception raised when community policy does not exist"""
    pass

class CommunityPolicy:
    def __init__(self, name, description, datatype, allowed_values=[]):
        self.name = name
        self.description = description
        self.datatype = datatype
        self.allowed_values = allowed_values

class CommunityPolicyDefinitions(list):
    def __init__(self):
        self.extend([
            CommunityPolicy('publication_workflow', 'Publication workflow to be followed for new records', str, [*publication_workflows.keys()]),
            CommunityPolicy('restricted_submission', 'Allow members-only submission of new records', bool)
        ])

    def __getattr__(self, policy_name):
        for p in self:
            if p.name.title().replace('_', '') == policy_name:
                return p
        raise InvalidCommunityPolicy()

    def keys(self):
        return filter(lambda x: x.name, self)

CommunityPolicies = CommunityPolicyDefinitions()
