package bytedance

import (
	"math"
	"testing"
)

func TestMedianFinder(t *testing.T) {
	t.Run("示例1", func(t *testing.T) {
		mf := NewMedianFinder()
		mf.AddNum(1)    // arr = [1]
		mf.AddNum(2)    // arr = [1, 2]
		got := mf.FindMedian()
		if !floatEqual(got, 1.5) {
			t.Errorf("FindMedian() = %v, want 1.5", got)
		}
		mf.AddNum(3)    // arr = [1, 2, 3]
		got = mf.FindMedian()
		if !floatEqual(got, 2.0) {
			t.Errorf("FindMedian() = %v, want 2.0", got)
		}
	})

	t.Run("单个元素", func(t *testing.T) {
		mf := NewMedianFinder()
		mf.AddNum(42)
		if got := mf.FindMedian(); got != 42 {
			t.Errorf("FindMedian() = %v, want 42", got)
		}
	})

	t.Run("偶数个元素", func(t *testing.T) {
		mf := NewMedianFinder()
		mf.AddNum(1)
		mf.AddNum(2)
		mf.AddNum(3)
		mf.AddNum(4)
		got := mf.FindMedian()
		if !floatEqual(got, 2.5) {
			t.Errorf("FindMedian() = %v, want 2.5 (arr=[1,2,3,4])", got)
		}
	})

	t.Run("奇数个元素", func(t *testing.T) {
		mf := NewMedianFinder()
		mf.AddNum(6)
		mf.AddNum(10)
		mf.AddNum(2)
		got := mf.FindMedian()
		if !floatEqual(got, 6.0) {
			t.Errorf("FindMedian() = %v, want 6.0 (arr=[2,6,10])", got)
		}
	})

	t.Run("负数", func(t *testing.T) {
		mf := NewMedianFinder()
		mf.AddNum(-1)
		mf.AddNum(-2)
		mf.AddNum(-3)
		got := mf.FindMedian()
		if !floatEqual(got, -2.0) {
			t.Errorf("FindMedian() = %v, want -2.0 (arr=[-3,-2,-1])", got)
		}
	})
}

// floatEqual 判断两个 float64 是否在 10^-5 误差内相等
func floatEqual(a, b float64) bool {
	return math.Abs(a-b) < 1e-5
}
