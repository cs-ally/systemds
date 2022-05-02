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
# Autogenerated From : scripts/builtin/executePipeline.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode, Matrix, Frame, List, MultiReturn, Scalar
from systemds.script_building.dag import OutputType
from systemds.utils.consts import VALID_INPUT_TYPES


def executePipeline(X: Matrix):
    """
    :param flagsCount: ---
    :param test: ---
    :return: 'OperationNode' containing validation check & convert the matrix row-vector into list & flag & append flag   & append flag & append flag & of hyper-parameters and loop till that & flag & and remove categorical & and remove numerics & + 1 for nan replacement & matrix & matrix & ohe call, to call inside eval as a function & encoding of categorical features & features & ohe call, to call inside eval as a function & to call inside eval as a function & doing relative over-sampling & count  & replace the null with default values & replace the null with default values & flip the noisy labels & best option 
    """
    params_dict = {'X': X}
    
    vX_0 = Matrix(X.sds_context, '')
    vX_1 = Matrix(X.sds_context, '')
    vX_2 = Matrix(X.sds_context, '')
    output_nodes = [vX_0, vX_1, vX_2, ]

    op = MultiReturn(X.sds_context, 'executePipeline', output_nodes, named_input_nodes=params_dict)

    vX_0._unnamed_input_nodes = [op]
    vX_1._unnamed_input_nodes = [op]
    vX_2._unnamed_input_nodes = [op]

    return op
