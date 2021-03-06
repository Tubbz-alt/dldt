"""
 Copyright (c) 2018-2019 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from mo.front.kaldi.extractors.common_ext_test import KaldiFrontExtractorTest
from extensions.front.kaldi.tanh_component_ext import TanhFrontExtractor
from extensions.ops.activation_ops import Tanh
from mo.ops.op import Op


class TanhFrontExtractorTest(KaldiFrontExtractorTest):
    @classmethod
    def register_op(cls):
        Op.registered_ops['Tanh'] = Tanh

    def test_assertion(self):
        self.assertRaises(AttributeError, TanhFrontExtractor.extract, None)

    def test_extracted_blobs_add_shift(self):
        TanhFrontExtractor.extract(self.test_node)
        self.assertTrue(self.test_node.op, 'Tanh')
