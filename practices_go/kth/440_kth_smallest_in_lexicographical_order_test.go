package bytedance

import "testing"

func Test_findKthNumber(t *testing.T) {
	tests := []struct {
		name string
		n    int
		k    int
		want int
	}{
		{
			name: "示例1: n=13, k=2",
			n:    13,
			k:    2,
			want: 10,
		},
		{
			name: "示例2: n=1, k=1",
			n:    1,
			k:    1,
			want: 1,
		},
		{
			name: "测试用例3: n=100, k=10",
			n:    100,
			k:    10,
			want: 17,
		},
		{
			name: "测试用例4: n=10, k=3",
			n:    10,
			k:    3,
			want: 2,
		},
		{
			name: "测试用例5: n=9, k=5",
			n:    9,
			k:    5,
			want: 5,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := findKthNumberInDict(tt.n, tt.k); got != tt.want {
				t.Errorf("findKthNumber() = %v, want %v", got, tt.want)
			}
		})
	}
}
