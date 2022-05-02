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
# Autogenerated From : scripts/builtin/km.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode, Matrix, Frame, List, MultiReturn, Scalar
from systemds.script_building.dag import OutputType
from systemds.utils.consts import VALID_INPUT_TYPES


def km(X: Matrix,
       TE: Matrix,
       GI: Matrix,
       SI: Matrix,
       **kwargs: Dict[str, VALID_INPUT_TYPES]):
    """
    :param number: (categorical features) for grouping and/or stratifying
    :param alpha: Parameter to compute 100*(1-alpha)% confidence intervals for the survivor
    :param function: median
    :param err_type: Parameter to specify the error type according to "greenwood" (the default) or "peto"
    :param conf_type: Parameter to modify the confidence interval; "plain" keeps the lower and
    :param upper: the confidence interval unmodified, "log" (the default)
    :param corresponds: transformation and "log-log" corresponds to the
    :param test_type: If survival data for multiple groups is available specifies which test to
    :param perform: survival data across multiple groups: "none" (the default)
    :return: 'OperationNode' containing 7 consecutive columns in km corresponds to a unique & and strata in the data with the following schema & number of factors used for stratifying, i.e., ncol(si)) & of groups and strata is equal to 1, m will have 4 columns with & 4 matrix t and an g x 5 matrix t_groups_oe with 
    """
    params_dict = {'X': X, 'TE': TE, 'GI': GI, 'SI': SI}
    params_dict.update(kwargs)
    
    vX_0 = Matrix(X.sds_context, '')
    vX_1 = Matrix(X.sds_context, '')
    vX_2 = Matrix(X.sds_context, '')
    vX_3 = Matrix(X.sds_context, '')
    output_nodes = [vX_0, vX_1, vX_2, vX_3, ]

    op = MultiReturn(X.sds_context, 'km', output_nodes, named_input_nodes=params_dict)

    vX_0._unnamed_input_nodes = [op]
    vX_1._unnamed_input_nodes = [op]
    vX_2._unnamed_input_nodes = [op]
    vX_3._unnamed_input_nodes = [op]

    return op
