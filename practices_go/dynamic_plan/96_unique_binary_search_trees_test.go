package dynamicplan

import "testing"

func TestNumTrees(t *testing.T) {
	tests := []struct {
		name string
		n    int
		want int
	}{
		{
			name: "示例1: n=3",
			n:    3,
			want: 5,
		},
		{
			name: "示例2: n=1",
			n:    1,
			want: 1,
		},
		{
			name: "n=2",
			n:    2,
			want: 2,
		},
		{
			name: "n=4",
			n:    4,
			want: 14,
		},
		{
			name: "n=5",
			n:    5,
			want: 42,
		},
		{
			name: "边界值: n=19",
			n:    19,
			want: 1767263190,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := numTrees(tt.n); got != tt.want {
				t.Errorf("numTrees() = %v, want %v", got, tt.want)
			}
		})
	}
}
