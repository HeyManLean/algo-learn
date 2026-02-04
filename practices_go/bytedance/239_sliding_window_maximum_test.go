package bytedance

import (
	"reflect"
	"testing"
)

func TestMaxSlidingWindow(t *testing.T) {
	tests := []struct {
		name   string
		nums   []int
		k      int
		expect []int
	}{
		{
			name:   "示例1",
			nums:   []int{1, 3, -1, -3, 5, 3, 6, 7},
			k:      3,
			expect: []int{3, 3, 5, 5, 6, 7},
		},
		{
			name:   "示例2：单元素",
			nums:   []int{1},
			k:      1,
			expect: []int{1},
		},
		{
			name:   "窗口等于数组长度",
			nums:   []int{1, -1},
			k:      2,
			expect: []int{1},
		},
		{
			name:   "递减序列",
			nums:   []int{7, 6, 5, 4, 3, 2, 1},
			k:      3,
			expect: []int{7, 6, 5, 4, 3},
		},
		{
			name:   "递增序列",
			nums:   []int{1, 2, 3, 4, 5},
			k:      2,
			expect: []int{2, 3, 4, 5},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := maxSlidingWindow(tt.nums, tt.k)
			if !reflect.DeepEqual(got, tt.expect) {
				t.Errorf("maxSlidingWindow() = %v, want %v", got, tt.expect)
			}
		})
	}
}
