# Copyright 2018 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""URL routing definitions."""

import webapp2

import config
from core.controllers import frontend_errors
from core.controllers import outgoing_emails

FRONTEND_ERROR_URL = '/ajax/frontend_errors'
MAIL_HANDLER_URL = '/ajax/mailhandler'
URLS = [
    (FRONTEND_ERROR_URL, frontend_errors.FrontendErrorHandler),
    (MAIL_HANDLER_URL, outgoing_emails.ForwardToAdminEmailHandler),
]

#pylint: disable=invalid-name
app = webapp2.WSGIApplication(URLS, debug=config.DEBUG)
#pylint: enable=invalid-name
