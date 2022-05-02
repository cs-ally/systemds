# -------------------------------------------------------------
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# -------------------------------------------------------------

# Autogenerated By   : src/main/python/generator/generator.py
# Autogenerated From : scripts/builtin/stableMarriage.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode, Matrix, Frame, List, MultiReturn, Scalar
from systemds.script_building.dag import OutputType
from systemds.utils.consts import VALID_INPUT_TYPES


def stableMarriage(P: Matrix,
                   A: Matrix,
                   **kwargs: Dict[str, VALID_INPUT_TYPES]):
    """
    :param It: a square matrix with no zeros.
    :param It: a square matrix with no zeros.
    :param ordered: If true, P and A are assumed to be ordered,
    :param index: vice-versa (higher is better).
    :return: 'OperationNode' containing to the match. & 1 (2.0 preference value) and acceptor 2 (1.0 preference value). & 3 (2.0 preference value) and proposer 2 & matched with proposer 3 (since [1,3] is non-zero) at a & 3.0. & matched with proposer 2 (since [2,2] is non-zero) at a & 3.0. & matched with proposer 1 (since [3,1] is non-zero) at a & 1.0. 
    """
    params_dict = {'P': P, 'A': A}
    params_dict.update(kwargs)
    return Matrix(P.sds_context,
        'stableMarriage',
        named_input_nodes=params_dict)
