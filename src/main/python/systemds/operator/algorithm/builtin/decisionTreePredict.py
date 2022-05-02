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
# Autogenerated From : scripts/builtin/decisionTreePredict.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode, Matrix, Frame, List, MultiReturn, Scalar
from systemds.script_building.dag import OutputType
from systemds.utils.consts import VALID_INPUT_TYPES


def decisionTreePredict(M: Matrix,
                        X: Matrix,
                        strategy: str):
    """
    :param to: in the learned tree and each row contains the following information:
    :param categorical: if the feature is categorical)
    :param that: looks at if j is an internal node, otherwise 0
    :param the: as R input vector
    :param otherwise: of the subset of values
    :param stored: 6,7,... if j is categorical
    :param If: a leaf node: number of misclassified samples reaching at node j
    :param to: at M[6,j] if the feature chosen for j is scale,
    :param otherwise: feature chosen for j is categorical rows 6,7,... depict the value subset chosen for j
    :param If: a leaf node 1 if j is impure and the number of samples at j > threshold, otherwise 0
    :param strategy: strategy, can be one of ["GEMM", "TT", "PTT"], referring to "Generic matrix multiplication", 
    :return: 'OperationNode' containing  
    """
    params_dict = {'M': M, 'X': X, 'strategy': strategy}
    return Matrix(M.sds_context,
        'decisionTreePredict',
        named_input_nodes=params_dict)
