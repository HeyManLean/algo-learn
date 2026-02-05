package bytedance

import "testing"

func Test_reversePairs(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want int
	}{
		{
			name: "示例: [7,5,6,4]",
			nums: []int{7, 5, 6, 4},
			want: 5,
		},
		{
			name: "空数组",
			nums: []int{},
			want: 0,
		},
		{
			name: "单元素",
			nums: []int{1},
			want: 0,
		},
		{
			name: "完全逆序 [3,2,1]",
			nums: []int{3, 2, 1},
			want: 3,
		},
		{
			name: "已升序无逆序 [1,2,3]",
			nums: []int{1, 2, 3},
			want: 0,
		},
		{
			name: "两元素逆序",
			nums: []int{2, 1},
			want: 1,
		},
		{
			name: "1,3,2,3,1",
			nums: []int{1, 3, 2, 3, 1},
			want: 4,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := reversePairs(tt.nums); got != tt.want {
				t.Errorf("reversePairs() = %v, want %v", got, tt.want)
			}
		})
	}
}
