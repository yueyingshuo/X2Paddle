#   Copyright (c) 2020  PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from enum import Enum


class Kind(Enum):
    Program = 1
    Code = 2


class Pass(object):
    name = "pass"

    def __init__(self, kind):
        self.kind = kind

    def apply(self, graph):
        raise NotImplementedError("The apply function must be implemented!")

    @classmethod
    def get_name(cls):
        return cls.name


class ProgramPass(Pass):
    def __init__(self):
        super(ProgramPass, self).__init__(Kind.Program)


class CodePass(Pass):
    def __init__(self):
        super(CodePass, self).__init__(Kind.Code)
