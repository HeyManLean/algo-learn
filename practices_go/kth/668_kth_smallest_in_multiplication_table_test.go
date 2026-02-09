package bytedance

import "testing"

func TestFindKthNumber(t *testing.T) {
	tests := []struct {
		name string
		m    int
		n    int
		k    int
		want int
	}{
		{
			name: "示例1",
			m:    3,
			n:    3,
			k:    5,
			want: 3,
		},
		{
			name: "示例2",
			m:    2,
			n:    3,
			k:    6,
			want: 6,
		},
		{
			name: "1x1乘法表",
			m:    1,
			n:    1,
			k:    1,
			want: 1,
		},
		{
			name: "第一个元素",
			m:    5,
			n:    5,
			k:    1,
			want: 1,
		},
		{
			name: "最后一个元素",
			m:    3,
			n:    3,
			k:    9,
			want: 9,
		},
		{
			name: "中间元素",
			m:    4,
			n:    4,
			k:    8,
			want: 6,
		},
		{
			name: "大数据量",
			m:    9895,
			n:    28405,
			k:    100787757,
			want: 31666344,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := findKthNumber(tt.m, tt.n, tt.k)
			if got != tt.want {
				t.Errorf("findKthNumber() = %v, want %v", got, tt.want)
			}
		})
	}
}
