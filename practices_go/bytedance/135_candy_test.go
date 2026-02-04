package bytedance

import "testing"

func Test_candy(t *testing.T) {
	tests := []struct {
		name        string
		ratings     []int
		wantCandies int
	}{
		{
			name:        "示例1: [1,0,2]",
			ratings:     []int{1, 0, 2},
			wantCandies: 5,
		},
		{
			name:        "示例x: [1,2,87,87,87,2,1]",
			ratings:     []int{1, 2, 87, 87, 87, 2, 1},
			wantCandies: 13,
		},
		{
			name:        "示例2: [1,2,2]",
			ratings:     []int{1, 2, 2},
			wantCandies: 4,
		},
		{
			name:        "单元素",
			ratings:     []int{1},
			wantCandies: 1,
		},
		{
			name:        "严格递增",
			ratings:     []int{1, 2, 3, 4},
			wantCandies: 10, // 1+2+3+4
		},
		{
			name:        "严格递减",
			ratings:     []int{4, 3, 2, 1},
			wantCandies: 10, // 4+3+2+1
		},
		{
			name:        "全相同",
			ratings:     []int{2, 2, 2, 2},
			wantCandies: 4,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := candy(tt.ratings); got != tt.wantCandies {
				t.Errorf("candy(%v) = %v, want %v", tt.ratings, got, tt.wantCandies)
			}
		})
	}
}
