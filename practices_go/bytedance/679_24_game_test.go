package bytedance

import "testing"

func Test_judgePoint24(t *testing.T) {
	tests := []struct {
		name  string
		cards []int
		want  bool
	}{
		{
			name:  "示例1: [4,1,8,7] 可得到24",
			cards: []int{4, 1, 8, 7},
			want:  true,
		},
		{
			name:  "示例2: [1,2,1,2] 无法得到24",
			cards: []int{1, 2, 1, 2},
			want:  false,
		},
		{
			name:  "示例3: [3,3,8,8] 8/(3-8/3)=24",
			cards: []int{3, 3, 8, 8},
			want:  true,
		},
		{
			name:  "四个相同数字 如 [6,6,6,6] 可得到24",
			cards: []int{6, 6, 6, 6},
			want:  true,
		},
		{
			name:  "简单乘法 [2,3,4,1] 4*3*2*1=24",
			cards: []int{2, 3, 4, 1},
			want:  true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := judgePoint24(tt.cards); got != tt.want {
				t.Errorf("judgePoint24(%v) = %v, want %v", tt.cards, got, tt.want)
			}
		})
	}
}
