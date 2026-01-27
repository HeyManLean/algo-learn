package bytedance

import "testing"

func TestNthUglyNumber(t *testing.T) {
	tests := []struct {
		name string
		n    int
		want int
	}{
		{
			name: "示例1",
			n:    10,
			want: 12,
		},
		{
			name: "示例2",
			n:    1,
			want: 1,
		},
		{
			name: "n=2",
			n:    2,
			want: 2,
		},
		{
			name: "n=3",
			n:    3,
			want: 3,
		},
		{
			name: "n=4",
			n:    4,
			want: 4,
		},
		{
			name: "n=5",
			n:    5,
			want: 5,
		},
		{
			name: "n=6",
			n:    6,
			want: 6,
		},
		{
			name: "n=7",
			n:    7,
			want: 8,
		},
		{
			name: "n=8",
			n:    8,
			want: 9,
		},
		{
			name: "n=9",
			n:    9,
			want: 10,
		},
		{
			name: "边界值n=1690",
			n:    1690,
			want: 2123366400,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := nthUglyNumber(tt.n); got != tt.want {
				t.Errorf("nthUglyNumber(%d) = %d, want %d", tt.n, got, tt.want)
			}
		})
	}
}
