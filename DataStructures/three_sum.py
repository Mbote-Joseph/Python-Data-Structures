# Copyright 2025 josephmbote
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        List = set()
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    total = nums[i] + nums[j] + nums[k]
                    if total == 0 and i != j and j !=k and i != k:
                        List.add(tuple([nums[i],nums[j],nums[k]]))
                    break
                
        return [list(t) for t in List]