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
# Autogenerated From : scripts/builtin/arima.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode, Matrix, Frame, List, MultiReturn, Scalar
from systemds.script_building.dag import OutputType
from systemds.utils.consts import VALID_INPUT_TYPES


def arima(X: Matrix,
          **kwargs: Dict[str, VALID_INPUT_TYPES]):
    """
    :param p: non-seasonal AR order
    :param d: non-seasonal differencing order
    :param q: non-seasonal MA order
    :param P: seasonal AR order
    :param D: seasonal differencing order
    :param Q: seasonal MA order
    :param s: period in terms of number of time-steps
    :param include_mean: center to mean 0, and include in result
    :param solver: solver, is either "cg" or "jacobi"
    :return: 'OperationNode' containing  
    """
    params_dict = {'X': X}
    params_dict.update(kwargs)
    return Matrix(X.sds_context,
        'arima',
        named_input_nodes=params_dict)
